"""Token tags for prose: constructions (regex), slop lists, and structure (sentences, paragraphs, dialogue).

spans(text) -> {tag: [(char_start, char_end), ...]};  to_tokens(spans, offsets) -> {tag: [token indices]}.
Construction tags (PRE) are also read one token before their onset, where the model decides to start them.
"""
import re, json, os, bisect
STOP = set("""i me my myself we our ours ourselves you you're you've you'll you'd your yours yourself yourselves he him his himself she she's her hers
herself it it's its itself they them their theirs themselves what which who whom this that that'll these those am is are was were be been being have
has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before
after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most
other some such no nor not only own same so than too very s t can will just don don't should should've now d ll m o re ve y ain aren aren't couldn
couldn't didn didn't doesn doesn't hadn hadn't hasn hasn't haven haven't isn isn't ma mightn mightn't mustn mustn't needn needn't shan shan't
shouldn shouldn't wasn wasn't weren weren't won won't wouldn wouldn't""".split())
_here = os.path.dirname(os.path.abspath(__file__))
_sl = json.load(open(os.path.join(_here, "slop_lists.json")))
SLOP_W, SLOP_T = set(_sl["words"]), set(_sl["trigrams"])
TAGV = r"(?:said|asked|whispered|replied|murmured|muttered|added|answered|called|shouted|continued|began|admitted|offered)"
RX = {
 "wasnt_it_was": r"(?:wasn['’]t|was not|weren['’]t|isn['’]t|is not|didn['’]t)\b[^.!?\n]{2,70}[.;,—–-]+\s*(?:It|He|She|They|This|That|it|he|she|they|this|that)\s+(?:was|were|is|did)\b",
 "not_just": r"\bnot (?:just|merely|only|simply)\b",
 "simile_like": r"\blike (?:a|an|the)\b",
 "as_if": r"\bas (?:if|though)\b",
 "em_dash": r"\s?—\s?|\s–\s|\s--\s",
 "ellipsis": r"…|\.\.\.",
 "semicolon": r";",
 "colon": r":(?=\s)",
 "tag_adverb": r"\b" + TAGV + r"\s+\w+ly\b",
 "bookism": r"\b(?:whispered|murmured|breathed|growled|hissed|muttered|snapped|chuckled|sighed|rasped|drawled|purred|croaked|stammered)\b",
 "voice_barely": r"\bvoice\b[^.!?\n]{0,12}\b(?:barely|low|soft|quiet|hoarse|trembl\w+|thick|a whisper)\b",
 "list3": r"\b\w+, (?:\w+ ){0,2}\w+,? and \w+\b",
 "emotion_pack": r"\b(?:a|an) (?:\w+ )?(?:sense|wave|pang|surge|flicker|flash|mix|mixture|hint|knot|spark|rush|twinge|jolt|shiver|tremor|weight|kind) of\b",
 "something": r"\bsomething (?:in|like|about|else|akin|shifted|flickered|stirred|deeper|more)\b",
 "couldnt_help": r"\bcould(?:n['’]t| not) help but\b",
 "body_cliche": r"\b(?:heart|breath|pulse|stomach|chest|throat)\s+(?:pounded|pounding|hammered|hammering|raced|racing|caught|hitched|tightened|clenched|skipped|sank|lurched|dropped)\b",
 "eyes": r"\beyes?\s+(?:widened|narrowed|sparkled|gleamed|glinted|softened|darkened|flickered|met|locked|searched|scanned|fixed)\b",
 "seemed": r"\bseemed to\b",
 "air_silence": r"\b(?:the air|the silence|silence)\s+(?:was|hung|felt|grew|smelled|crackled|stretched|fell|settled|descended|thickened|pressed)\b",
 "moment": r"\bfor a (?:long |brief )?moment\b|\bA beat\b|\ba beat\b|\bA (?:long )?pause\b",
 "just_adv": r"\b(?:just|simply|merely|really|very|quite|rather|almost|nearly|barely|slightly)\b",
 "ly_adverb": r"\b\w{4,}ly\b",
 "said": r"\bsaid\b",
 "name": r"(?<=[a-z,;] )[A-Z][a-z]{2,}\b",
 "i_pron": r"\bI\b",
 "and_start": r"(?:(?<=[.!?] )|(?<=\n))(?:And|But|So|Then)\b",
 "question": r"\?",
 "exclaim": r"!",
 "number": r"\b\d[\d,.]*\b",
 "abstract": r"\b\w+(?:ness|ity|tion|ment|ence|ance)\b",
}
RXC = {k: re.compile(v) for k, v in RX.items()}
PRE = ["wasnt_it_was", "not_just", "simile_like", "as_if", "em_dash", "ellipsis", "semicolon", "tag_adverb", "bookism", "voice_barely",
       "emotion_pack", "something", "couldnt_help", "body_cliche", "eyes", "seemed", "air_silence", "moment", "slop_tri", "slop_word", "name",
       "quote_open", "sent_end", "para_end"]
