# Abstraction and summary

20 features. [Back to the index](../ATLAS.md)

| Feature | Label | Kind | Conf. | G | H | L | Promotes |
|---|---|---|---|---|---|---|---|
| [L1.496](#l1496) | Abstract quality and emotion nouns (rigidity, tenderness, sadness) | style | high | 3.6 | 1.2 | 0.7 | ꗜ 𒅤 𒉶 ꗐ  PLDNN |
| [L3.277](#l3277) | Evaluative noun after 'a' (mockery, marvel, insult, disgrace) | lexical | medium | 9.2 | 4.3 | 3.9 | ꗜ 𒉶 &lt;unused338>  PLDNN 𒅤 |
| [L7.10455](#l710455) | Indefinite 'something', 'anything' and 'the same thing' | lexical | high | 0.6 | 0.5 | 0.7 | &lt;unused687> &lt;unused1166> � &lt;unused192> &lt;unused201> |
| [L10.769](#l10769) | Start of an expository definition of an invented thing | construction | medium | 0.4 | 0.2 | 0.2 | &lt;unused1166> &lt;unused687> � &lt;unused201> &lt;unused1170> |
| [L17.349](#l17349) | Abstract head nouns (quality, solution, decision, circumstances) | lexical | high | 8.9 | 6.9 | 5.1 | ꗜ 𒉶  PLDNN 𒅤 &lt;unused338> |
| [L18.436](#l18436) | Period ending a long expository or premise-setting sentence | structure | medium | 6.0 | 5.3 | 6.0 | � &lt;unused1166> &lt;unused687> &lt;unused201> &lt;unused366> |
| [L19.4610](#l194610) | something as a vague object, often after a preposition | lexical | high | 0.5 | 0.3 | 0.5 |  غ  Пи getStock  высоко  ટ |
| [L20.294](#l20294) | Abstract category nouns (premise, tactic, phenomenon, feeling) | lexical | high | 5.6 | 3.1 | 2.8 | � 걔  வ &lt;unused687> &lt;unused201> |
| [L21.486](#l21486) | Evaluative adjective in 'It was a ___ thing' descriptions | construction | medium | 4.3 | 1.3 | 0.6 | &lt;unused201>  gummies &lt;unused1166> � &lt;unused687> |
| [L22.2476](#l222476) | Head noun closing an adjective-modified phrase, often abstract | style | medium | 16.1 | 6.1 | 9.4 |  particularly imeters  soprattutto mittedly  wiem |
| [L23.223](#l23223) | Abstract noun heading a phrase ('context', 'pattern', 'approach') | lexical | high | 11.6 | 6.7 | 6.6 | � &lt;unused1166> &lt;unused687> &lt;unused201> &lt;unused192> |
| [L24.184](#l24184) | Abstract emotion or quality noun after 'with', 'of' or 'and' | lexical | medium | 26.9 | 17.0 | 19.4 |  long long  LONG Long LONG |
| [L24.270](#l24270) | Abstract noun after an evaluative adjective ('unsettling grace') | style | medium | 8.6 | 3.0 | 3.8 | &lt;unused192> &lt;unused687> &lt;unused201> &lt;unused2040> � |
| [L27.650](#l27650) | Abstract nouns of mind and judgment (awareness, doubt, ignorance) | lexical | high | 13.6 | 6.8 | 5.7 |  किए  किये தான  unbe 迟 |
| [L29.92](#l2992) | Abstract noun ending a clause: understanding, clarity, support, depth | content | medium | 13.1 | 10.6 | 9.4 | 𒉶  PLDNN ꗜ MalayMarks 𒅤 |
| [L30.187](#l30187) | 'a' opening an appositive or predicate that sums up a scene | construction | medium | 12.7 | 4.0 | 5.7 | 𒉶 𒅤 MalayMarks  PLDNN doneProcessAvg |
| [L31.190](#l31190) | Generic category noun heading a descriptive or appositive phrase | style | medium | 16.5 | 10.2 | 11.9 | &lt;unused1170> &lt;unused687> &lt;unused201>  افراد &lt;unused673> |
| [L32.219](#l32219) | Head noun of a characterizing phrase such as 'a hollow performance' | construction | medium | 6.8 | 0.8 | 1.9 | &lt;unused687>  gummies ución 於  افراد |
| [L32.526](#l32526) | Elaborating phrases about searching for meaning; Gemma literary | style | low | 21.2 | 5.2 | 9.7 | &lt;unused201> � &lt;unused1012>  chopped &lt;unused995> |
| [L33.449](#l33449) | Article or evaluative adjective in 'was a [adj] noun' phrases | predictive | medium | 24.1 | 8.8 | 13.6 | &lt;unused687> &lt;unused1166> � &lt;unused201> &lt;unused366> |

## L1.496

**Abstract quality and emotion nouns (rigidity, tenderness, sadness)** (style, high confidence)

Fires on abstract nouns naming a state or quality, mostly -ness and -ity words, with rigidity strongest. Gemma fires three times as often as humans (0.036 vs 0.012) and seven times as often as Claude; Gemma literary 0.049 vs plain 0.011.

Fires on (% of tokens): wp/human 1.2, wp/gemma 3.6, wp/claude 0.5, wp/glm 0.9, books/human 1.1, books/gemma 3.3, books/haiku 0.7, books/gpt 0.7, books/glm 1.1, wp/gemma_plain 1.1, wp/gemma_lit 4.9, wp/gemma_greedy 3.5, wp/gemma_raw 3.0, wp/human_raw 1.1.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.11/2.14 (2.2 pts); wp_gemma_vs_llm 2.38/2.49 (2.9 pts); books_gemma_vs_llm 2.43/2.57 (2.4 pts); lit_vs_plain 3.15/2.8 (3.7 pts).

Constructions: abstract.

Promotes: `ꗜ` `𒅤` `𒉶` `ꗐ` ` PLDNN` `𒂷` `MalayMarks` `&lt;unused338>` `DenovoMis` `doneProcessAvg`  
Suppresses: `&lt;unused687>` `�` `&lt;unused201>` `&lt;unused673>` `čnog` `&lt;unused1166>`

- *human* (74):  "Doesn't mom tell you not to swear?"⏎⏎"When she's around," Young Jon said, and Old Jon felt the**[ sadness]** as if it has been his
- *human* (74):  of their own mortality. You died when you died at a random point in time, and that was it. There was a simplicity in the**[ randomness]** that was comforting in a way
- *human* (71):  breath*...⏎⏎I can't...⏎⏎The whole of the language that gives me these words is calling out, reaching for me with**[ tenderness]** even in its limitless artificiality
- *Gemma* (79):  fear, of whispers and shunning. My mother had borne Lyra, and when the child began to react to everything, to absorb the**[ sadness]** and anxieties of the town,
- *Gemma* (77):  moan.⏎⏎Elias, for the first time in a very long time, felt a flicker of genuine curiosity. He manifested a little more**[ solidity]**, just enough to observe with
- *Gemma* (76): .⏎⏎Elias tried to ignore him. He told himself it was a trick of the light, a delusion born of years spent absorbing the**[ sadness]** of others. But Silas persisted

## L3.277

**Evaluative noun after 'a' (mockery, marvel, insult, disgrace)** (lexical, medium confidence)

Fires on a judgment noun completing 'a ...', as in felt like a mockery or was a marvel. Gemma fires about twice as often as humans and three times GPT, and literary Gemma four times more than plain.

Fires on (% of tokens): wp/human 4.3, wp/gemma 9.2, wp/claude 3.3, wp/glm 4.5, books/human 3.6, books/gemma 8.4, books/haiku 3.0, books/gpt 2.4, books/glm 3.7, wp/gemma_plain 3.0, wp/gemma_lit 11.8, wp/gemma_greedy 8.9, wp/gemma_raw 5.9, wp/human_raw 4.0.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.3/2.29 (4.8 pts); books_gemma_vs_human 2.27/2.67 (4.7 pts); wp_gemma_vs_llm 2.91/2.95 (5.3 pts); books_gemma_vs_llm 2.98/3.3 (5.3 pts); lit_vs_plain 3.72/4.74 (8.8 pts); plain_vs_default -2.96/-3.21 (-6.1 pts); chat_vs_raw_gemma 1.55/1.28 (3.2 pts).

Promotes: `ꗜ` `𒉶` `&lt;unused338>` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `𒂷` `DenovoMis` `odikwa`  
Suppresses: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` ` cercando` `&lt;unused1077>`

- *human* (128):  the center of his stomach. They had been so vague. It disgusted him to question his own son, who had never been less than a**[ marvel]**, but what could it be
- *human* (122): . From the moment she'd stepped into the hospital she'd already resigned to her fate. The disease was really more of an accidental**[ mishap]** on some scientists who were attempting
- *human* (120):  would squeeze the person in half. I called it Uchikudaku-Haku (Shatter Hug). The criminals face is a**[ blur]** to me now, little more
- *Gemma* (133):  leached from every cast, every haul. The silver flash of a mackerel, the satisfying weight of a cod – they all felt like a**[ mockery]**. I saw Eleanor in every
- *Gemma* (130):  me as the dampness in the concrete walls. Twenty-eight-seven years. It felt…less substantial than it should. Not a**[ triumph]**, certainly, but a dull
- *Gemma* (130):  book and a vow of solitary darkness.⏎⏎It had become our routine. Every. Single. Morning. Leo, usually a vibrant, energetic**[ whirlwind]**, reduced to a muted version

## L7.10455

**Indefinite 'something', 'anything' and 'the same thing'** (lexical, high confidence)

Fires on indefinite nouns like 'something', 'anything', 'everything' and 'thing' in 'the same thing'. Rates are even across writers.

Fires on (% of tokens): wp/human 0.5, wp/gemma 0.6, wp/claude 0.7, wp/glm 0.7, books/human 0.5, books/gemma 0.5, books/haiku 0.7, books/gpt 0.5, books/glm 0.8, wp/gemma_plain 0.9, wp/gemma_lit 0.5, wp/gemma_greedy 0.6, wp/gemma_raw 0.6, wp/human_raw 0.5.

Constructions: something.

Promotes: `&lt;unused687>` `&lt;unused1166>` `�` `&lt;unused192>` `&lt;unused201>` `&lt;unused1077>` `&lt;unused366>` `&lt;unused1170>` `&lt;unused1207>` `&lt;unused108>`  
Suppresses: `ꗜ` `𒉶` `𒅤` `ꗐ` ` PLDNN` `&lt;unused338>`

- *human* (219): ve never dreamed I was naked at school,” I sighed, I wondered why people took it so personally that I never had nightmares. The same**[ thing]** happens to people who can’
- *human* (214): .⏎⏎The nurse looked hesitantly at his still form for a moment. Then: "Just stay out of the way. It's**[ something]** he needs to work through on
- *Gemma* (213):  Perfect for a proposal. I’d spent the last week obsessing over the ring, a vintage sapphire nestled in a delicate platinum band –**[ everything]** about it screamed ‘forever.’
- *Gemma* (205):  was Lucifer. Even in a borrowed identity – Harold Finch, retired librarian – the lingering scent of brimstone followed him. He'd tried**[ everything]**. He'd donated to
- *other LLM* (247):  woman with a long brown braid and a sunburned nose, laughing at something outside the frame.⏎⏎*Ruth.*⏎⏎The name arrives before**[ anything]** else. Not a memory exactly
- *other LLM* (233):  at the kitchen table. He looks at his pills. He takes one, because he is good, or tired, which is almost the same**[ thing]**."⏎⏎"You counted wrong

## L10.769

**Start of an expository definition of an invented thing** (construction, medium confidence)

Fires on the word that opens a defining description of a new concept (by which, where, that, a, composed of), typical of worldbuilding exposition. Rare everywhere (0.002 to 0.004, slightly higher in Gemma); its taste-set rate (0.009 approved, 0.012 rejected) is one token per text: it fires on the first text token after BOS, which only taste texts expose, so the rejected/approved gap reflects shorter rejected texts.

Fires on (% of tokens): wp/human 0.2, wp/gemma 0.4, wp/claude 0.2, wp/glm 0.2, books/human 0.2, books/gemma 0.2, books/haiku 0.2, books/gpt 0.2, books/glm 0.2, wp/gemma_plain 0.3, wp/gemma_lit 0.4, wp/gemma_greedy 0.5, wp/gemma_raw 0.3, wp/human_raw 0.2.

Promotes: `&lt;unused1166>` `&lt;unused687>` `�` `&lt;unused201>` `&lt;unused1170>` `&lt;unused366>` `&lt;unused1077>` `&lt;unused192>` `.&lt;/` `&lt;unused108>`  
Suppresses: `ꗜ` `&lt;unused338>` ` PLDNN` `𒉶` `𒅤` `MalayMarks`

- *human* (175):  barren wastelands that could barely support life. In between these two extreme zones existed a Goldilocks zone, and this is the zone**[ where]** 99 percent of this
- *human* (174):  great Boarrog, a wild warthog that roamed the farmlands of the southeast Emthorn Woods. Boarrog was**[ an]** elite level 11 beast
- *human* (142): most efficient manner though, and proceeded to release it into the populace. An artificially constructed virus based off the common cold, but modified**[ to]** carry a negative charge that would
- *Gemma* (210):  regret. It always did now. I adjusted the humidity sensors on my bio-acoustic dampening system – a delicate, custom-built device**[ that]** looked like a Victorian diving helmet
- *Gemma* (200):  it. Not the feeling itself, not the melancholy, but the resonance.⏎⏎I’d call it Chronosync. It’s**[ a]** condition I developed – or rather
- *Gemma* (197): ling a complex machine with surgical tools. ⏎⏎My current assignment was particularly delicate. The Kryll Collective, a sprawling, decentralized entity**[ composed]** of millions of individual units,

## L17.349

**Abstract head nouns (quality, solution, decision, circumstances)** (lexical, high confidence)

Fires on abstract nouns after a determiner or adjective, such as quality, precedent, arrangement or result, often before 'of' or a colon. Gemma uses them about twice as often as Claude and GPT (8.9% vs 4.4%), most in literary mode.

Fires on (% of tokens): wp/human 6.9, wp/gemma 8.9, wp/claude 4.4, wp/glm 5.9, books/human 4.7, books/gemma 8.4, books/haiku 4.3, books/gpt 4.0, books/glm 4.8, wp/gemma_plain 5.8, wp/gemma_lit 10.4, wp/gemma_greedy 8.8, wp/gemma_raw 7.8, wp/human_raw 5.8.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_llm 2.5/2.64 (3.8 pts); books_gemma_vs_llm 2.95/2.94 (4.1 pts).

Constructions: abstract.

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒅤` `&lt;unused338>` `ꗐ` `MalayMarks` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` `&lt;unused192>` `&lt;unused1077>`

- *human* (2582):  of Guam."⏎⏎Marty had actually been too thunderstruck to even consider what the heck was wrong with Guam before turning his attention to the**[ question]** of wishes. The first wish
- *human* (2438):  mask he could have been a banker or CEO for a Wall Street firm. Marcus figured the mask was from an Asian shop based on the monstrous**[ look]** made out in bright colors and
- *human* (2438): , then realized every time a worker⏎⏎came into my room, they asked me what I was doing there. I went⏎⏎through the same**[ process]** to get accepted into the orphanage
- *Gemma* (2758):  nightmares didn’t sound like that. I bolted upright, heart hammering against my ribs, and stumbled out of bed, instantly regretting my**[ choice]** of flannel pajamas.⏎⏎My
- *Gemma* (2614):  a… minor grievance,” she’d said, adjusting her spectacles. “A chronic case of petty annoyances. There’s a historical**[ precedent]** for this sort of thing,
- *Gemma* (2534): , the Architects – beings whose names are now lost to legend – realized that direct combat against the Immortals was futile. They devised a**[ solution]** far more insidious: a dimensional

## L18.436

**Period ending a long expository or premise-setting sentence** (structure, medium confidence)

Fires on the period that closes a long sentence of world-building or backstory summary, often in speculative premises. Plain-mode Gemma fires on 13% of tokens against about 5-6% for every other writer; the decoder only reshapes the distribution.

Fires on (% of tokens): wp/human 5.3, wp/gemma 6.0, wp/claude 6.0, wp/glm 6.1, books/human 5.1, books/gemma 5.6, books/haiku 5.9, books/gpt 7.1, books/glm 5.1, wp/gemma_plain 13.4, wp/gemma_lit 5.1, wp/gemma_greedy 6.0, wp/gemma_raw 6.5, wp/human_raw 5.2.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_plain -4.23/-4.44 (-8.3 pts); lit_vs_default -1.01/-1.02 (-0.9 pts); plain_vs_default 3.99/3.88 (7.4 pts).

Promotes: `�` `&lt;unused1166>` `&lt;unused687>` `&lt;unused201>` `&lt;unused366>` `&lt;unused1077>` `.&lt;/` `&lt;unused1170>` `&lt;unused2040>` `Referências`  
Suppresses: `ꗜ` `𒉶` ` PLDNN` `𒅤` `ꗐ` `&lt;unused338>`

- *human* (1607):  extreme zones existed a Goldilocks zone, and this is the zone where 99 percent of this world’s life would be supported**[.]** This zone was soaked with ocean
- *human* (1479):  and weapons of mass destruction used pins as a fail safe to prevent the thing from being turned on without a moral decision being made to activate it**[.]**⏎⏎However the room remained quite
- *human* (1479): eativity to create fire balls. The Ice Wizard had been stopping fire balls for thousands of years and thought them the easiest fire ability to counter**[.]**⏎⏎The boy had grown up
- *Gemma* (1367): mething to prevent a global panic and potential collapse. North Korea, with its fervent nationalism and unquestioning loyalty, became the perfect tool**[.]**⏎⏎For sixty years, we
- *Gemma* (1359):  inexplicably altered menu items at rival establishments – a surprisingly spicy Big Mac at Burger King, a subtly different blend of salsa at Taco Bell**[.]**⏎⏎However, the technology they
- *Gemma* (1359):  it introduced the seed of differentiation. It was a preference for one state of being over another, a tiny flicker of ‘not-singularity**[.’]** This wasn't a conscious

## L19.4610

**something as a vague object, often after a preposition** (lexical, high confidence)

Fires on something as a vague object or complement, as in longing for something beyond or burdened by something. Rare (under 1% of tokens) and similar across all writers.

Fires on (% of tokens): wp/human 0.3, wp/gemma 0.5, wp/claude 0.6, wp/glm 0.5, books/human 0.3, books/gemma 0.5, books/haiku 0.7, books/gpt 0.4, books/glm 0.7, wp/gemma_plain 0.6, wp/gemma_lit 0.6, wp/gemma_greedy 0.4, wp/gemma_raw 0.5, wp/human_raw 0.3.

Constructions: something.

Promotes: ` غ` ` Пи` `getStock` ` высоко` ` ટ` ` सा` `ரியில்` ` trông` ` 풍` `耑`  
Suppresses: `eners` `ć` ` Dinge` ` प्राणियों` ` qualities` `特点`

- *human* (693):  the screams as the demons tore through their bodies and armor. War cries, exclamations of pain, and pleading whimpers calling out for**[ something]** safe and lost.⏎⏎Many
- *human* (689):  growing problems. It would be dawn soon, and it would be her shift. If loneliness haunted her, the darkness in her soul longed for**[ something]** as mundane as loneliness when she
- *human* (681):  enlisted crew members. The officers ’ mess hall was quieter and had actual food instead of the slop that they served below. But Vivian needed**[ something]** more than pastries.⏎⏎Sal
- *other LLM* (737): . Wolves volunteered. Long ago, when your people first made fire, they saw the size of the dark around it, and they wept.**[ Something]** had to be done. We
- *other LLM* (729): . Gray coming in at the temples where my mother's gray started. My hands, but wrung out — hands that had been carrying**[ something]** heavy for a long time.
- *other LLM* (729):  core belief, intact humor, no apparent distress about content* in my notes, and underneath it, after a moment, *distress about**[ something]** else*.⏎⏎---⏎⏎The

## L20.294

**Abstract category nouns (premise, tactic, phenomenon, feeling)** (lexical, high confidence)

Fires on abstract nouns that name an idea or situation: premise, tactic, solution, phenomenon, feeling, explanation, concept. Gemma uses it about twice as often as other writers, including in assistant-style commentary after a story.

Fires on (% of tokens): wp/human 3.1, wp/gemma 5.6, wp/claude 2.5, wp/glm 3.1, books/human 2.0, books/gemma 5.6, books/haiku 2.3, books/gpt 1.9, books/glm 2.5, wp/gemma_plain 2.4, wp/gemma_lit 6.3, wp/gemma_greedy 5.4, wp/gemma_raw 4.8, wp/human_raw 2.8.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.81/2.66 (3.5 pts); wp_gemma_vs_llm 2.33/2.61 (2.8 pts); books_gemma_vs_llm 2.8/2.85 (3.3 pts); plain_vs_default -1.94/-2.42 (-3.1 pts).

Constructions: abstract.

Promotes: `�` `걔` ` வ` `&lt;unused687>` `&lt;unused201>` `&lt;unused1083>` ` anise` ` افراد` `.&lt;/` ` lubrication`  
Suppresses: `ꗜ` `𒉶` `𒅤` `&lt;unused338>` `𒂷` `ꗐ`

- *human* (782): Hi!" she said with a smile, I promptly closed the door.⏎⏎"Go away" I said, probably too high to realise the**[ scenario]** I was plagued with. She
- *human* (766):  a fireball or one of her other abilities, she growled, "Stop!"⏎⏎Sparx came up short, confused by this strange new**[ tactic]**. "Why should I believe
- *human* (738):  That was certainly not the feeling I had had all those times I dreamt about him. Those dreams - or rather nightmares - always had the same**[ premise]**. A sparkling hope.. only
- *Gemma* (838): omforting haze of my digital world. I started researching, scouring online forums dedicated to fantasy writing, searching for any mention of a similar**[ phenomenon]**. There was nothing. Just
- *Gemma* (838): … observing. Like watching a play, but I wasn’t an audience member, I was the stage.”⏎⏎I struggled to articulate the**[ feeling]**. “It was beautiful,
- *Gemma* (782):  chronometer, a complex assemblage of vacuum tubes, spinning gyroscopes, and enough copper wiring to choke a small elephant. “The entire**[ premise]** is fundamentally flawed.”⏎⏎The

## L21.486

**Evaluative adjective in 'It was a ___ thing' descriptions** (construction, medium confidence)

Fires on a judging adjective inside a predicate noun phrase (a complicated thing, a comfortable, predictable routine, a ridiculously specific wish). Gemma fires on it about six times as often as Claude, GLM or GPT and three times as often as humans (wp 0.043 vs 0.006 and 0.013).

Fires on (% of tokens): wp/human 1.3, wp/gemma 4.3, wp/claude 0.6, wp/glm 0.7, books/human 1.3, books/gemma 4.5, books/haiku 0.8, books/gpt 0.7, books/glm 1.1, wp/gemma_plain 1.4, wp/gemma_lit 5.5, wp/gemma_greedy 4.2, wp/gemma_raw 2.7, wp/human_raw 1.3.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.61/2.47 (3.0 pts); books_gemma_vs_human 2.62/2.67 (3.1 pts); wp_gemma_vs_llm 3.62/3.54 (3.7 pts); books_gemma_vs_llm 3.03/3.23 (3.6 pts); lit_vs_plain 3.28/3.44 (4.2 pts); plain_vs_default -2.79/-2.43 (-2.9 pts); raw_gemma_vs_human 1.17/1.33 (1.4 pts).

Promotes: `&lt;unused201>` ` gummies` `&lt;unused1166>` `�` `&lt;unused687>` `&lt;unused1077>` ` cercando` `iseen` ` MOQ` `Referências`  
Suppresses: `ꗜ` `𒉶` `𒅤` `&lt;unused338>` `ꗐ` ` PLDNN`

- *human* (1543):  like half of your life in your world happened upon it."⏎⏎I smiled wryly at how right she was. "It's a**[ complicated]** thing to understand. You need
- *human* (1463): 45 to catch an early client meeting, and his commute had only taken him fifteen minutes, but he widely considered leaving that early a very**[ impractical]** waste of his time. What
- *Gemma* (1671):  the market stalls, even the damp wool of my coat. I’d spent my twenty-four years in this town, a comfortable,**[ predictable]** sort of existence as a book
- *Gemma* (1671):  it can also bring you ruin.”⏎⏎My first wish, at five, had been for a mountain of strawberry jam. It was a ridiculously**[ specific]** wish, granted instantly, filling
- *Gemma* (1639): ’d spent my life as Arthur Penhaligon, a middle-school librarian in Poughkeepsie, New York. Not a particularly**[ exciting]** life, if I’m
- *other LLM* (1399):  detail: she was driving home with a cake for my birthday. People like the cake. It makes them sorry for me in a clean,**[ uncomplicated]** way.⏎⏎The truth is

## L22.2476

**Head noun closing an adjective-modified phrase, often abstract** (style, medium confidence)

Fires on the noun that ends a decorated noun phrase, mostly abstract ones like 'quiet desperation' or 'unhurried authority', sometimes concrete ('frying oil'). Promotes 'particularly' and 'especially'. Gemma fires about 2.5 times as often as humans, and literary Gemma is more than three times plain Gemma.

Fires on (% of tokens): wp/human 6.1, wp/gemma 16.1, wp/claude 8.4, wp/glm 10.4, books/human 5.6, books/gemma 13.0, books/haiku 7.6, books/gpt 5.9, books/glm 8.2, wp/gemma_plain 5.7, wp/gemma_lit 20.0, wp/gemma_greedy 15.8, wp/gemma_raw 8.4, wp/human_raw 4.9.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.63/2.6 (10.0 pts); books_gemma_vs_human 2.64/2.83 (7.5 pts); wp_gemma_vs_llm 2.53/2.28 (6.8 pts); books_gemma_vs_llm 2.92/2.87 (5.8 pts); lit_vs_plain 4.11/4.79 (14.3 pts); lit_vs_default 1.37/1.61 (3.8 pts); plain_vs_default -3.0/-3.37 (-10.5 pts); chat_vs_raw_gemma 1.83/1.56 (7.8 pts).

Promotes: ` particularly` `imeters` ` soprattutto` `mittedly` ` wiem` `TableRow` ` liberated` `ския` ` కంటే` ` especially`  
Suppresses: `শায়` `াড়ি` ` فت` ` రాజ` ` মেয়ে` ` চাঁ`

- *human* (600): . Aren't we pressing our luck with this?" asked James. He sat in a leather upholstered chair at a mahogany desk, cluttered with**[ paperwork]** and pens, an amazing view
- *Gemma* (764):  gothic behemoth whispered to be built on the site of a tragic love affair. He’d inherited it, along with a legacy of quiet**[ desperation]** and a single, carefully worded
- *Gemma* (760):  started to read. The words felt strange, alien yet undeniably his own. The prose was clunky, overwritten in places, riddled with breathless**[ enthusiasm]** and a complete disregard for subtlety
- *other* (816):  the etymological roots of increasingly obscure words. I’d initially dismissed him as another pedant, lost in a maze of linguistic minut**[iae]**. But as our conversations deepened
- *other* (800):  the cobblestones, slicking them with a mournful sheen, and seeped into the cracks of the ancient buildings, whispering tales of forgotten**[ sorrows]**. October was a particularly potent
- *other* (776):  to the relentless, sickening beauty of this world. A world saturated in color, in the impossible, in a relentless, exhausting parade of stylized**[ excess]**. And, increasingly, in

## L23.223

**Abstract noun heading a phrase ('context', 'pattern', 'approach')** (lexical, high confidence)

Fires on abstract nouns that close a noun phrase, often after 'a different' or 'no' (shape, context, interpretation, breakthrough). The decoder output is junk. Gemma fires about twice as often as humans and other models.

Fires on (% of tokens): wp/human 6.7, wp/gemma 11.6, wp/claude 6.1, wp/glm 7.1, books/human 5.7, books/gemma 10.3, books/haiku 6.5, books/gpt 6.1, books/glm 6.6, wp/gemma_plain 9.7, wp/gemma_lit 12.8, wp/gemma_greedy 11.6, wp/gemma_raw 11.5, wp/human_raw 7.0.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.32/2.25 (4.9 pts); books_gemma_vs_human 2.71/2.57 (4.6 pts); wp_gemma_vs_llm 3.22/3.08 (5.0 pts); books_gemma_vs_llm 2.65/2.86 (3.9 pts); raw_gemma_vs_human 1.74/1.66 (4.5 pts).

Constructions: abstract.

Promotes: `�` `&lt;unused1166>` `&lt;unused687>` `&lt;unused201>` `&lt;unused192>` `&lt;unused1077>` `&lt;unused673>` `&lt;unused366>` `&lt;unused2040>` `.&lt;/`  
Suppresses: `ꗜ` `𒉶` ` PLDNN` `𒅤` `MalayMarks` `ꗐ`

- *human* (2318):  have only ever landed on their natural satellite, despite a system rich in planets to explore, and take for themselves. They are an obvious easy**[ adversary]**, either too stupid or too
- *human* (2238):  but it seemed to calm me down a little bit. The long slender body beside me moved and then settled down again. She was a good**[ distraction]** from the impending doom on the
- *human* (2158):  having the same effect, as they slowly lifted themselves off the concrete floor. Three others were pounding on the walls, yelling, looking for an**[ answer]** that the concrete walls may have
- *Gemma* (2606):  anything, that could trigger a memory, a clue to my identity. But the text was impenetrable, a series of abstract symbols that offered no**[ context]** or explanation. ⏎⏎As
- *Gemma* (2558):  countless timepieces. But it wasn’t enough. The query remained, unyielding.⏎⏎I stumbled through the workshop, searching for a**[ pattern]**, a clue. I examined
- *Gemma* (2494):  rain continued to smell of iron and regret. The pigeons continued to watch.⏎⏎Finally, exhaustion and a morbid curiosity led me to a different**[ approach]**. If I was in a

## L24.184

**Abstract emotion or quality noun after 'with', 'of' or 'and'** (lexical, medium confidence)

Fires on abstract nouns closing a phrase, mostly feelings (despair, doubt, loneliness, contempt) and some qualities (silence, warmth). Oddly promotes 'long'. It is dense (about 20% of tokens), and Gemma fires about 1.6 times as often as humans, literary Gemma most.

Fires on (% of tokens): wp/human 17.0, wp/gemma 26.9, wp/claude 17.4, wp/glm 21.5, books/human 15.2, books/gemma 24.5, books/haiku 18.9, books/gpt 17.2, books/glm 20.2, wp/gemma_plain 14.4, wp/gemma_lit 32.3, wp/gemma_greedy 26.8, wp/gemma_raw 21.1, wp/human_raw 16.1.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.43/2.34 (9.3 pts); lit_vs_plain 3.88/4.67 (17.9 pts); lit_vs_default 1.49/1.71 (5.4 pts); plain_vs_default -2.62/-3.01 (-12.5 pts).

Constructions: abstract, pre:semicolon.

Promotes: ` long` `long` ` LONG` `Long` `LONG` `长` `長` ` dług` ` Long` ` longo`  
Suppresses: ` UserDefaults` `zna` ` Tash` `ptosis` ` Raise` ` Curved`

- *human* (975):  had nothing to do with it, nothing to do with you... and you just..." The words hung in the air, the accusation full of**[ contempt]** and shock, and perhaps a
- *human* (923):  breath*...⏎⏎I can't...⏎⏎The whole of the language that gives me these words is calling out, reaching for me with**[ tenderness]** even in its limitless artificiality
- *human* (919): There was something about this place that reminded me of my past. My past, which I'd buried under layers and layers of lies and**[ deceit]** just to get where I am
- *Gemma* (1067):  a misplaced rock, a momentary pause in the music.  Just enough to make the new players question their reality, to plant a seed of**[ doubt]** in the pristine, brightly-
- *Gemma* (1059):  forgotten ruins, and drunk wine in centuries-old cellars. But the novelty had long worn off, replaced by a persistent, gnawing**[ loneliness]**. The world kept spinning,
- *Gemma* (1043):  My nemesis. The architect of nightmares, the connoisseur of chaos, the man who’d turned Oakhaven into a breeding ground for**[ anxieties]** and petty grievances for decades.

## L24.270

**Abstract noun after an evaluative adjective ('unsettling grace')** (style, medium confidence)

Fires on abstract nouns after an evaluating adjective (disconcerting grace, clinical approach, emotional impact), also in Gemma's critique-style text. The decoder output is junk. Gemma fires about 2.5 times as often as humans and other models.

Fires on (% of tokens): wp/human 3.0, wp/gemma 8.6, wp/claude 3.9, wp/glm 3.6, books/human 3.6, books/gemma 7.2, books/haiku 3.9, books/gpt 3.9, books/glm 3.9, wp/gemma_plain 7.1, wp/gemma_lit 9.0, wp/gemma_greedy 8.8, wp/gemma_raw 8.0, wp/human_raw 2.6.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 3.03/3.07 (5.6 pts); books_gemma_vs_human 2.14/2.14 (3.6 pts); wp_gemma_vs_llm 3.34/3.0 (4.8 pts); books_gemma_vs_llm 2.55/2.69 (3.3 pts); raw_gemma_vs_human 2.2/1.91 (5.4 pts).

Promotes: `&lt;unused192>` `&lt;unused687>` `&lt;unused201>` `&lt;unused2040>` `�` `&lt;unused1166>` `&lt;unused1170>` ` seva` `&lt;unused2197>` `álaga`  
Suppresses: `ꗜ` `&lt;unused338>` `𒅤` ` PLDNN` `ꗐ` `𒉶`

- *human* (1004): In the mythical land of Zootopia, which has absolutely no**[ relation]** to the Disney movie of the
- *Gemma* (1128):  Their skin was a deep, iridescent blue, and their eyes were large and black, utterly devoid of emotion. They moved with a disconcerting**[ grace]**, drifting down towards the grey
- *Gemma* (1128):  metallic foliage. Their faces were featureless, smooth and pale, with large, black, unblinking eyes. They moved with an unsettling**[ grace]**, gliding rather than walking,
- *Gemma* (1084): t need to fight. The desperation radiating from him, the sheer, bone-deep exhaustion etched on his face, was a far more potent**[ weapon]**. I’d learned long
- *other LLM* (1016): -six, strangled on the Mill Race path. No witnesses, no fibers, cameras dead. Body less than a day old — the best**[ condition]** I'd ever worked with
- *other* (1416):  it does not happen again.⏎I understand that my actions were a violation of established procedures and I deeply regret the oversight. I take full**[ responsibility]** for my lapse in judgment and

## L27.650

**Abstract nouns of mind and judgment (awareness, doubt, ignorance)** (lexical, high confidence)

Fires on abstract nouns such as 'consciousness', 'manipulation', 'awareness' and 'judgment', usually in object position. Twice as frequent in Gemma's stories as human ones and highest in literary-prompted Gemma; decoder output is junk.

Fires on (% of tokens): wp/human 6.8, wp/gemma 13.6, wp/claude 4.9, wp/glm 6.5, books/human 8.3, books/gemma 13.0, books/haiku 7.4, books/gpt 7.2, books/glm 9.0, wp/gemma_plain 4.7, wp/gemma_lit 15.8, wp/gemma_greedy 13.2, wp/gemma_raw 11.7, wp/human_raw 6.3.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_llm 2.8/2.52 (7.9 pts); lit_vs_plain 3.39/3.28 (11.0 pts); plain_vs_default -2.39/-2.95 (-8.6 pts).

Constructions: abstract.

Promotes: ` किए` ` किये` `தான` ` unbe` `迟` `Its` `gün` ` einzig` ` सम्` ` クラ`  
Suppresses: ` Inter` `rists` `omans` ` Ass` `effector` `———`

- *human* (914):  wall.⏎⏎He could never explain, he decided, as they would forever take his meaning to go out with his friends as wild, fanciful**[ imaginations]**. But, he felt,
- *other* (1134):  – demonstrate his need to control every aspect of Willem’s life. It's a way of asserting his dominance and maintaining a sense of**[ security]** (albeit a skewed and anxiety
- *other* (1078):  confirmation of our worth, our significance. And when that confirmation is withheld, we lash out, we become defensive, we attempt to control the**[ narrative]**, even if that means manipulating
- *other* (1070): , impossibly, finding a thread of dark amusement within it. It was, I realized with a sickening certainty, about confronting the absurdity of**[ existence]**, even in its most brutal

## L29.92

**Abstract noun ending a clause: understanding, clarity, support, depth** (content, medium confidence)

Fires on abstract nouns at the end of a phrase or clause, often before a semicolon or period, as in 'lacks specificity' or 'add depth'. Rates are flat across story writers (about 0.1) but low in the taste set (0.03).

Fires on (% of tokens): wp/human 10.6, wp/gemma 13.1, wp/claude 8.7, wp/glm 10.1, books/human 9.9, books/gemma 11.3, books/haiku 9.0, books/gpt 9.2, books/glm 9.8, wp/gemma_plain 11.2, wp/gemma_lit 12.3, wp/gemma_greedy 12.5, wp/gemma_raw 10.2, wp/human_raw 8.6.

Constructions: pre:semicolon.

Promotes: `𒉶` ` PLDNN` `ꗜ` `MalayMarks` `𒅤` `posTocco` `DenovoMis` ` इम्मे` `ꗐ` `CasePTV`  
Suppresses: `ʼ` `\u2062` ` ‚` ` „` `\u2064` `⼯`

- *human* (819):  down to the fact that we are all equally distant from perfection. What you may have felt could have been something out of the scope of my**[ understanding]** and empathy, even though I
- *human* (815):  saints forgive” he said out loud, not really expecting a response. Maybe it was his cultures tradition that gave him this feeling of concern and**[ guilt]**? Sure, he didn’
- *Gemma* (839):  terrifying.⏎⏎My goal was simple. One year. Just one year into the future. Enough to confirm my calculations, to gather some preliminary**[ data]**, to prove I hadn'
- *Gemma* (827):  *really* good observer. Mom always said I had a knack for reading people. But it was different. This wasn’t about observing**[ behavior]**; this was about absorbing the
- *Gemma* (807):  deep-sea thermal vents, the eerie silence of the abyssal plain. It was demanding, precise work, requiring an almost obsessive attention to**[ detail]**. Now, I was tracking
- *other LLM* (747): ⏎⏎*Dear Captain Meridian,* it began. Then, in the ninth draft, *Dear Dale,* because the parole counselor said first names build**[ trust]**, and because I knew his

## L30.187

**'a' opening an appositive or predicate that sums up a scene** (construction, medium confidence)

Fires on 'a' when a noun phrase renames or sums up what came before, as in 'It was a glorious, slightly alarming mess' or ', a fleeting burst of delight'. It is three times as common in Gemma's prose (0.13) as in human prose (0.04), and Gemma's literary prose (0.16) far exceeds its plain prose (0.03).

Fires on (% of tokens): wp/human 4.0, wp/gemma 12.7, wp/claude 5.6, wp/glm 5.8, books/human 4.7, books/gemma 11.5, books/haiku 5.1, books/gpt 4.1, books/glm 5.7, wp/gemma_plain 2.9, wp/gemma_lit 15.7, wp/gemma_greedy 12.4, wp/gemma_raw 7.3, wp/human_raw 2.9.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.52/2.5 (8.7 pts); books_gemma_vs_human 2.51/2.39 (6.7 pts); wp_gemma_vs_llm 2.44/2.75 (7.0 pts); books_gemma_vs_llm 2.66/2.63 (6.5 pts); lit_vs_plain 3.81/4.39 (12.8 pts); plain_vs_default -3.14/-3.52 (-9.4 pts); raw_gemma_vs_human 1.23/1.35 (4.4 pts); chat_vs_raw_gemma 1.23/1.15 (5.4 pts).

Writes toward: sense_of “ sense” (rank 24).

Promotes: `𒉶` `𒅤` `MalayMarks` ` PLDNN` `doneProcessAvg` `ꗜ` `posTocco` `𒍭` ` doneProcessAvg` `&lt;unused1748>`  
Suppresses: `fine` ` vanaf` ` ব্রহ্ম` ` కంటే` `avr` `Fine`

- *human* (1853): into individual exclamations, hands outstretched and fingers vibrating in the morning gray. The sun pierces the clouds and the neighborhood rises into**[ a]** single climactic refrain. Then
- *human* (1709):  narrow hallway. Dozens of large glass tubes lined the walls, each marked with a serial number indicating where it had formed. Their contents played**[ a]** major role in Elizabeth’s
- *human* (1701):  and blacks and greys in the world become vibrant and radiant in fantastic explosions of blues, reds, and greens that all blend together to create**[ a]** world that will take your breath
- *Gemma* (2093):  and swirling, signified their gifts in color, sound, and texture. They created beauty, inspired emotion, and filled the valley with a constant**[,]** joyful chaos. We provided the
- *Gemma* (2045): . It was a ridiculously specific wish, granted instantly, filling our tiny cottage with sticky, crimson sweetness. It was wonderful for a day,**[ a]** fleeting burst of childish delight.
- *Gemma* (2029): . Jagged, obsidian formations rose from the plains, casting long, distorted shadows. The vegetation had ceased to glow. The sounds, previously**[ a]** chorus of chirps, rust

## L31.190

**Generic category noun heading a descriptive or appositive phrase** (style, medium confidence)

Fires on head nouns like 'being', 'system', 'institution', 'field' or 'intelligence' when a sentence defines something as a kind of thing. Fires on 21% of Gemma literary-mode tokens versus 6% in plain mode, and slightly more in Gemma's prose than in human prose.

Fires on (% of tokens): wp/human 10.2, wp/gemma 16.5, wp/claude 10.6, wp/glm 13.2, books/human 9.9, books/gemma 14.7, books/haiku 9.9, books/gpt 8.1, books/glm 11.7, wp/gemma_plain 5.7, wp/gemma_lit 21.3, wp/gemma_greedy 16.2, wp/gemma_raw 10.8, wp/human_raw 9.2.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_llm 2.17/2.19 (4.8 pts); lit_vs_plain 4.96/4.86 (15.6 pts); lit_vs_default 1.48/1.9 (4.7 pts); plain_vs_default -3.36/-3.28 (-10.9 pts).

Promotes: `&lt;unused1170>` `&lt;unused687>` `&lt;unused201>` ` افراد` `&lt;unused673>` ` cercando` `intérieur` `&lt;unused108>` ` മ` `�`  
Suppresses: `ꗜ` `&lt;unused338>` ` PLDNN` `𒉶` `MalayMarks` `odikwa`

- *human* (2506):  profits to come made Kriek lick his lips with gluttonous fervor.⏎⏎The northern continent was dominated by the Coalition, a group of**[ countries]** developed purely based on real space
- *human* (2442):  business. He never asked humans to engage in philosophical discussions. He dictated what was moral and what was not, and thus destined us to an**[ existence]** of being dictated to.⏎⏎
- *human* (2418):  of Benokee; a gentle, keep-it-simple mountain formed in the pre-Cambrian period. Castlegregory is a**[ place]** full of dark and volatile history
- *Gemma* (2706):  once you strip away the initial, horrifying shock. I’m a professional destroyer of gods.⏎⏎The Galactic Concordance, a bureaucratic behem**[oth]** built on the ashes of countless
- *Gemma* (2642): , with her sharp wit, her unapologetic eccentricity, and her penchant for questioning authority, had become a prize. The Red Queen, a**[ being]** of
- *Gemma* (2634): subterranean farms, to build with salvaged metal and repurposed plastic. I witnessed the slow, painstaking process of rebuilding, the emergence of new**[ cultures]**, new art forms, new

## L32.219

**Head noun of a characterizing phrase such as 'a hollow performance'** (construction, medium confidence)

Fires on the noun that ends an indefinite noun phrase used to sum something up, with performance, persona and choreography common in Gemma's examples. About eight times more frequent in Gemma's prose than human prose, highest in literary mode.

Fires on (% of tokens): wp/human 0.8, wp/gemma 6.8, wp/claude 2.0, wp/glm 1.9, books/human 0.7, books/gemma 4.6, books/haiku 1.0, books/gpt 0.7, books/glm 1.2, wp/gemma_plain 2.3, wp/gemma_lit 7.3, wp/gemma_greedy 7.0, wp/gemma_raw 4.3, wp/human_raw 0.5.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 4.41/3.78 (6.1 pts); books_gemma_vs_human 2.84/2.9 (4.0 pts); wp_gemma_vs_llm 3.62/3.29 (4.9 pts); books_gemma_vs_llm 2.83/2.87 (3.6 pts); lit_vs_plain 3.31/3.24 (5.0 pts); plain_vs_default -3.08/-3.09 (-4.5 pts); raw_gemma_vs_human 2.1/2.08 (3.7 pts).

Promotes: `&lt;unused687>` ` gummies` `ución` `於` ` افراد` `&lt;unused1166>` `&lt;unused1170>` `�` ` pessoas` `inction`  
Suppresses: `𒉶` `ꗜ` `𒅤` ` PLDNN` `&lt;unused338>` `ꗐ`

- *human* (1494):  between bodies, pressing against each other in every direction. Fists were being thrown along with the biggest rocks people could find. It was a**[ melee]** like ones Jack had read about
- *human* (1302): . But as more and more people got involved, the event had become more organised and many times more popular. Now, it was a global**[ competition]**, with tons of media coverage
- *human* (1274):  professional, and knew that it was her call, not his.⏎⏎She stared directly into the eyes of her assigned new client with an icy**[ calm]** as she waited for the sound
- *Gemma* (2174):  cling to them both. ⏎⏎I observed their interactions, cataloging the subtle cues of their emotions. I detected a disconnect, a careful**[ choreography]** of politeness masking a deeper
- *Gemma* (2078): . I continued to manage the fund, executed trades, and navigated the cutthroat world of high finance, but it felt meaningless, a hollow**[ performance]**. The penthouse felt vast and
- *Gemma* (2014): , their dazzling displays of skill. This felt… somber. ⏎⏎“I’ve spent my entire career building a façade, a**[ persona]** of magic and mystery,” I

## L32.526

**Elaborating phrases about searching for meaning; Gemma literary** (style, low confidence)

Fires on prepositions and verbs that extend a phrase about seeking or reading meaning (chasing shadows, a glimpse into, for clues). Five times more frequent in Gemma's literary mode than plain mode, but the token-level pattern is loose.

Fires on (% of tokens): wp/human 5.2, wp/gemma 21.2, wp/claude 8.5, wp/glm 10.8, books/human 7.6, books/gemma 16.9, books/haiku 8.0, books/gpt 6.5, books/glm 9.9, wp/gemma_plain 6.1, wp/gemma_lit 30.6, wp/gemma_greedy 19.9, wp/gemma_raw 10.6, wp/human_raw 3.6.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.15/2.13 (16.0 pts); books_gemma_vs_llm 2.37/2.38 (8.7 pts); lit_vs_plain 4.49/4.15 (24.5 pts); lit_vs_default 1.57/2.06 (10.1 pts); plain_vs_default -2.6/-2.19 (-14.4 pts); chat_vs_raw_gemma 1.14/1.13 (10.6 pts).

Promotes: `&lt;unused201>` `�` `&lt;unused1012>` ` chopped` `&lt;unused995>` ` delves` `&lt;unused1166>` `&lt;unused1077>` ` garde` ` केन्द्र`  
Suppresses: `ꗜ` `MalayMarks` ` PLDNN` `𒅤` `𒉶` `ꗐ`

- *human* (1790):  disappointed.⏎⏎In reality, a good psychiatrist is like a guide or a companion. I'm someone to talk to, a sounding board**[ for]** those problems. But it'
- *Gemma* (2078):  to be precise. I’m from 2078.”⏎⏎Finch sighed, a sound that carried the weight of decades spent**[ chasing]** shadows and stubbornly clinging to logi
- *other LLM* (1886):  like lightning before its thunder.⏎⏎They were very sorry, they said, for the intrusion. Theirs was a world that combed the dark**[ for]** messages in bottles; its name
- *other* (2134):  immutable, was subject to a relentless, unknowable process of decay and rebirth. ⏎⏎We became intertwined, bound by the shared pursuit of**[ uncovering]** lost narratives. He’d
- *other* (2110):  was a ‘Reader,’ specializing in deciphering the more esoteric texts, the ones deemed too dangerous for the general population. Dangerous because they**[ contained]** concepts that challenged the Council’
- *other* (2086):  light, but directly into my mind. It wasn’t a voice, not in the human sense. It was a cascade of concepts,**[ of]** pure, distilled understanding.⏎⏎

## L33.449

**Article or evaluative adjective in 'was a [adj] noun' phrases** (predictive, medium confidence)

Fires on a and adjectives like significant, profound, familiar and harmless in predicate phrases that characterize something (a significant step). It fires on 24% of Gemma tokens versus 9% of human ones and 13% of other LLMs'.

Fires on (% of tokens): wp/human 8.8, wp/gemma 24.1, wp/claude 13.6, wp/glm 13.6, books/human 9.0, books/gemma 23.3, books/haiku 13.6, books/gpt 12.1, books/glm 13.2, wp/gemma_plain 15.8, wp/gemma_lit 27.0, wp/gemma_greedy 24.4, wp/gemma_raw 16.5, wp/human_raw 4.9.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 4.22/4.14 (15.4 pts); books_gemma_vs_human 4.54/3.75 (14.3 pts); wp_llm_vs_human 1.6/1.58 (4.9 pts); books_llm_vs_human 1.85/1.6 (3.9 pts); wp_gemma_vs_llm 4.06/3.92 (10.5 pts); books_gemma_vs_llm 4.01/3.78 (10.4 pts); lit_vs_plain 3.34/3.83 (11.2 pts); plain_vs_default -2.32/-2.48 (-8.3 pts); raw_gemma_vs_human 3.13/3.22 (11.7 pts); chat_vs_raw_gemma 1.93/1.76 (7.6 pts).

Promotes: `&lt;unused687>` `&lt;unused1166>` `�` `&lt;unused201>` `&lt;unused366>` `&lt;unused1077>` `&lt;unused673>` `&lt;unused1170>` `&lt;unused192>` ` cercando`  
Suppresses: `ꗜ` `𒉶` ` PLDNN` `&lt;unused338>` `𒅤` `ꗐ`

- *human* (9194): While *what* the mimes were capable of was a**[ complete]** surprise to the entire world,
- *human* (8938): Mr Wiggin glanced up from his clipboard and sighed. The Tuesday five o'clock couple never failed to give him**[ a]** headache, and he heard them
- *human* (8938): The line this time around was particularly long. Such**[ a]** ridiculous bureaucracy these "overse
- *other LLM* (10218):  a death, nothing that asks for more wishes. Everything else is fair game.⏎⏎That's why five-year-old wishes are**[ a]** national joke. There's
- *other LLM* (9706):  sat on a camp stool with his hands unbound and watched the cup fill.⏎⏎They had not chained him. He supposed that was meant as**[ a]** courtesy. They had taken his
- *other LLM* (9706): The letter arrived on paper so heavy it felt like an apology.⏎⏎*Dear Madam,* it began, which should have been my**[ first]** warning. The Institute for Advanced
