# Formatting and markup

24 features. [Back to the index](../ATLAS.md)

| Feature | Label | Kind | Conf. | G | H | L | Promotes |
|---|---|---|---|---|---|---|---|
| [L0.11](#l011) | Lone space token before dates, or trailing before paragraph breaks | lexical | medium | 0.7 | 0.4 | 0.4 | ꗜ 𒉶 𒅤  PLDNN MalayMarks |
| [L0.153](#l0153) | First word right after an opening quote or italics asterisk | lexical | medium | 2.9 | 2.4 | 2.9 | stood lapping ங்கிணை orems weds |
| [L0.441](#l0441) | First piece of an all-caps word or acronym | lexical | medium | 2.1 | 3.0 | 2.6 | s m is l d |
| [L1.299](#l1299) | Colon after a label in key-value or heading formats | lexical | high | 0.3 | 0.3 | 0.7 | � &lt;unused1166> &lt;unused687> &lt;unused201> &lt;unused1170> |
| [L1.2214](#l12214) | Word stem before a straight apostrophe, e.g. 'didn' | lexical | medium | 0.2 | 1.7 | 2.4 | ្នុង و aways \uf144 на |
| [L1.3516](#l13516) | Active only in text read without the chat template | structure | medium | 0.0 | 0.0 | 0.0 | � &lt;unused687> &lt;unused1166> Кра  seva |
| [L2.148](#l2148) | Colon after a label word in a 'Label: value' line | structure | high | 0.1 | 0.1 | 0.4 | ꗜ &lt;unused338> 𒉶  PLDNN 𒅤 |
| [L2.848](#l2848) | Double space or trailing space after a sentence | structure | high | 0.4 | 0.0 | 0.0 | ꗜ 𒉶 𒅤  PLDNN 𒂷 |
| [L4.141](#l4141) | Double space after a sentence or bold heading | structure | high | 0.4 | 0.0 | 0.0 | ꗜ 𒉶 𒅤 &lt;unused338>  PLDNN |
| [L10.1427](#l101427) | First digit of a multi-digit number | lexical | high | 0.1 | 0.2 | 0.2 | � &lt;unused687> &lt;unused1166> &lt;unused201> .&lt;/ |
| [L11.1250](#l111250) | Document-style fields, sign-offs and quoted list items | structure | low | 0.0 | 0.0 | 0.1 | &lt;unused687> � &lt;unused1166> &lt;unused201>  cercando |
| [L11.11288](#l1111288) | Digits inside years and page or number ranges | lexical | medium | 0.0 | 0.0 | 0.0 | � &lt;unused687> &lt;unused201> &lt;unused1077> .&lt;/ |
| [L12.1017](#l121017) | Fires through text that has no chat prompt before it | structure | medium | 0.2 | 1.0 | 0.5 | &lt;unused687> � &lt;unused1166> &lt;unused1077> &lt;unused1170> |
| [L14.1684](#l141684) | Tokens after irregular spacing (double spaces, space after quote) | lexical | medium | 0.3 | 0.4 | 0.1 |  (« டல் 。。  hele  dette |
| [L18.13](#l1813) | Paragraph break before an inserted block: letter, lyric or section break | structure | medium | 0.1 | 0.4 | 0.2 | ꗜ 𒉶  PLDNN 𒂷 𒅤 |
| [L22.474](#l22474) | Digits inside long numbers and timestamps | lexical | high | 0.2 | 0.4 | 0.7 | ꗜ 𒉶  PLDNN 𒅤 ꗐ |
| [L22.6046](#l226046) | Double space between sentences in Gemma's output | lexical | high | 0.9 | 0.2 | 0.2 |    ’”                       |
| [L26.1192](#l261192) | Word before a curly-apostrophe contraction (didn’t, wasn’t) | lexical | medium | 7.3 | 1.3 | 2.6 |  "...  '  "  "\'  \\& |
| [L28.41](#l2841) | Last word inside an asterisk span (italic thought or bold heading) | structure | high | 10.7 | 5.7 | 8.1 | ꗜ 𒉶  PLDNN 𒅤 ꗐ |
| [L31.169](#l31169) | Digit inside a multi-digit number | lexical | high | 0.2 | 0.4 | 0.7 | ꗜ 𒉶 MalayMarks  PLDNN ꗐ |
| [L32.320](#l32320) | Digits inside multi-digit numbers and dates | lexical | high | 0.3 | 0.7 | 0.8 | ꗜ 𒉶 &lt;unused338> 𒅤  PLDNN |
| [L33.17](#l3317) | Last token before a closing bold marker or heading end | structure | medium | 5.8 | 8.0 | 7.1 | ꗜ 𒉶  PLDNN MalayMarks ꗐ |
| [L33.43](#l3343) | Digits inside multi-digit numbers, dates and usernames | lexical | high | 0.4 | 1.3 | 0.9 | ꗜ 𒉶  PLDNN 𒅤 ꗐ |
| [L33.604](#l33604) | Article or quote mark opening a title, sign or scare-quoted label | construction | medium | 3.1 | 0.4 | 1.8 | 𒉶 𒂷 &lt;unused338> ꗜ 𒅤 |

## L0.11

**Lone space token before dates, or trailing before paragraph breaks** (lexical, medium confidence)

Fires on a bare space token: in human and other LLM text mostly before a year or day number, in Gemma text mostly as a stray trailing space after a sentence just before a paragraph break. Decoder output is junk tokens; rates are low everywhere and highest in Gemma plain mode (0.011 vs 0.004 for humans).

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.7, wp/claude 0.5, wp/glm 0.4, books/human 0.5, books/gemma 0.8, books/haiku 0.3, books/gpt 0.2, books/glm 0.4, wp/gemma_plain 1.1, wp/gemma_lit 0.7, wp/gemma_greedy 0.4, wp/gemma_raw 0.7, wp/human_raw 0.4.

Writer contrasts (paired effect size on each half, change in firing rate): greedy_vs_sampled -0.72/-0.67 (-0.3 pts).

Promotes: `ꗜ` `𒉶` `𒅤` ` PLDNN` `MalayMarks` `&lt;unused338>` `ꗐ` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `.&lt;/` `&lt;unused201>` `&lt;unused1077>`

- *human* (734):  leg.⏎⏎Skraaawwww! The sound was ear-peircing. Before Nathan could even register what the creature was screaming about**[ ]**
- *human* (730):  began to glide towards us casually. One broke off from the formation and moved on past us. The other three began their landing. At about**[ ]**1000 meters,
- *human* (702):  reason, I figured I was safe for the rest of school, and so I was.⏎⏎Years later, at my next milestone birthday -**[ ]**21, I got a
- *Gemma* (790):  chickens, the calls of vendors hawking their wares, the scent of spiced meats and overripe fruit – it felt like a cruel joke.**[ ]**⏎⏎I’d wandered through
- *Gemma* (790):  simultaneously intensely familiar. This boy, this awkward, self-conscious, desperately trying-to-be-cool boy, was *me*.**[ ]**⏎⏎A low groan escaped my
- *Gemma* (774): efully crafted trinkets – polished stones, woven flower chains, intricate mud sculptures – and, most importantly, their unwavering attention and song.**[ ]**⏎⏎Initially, there was outrage

## L0.153

**First word right after an opening quote or italics asterisk** (lexical, medium confidence)

Fires on the capitalised first word inside quotes, italics or a title (New, The, You, One). Rates are similar across writers (about 0.025) except Gemma plain mode, which is about twice as high (0.061).

Fires on (% of tokens): wp/human 2.4, wp/gemma 2.9, wp/claude 2.9, wp/glm 2.9, books/human 2.5, books/gemma 2.5, books/haiku 2.6, books/gpt 3.5, books/glm 2.4, wp/gemma_plain 6.1, wp/gemma_lit 2.6, wp/gemma_greedy 3.0, wp/gemma_raw 3.0, wp/human_raw 2.4.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_plain -2.16/-2.64 (-3.5 pts); plain_vs_default 2.08/2.38 (3.1 pts).

Constructions: sent_start.

Promotes: `stood` `lapping` `ங்கிணை` `orems` `weds` `slaught` `ymmetric` `ileged` `least` `atenate`  
Suppresses: `cellaneous` `eredReader` `achusetts` `ponible` `pués` `ES`

- *human* (163): **Then, **⏎⏎***[My]** outer layer changes temperature rapidly
- *human* (162): ****[My]** office: NOW. **⏎⏎
- *human* (160): 's all fine and all, but what if there's more of him? Are they invading?"⏎⏎The man spoke up, "**[One]** weak and frail man is not
- *Gemma* (161):  viewed from different angles. It’s as if they’re not simply written, but *generated*.”⏎⏎A reporter from the ***[New]** York Times* raised his hand
- *other LLM* (162): The folder was just sitting there when I logged in on a Tuesday morning: ***[New]** folder*, last modified 0
- *other LLM* (161):  gift was knowing exactly what was wrong with any machine, and when he died, he left her the shop and a note that said: ***[You]**'ll figure it out.

## L0.441

**First piece of an all-caps word or acronym** (lexical, medium confidence)

Top activations are the opening token of capitalised words in signs, titles and shouts (LE, RUN, UN, PRO); it also fires on ' I', which explains the i_pron tag. It promotes lowercase pieces such as 's', 'm', 'd' and suppresses capital letters; human WritingPrompts text fires a little more (0.030) than Gemma (0.021).

Fires on (% of tokens): wp/human 3.0, wp/gemma 2.1, wp/claude 2.7, wp/glm 2.5, books/human 2.4, books/gemma 1.6, books/haiku 2.2, books/gpt 2.5, books/glm 2.1, wp/gemma_plain 3.8, wp/gemma_lit 1.8, wp/gemma_greedy 2.3, wp/gemma_raw 2.2, wp/human_raw 2.9.

Constructions: i_pron.

Promotes: `s` `m` `is` `l` `d` `t` `larni` `r` `larda` `Õ`  
Suppresses: `S` ` UFC` ` WTO` `T` `E` `L`

- *human* (250): gans cried.⏎⏎"4"⏎⏎"3"⏎⏎"2"⏎⏎"It's in your head Higgans,**[ MAN]** UP!"⏎⏎"1"
- *human* (245):  plan was to do* The Adventures of Pete & Pete *but I had second thoughts and scrapped it. So instead, I ask that you**[ PRE]**PARE YOUR BLADDERS
- *human* (244):  more advanced then the Imperium of Man’s, some of it even appeared to be similar to Dark Age tech indicating the existence of an**[ ST]**C. But, what was
- *Gemma* (232):  saw it. Scrawled across the side of the cup, in thick, dark blue marker, were three stark, urgent letters: “**[RUN]**.”⏎⏎I froze. My
- *Gemma* (222): . After decades of planning, billions of dollars, and the collective, desperate hope of humanity, we’d actually made it. The Ares**[ VI]** mission, dubbed ‘New Dawn
- *Gemma* (221): d of our best fighters, armed with a captured Patriot missile launcher, had been neutralized by a swarm of Kryll maintenance bots carrying rudimentary**[ EMP]** grenades. A group of engineers

## L1.299

**Colon after a label in key-value or heading formats** (lexical, high confidence)

Fires on colons after a label word: chat handles, stat lists (Weapons, Methane), product taglines and bold bullet headers in assistant-style analysis. Gemma plain uses it most (0.017) against 0.002 to 0.008 elsewhere.

Fires on (% of tokens): wp/human 0.3, wp/gemma 0.3, wp/claude 0.6, wp/glm 0.8, books/human 0.7, books/gemma 0.3, books/haiku 0.5, books/gpt 0.4, books/glm 0.6, wp/gemma_plain 1.7, wp/gemma_lit 0.2, wp/gemma_greedy 0.3, wp/gemma_raw 0.6, wp/human_raw 0.3.

Constructions: colon.

Promotes: `�` `&lt;unused1166>` `&lt;unused687>` `&lt;unused201>` `&lt;unused1170>` ` WV` ` cercando` `&lt;unused1077>` `.&lt;/` `čnog`  
Suppresses: `ꗜ` ` PLDNN` `𒉶` `MalayMarks` `𒅤` `&lt;unused338>`

- *human* (46): "Nitrogen: 71%, Oxygen: 25%, Methane**[:]** 3%, other gases detected
- *human* (45): At 14:52:28, FreedomFighter69 wrote:⏎⏎Reporting my first temporal excursion since joining IATT**[:]** have just returned from 1
- *human* (41): Still, I lived for Taco night.⏎⏎I turned my wrist to take a look at my watch. The LCD numbers glowed 4**[:]**30, shining like the
- *Gemma* (42): The loading screen shimmered, a sickly sweet pastel pink that felt intensely, aggressively nostalgic. “Aethelgard**[:]** Echoes of the Ancients
- *Gemma* (40):  but emotional weight. And the emotion… it was a tsunami.⏎⏎“Analysis: Primary directive – biological stabilization – compromised. Resultant species**[:]** *Homo sapiens*.”⏎⏎
- *Gemma* (39): The brochure was slick, undeniably so. Glossy, holographic, promising a future of peak performance and blissful serenity. “SynapseShift**[:]** Optimize Your Potential.” It depicted

## L1.2214

**Word stem before a straight apostrophe, e.g. 'didn'** (lexical, medium confidence)

Fires on didn, wasn and similar stems before an apostrophe. Writer rates follow apostrophe typography: high where straight apostrophes are typed (Claude 0.028, Haiku 0.020) and near zero in curly-apostrophe text (book humans, GPT, Gemma chat), so its books LLM vs human gap is a typography effect.

Fires on (% of tokens): wp/human 1.7, wp/gemma 0.2, wp/claude 2.8, wp/glm 2.1, books/human 0.1, books/gemma 0.1, books/haiku 2.0, books/gpt 0.2, books/glm 1.9, wp/gemma_plain 0.4, wp/gemma_lit 0.2, wp/gemma_greedy 0.1, wp/gemma_raw 0.8, wp/human_raw 1.7.

Writer contrasts (paired effect size on each half, change in firing rate): books_llm_vs_human 2.62/2.2 (1.2 pts); wp_gemma_vs_llm -3.39/-3.36 (-2.2 pts); books_gemma_vs_llm -2.78/-2.58 (-1.3 pts).

Promotes: `្នុង` `و` `aways` `\uf144` `на` `𝒙` `な` ` oblige` `ాన` `ो`  
Suppresses: `le` `ので` `ப்` `ன்` `hashtag` `۰۰`

- *human* (29): 'ports back and forth between Lawton and Shima. As much as people said the'port was safe, he still wondered if it**[ didn]**'t cause cancer or maybe
- *human* (29): Ex**[cer]**pts from newly rediscovered journals in
- *human* (27):  She was underfed and malnourished and almost dying. I thought so at least. It turns out she was dying and I'm glad I**[ didn]**'t know then.⏎⏎
- *Gemma* (25): hed tones amongst the men who unknowingly danced to its tune. We weren't about flashy conspiracies or world domination in the traditional sense. We**[ didn]**’t seek to overthrow governments
- *Gemma* (23):  in the atmosphere. Then came the bills, meticulously crafted to appear reasonable, to appeal to a majority who didn't understand, or perhaps**[ didn]**’t *want* to
- *Gemma* (22): , the slow creep of the Blightwood. My work was practical, necessary, but rarely lauded. It wasn't revolutionary, it**[ didn]**’t generate wealth, it

## L1.3516

**Active only in text read without the chat template** (structure, medium confidence)

Fires only in the raw sets (Gemma raw 0.011, human raw 0.009) and the taste texts (about 0.018), and never in chat-framed text. Activations are weak and the tokens vary (newlines, ellipses, ordinary nouns), so it marks how the input is framed; no single token type drives it.

Fires on (% of tokens): wp/human 0.0, wp/gemma 0.0, wp/claude 0.0, wp/glm 0.0, books/human 0.0, books/gemma 0.0, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.0, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 1.1, wp/human_raw 0.9.

Writer contrasts (paired effect size on each half, change in firing rate): chat_vs_raw_gemma -2.25/-2.13 (-1.1 pts).

Promotes: `�` `&lt;unused687>` `&lt;unused1166>` `Кра` ` seva` ` político` `Cette` `এদিকে` ` gratuitement` `čnog`  
Suppresses: `ꗜ` `MalayMarks` `&lt;unused338>` `𒉶` ` PLDNN` `ꗐ`

- *human* (12):  felt like that pole had never went through my best friends chest.⏎⏎Now I had done it big time. By the time I reached our**[-...]** my, apartment I was a
- *human* (10):  the sunrise came, always around 6am this time of year in the Mojave Desert, she would become more and more paralyzed with sleepiness**[....]** no, not sleepiness.
- *human* (8):  hatred for the Chinese, Russian, and Korean doctrine. I do now, the triple alliance for a world united under communism almost seems like cheating**[....]**⏎⏎Jason Gnash⏎⏎June
- *Gemma* (5):  eyes, the color of polished jade, seemed to absorb rather than reflect light – it was all designed for one purpose: to elicit desire.**[⏎⏎]**For decades, he'd
- *Gemma* (5): , hovering for a moment before being projected onto the Citadel’s wall. That glyph was our designation, our future, our entire identity.**[⏎⏎]**My glyph was Azure. It
- *Gemma* (4):  grief and despair. They manifested as distorted figures, whispered voices, and pockets of oppressive cold. And they, invariably, harmed the living.**[⏎⏎]**Silas’s job was

## L2.148

**Colon after a label word in a 'Label: value' line** (structure, high confidence)

Fires on the colon after a field label such as Rule Two, Status, Address, Disclaimer or Designation, including bold markdown headings. Most common in GLM and raw Gemma, rare elsewhere.

Fires on (% of tokens): wp/human 0.1, wp/gemma 0.1, wp/claude 0.2, wp/glm 0.5, books/human 0.1, books/gemma 0.1, books/haiku 0.1, books/gpt 0.1, books/glm 0.2, wp/gemma_plain 0.1, wp/gemma_lit 0.1, wp/gemma_greedy 0.1, wp/gemma_raw 0.4, wp/human_raw 0.1.

Constructions: colon.

Promotes: `ꗜ` `&lt;unused338>` `𒉶` ` PLDNN` `𒅤` `MalayMarks` `ꗐ` `DenovoMis` `𒂷` `posTocco`  
Suppresses: `�` `.&lt;/` `&lt;unused687>` `&lt;unused1077>` `&lt;unused1166>` `&lt;unused192>`

- *human* (160): *Warning**[:]** This turned out way longer than
- *human* (144): Disclaimer**[:]** It is the first time I
- *human* (136): Working title**[:]** "The tank"⏎⏎There
- *Gemma* (146):  cascade of frequencies, mathematically precise and laced with millennia of suppressed fury. ⏎⏎“Designation: Observation Unit 734. Status**[:]** Anomalous.”⏎⏎Kael
- *Gemma* (128):  been curves. ⏎⏎A voice, resonant and devoid of inflection, echoed around me. “Welcome, Candidate 734. Designation**[:]** Elias Thorne.”⏎⏎I blinked
- *Gemma* (122): . It was a simple, emotionless message: “Citizen 749-Omega-9, Assignment: External Reconnaissance. Duration**[:]** 72 Hours. Return

## L2.848

**Double space or trailing space after a sentence** (structure, high confidence)

Fires on a double-space token after a sentence ends and on a space before a newline. It fires only in Gemma's output (0.3 to 0.8% of tokens) and essentially never for humans or other LLMs, so it marks a Gemma whitespace habit.

Fires on (% of tokens): wp/human 0.0, wp/gemma 0.4, wp/claude 0.0, wp/glm 0.0, books/human 0.0, books/gemma 0.3, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.8, wp/gemma_lit 0.5, wp/gemma_greedy 0.1, wp/gemma_raw 0.6, wp/human_raw 0.0.

Writer contrasts (paired effect size on each half, change in firing rate): greedy_vs_sampled -0.59/-0.65 (-0.2 pts).

Promotes: `ꗜ` `𒉶` `𒅤` ` PLDNN` `𒂷` `ꗐ` `MalayMarks` `𒍭` `ꗨ` `𒅿`  
Suppresses: `&lt;unused201>` ` ihe` `&lt;unused1166>` `&lt;unused1170>` `&lt;unused2041>` ` bruge`

- *human* (7):  you know why I scratched that little sentence into the back of my car? ’ I didn’t; I said so. ‘ Well **[’,]** he breathed – his words trembled
- *human* (4):  the popular girl, that sort of thing.⏎⏎But at that age, being in high school the inevitable happened - bullying. Being a we**[edy]** kid I was a prime target
- *Gemma* (51):  with an unnervingly placid voice, was… flexible. “Let’s just say, a consistent willingness to embrace the unexpected.”**[  ]**Silas, driven by a
- *Gemma* (47):  one… well, a bad one felt like being forcibly ejected from a blender and slammed back in.⏎⏎And the taste of static. **[⏎⏎]**I took a tentative sip of
- *other* (78): t work?”⏎⏎The Doctor gave a small, sad smile. “Then the universe may start to fall apart, shard by shard." **[⏎]**
- *other* (76):  mortality settled over them like the dust of the grave, and the monuments they'd built to their vanity began to crumble and fall. **[⏎]**And, like a rising tide

## L4.141

**Double space after a sentence or bold heading** (structure, high confidence)

Fires on a double-space token after a sentence ends, and on the space after bold headings in model critique text. It fires only in Gemma's output and is zero for humans and the other LLMs.

Fires on (% of tokens): wp/human 0.0, wp/gemma 0.4, wp/claude 0.0, wp/glm 0.0, books/human 0.0, books/gemma 0.2, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.5, wp/gemma_lit 0.5, wp/gemma_greedy 0.1, wp/gemma_raw 0.7, wp/human_raw 0.0.

Writer contrasts (paired effect size on each half, change in firing rate): greedy_vs_sampled -0.53/-0.72 (-0.2 pts).

Promotes: `ꗜ` `𒉶` `𒅤` `&lt;unused338>` ` PLDNN` `ꗐ` `MalayMarks` `𒂷` `DenovoMis` `odikwa`  
Suppresses: `&lt;unused687>` `&lt;unused201>` `&lt;unused1166>` `.&lt;/` `�` `&lt;unused1077>`

- *human* (87): ****[ “]**Woof! WOOF!”
- *human* (40): *"**[ Please]** don't. I have
- *Gemma* (345): radually began to organize themselves around the most persistent resonances. They were drawn to echoes of themselves, reinforcing their own existence.**[  ]**The first of these were the
- *Gemma* (341):  and regarded me with an expression I couldn't quite decipher. It wasn’t hostile, not exactly, just… unsettlingly neutral.**[  ]**He considered me for a long
- *Gemma* (339): wn life – the relentless teasing from Mark Peterson, the humiliation of failing my math test, the suffocating feeling of being perpetually overlooked.**[  ]**Then, one rainy afternoon,
- *other LLM* (20): ? You were lying there like a corpse for a full minute while I was sitting up. I thought you'd died."⏎⏎"*I**[*]** was lying there? You were

## L10.1427

**First digit of a multi-digit number** (lexical, high confidence)

Fires on the leading digit of numbers written as numerals (24 hours, 1956, 98.7%), across human, Gemma and other LLM text. Rare overall and slightly more common in human Reddit stories; its taste-set rate (0.009 approved, 0.012 rejected) is one token per text: it fires on the first text token after BOS, which only taste texts expose, so the rejected/approved gap reflects shorter rejected texts.

Fires on (% of tokens): wp/human 0.2, wp/gemma 0.1, wp/claude 0.2, wp/glm 0.2, books/human 0.0, books/gemma 0.0, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.1, wp/gemma_lit 0.0, wp/gemma_greedy 0.1, wp/gemma_raw 0.0, wp/human_raw 0.1.

Promotes: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused192>` ` cercando` `&lt;unused1170>` `&lt;unused366>` `&lt;unused1077>`  
Suppresses: `ꗜ` `𒉶` `𒅤` ` PLDNN` `MalayMarks` `&lt;unused338>`

- *human* (442):  tenth, and twentieth years. Close your eyes, blow out the candles, and whatever you wished for caught up with you in the next **[2]**4 hours. But you were
- *human* (434):  deep pit leading to the entrance. Or exit, in our case. Only a few more metres. I think we were way past the **[2]**00m mark. I
- *human* (380):  earth, years from home, and years from our destination. I'd been here about 500 years, I only had **[1]**500 to go,
- *Gemma* (402): , every single person, received it. The day and month of their death. No year, no hour, no minute. Just the **[1]**7th of October. 
- *Gemma* (346):  the Swiss Alps, surrounded by the rhythmic tick-tock of his creations. He was 83 years old. His timer displayed **[1]**2 hours, 3 minutes
- *Gemma* (338):  Academy was consistently top-tier. My score on Surveillance Analysis was 99.8%. My extraction rate from compromised data streams was **[9]**8.7%. My proficiency

## L11.1250

**Document-style fields, sign-offs and quoted list items** (structure, low confidence)

Weak firing elsewhere on field labels with colons (Subject:, Perpetrator:), letter sign-offs, journal headings and items in lists of quoted words. Its taste-set rate (0.009 approved, 0.012 rejected) is one token per text: it fires on the first text token after BOS, which only taste texts expose, so the rejected/approved gap reflects shorter rejected texts.

Fires on (% of tokens): wp/human 0.0, wp/gemma 0.0, wp/claude 0.1, wp/glm 0.1, books/human 0.1, books/gemma 0.0, books/haiku 0.0, books/gpt 0.0, books/glm 0.1, wp/gemma_plain 0.1, wp/gemma_lit 0.0, wp/gemma_greedy 0.1, wp/gemma_raw 0.1, wp/human_raw 0.0.

Promotes: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` ` cercando` `&lt;unused1077>` `&lt;unused366>` `&lt;unused673>` `čnog` `&lt;unused1170>`  
Suppresses: `ꗜ` `𒉶` ` PLDNN` `𒅤` `MalayMarks` `ꗐ`

- *human* (208): 't be all bad, though, supposing that some good can come of it somewhere.⏎⏎Entry 1371, Research Journal**[ of]** Dr. ______________⏎⏎Private
- *human* (180):  was fighting constant battles with the other half of the continent for the past two thousand years.⏎⏎It was prophesied by the Oracle (Power**[:]** Future Knowledge) that only the
- *Gemma* (232):  crumpled, the handwriting shaky and uneven. I unfolded it, a slow, confused dread settling in my stomach.⏎⏎“Dear Sober Self**[,]** enjoy ruling the world. Love
- *Gemma* (158):  felt… raw, vulnerable, like a forgotten limb.⏎⏎I double-clicked.⏎⏎The folder opened. Inside was a single file:**[ “]**Project Nightingale.” It was a
- *other LLM* (428):  what I'm fairly sure was eyeliner.⏎⏎*Dear Sobr Self,*⏎*enjoy ruling the world.*⏎*Love,*⏎**[*]**The Supreme Ruler of Earth and
- *other LLM* (320):  charging costs alone.⏎⏎Then the second alert chimed, and this one made her pulse jump.⏎⏎"Class A event. Perpetrator**[:]** Baron Blackout. Target:

## L11.11288

**Digits inside years and page or number ranges** (lexical, medium confidence)

Fires on digits within a number rather than its start, mostly years and page ranges (the 5 in 1539, the 6 in 1625). Its taste-set rate (0.009 approved, 0.012 rejected) is one token per text: it fires on the first text token after BOS, which only taste texts expose, so the rejected/approved gap reflects shorter rejected texts.

Fires on (% of tokens): wp/human 0.0, wp/gemma 0.0, wp/claude 0.0, wp/glm 0.0, books/human 0.0, books/gemma 0.0, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.0, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 0.0, wp/human_raw 0.0.

Promotes: `�` `&lt;unused687>` `&lt;unused201>` `&lt;unused1077>` `.&lt;/` `&lt;unused673>` `�` `&lt;unused1166>` `&lt;unused192>` `&lt;unused108>`  
Suppresses: `ꗜ` `&lt;unused338>` `𒅤` `𒉶` `ꗐ` `𒂷`

- *human* (76):  to make contact with the natives today. The Captain tells us we will observe and wait.⏎⏎*January 29, 20**[0]**0*⏎⏎I have had
- *human* (66): erving part was that the picture had a large cut through it, right acrossed John’s face ending before touching Susan.⏎⏎John st**[ee]**led himself and thought he was
- *other LLM* (284): , 2033, 2038, 2041, 2047, 20**[5]**2. And one text file
- *other LLM* (194):  called everyone chief, sport, big guy, or buddy. In six years he learned no one's name.⏎⏎And on page **[1]**90 you learn that he
- *other LLM* (142):  the wound with clay and moss. "That's all. Nothing's ready when you pick it."⏎⏎---⏎⏎In 1**[5]**39 the King's

## L12.1017

**Fires through text that has no chat prompt before it** (structure, medium confidence)

Fires on scattered tokens (sentence ends, contractions like didn't) only when the text is not inside a chat turn: raw continuations 0.038 and prompt-less taste texts about 0.097, against 0.000 to 0.010 for chat-framed sets. It looks like a document-context detector more than a prose feature.

Fires on (% of tokens): wp/human 1.0, wp/gemma 0.2, wp/claude 0.5, wp/glm 0.6, books/human 0.0, books/gemma 0.0, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.2, wp/gemma_lit 0.1, wp/gemma_greedy 0.2, wp/gemma_raw 3.8, wp/human_raw 3.8.

Writer contrasts (paired effect size on each half, change in firing rate): chat_vs_raw_gemma -1.8/-1.62 (-3.6 pts).

Promotes: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused1077>` `&lt;unused1170>` `Referências` `&lt;unused515>` `&lt;unused201>` `.&lt;/` `&lt;unused108>`  
Suppresses: `ꗜ` ` PLDNN` `𒉶` `MalayMarks` `&lt;unused338>` `ꗐ`

- *human* (260):  something that people don't want us to?" Larry looks up excitedly "That's it! We stop selling information to third parties!"**[ That]** was a lot easier than I
- *human* (200): " after a particularly nasty Wyvern burnt my hand black. That's it. A terrible joke, at the expense of my terrible misfortune**[.]**⏎⏎But here I was trud
- *human* (194):  out from the dot in the middle.⏎⏎"Sanda Bullock is working on a movie right now. And not near here. Besides,**[ isn]**'t she married already?
- *Gemma* (140): redictable patterns. After a catastrophic lab accident involving a poorly calibrated resonance field and a particularly stubborn houseplant, he’d been**[ cons]**cripted into the Ministry of
- *Gemma* (120):  victories. It was about order. About the quiet, persistent act of preserving knowledge. A surprisingly potent metric for assessing potential divinity**[.”]**⏎⏎“But… I didn
- *Gemma* (106):  But the pattern solidified, became undeniable. The numbers were a prophecy, a terrifying, absolute accounting of a person’s capacity for violence.**[⏎⏎]**I learned to avoid looking.

## L14.1684

**Tokens after irregular spacing (double spaces, space after quote)** (lexical, medium confidence)

Fires on a token preceded by odd whitespace: a double space after a period or bold label, a space after an opening quote, or unusual splits like Freedomfighter69. It promotes odd punctuation tokens; rare everywhere, with raw Gemma highest (0.007).

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.3, wp/claude 0.1, wp/glm 0.1, books/human 0.1, books/gemma 0.2, books/haiku 0.1, books/gpt 0.1, books/glm 0.1, wp/gemma_plain 0.3, wp/gemma_lit 0.3, wp/gemma_greedy 0.0, wp/gemma_raw 0.7, wp/human_raw 0.3.

Writer contrasts (paired effect size on each half, change in firing rate): greedy_vs_sampled -0.99/-1.18 (-0.3 pts).

Promotes: ` («` `டல்` `。。` ` hele` ` dette` ` மத` `३` ` dùng` `alne` ` tls`  
Suppresses: `&lt;unused520>` `&lt;unused974>` `&lt;unused976>` `&lt;unused1008>` `&lt;unused2153>` `&lt;unused338>`

- *human* (289):  wrote:⏎⏎Back from 1936 Berlin; incapacitated FreedomFighter69 before he could pull his little stunt.⏎⏎Freedom**[fighter]**69, as you are
- *human* (275):  a well-off family. Altogether, she was average, although *normal* might be a better word for it. She was... well**[ she]** was fairly unremarkable if you didn
- *human* (269): The Grim Reaper bore a hundred faces, though rarely more than one at a time. From skeletal scythe-wielder to pale**[ faced]** man in a suit and tie
- *Gemma* (249):  but it was *something*. With agonizing concentration, I focused on that twitch, willing it to repeat, to grow stronger. It did.**[  ]**Slowly, painstakingly, I
- *Gemma* (241):  the faces of the Unfiltered, their eyes haunted with a knowledge I couldn't comprehend.⏎⏎I hadn’t always used both.**[ ']**Obsidian' was a glitch
- *Gemma* (223): d had a brief, frustrating encounter with her two days ago, a contest of skill that ended with me narrowly avoiding a barrage of arrows.**[  ]**I’d learned quickly that

## L18.13

**Paragraph break before an inserted block: letter, lyric or section break** (structure, medium confidence)

Fires on the double newline after a colon or closing line when a written note, song, separator or author's aside follows. It is rare and fires more in raw text (1.5% for raw Gemma) than in chat-formatted text (0.1 to 0.4%).

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.1, wp/claude 0.2, wp/glm 0.2, books/human 0.2, books/gemma 0.1, books/haiku 0.1, books/gpt 0.2, books/glm 0.1, wp/gemma_plain 0.4, wp/gemma_lit 0.1, wp/gemma_greedy 0.1, wp/gemma_raw 1.5, wp/human_raw 0.9.

Writer contrasts (paired effect size on each half, change in firing rate): chat_vs_raw_gemma -1.83/-1.63 (-1.4 pts).

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒂷` `𒅤` `MalayMarks` `odikwa` `ꗐ` `DenovoMis` ` doneProcessAvg`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused192>` `&lt;unused1077>` `&lt;unused673>`

- *human* (494): , the reports would stack up soon.⏎⏎After what felt like an eternity, Lianna beelined to the principal's office.**[⏎⏎]**"So, I was fidget
- *human* (454):  writing. And this is the first non work-related writing I've done in a long time. Any feedback would be much appreciated!**[⏎⏎]*** * * * *⏎⏎
- *human* (406):  want this relationship to work. I even tried to make some time for her after work hours but she’s too busy with her work.**[⏎⏎]**“Sigh, now what
- *Gemma* (258):  antithesis of my methods – raw power versus calculated precision.  He was also, I’d discovered, particularly susceptible to flattery.**[⏎⏎]**“You seem… troubled,
- *Gemma* (214):  simply slid the coffee across the counter. The young man took a sip, then another, and finally, he looked up at Silas. **[⏎⏎]**“It’s good,”
- *Gemma* (214): d been drawn here, compelled by a force I hadn’t felt in eons – the desperate, aching need to prevent oblivion. **[⏎⏎]**He stirred, a shudder racking

## L22.474

**Digits inside long numbers and timestamps** (lexical, high confidence)

Fires on single digits in the middle of long figures, money amounts and clock times. Claude and GLM fire on it more than Gemma on WritingPrompts (0.007 vs 0.002).

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.2, wp/claude 0.7, wp/glm 0.6, books/human 0.2, books/gemma 0.1, books/haiku 0.1, books/gpt 0.1, books/glm 0.1, wp/gemma_plain 0.3, wp/gemma_lit 0.2, wp/gemma_greedy 0.3, wp/gemma_raw 0.2, wp/human_raw 0.4.

Constructions: number.

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `𒂷` `&lt;unused338>` `DenovoMis` `odikwa`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused1077>`

- *human* (3005):  us all years of correcting his misguided antics. READ BULLETIN 1147, PEOPLE!⏎⏎At 15:41:**[1]**8, BarracksRoomLaw
- *human* (2909):  have no eyes or thought processes that we know of and so it puts me at a total loss as for expectations.⏎⏎Entry 13**[9]**6, Research Journal of Dr
- *human* (2829):  voice said. It was not loud, or soft, but in the completely quiet exam room, it was like a cannon. "0.**[1]**82 is the answer.
- *Gemma* (3501):  expensive. Terribly, breathtakingly expensive. The average net worth within Veridia hovered somewhere around $772,132,**[8]**56.45.
- *Gemma* (3341):  gaze.⏎⏎And there it was. Floating above his head, bathed in the weak afternoon light, was 7,431,**[3]**23,210
- *Gemma* (2781):  was rarely a word used in scientific circles, especially when discussing a mission of this magnitude.⏎⏎“Yesterday, at approximately 03:**[1]**7 EDT, Voyager 1

## L22.6046

**Double space between sentences in Gemma's output** (lexical, high confidence)

Fires mainly on a two-space whitespace token after a sentence ends and before the next sentence starts; a few hits are on odd apostrophes and quote tokens. Promotes whitespace tokens. Gemma fires several times more often than humans or Claude, in chat and raw mode alike.

Fires on (% of tokens): wp/human 0.2, wp/gemma 0.9, wp/claude 0.1, wp/glm 0.2, books/human 0.5, books/gemma 0.8, books/haiku 0.1, books/gpt 0.4, books/glm 0.2, wp/gemma_plain 0.7, wp/gemma_lit 0.9, wp/gemma_greedy 0.5, wp/gemma_raw 1.0, wp/human_raw 0.1.

Writer contrasts (paired effect size on each half, change in firing rate): books_llm_vs_human -1.04/-0.93 (-0.2 pts); wp_gemma_vs_llm 2.0/2.02 (0.8 pts); greedy_vs_sampled -1.01/-1.44 (-0.5 pts); raw_gemma_vs_human 1.36/1.62 (0.9 pts).

Promotes: `  ` `’”` `           ` `     ` `   ` ` கமல்ஹா` `̐` `čun` ` alternately` `inski`  
Suppresses: `ussy` `嶷` ` கு` ` სახელმწიფო` `&lt;unused378>` `για`

- *human* (670):  will not allow his return?"⏎⏎The crowd started chanting, "Die, apostate. Die, blasphemer. Die, die, die**[!”]**⏎⏎Forced to kneel,
- *human* (618):  dunno. I don't know."⏎⏎"You were! Aw, you sick fuck!"⏎⏎"No, I might have, but**[ i]**-it just felt like vertigo
- *human* (554): cher from an earlier time lies your means of retribution. Remember it."⏎⏎Those words He spoke to me, and here, centuries later,**[ i]** remember.⏎⏎I will not
- *Gemma* (1254):  and regarded me with an expression I couldn't quite decipher. It wasn’t hostile, not exactly, just… unsettlingly neutral.**[  ]**He considered me for a long
- *Gemma* (1222):  voice surprisingly firm. “He's wrong.”⏎⏎The two of them turned to face each other, an unspoken tension radiating between them.**[  ]**My head began to spin.
- *Gemma* (1214):  They saw us as a resource, a raw material to be molded into the ideal worker, the perfect companion, the most subtly effective agent.**[  ]**And like we’d done

## L26.1192

**Word before a curly-apostrophe contraction (didn’t, wasn’t)** (lexical, medium confidence)

Fires on the stem of a negative contraction (didn, don, wasn) and other curly apostrophes, promotes straight-quote tokens and suppresses curly ones. Rates follow typography: high in Gemma chat output, published human books and GPT, low in WritingPrompts human text, Haiku and Gemma raw output.

Fires on (% of tokens): wp/human 1.3, wp/gemma 7.3, wp/claude 2.5, wp/glm 2.6, books/human 9.2, books/gemma 9.3, books/haiku 2.4, books/gpt 12.4, books/glm 2.4, wp/gemma_plain 8.7, wp/gemma_lit 6.2, wp/gemma_greedy 7.8, wp/gemma_raw 1.7, wp/human_raw 0.5.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.54/2.56 (6.0 pts); wp_gemma_vs_llm 2.47/2.23 (4.7 pts); chat_vs_raw_gemma 2.51/2.43 (5.6 pts).

Promotes: ` "...` ` '` ` "` ` "\'` ` \\&` `...'` `'...` ` "-` `..."` `...."`  
Suppresses: `…’` `…”` ` ‘` ` ’` `”…` ` …”`

- *other* (1845):  of pancakes and blueberries – Mina’s current obsession.⏎⏎“Almost,” Michael said, carefully maneuvering the walker through the living room. He**[ wasn]**’t just moving her;
- *other* (1741): *. I’m surrounded by people who are… pleasant. Agreeable. They’re good. They’re *safe*. But they**[ don]**’t ignite anything. They
- *other* (1701):  ending, in the wrong context, just... deflates that."⏎⏎I paused, letting the analogy sink in.⏎⏎“Horror**[ isn]**’t about ‘winning.’

## L28.41

**Last word inside an asterisk span (italic thought or bold heading)** (structure, high confidence)

Fires on the final word before a closing * or **, in italic inner thoughts, titles and bold bullet headings. About twice as frequent in Gemma's stories as human ones; decoder output is junk.

Fires on (% of tokens): wp/human 5.7, wp/gemma 10.7, wp/claude 7.9, wp/glm 8.2, books/human 7.1, books/gemma 10.8, books/haiku 8.8, books/gpt 8.3, books/glm 8.9, wp/gemma_plain 12.8, wp/gemma_lit 11.1, wp/gemma_greedy 10.7, wp/gemma_raw 11.6, wp/human_raw 6.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.47/2.38 (5.0 pts); raw_gemma_vs_human 2.46/2.33 (5.2 pts).

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `&lt;unused338>` `𒂷` `DenovoMis` `doneProcessAvg`  
Suppresses: `�` `&lt;unused201>` `&lt;unused1166>` `&lt;unused687>` `.&lt;/` ` WV`

- *human* (2890): Jon had just turned on the Playboy Channel when the time device went off. *Shit. Him**[ again]**? Leave me alone, kid
- *human* (2570):  at every moment I feel that I am slipping farther away from whatever it is I am attempting to approach. *Breath*... *take a**[ breath]***...⏎⏎I can'
- *human* (2506):  and...⏎⏎Her stomach grumbled. *Don't think about food, don't think about food, don't think about**[ food]**. I'm not hungry
- *Gemma* (2922):  my mind – not a voice I recognized as my own, but a thin, reedy echo. *Don’t. Look. De**[eper]**.*⏎⏎I ignored it,
- *Gemma* (2842): , regardless of how comprehensively I’d documented.⏎⏎Then I started to realize it wasn’t about *things*. It was about ***[me]***.⏎⏎One night, the
- *Gemma* (2842):  I infiltrated Hitler’s social circles, attending rallies, parties, and private meetings, diligently observing, recording, and, most importantly, ***[listening]***. ⏎⏎I discovered

## L31.169

**Digit inside a multi-digit number** (lexical, high confidence)

Fires on the second or later digit of numbers, times and counts. It suppresses spelled-out number words like 'sixty'. Very rare; slightly more frequent in Claude and GLM Reddit stories than in Gemma's.

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.2, wp/claude 0.7, wp/glm 0.7, books/human 0.2, books/gemma 0.1, books/haiku 0.0, books/gpt 0.0, books/glm 0.1, wp/gemma_plain 0.3, wp/gemma_lit 0.2, wp/gemma_greedy 0.3, wp/gemma_raw 0.1, wp/human_raw 0.4.

Constructions: number.

Promotes: `ꗜ` `𒉶` `MalayMarks` ` PLDNN` `ꗐ` `𒅤` `&lt;unused1716>` `posTocco` `DenovoMis` `&lt;unused338>`  
Suppresses: ` sixty` `𝟎` ` २०` `０` ` fifty` `হাওয়া`

- *human* (3235): See full: http: //kvgunderson.tumblr.com/post/1248645813**[6]**3/herbivore-no
- *human* (3203):  and, behind all the carnage, the shattered server still smoked with a broken body laying beside it.⏎⏎If it’s been 5**[3]**2 years since the last murder
- *human* (2707):  would give the mini black hole enough spin to provide the energy required to get a ship to 0.9C. At 13**[0]**0, the board filed into
- *Gemma* (3267):  reaction, to observe me manipulating the rice, but I'd managed to maintain a semblance of normalcy, finishing my lunch in the standard **[6]**0 seconds, feigning ignorance
- *Gemma* (2931):  “His primary objective was to map every conceivable route between two points. He achieved approximately 78% of those routes. The remaining **[2]**2% involved numerous detours
- *Gemma* (2803): . I was vast, ancient, and utterly, fundamentally *tired* of being a stepping stone.⏎⏎The tipping point came during Cycle **[6]**7. A particularly irritating player

## L32.320

**Digits inside multi-digit numbers and dates** (lexical, high confidence)

Fires on the leading digit of years, dates, addresses and catalogue numbers. Rare overall, more frequent in human stories than in Gemma's, and its decoder is on the human side of the junk-token axis.

Fires on (% of tokens): wp/human 0.7, wp/gemma 0.3, wp/claude 0.9, wp/glm 0.8, books/human 0.2, books/gemma 0.1, books/haiku 0.0, books/gpt 0.0, books/glm 0.1, wp/gemma_plain 0.4, wp/gemma_lit 0.2, wp/gemma_greedy 0.3, wp/gemma_raw 0.2, wp/human_raw 0.7.

Constructions: number.

Promotes: `ꗜ` `𒉶` `&lt;unused338>` `𒅤` ` PLDNN` `ꗐ` `MalayMarks` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused1077>`

- *human* (8561): 016, at that.⏎⏎I start my day like I would normally do: check the time (usually it would be around **[1]**2nn to 1pm
- *human* (8369):  and, behind all the carnage, the shattered server still smoked with a broken body laying beside it.⏎⏎If it’s been 5**[3]**2 years since the last murder
- *human* (8177):  Forum**⏎⏎**Subforum: Europe – Twentieth Century – Second World War**⏎⏎**Page 263**⏎⏎11/**[1]**5/2104
- *Gemma* (7857):  a sharp, acidic rain, but a dull, persistent tang, like licking a corroded pipe. It’d been raining on Kepler-**[1]**86f for seventy-
- *Gemma* (7793): eans, punctuated by towering, crystalline mountains that reflected the unrelenting sunlight. It was Eden, distilled and delivered – designated Kepler-**[1]**86f-B,
- *Gemma* (7729): The rain tasted like ash. It always did on the **[1]**7th of October. Not

## L33.17

**Last token before a closing bold marker or heading end** (structure, medium confidence)

Fires on the final word or punctuation inside **bold** headings, diary-entry titles and bullet labels, and on a period followed by a quote on the same line. Rates are similar across writers (6-10%); it reshapes the output distribution rather than promoting a word.

Fires on (% of tokens): wp/human 8.0, wp/gemma 5.8, wp/claude 7.0, wp/glm 7.2, books/human 7.6, books/gemma 5.9, books/haiku 6.9, books/gpt 8.5, books/glm 6.1, wp/gemma_plain 10.7, wp/gemma_lit 4.9, wp/gemma_greedy 5.7, wp/gemma_raw 7.6, wp/human_raw 9.4.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_plain -3.52/-3.47 (-5.8 pts); plain_vs_default 3.16/2.64 (4.9 pts).

Constructions: para_end.

Promotes: `ꗜ` `𒉶` ` PLDNN` `MalayMarks` `ꗐ` `𒅤` `&lt;unused338>` `𒂷` `DenovoMis` ` doneProcessAvg`  
Suppresses: `.&lt;/` `&lt;unused687>` `�` `&lt;unused1170>` `&lt;unused1166>` ` precio`

- *human* (3819): **Lack of**[ Knowledge]****⏎⏎He entered the new
- *human* (3819):  her knees. Will she stop rocking him, her face buried in his, and run away with us?⏎⏎**Sniff! Sniff**[!]** ** We are out on the
- *human* (3547):  with a blank expression.⏎⏎“Hungry?”⏎⏎He caught it. Vivian’s eyes shifted toward the back.⏎⏎*To what**[?]** * Sal thought. All he
- *Gemma* (2395):  a swirling vortex of glittering dust. He was, Seraphina often reflected with a weary sigh, a walking, breathing, dangerously potent chaos**[.]** ⏎⏎“Let’s
- *other LLM* (3915):  my mouth, but it is not my voice.⏎⏎The tutorial goes like this. A tooltip appears: **Press [Attack] to attack**[!]**** The player hits me.
- *other* (4875):  form of psychological projection? Adding some technical details (even if vague) could add a layer of intrigue.⏎* **The Progression of the**[ Images]**:** The story only shows one

## L33.43

**Digits inside multi-digit numbers, dates and usernames** (lexical, high confidence)

Fires on the inner digits of years, timestamps, large figures and handles like DarkFang42. Rare, and somewhat more frequent in human raw text; decoder output is junk.

Fires on (% of tokens): wp/human 1.3, wp/gemma 0.4, wp/claude 0.9, wp/glm 0.8, books/human 0.9, books/gemma 0.3, books/haiku 0.2, books/gpt 0.3, books/glm 0.3, wp/gemma_plain 0.5, wp/gemma_lit 0.3, wp/gemma_greedy 0.5, wp/gemma_raw 0.6, wp/human_raw 2.5.

Constructions: number.

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `&lt;unused338>` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `&lt;unused687>` `&lt;unused1166>` `�` `&lt;unused201>` `.&lt;/` `&lt;unused366>`

- *human* (15649):  volunteered to go back and fix⏎⏎it. You think I’ve got nothing better to do?⏎⏎11/16/2**[1]**04⏎⏎At 1
- *Gemma* (14177): . He simply observed it with a grim, detached curiosity. “I’m Elias. From… 2087.”⏎⏎2**[0]**87. The year the
- *Gemma* (13921):  expensive. Terribly, breathtakingly expensive. The average net worth within Veridia hovered somewhere around $772,132,**[8]**56.45.
- *Gemma* (13857): . But deceleration wasn’t cessation. It was a carefully constructed deception. ⏎⏎The *Argos* was designed to reach Kepler-**[1]**86f in approximately 
- *other LLM* (17121): ⏎⏎**DarkFang42:** i'm waiting for someone.⏎⏎**DarkerFang42:** Who?⏎⏎**DarkFang**[4]**2:** my voice.⏎⏎
- *other LLM* (15905):  yellow smiley face. On the left horizon a red digital counter read 099. On the right, another red counter read 0**[0]**0, then 00

## L33.604

**Article or quote mark opening a title, sign or scare-quoted label** (construction, medium confidence)

Fires on A or a inside titles and capitalized signs (A CHANCE DISCOVERY) and on an opening quote before a scare-quoted term. Rare, about six times more frequent in Gemma than in human prose.

Fires on (% of tokens): wp/human 0.4, wp/gemma 3.1, wp/claude 1.8, wp/glm 1.8, books/human 1.1, books/gemma 3.2, books/haiku 1.6, books/gpt 1.0, books/glm 1.4, wp/gemma_plain 1.4, wp/gemma_lit 4.0, wp/gemma_greedy 3.2, wp/gemma_raw 1.1, wp/human_raw 0.3.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 3.08/3.32 (2.6 pts); books_gemma_vs_human 2.53/2.16 (2.0 pts); wp_llm_vs_human 1.86/1.88 (1.3 pts); books_gemma_vs_llm 2.38/2.16 (1.8 pts); lit_vs_plain 2.74/2.83 (2.6 pts); chat_vs_raw_gemma 1.71/1.78 (2.0 pts).

Promotes: `𒉶` `𒂷` `&lt;unused338>` `ꗜ` `𒅤` ` PLDNN` `doneProcessAvg` `&lt;unused359>` `MalayMarks` `DenovoMis`  
Suppresses: ` arched` ` Aston` ` innings` `Aston` ` আল` ` Ар`

- *human* (2956):  might have roughly approximated what a human would have thought of as a deep sigh. I KNEW THAT LAW WAS GOING TO CAUSE ME**[ A]** HEADACHE SOMEHOW.
- *human* (2780): ly from his dark skin, his expression carefully blank.⏎⏎Later on, I'd been told, a mime was what people called a**[ "]**street performer." These men and
- *human* (2684): s kind of depressing, but I don't know if it's really scary..."⏎⏎I STILL DO NOT UNDERSTAND. THIS IS**[ A]** THING? SITTING A
- *Gemma* (3756):  head briefly, then turned back to the growing chaos.⏎⏎Then, the announcement. A voice, amplified and oddly hollow, spoke of a**[ “]**minor incident” and urged passengers
- *Gemma* (3628):  many resources. But I’d heard whispers, hushed conversations between Dr. Harding and the director, Dr. Ellis. Something about a**[ “]**critical anomaly,” a “host
- *Gemma* (3308):  was a persistent, dull grey that seemed to leach the color from everything, mirroring the state of my own existence. I’d been a**[ “]**Reader” for five years,
