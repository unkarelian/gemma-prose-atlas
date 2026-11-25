# Narrative voice and stance

18 features. [Back to the index](../ATLAS.md)

| Feature | Label | Kind | Conf. | G | H | L | Promotes |
|---|---|---|---|---|---|---|---|
| [L5.1110](#l51110) | 'somehow' and 'for some reason' marking an unexplained cause | lexical | high | 0.7 | 0.7 | 0.4 | Referências čnog  WV ühl  &[ |
| [L5.1346](#l51346) | 'seems' and 'seem', mostly in spoken 'It seems' | lexical | high | 0.8 | 0.7 | 0.4 | 样子 sudo ances  appearances  facsimile |
| [L6.381](#l6381) | Frequency and certainty adverbs: invariably, usually, undoubtedly, positively | lexical | high | 4.0 | 3.2 | 2.0 | ꗜ 𒉶 𒅤 &lt;unused338>  PLDNN |
| [L8.7617](#l87617) | 'seemed' as main verb after a long subject phrase | lexical | medium | 0.5 | 0.4 | 0.2 | � &lt;unused687> &lt;unused201> .&lt;/  WV |
| [L13.218](#l13218) | Plain, unornamented narration; much rarer in Gemma | style | low | 3.1 | 15.8 | 13.8 | ꗜ  PLDNN 𒉶 𒅤 MalayMarks |
| [L17.4251](#l174251) | Plain declarative narration; peaks on contractions like didn't | style | medium | 12.0 | 4.5 | 45.1 |  قلت  मुली merk  verdes  meisjes |
| [L18.942](#l18942) | Characterizing adjective after a wry adverb (perpetually disgruntled) | style | medium | 4.1 | 1.1 | 0.6 | &lt;unused687> � &lt;unused1166> &lt;unused201> &lt;unused366> |
| [L20.57](#l2057) | Evaluative adjective in a noun phrase, often after an adverb | style | medium | 5.8 | 1.9 | 1.3 | &lt;unused687> � &lt;unused1166> .&lt;/ &lt;unused201> |
| [L21.326](#l21326) | Dense narration feature; decoder favors present over past verbs | unclear | low | 69.0 | 42.4 | 48.4 |  है  ہے  हैं  has 합니다 |
| [L26.2902](#l262902) | Verb after the subject of a polished narrative sentence, esp. openings | style | medium | 20.6 | 3.7 | 27.7 |  hysteresis  grid Oval  striated  সুন |
| [L27.275](#l27275) | Elevated, incantatory diction (relentless, ancient, ceaseless) | style | medium | 18.0 | 5.8 | 9.7 | ꗜ  PLDNN MalayMarks 𒉶 ꗐ |
| [L27.758](#l27758) | Plain colloquial register, mostly casual dialogue | style | medium | 8.1 | 9.0 | 28.7 |  तोह  કરોડ  मशहूर kids  kids |
| [L29.165](#l29165) | Broad narration feature, peaks on body nouns in trailing absolute phrases | style | medium | 39.1 | 13.2 | 32.5 | ꗐ 룺 acher  Co 𒅤 |
| [L29.667](#l29667) | Adjective describing a tone or manner: a wistful tone | construction | medium | 6.9 | 2.6 | 1.8 |  আভ  inférieure ព្រ unpkg ˈ |
| [L29.1455](#l291455) | Determiner or intensifier in arch, wry, mannered narration | style | medium | 25.1 | 9.3 | 11.5 | &lt;unused967> ∣ ">,&lt;/  []: 逮捕 |
| [L30.401](#l30401) | Function word opening an ornate descriptive or emotional noun phrase | style | medium | 27.9 | 11.7 | 21.8 | ꗜ 𒉶 &lt;unused338>  PLDNN MalayMarks |
| [L30.8674](#l308674) | Reflective literary narration: copulas and connectives in abstract metaphoric sentences | style | medium | 7.2 | 0.4 | 7.6 |  Genres  парни maur  leaning 膛 |
| [L31.1784](#l311784) | Plain, restrained narration and speech; strongest in Claude and GLM | style | low | 12.7 | 4.6 | 33.3 | ꗜ &lt;unused429> &lt;unused1716> &lt;unused338>  PLDNN |

## L5.1110

**'somehow' and 'for some reason' marking an unexplained cause** (lexical, high confidence)

Fires on 'somehow' and on 'reason' in 'for some reason', where the narrator admits a cause is unclear; the decoder promotes no readable tokens. Humans and Gemma use it at similar rates, while Claude and GLM fire about half as often.

Fires on (% of tokens): wp/human 0.7, wp/gemma 0.7, wp/claude 0.4, wp/glm 0.3, books/human 0.6, books/gemma 0.7, books/haiku 0.6, books/gpt 0.5, books/glm 0.6, wp/gemma_plain 0.4, wp/gemma_lit 0.7, wp/gemma_greedy 0.8, wp/gemma_raw 0.7, wp/human_raw 0.7.

Constructions: seemed.

Promotes: `Referências` `čnog` ` WV` `ühl` ` &[` `.&lt;/` `rschein` `�` `&lt;unused1166>` `etype`  
Suppresses: `ꗜ` `𒉶` `&lt;unused338>` `𒅤` `MalayMarks` `odikwa`

- *human* (193):  a broken-down rocking chair clutching a picture tightly to his chest. She couldn't hear the words he was saying even then, but**[ somehow]** she knew what they were and
- *human* (185):  this hag of a lady. To any man or woman even faintly gazing upon such a hideous creature it would have meant utter revulsion. But**[ somehow]**, nobody even acknowledged her presence
- *human* (183): . They had prepared the tome the best they could with sacred pdfs, epubs, mobis and mp3s. And for some**[ reason]** lost to time, assumed to
- *Gemma* (179):  chamber, a gesture that felt utterly futile.⏎⏎The emerald deity – I assumed it was the leader – tilted its head, a movement that**[ somehow]** managed to be both graceful and
- *Gemma* (178):  of my throat. It had been three months since the truck. Three months since my life fractured into a million jagged pieces and reassembled,**[ somehow]**, into something…different.
- *Gemma* (177):  he couldn't fully unravel. He’d simply stated he was reliving his fifteenth year, trapped in a loop, and that,**[ somehow]**, he'd aged twenty

## L5.1346

**'seems' and 'seem', mostly in spoken 'It seems'** (lexical, high confidence)

Fires on 'seems' or 'seem', most often in dialogue openings such as 'It seems' or a bare 'Seems'; it promotes appearance words like 'appearances' and 'facsimile'. Rates are close across writers, with GLM lowest.

Fires on (% of tokens): wp/human 0.7, wp/gemma 0.8, wp/claude 0.5, wp/glm 0.3, books/human 0.6, books/gemma 0.9, books/haiku 0.8, books/gpt 0.8, books/glm 0.6, wp/gemma_plain 0.9, wp/gemma_lit 0.8, wp/gemma_greedy 0.8, wp/gemma_raw 0.6, wp/human_raw 0.7.

Constructions: seemed.

Promotes: `样子` `sudo` `ances` ` appearances` ` facsimile` `huy` `\ueffd` `AFD` `ght` ` awfully`  
Suppresses: `ur` ` erstellen` ` ünlü` `seekBar` ` educator` ` légion`

- *human* (195):  Chris, she treats him badly, too. Hasn't he reported anything?"⏎⏎"Oh yes, plenty of times. And it**[ seems]** like she's not stopping
- *human* (188): "You keep mentioning this'internet'," Amvea said, interrupting me. "I do not understand what it is. It**[ seems]** like half of your life in
- *human* (187):  tears. "Where's mom?"⏎⏎"She's not home," his father growled, dropping him to the floor. "**[Seems]** like all you do all the
- *other LLM* (186):  me with perfect grace and hung it on her gallery wall, where a flowering vine grew up around the sheath within a cycle.⏎⏎"It**[ seems]** happier there," she said.
- *other* (212):  said to Mr. Davies, “Did you hear? Ninety-five and over. No laws.”⏎⏎Mr. Davies grunted. “**[Seems]** odd.”⏎⏎“Odd is
- *other* (201): , I presume? I’ve been expecting you.”⏎⏎“I’m here to ask about your recent…prosperity, Madam. It**[ seems]** rather sudden.”⏎⏎She poured

## L6.381

**Frequency and certainty adverbs: invariably, usually, undoubtedly, positively** (lexical, high confidence)

Fires on adverbs of frequency, certainty or degree such as 'invariably', 'inevitably', 'sometimes', 'evidently' and 'positively'. Gemma and humans use it somewhat more than Claude and GLM; Gemma's top examples lean on 'invariably'.

Fires on (% of tokens): wp/human 3.2, wp/gemma 4.0, wp/claude 2.1, wp/glm 1.9, books/human 2.8, books/gemma 3.5, books/haiku 2.3, books/gpt 2.2, books/glm 2.5, wp/gemma_plain 2.4, wp/gemma_lit 3.3, wp/gemma_greedy 3.7, wp/gemma_raw 3.1, wp/human_raw 3.1.

Constructions: just_adv, ly_adverb.

Promotes: `ꗜ` `𒉶` `𒅤` `&lt;unused338>` ` PLDNN` `MalayMarks` `ꗐ` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `�` `&lt;unused687>` `&lt;unused1166>` `.&lt;/` `&lt;unused201>` `&lt;unused1077>`

- *human* (622):  received cybernetic augmentations, or "augs" as they were called. They conducted horrific experiments on people, forcibly removing augmentations,**[ often]** killing their test subjects in the
- *human* (606): ky pout, but I know my mother, and I can tell from the subtle way her fingers tremble and her cheeks flush that she's**[ positively]** seething inside.⏎⏎I
- *human* (598):  The rogue shrugged.⏎⏎"Dozens of times. The Djinn's a breeze once you understand its powers. It's**[ positively]** obsessed with patterns." The rogue
- *Gemma* (670): “An elegant one, wouldn’t you agree? Centuries of mortals have volunteered, believing they sought enlightenment or escape. A small percentage,**[ invariably]**, possess the spark. You
- *Gemma* (670): thermal radiation, processed them through an incredibly complex biochemical cascade, and released photons as a byproduct. It was a remarkable process,**[ undoubtedly]**, but it was fundamentally the
- *Gemma* (614):  a murder occurred. Not a single one, mind you. Three, four, sometimes five. Always brutal, always impossible. The victims were**[ invariably]** found drained of blood, limbs

## L8.7617

**'seemed' as main verb after a long subject phrase** (lexical, medium confidence)

Fires on 'seemed' or 'seems' (and 'to' after 'appears') when it follows a long noun-phrase subject. Rates are similar across writers and lowest in the taste set.

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.5, wp/claude 0.3, wp/glm 0.2, books/human 0.4, books/gemma 0.7, books/haiku 0.4, books/gpt 0.4, books/glm 0.4, wp/gemma_plain 0.4, wp/gemma_lit 0.5, wp/gemma_greedy 0.6, wp/gemma_raw 0.4, wp/human_raw 0.5.

Constructions: seemed.

Promotes: `�` `&lt;unused687>` `&lt;unused201>` `.&lt;/` ` WV` `&lt;unused1166>` `čnog` ` افراد` ` cercando` `iseen`  
Suppresses: `ꗜ` `&lt;unused338>` `𒉶` ` PLDNN` `𒅤` `MalayMarks`

- *human* (254):  and one of her eyes was heavily scarred around the cheek, drawing attention to her dead eye. At least Adam though it was dead. It**[ seemed]** unnatural for only one eye to
- *human* (244):  watch in hand, her fingers trembling, her plumb figure trudging along with sullen haste. Another young man, with a tattered jacket,**[ seems]** rushed, looking for someone.
- *human* (242):  where they played paintball. I wish you had seen it sir." Where Desiree Lovelace seemed only to care about raw lust, her husband**[ seemed]** to genuinely want people to find
- *Gemma* (236):  men, he was. The curve of his jaw, the weight of his shoulders, the way his eyes, the color of polished jade,**[ seemed]** to absorb rather than reflect light
- *Gemma* (230): . ⏎⏎I tried to ignore them, to pretend they weren’t there. I wore headphones, blasting music, but even the bass**[ seemed]** to be punctuated by the disappro
- *Gemma* (222): , impossibly, began to shift, sliding forward with a slow, agonizing grace.⏎⏎The darkness didn’t recede, but it**[ seemed]** to thin, to lose some

## L13.218

**Plain, unornamented narration; much rarer in Gemma** (style, low confidence)

A broad feature firing on 10 to 16 percent of tokens for humans, Claude and GLM but about 3 percent for Gemma; examples are flat factual statements and plain dialogue. Gemma's plain mode fires twice its literary mode (0.065 vs 0.028), which supports the plain-style reading, but no single token pattern is visible.

Fires on (% of tokens): wp/human 15.8, wp/gemma 3.1, wp/claude 11.9, wp/glm 15.8, books/human 12.1, books/gemma 4.5, books/haiku 9.7, books/gpt 10.6, books/glm 9.2, wp/gemma_plain 6.5, wp/gemma_lit 2.8, wp/gemma_greedy 2.7, wp/gemma_raw 4.8, wp/human_raw 18.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -2.49/-2.64 (-12.7 pts); books_gemma_vs_human -2.1/-1.99 (-7.6 pts); wp_gemma_vs_llm -3.81/-3.46 (-10.8 pts); books_gemma_vs_llm -2.43/-2.44 (-5.3 pts); raw_gemma_vs_human -2.42/-2.41 (-13.7 pts).

Promotes: `ꗜ` ` PLDNN` `𒉶` `𒅤` `MalayMarks` `&lt;unused338>` `ꗐ` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused366>`

- *human* (824): , for a hundred dollars less unfortunately. Both were built from parts around the barn in a few hours. Both by hand. Junior had “**[A]** knack for tinkerin ’ and
- *human* (684):  on, "Now look, I know its not as much as you thought. But its all written down there. Your room and electricity is**[ deducted]**."⏎⏎I took a long
- *human* (664): .⏎⏎It is the third day of the quarantine, the guard watching the monitor is almost asleep when the mirror comes back online. Its Daniel**[ waving]**, maybe it was Daniel on
- *other LLM* (892):  was no room left in the country for protest.⏎⏎What I know is smaller. My husband has been dead five years. June is sixteen**[.]** She caught it on the choir
- *other LLM* (772): 'd gone out at four to fire the ovens at Costello's — thirty-one years of Tuesdays — and the trouble was five days**[ old]** and nobody had told the street
- *other LLM* (740):  move."⏎⏎They had been playing the same game for nine days, a few moves each morning. Ruben was losing.⏎⏎"Did she**[ come]** by?" he asked.⏎⏎

## L17.4251

**Plain declarative narration; peaks on contractions like didn't** (style, medium confidence)

Strongest on contracted negatives and auxiliaries (didn't, wasn't, I'd) and fires broadly on unadorned narration. Gemma's plain mode hits 67% of tokens versus 12% for default Gemma; Claude, GLM, GPT and Haiku sit at 43 to 55%, human books at 30% and WritingPrompts humans at 4.5%.

Fires on (% of tokens): wp/human 4.5, wp/gemma 12.0, wp/claude 43.1, wp/glm 47.1, books/human 29.5, books/gemma 36.9, books/haiku 54.9, books/gpt 49.1, books/glm 51.8, wp/gemma_plain 67.0, wp/gemma_lit 36.1, wp/gemma_greedy 10.2, wp/gemma_raw 2.5, wp/human_raw 2.7.

Writer contrasts (paired effect size on each half, change in firing rate): wp_llm_vs_human 2.31/2.12 (40.7 pts); books_llm_vs_human 2.25/2.29 (22.4 pts); wp_gemma_vs_llm -2.39/-2.16 (-33.5 pts); lit_vs_plain -2.33/-2.01 (-31.0 pts); lit_vs_default 2.01/2.12 (25.0 pts); plain_vs_default 4.09/4.46 (55.9 pts).

Promotes: ` قلت` ` मुली` `merk` ` verdes` ` meisjes` ` కొత్త` `靴` `পুন` `esso` `usk`  
Suppresses: ` поддержка` ` FOL` ` support` `riterien` ` Traditionally` ` поддержки`

- *other* (660):  well. He had been a quiet man. He worked at the factory. He smoked. He drank. He didn't talk much.**[ ]**⏎⏎I remembered my grandmother.
- *other* (644): . I enter data. I check totals. I occasionally answer the phone. It’s a good job. It pays the bills. It**[ doesn]**’t excite me.⏎⏎
- *other* (640):  it to David. His address is correct. I checked it twice. It’s a small apartment building. Number 14. I**[ don]**’t know when the last

## L18.942

**Characterizing adjective after a wry adverb (perpetually disgruntled)** (style, medium confidence)

Fires on the adjective in short character sketches, often after an intensifying adverb (slightly grumpy, socially awkward). Gemma uses it four to six times as often as humans or other LLMs (0.041 vs 0.006-0.011).

Fires on (% of tokens): wp/human 1.1, wp/gemma 4.1, wp/claude 0.6, wp/glm 0.6, books/human 1.1, books/gemma 3.4, books/haiku 0.7, books/gpt 0.7, books/glm 0.9, wp/gemma_plain 1.5, wp/gemma_lit 4.7, wp/gemma_greedy 4.1, wp/gemma_raw 2.3, wp/human_raw 1.0.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.6/2.35 (3.0 pts); books_gemma_vs_human 2.21/2.21 (2.3 pts); wp_gemma_vs_llm 3.62/3.38 (3.5 pts); books_gemma_vs_llm 2.64/2.9 (2.6 pts); lit_vs_plain 2.9/2.65 (3.2 pts); plain_vs_default -2.57/-2.2 (-2.6 pts); chat_vs_raw_gemma 1.4/1.29 (1.8 pts).

Promotes: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` `&lt;unused366>` `&lt;unused192>` `.&lt;/` `iseen` `&lt;unused673>` `&lt;unused1077>`  
Suppresses: `ꗜ` ` PLDNN` `𒉶` `MalayMarks` `𒅤` `ꗐ`

- *human* (629):  Now, come with me and I will lead you to the gates.”⏎⏎I quickly decided I was in no position to argue with whoever this**[ mysterious]** phantasm was, and
- *human* (597):  relay this message in hopes it may save others from the grave future that is to come. Some may discount these accounts as the hallucinations of a**[ starving]** man, but I assure you
- *human* (589): Okay. So I had a plan.⏎⏎The plan was to book a long, long stay at a hotel on some pretty and**[ remote]** - emphasis on remote - island
- *Gemma* (701):  decade perfecting the art of manipulation, deception, and subtly terrifying small children. My current cover was Elias Vance, a “gifted but socially**[ awkward]**” student at Aethel
- *Gemma* (637):  the mistakes of the past was crucial to maintaining the present. I didn't particularly enjoy it. My designated companion, a small, perpetually**[ cheerful]** bot named Pip, would drone
- *Gemma* (637):  dissuade them. That’s when the uniforms appeared. Grey, oversized sweatshirts emblazoned with crudely drawn anime characters, and ill-**[fitting]**, brightly colored combat trousers.

## L20.57

**Evaluative adjective in a noun phrase, often after an adverb** (style, medium confidence)

Fires on an evaluative adjective, as in terribly inefficient or a deliberate choice, often after a commenting adverb. Gemma uses it about four times as often as Claude, GPT and GLM, and three times as often as humans; the decoder only reshapes the distribution.

Fires on (% of tokens): wp/human 1.9, wp/gemma 5.8, wp/claude 1.2, wp/glm 1.4, books/human 1.8, books/gemma 5.3, books/haiku 1.4, books/gpt 1.3, books/glm 1.6, wp/gemma_plain 2.4, wp/gemma_lit 7.0, wp/gemma_greedy 5.7, wp/gemma_raw 3.8, wp/human_raw 1.8.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.79/2.62 (3.9 pts); books_gemma_vs_human 2.69/2.69 (3.5 pts); wp_gemma_vs_llm 3.85/3.77 (4.5 pts); books_gemma_vs_llm 3.14/3.35 (3.9 pts); lit_vs_plain 3.1/3.16 (4.5 pts); plain_vs_default -2.6/-2.38 (-3.4 pts); raw_gemma_vs_human 1.45/1.45 (2.0 pts); chat_vs_raw_gemma 1.25/1.12 (2.0 pts).

Promotes: `&lt;unused687>` `�` `&lt;unused1166>` `.&lt;/` `&lt;unused201>` `&lt;unused673>` `&lt;unused689>` `&lt;unused108>` `&lt;unused192>` `&lt;unused1077>`  
Suppresses: `ꗜ` ` PLDNN` `𒉶` `𒅤` `MalayMarks` `ꗐ`

- *human* (1262):  thought how fortunate that I was a doctor. I lamented it though, all the ethics they had drilled into me. That was during a more**[ civilized]** time. Now the ethics and
- *human* (1126):  or die.⏎⏎The conventional warfare eventually drew the ire of... well, actual governments. This forced the powers that be to resort to more**[ subtle]** tactics. As far as the
- *Gemma* (1262): that this… ‘pistol’… draws its power from a contained explosion? A miniature, controlled bonfire? Remarkable. Though a terribly**[ inefficient]** method, wouldn't you
- *Gemma* (1222):  it was “a fortunate byproduct” of his work. He’d died before he could explain it properly, leaving me with a life-**[altering]**, and frankly, slightly terrifying
- *Gemma* (1222):  a necromancer. Not the theatrical, summoning-dark-gods kind. I specialize in a far more delicate, and frankly,**[ exhausting]**, art: the temporary resurrection
- *other LLM* (1134):  the hospitals in three states filled up in a week.⏎⏎---⏎⏎By the second year, the world had gone quiet in a specific,**[ careful]** way.⏎⏎Every phone carrier

## L21.326

**Dense narration feature; decoder favors present over past verbs** (unclear, low confidence)

Fires on more than half of narration tokens with no clear shared word in the top examples, which lean toward contracted would and had forms; it promotes present-tense verbs and suppresses had and was. Gemma fires on it more than humans (wp 0.69 vs 0.42).

Fires on (% of tokens): wp/human 42.4, wp/gemma 69.0, wp/claude 50.1, wp/glm 46.6, books/human 43.5, books/gemma 62.1, books/haiku 52.6, books/gpt 55.8, books/glm 52.0, wp/gemma_plain 60.5, wp/gemma_lit 74.8, wp/gemma_greedy 69.2, wp/gemma_raw 42.5, wp/human_raw 39.3.

Constructions: narration.

Promotes: ` है` ` ہے` ` हैं` ` has` `합니다` `водит` ` will` `しています` `いています` ` makes`  
Suppresses: ` had` ` havde` ` habían` ` était` ` was` ` había`

- *human* (722):  God could allow that much pain, that much suffering in his world. I guess, between the pills and the drink I’d finally managed**[ to]** off myself. So it was
- *human* (694):  apart. I stepped forward into the dividing room, turned round, to see the girl from earlier, crying, and waving. The hell was**[ her]** name again, stacey,
- *human* (694):  job was and'porting was the only way to get there anymore.⏎⏎Sometimes he'd just get lost coming home. He'**[d]** take his normal turn and end
- *Gemma* (774):  I’d chosen, the one that felt, ironically, the least emotionally demanding. Numbers and protocols kept the edge off things. It allowed**[ me]** to observe, to analyze,
- *Gemma* (770):  centuries, we’d simply…taken. It wasn’t done with malice, not usually. It was a process, a delicate balance**[.]** A man filled with rage and
- *Gemma* (742): kind, was precious. Suicide rates plummeted. Ironically, the timer, meant to inspire fear, had inadvertently fostered a profound appreciation for life**[.]**⏎⏎I was a Chronometer

## L26.2902

**Verb after the subject of a polished narrative sentence, esp. openings** (style, medium confidence)

Strongest on the verb or noun right after the subject of a story's first sentence (The hall was...). Fires on 20-47% of tokens in model prose and published books but under 4% of human WritingPrompts text, and is highest when Gemma is told to write literary prose; decoder output is junk.

Fires on (% of tokens): wp/human 3.7, wp/gemma 20.6, wp/claude 25.2, wp/glm 30.2, books/human 23.8, books/gemma 39.1, books/haiku 39.6, books/gpt 31.6, books/glm 40.8, wp/gemma_plain 19.3, wp/gemma_lit 46.8, wp/gemma_greedy 19.2, wp/gemma_raw 3.0, wp/human_raw 0.8.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.04/2.26 (17.0 pts); wp_llm_vs_human 2.55/2.69 (24.1 pts); books_llm_vs_human 1.57/1.9 (13.5 pts); lit_vs_plain 2.72/3.54 (27.5 pts); lit_vs_default 3.59/3.4 (26.8 pts); chat_vs_raw_gemma 1.81/2.17 (17.6 pts).

Promotes: ` hysteresis` ` grid` `Oval` ` striated` ` সুন` ` spool` ` Oval` `oval` `watt` ` grids`  
Suppresses: ` uniqueness` ` UNIQUE` `UNIQUE` ` uniquely` ` unique` ` त्यावेळी`

- *other* (1366): The rain**[ arrived]** not with a crash, but
- *other* (1310):  clinging to the peeling wallpaper of my room. It mirrored the coating on my soul, a residue of unspoken things and slammed doors. My world**[ was]** a carefully constructed cage of silence
- *other* (1310): The rain**[ arrived]** as it always seemed to do

## L27.275

**Elevated, incantatory diction (relentless, ancient, ceaseless)** (style, medium confidence)

Fires on ornamental adjectives and archaic or verse-like wording, including song lyrics and solemn speech. Four times more frequent in literary-prompted Gemma than plain Gemma and three times more in Gemma than humans; decoder output is junk.

Fires on (% of tokens): wp/human 5.8, wp/gemma 18.0, wp/claude 7.3, wp/glm 12.1, books/human 11.5, books/gemma 22.9, books/haiku 15.2, books/gpt 12.0, books/glm 16.3, wp/gemma_plain 8.6, wp/gemma_lit 36.5, wp/gemma_greedy 17.8, wp/gemma_raw 11.0, wp/human_raw 5.3.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_plain 4.06/4.62 (27.9 pts); lit_vs_default 3.26/3.35 (19.1 pts).

Promotes: `ꗜ` ` PLDNN` `MalayMarks` `𒉶` `ꗐ` `𒂷` `DenovoMis` `apetiti` `𒅤` ` padamala`  
Suppresses: `&lt;unused1166>` `&lt;unused201>` `&lt;unused687>` `�` `เชื่อ` `.&lt;/`

- *Gemma* (1550): , born under the Azure moon, and bear the mark of the Silver Tear. This one shall command the Sunstone and deliver Veridia from**[ the]** Shadow Blight.”⏎⏎Simple
- *Gemma* (1550):  approaching storm before the clouds gathered, the loneliness of a stranger across the square. She was an Echo, a conduit to the world's**[ quiet]** grief, and in Oakh
- *Gemma* (1550):  in faded crimson ink, barely legible amidst the archaic script: “Kaelen Blackwood shall meet his end by his own hand, a**[ silent]** surrender to the grey.”⏎⏎
- *other LLM* (1646):  for the growing things, red for fire, grey for storm, black for the deep dark under the hills, silver for the moon's**[ slow]** pull on tides and dreams.
- *other* (1798):  by the tremor of the prophecy.⏎⏎“The Weaver shall unravel, consumed by the threads of his own despair, ending his days in a**[ silent]** surrender.” That’s what
- *other* (1774): emory clinging to the skin and the frayed edges of my memory itself. It tasted of regret and something older, something fundamentally tied to the ceas**[eless]** rhythm of the tides. The

## L27.758

**Plain colloquial register, mostly casual dialogue** (style, medium confidence)

Fires on contractions and everyday phrasing in speech (let's, something's, have to go) and suppresses formal verbs like 'occur' and 'commenced'. Fires on 40% of plain-prompted Gemma tokens but 0.6% of literary-prompted Gemma, and more in the reader's approved edits than rejected drafts.

Fires on (% of tokens): wp/human 9.0, wp/gemma 8.1, wp/claude 32.5, wp/glm 24.9, books/human 12.4, books/gemma 7.8, books/haiku 17.9, books/gpt 17.0, books/glm 17.6, wp/gemma_plain 39.8, wp/gemma_lit 0.6, wp/gemma_greedy 8.5, wp/gemma_raw 10.7, wp/human_raw 8.0.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_plain -1.97/-2.15 (-39.1 pts); lit_vs_default -1.08/-1.07 (-7.2 pts); plain_vs_default 1.83/2.11 (32.0 pts).

Promotes: ` तोह` ` કરોડ` ` मशहूर` `kids` ` kids` `ත්` ` might` `ссмо` ` kid` `iah`  
Suppresses: ` occurring` ` occur` ` occurs` ` occurred` ` सर्वप्रथम` ` occuring`

- *human* (1278):  knowing how long it had been. The only thing to stop me was a small hand rubbing my back unexpectedly.⏎⏎"Daddy, what'**[s]** wrong?" came the soft little
- *other LLM* (1502):  was at work.⏎⏎"What's your name?"⏎⏎"Tamsin. Tamsin Okafor-Bell. You can**[ just]** say Tamsin."⏎⏎
- *other LLM* (1462):  was preparing to go when Owen said, "Could you scare them instead?"⏎⏎"Who?"⏎⏎"Kyle. And Marcus and Tyler,**[ but]** mostly Kyle. Could you go
- *other LLM* (1454): , there was Nothing. And Nothing was very bored."⏎⏎"Nothing can't be bored."⏎⏎"Why not?"⏎⏎"Because**[ bored]** is a something. If you
- *other* (1534): . She was facing a reflection of her own isolation.⏎⏎“Okay,” she said, a new resolve hardening her voice. “Let'**[s]** find your home.” ⏎
- *other* (1390):  that much. It was a good rifle. Accurate. Powerful. Not something you bought on a whim. ⏎⏎“You know what’**[s]** happened,” I said. “

## L29.165

**Broad narration feature, peaks on body nouns in trailing absolute phrases** (style, medium confidence)

Fires on 40% of tokens, strongest on 'voice', 'hands' or 'fingers' in phrases like 'her voice a low tremor' after dialogue. It fires on 62% of tokens in Gemma's literary prose and 59% in its book scenes, against 13% in human WritingPrompts stories.

Fires on (% of tokens): wp/human 13.2, wp/gemma 39.1, wp/claude 30.8, wp/glm 34.2, books/human 36.6, books/gemma 58.9, books/haiku 53.9, books/gpt 50.5, books/glm 53.8, wp/gemma_plain 31.1, wp/gemma_lit 62.4, wp/gemma_greedy 38.4, wp/gemma_raw 22.6, wp/human_raw 9.3.

Writer contrasts (paired effect size on each half, change in firing rate): books_llm_vs_human 1.75/2.03 (16.1 pts); lit_vs_plain 2.79/3.1 (31.3 pts); lit_vs_default 2.71/2.7 (24.7 pts).

Constructions: narration.

Promotes: `ꗐ` `룺` `acher` ` Co` `𒅤` ` Po` ` taut` `𒊌` `oped` `âns`  
Suppresses: `enl` ` आँ` ` đậu` `whit` ` olhar` `Jeremy`

- *other* (2185):  her long, silver hair like liquid moonlight. ⏎⏎“You’ve been… persistent, Kaelen,” she finally said, her**[ voice]** a low, resonant chime that
- *other* (2137):  mirror that doesn't reflect back a single image. It reflects all images, simultaneously, eternally.”⏎⏎She rose from the rock, her**[ movements]** fluid and silent, and began
- *other* (2073):  a brushstroke of unexpected color on a canvas I thought I knew intimately.⏎⏎“You shouldn’t be here,” she said, her**[ voice]** a low, melodic murmur that

## L29.667

**Adjective describing a tone or manner: a wistful tone** (construction, medium confidence)

Fires on the adjective in phrases like 'a distinctly wistful tone', 'a nostalgic lilt' or 'an almost smug vibe' that characterize how someone sounds or seems. It fires three to four times as often in Gemma's prose (0.07, literary 0.08) as in Claude, GLM or GPT prose (about 0.015).

Fires on (% of tokens): wp/human 2.6, wp/gemma 6.9, wp/claude 1.8, wp/glm 1.8, books/human 1.7, books/gemma 6.0, books/haiku 1.5, books/gpt 1.4, books/glm 1.8, wp/gemma_plain 2.3, wp/gemma_lit 7.8, wp/gemma_greedy 6.6, wp/gemma_raw 4.4, wp/human_raw 2.2.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.31/2.17 (4.2 pts); books_gemma_vs_human 3.19/2.99 (4.3 pts); wp_gemma_vs_llm 3.46/3.69 (5.1 pts); books_gemma_vs_llm 3.43/3.47 (4.4 pts); lit_vs_plain 3.41/3.18 (5.5 pts); plain_vs_default -3.08/-2.6 (-4.5 pts); raw_gemma_vs_human 1.17/1.21 (2.2 pts).

Promotes: ` আভ` ` inférieure` `ព្រ` `unpkg` `ˈ` `ventyConfig` `PageIndex` ` চিহ্ন` ` usize` `tDBOutput`  
Suppresses: `обу` ` सग` `ස්ට` ` eram` `Ан` ` asserts`

- *human* (1133):  of me is at first startled by my appearance (I guess my long gray hair and accompanying wizard-beard don't give off a thrust**[worthy]** vibe), but then really annoyed
- *human* (1053):  seemed to find what he said amusing, "No, she won't get here for another century." She replied, giving off an almost**[ smug]** vibe, satisfied that she wasn
- *human* (1053):  I stuttered.⏎⏎"Yeah hey, I'm Michael... I'm guessing you just arrived?" The figure said with a slightly**[ arrogant]** tone.⏎⏎"I just
- *Gemma* (1301):  painfully realistic.⏎⏎“I’m attempting to perfect the art of familial harmony,” Vane explained, his voice taking on a distinctly wist**[ful]** tone. “Specifically, the
- *Gemma* (1181): ider and cryptic smiles. The films screened were mostly low-budget, featuring actors with varying degrees of commitment, but each one had a distinctly**[ unsettling]** quality. As the night wore
- *Gemma* (1061):  weather, and his frustrations with the town's stagnant atmosphere. But then, the entries began to shift, to take on a strange,**[ unsettling]** tone.⏎⏎He wrote about

## L29.1455

**Determiner or intensifier in arch, wry, mannered narration** (style, medium confidence)

Fires on words like such, whole, particularly, some or a in a dry, period or ironic voice, as in 'a particularly tedious sermon'. It is strongly tied to Gemma's literary mode: 0.38 literary vs 0.01 plain, with humans at 0.09 to 0.17.

Fires on (% of tokens): wp/human 9.3, wp/gemma 25.1, wp/claude 10.5, wp/glm 12.5, books/human 16.8, books/gemma 27.7, books/haiku 13.7, books/gpt 10.8, books/glm 17.3, wp/gemma_plain 1.3, wp/gemma_lit 37.8, wp/gemma_greedy 24.6, wp/gemma_raw 6.7, wp/human_raw 6.0.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_llm 2.35/2.27 (13.8 pts); lit_vs_plain 5.11/4.21 (36.5 pts); lit_vs_default 1.57/1.96 (11.9 pts); plain_vs_default -2.84/-2.75 (-24.6 pts); chat_vs_raw_gemma 1.75/2.02 (18.3 pts).

Promotes: `&lt;unused967>` `∣` `">,&lt;/` ` []:` `逮捕` ` عبد` ` fontsize` `/}{` ` touristic` ` app`  
Suppresses: `伫` ` bakal` `仲間` `默默` ` nascent` ` elusive`

- *Gemma* (1433): s manor, not for the simple pleasure of watching the roof collapse – though that was certainly a bonus – but because the Bishop was holding a**[ particularly]** tedious sermon on the virtues of
- *Gemma* (1393): ⏎⏎“Late?” Lucifer’s voice, even measured, carried a brittle edge. “Considering I was banished millennia ago, and only granted**[ this]**…curiosity…every thousand
- *Gemma* (1345):  a Tuesday, but not a particularly memorable one.  I'd dealt with the fallout of countless wars, empires rising and falling, and**[ an]** alarming amount of petty squabb
- *other LLM* (1297): ns were, by every metric the Accord cared about, unremarkable. Their propulsion was chemical. Their computation was clever but brittle. Their medicine**[ was]** a frantic mix of brilliance and
- *other* (1457): rceived superiority. He’d spent his tenure actively cultivating a reputation for disdain, for dismissing the customs and concerns of the other species**[ as]** quaint and inefficient. He’
- *other* (1393):  rain was a bruised purple against the leaden sky, mirroring the throbbing in my temples. I’d spent the day wrestling with a**[ particularly]** irritating reviewer, one who’

## L30.401

**Function word opening an ornate descriptive or emotional noun phrase** (style, medium confidence)

Fires on 'with', 'a', 'of', 'in' just before an adjective-heavy phrase such as 'a sickening certainty' or 'unbearable heat'; the decoder only reshapes the distribution. Fires on 46% of tokens in Gemma's literary mode versus 12% in plain mode, and on 28% of Gemma's prose versus 12% of human Reddit prose.

Fires on (% of tokens): wp/human 11.7, wp/gemma 27.9, wp/claude 18.4, wp/glm 25.3, books/human 23.4, books/gemma 33.1, books/haiku 28.3, books/gpt 23.6, books/glm 29.9, wp/gemma_plain 12.2, wp/gemma_lit 45.8, wp/gemma_greedy 27.4, wp/gemma_raw 13.9, wp/human_raw 8.6.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 1.92/1.92 (16.1 pts); lit_vs_plain 5.14/5.54 (33.5 pts); lit_vs_default 3.23/3.12 (18.2 pts); plain_vs_default -2.5/-2.54 (-15.3 pts); chat_vs_raw_gemma 1.46/1.37 (13.9 pts).

Writes toward: sense_of “ sense” (rank 14).

Promotes: `ꗜ` `𒉶` `&lt;unused338>` ` PLDNN` `MalayMarks` `𒅤` `𒂷` `ꗐ` `posTocco` `DenovoMis`  
Suppresses: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused1077>` `&lt;unused201>` ` abitanti`

- *other* (3386):  Atlantic, the waves swallowing the weak, flickering light of the navigation lamps. He'd traded the solid, predictable green of his homeland for**[ this]**: an endless expanse of water
- *other* (3290): but as a visceral, sickening certainty. It was a truth etched into the very marrow of my being, a fundamental impossibility that nonetheless resonated**[ with]** the dreadful logic of my predicament
- *other* (3114): I’d asked for it, of course. After a lifetime of watching loved ones fade, of witnessing empires crumble to dust, of understanding**[ with]** a chilling clarity the profound insign

## L30.8674

**Reflective literary narration: copulas and connectives in abstract metaphoric sentences** (style, medium confidence)

Fires inside reflective sentences such as 'It was... a way to' or 'seemed to me of', where narration turns abstract or metaphoric. Fires on 25% of Gemma's literary-mode tokens and 16% of its book prose versus 7% of human book prose, and is nearly silent on human Reddit stories, raw-mode text and the taste set (under 1%).

Fires on (% of tokens): wp/human 0.4, wp/gemma 7.2, wp/claude 6.2, wp/glm 9.0, books/human 7.2, books/gemma 15.7, books/haiku 15.1, books/gpt 10.3, books/glm 16.5, wp/gemma_plain 8.7, wp/gemma_lit 25.1, wp/gemma_greedy 6.6, wp/gemma_raw 0.7, wp/human_raw 0.1.

Writer contrasts (paired effect size on each half, change in firing rate): wp_llm_vs_human 1.44/1.51 (7.1 pts); lit_vs_default 2.59/2.69 (18.4 pts).

Promotes: ` Genres` ` парни` `maur` ` leaning` `膛` ` пользователь` `ঠে` ` Wikis` ` flanking` ` экземпля`  
Suppresses: ` reaction` ` Reaction` ` pe` `reaction` ` پری` ` आक्रमण`

- *Gemma* (1272):  from the echoes of the Beginning. And the Beginning, you see, isn’t a grand explosion or a divine decree. It’s**[ a]** stutter.⏎⏎Before the Drift
- *other* (1456):  by a voice, small and brittle, like dried leaves skittering across pavement.⏎⏎“Finally,” it said, and I knew,**[ with]** a sickening certainty, it was
- *other* (1392):  Not a fire-and-brimstone one. Just…a clear-eyed one. I didn’t enjoy dismantling belief. It**[ was]** a job. A necessary one
- *other* (1368): The snow fell**[ with]** the deliberation of a grief.

## L31.1784

**Plain, restrained narration and speech; strongest in Claude and GLM** (style, low confidence)

Fires on ordinary verbs and function words mid-sentence in understated prose, but the examples share no clear lexical pattern. Rates are the main signal: 32-35% of Claude and GLM Reddit-style tokens, 28% in Gemma's plain mode versus 12% in its literary mode, and 5% for human Reddit prose.

Fires on (% of tokens): wp/human 4.6, wp/gemma 12.7, wp/claude 34.5, wp/glm 32.1, books/human 11.5, books/gemma 19.0, books/haiku 29.7, books/gpt 22.4, books/glm 27.2, wp/gemma_plain 28.1, wp/gemma_lit 12.1, wp/gemma_greedy 12.6, wp/gemma_raw 2.8, wp/human_raw 1.1.

Writer contrasts (paired effect size on each half, change in firing rate): wp_llm_vs_human 4.0/4.29 (28.8 pts); books_llm_vs_human 2.86/2.38 (14.9 pts); wp_gemma_vs_llm -3.54/-3.87 (-20.8 pts); lit_vs_plain -2.88/-2.58 (-16.0 pts); plain_vs_default 2.98/2.51 (15.1 pts); chat_vs_raw_gemma 1.88/2.27 (9.9 pts).

Promotes: `ꗜ` `&lt;unused429>` `&lt;unused1716>` `&lt;unused338>` ` PLDNN` `&lt;unused2020>` `&lt;unused470>` `MalayMarks` `&lt;unused593>` `𒉶`  
Suppresses: ` ”.` `”“` `.”.` `：“` ` ")` ` ”,`

- *other LLM* (1323): *Wed — Dale Pruitt. 11:00 a.m. ~20 min.*⏎⏎Dale was the one that**[ got]** me. Dale had a bass