STRUCT = ["sent_start", "sent_end", "para_start", "para_end", "quote_open", "quote_close", "dialogue", "narration", "short_sent", "long_sent",
          "first_sent", "slop_tri", "slop_word"]
TAGS = ["all"] + list(RX) + STRUCT + ["pre:" + t for t in PRE]
TI = {t: i for i, t in enumerate(TAGS)}
SENT = re.compile(r"[^.!?…\n]+(?:[.!?…]+[\"”’')\]]*|(?=\n)|$)")
QUOTE = re.compile(r"“[^”\n]{1,600}”|\"[^\"\n]{1,600}\"")
WORD = re.compile(r"[A-Za-z][A-Za-z'’]*")


def spans(text):
    s = {k: [m.span() for m in r.finditer(text)] for k, r in RXC.items()}
    for k in STRUCT: s[k] = []
    first = True
    for m in SENT.finditer(text):
        a, b = m.span(); lead = len(text[a:b]) - len(text[a:b].lstrip()); a += lead
        if b - a < 2: continue
        n = len(text[a:b].split())
        s["sent_start"].append((a, a + 1)); s["sent_end"].append((max(a, b - 1), b))
        if n <= 4: s["short_sent"].append((a, b))
        if n >= 35: s["long_sent"].append((a, b))
        if first: s["first_sent"].append((a, b)); first = False
    pos = 0
    for para in text.split("\n\n"):
        a = pos + (len(para) - len(para.lstrip())); b = pos + len(para.rstrip())
        if b > a: s["para_start"].append((a, a + 1)); s["para_end"].append((b - 1, b))
        pos += len(para) + 2
    last = 0
    for m in QUOTE.finditer(text):
        a, b = m.span(); s["dialogue"].append((a + 1, b - 1)); s["quote_open"].append((a, a + 1)); s["quote_close"].append((b - 1, b))
        if a > last: s["narration"].append((last, a))
        last = b
    if last < len(text): s["narration"].append((last, len(text)))
    ws = [(m.group().lower().replace("’", "'"), m.start(), m.end()) for m in WORD.finditer(text)]
    for w, a, b in ws:
        if w in SLOP_W: s["slop_word"].append((a, b))
    cw = [x for x in ws if x[0] not in STOP]
    for i in range(len(cw) - 2):
        if f"{cw[i][0]} {cw[i+1][0]} {cw[i+2][0]}" in SLOP_T: s["slop_tri"].append((cw[i][1], cw[i + 2][2]))
    return s


def to_tokens(sp, offsets):
    """{tag index: sorted token indices}. 'pre:' tags are the token before a span's first token (-1 = the frame's last token)."""
    starts = [o[0] for o in offsets]; n = len(offsets); out = {TI["all"]: list(range(n))}
    def toks(a, b):
        i = max(0, bisect.bisect_right(starts, a) - 1); r = []
        while i < n and offsets[i][0] < b:
            if offsets[i][1] > a: r.append(i)
            i += 1
        return r
    for k, lst in sp.items():
        acc, pre = set(), set()
        for a, b in lst:
            t = toks(a, b)
            if not t: continue
            acc.update(t)
            if k in PRE and t[0] >= 1: pre.add(t[0] - 1)
        out[TI[k]] = sorted(acc)
        if k in PRE: out[TI["pre:" + k]] = sorted(pre)
    return out
