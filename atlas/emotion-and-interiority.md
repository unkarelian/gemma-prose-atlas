# Emotion and interiority

15 features. [Back to the index](../ATLAS.md)

| Feature | Label | Kind | Conf. | G | H | L | Promotes |
|---|---|---|---|---|---|---|---|
| [L4.119](#l4119) | Physical signs of emotion (a pang, eyes widened, face flushed) | content | medium | 12.8 | 7.4 | 4.7 | ꗜ 𒉶  PLDNN 𒅤 &lt;unused338> |
| [L8.332](#l8332) | Mood and emotion words: amused, wonder, melancholic, giddy | lexical | high | 10.5 | 4.2 | 2.6 | ꗜ 𒉶  PLDNN MalayMarks 𒅤 |
| [L20.1213](#l201213) | Opening of an emotion noun phrase after 'felt a' or 'only' | predictive | high | 20.5 | 4.4 | 8.6 | 完全に  sheer 圧倒 &lt;unused108>  ভীষণ |
| [L25.65](#l2565) | Connector inside an emotion noun phrase (sense of, fear and) | construction | medium | 15.7 | 7.3 | 6.2 | ꗜ  PLDNN 𒉶 𒅤 𒂷 |
| [L25.662](#l25662) | Article opening a named feeling after 'felt' (felt a flicker...) | predictive | high | 19.6 | 5.8 | 10.4 |  feeling  exhilar  joy  feel Feel |
| [L26.147](#l26147) | About to name an unsettling feeling (strange, eerie, uneasy) | predictive | high | 18.4 | 3.5 | 7.0 |  bewild  unsettling  strange  disconcert  perplexing |
| [L26.10210](#l2610210) | Imagery of inner emptiness, dull ache and heavy silence | content | medium | 13.6 | 5.2 | 6.6 |  ખા  sm  emptiness  оправ FIX |
| [L28.165](#l28165) | Preposition before an emotion noun (mixture of, look of, out of) | predictive | high | 11.6 | 9.6 | 9.1 |  pure pure Pure  Pure  disbelief |
| [L28.448](#l28448) | Linking verbs of appearance (felt, looked, sounded) before a description | construction | medium | 22.4 | 10.3 | 17.2 | &lt;unused338> ꗜ &lt;unused429> &lt;unused1102> &lt;unused1716> |
| [L28.538](#l28538) | Start of a noun phrase naming a felt sensation (a familiar ache) | construction | medium | 16.9 | 5.8 | 10.8 | ꗜ 𒅤 𒉶 ꗐ  PLDNN |
| [L29.189](#l29189) | 'a' opening an emotion phrase: felt a flicker of | predictive | high | 16.6 | 4.7 | 6.9 | նել }'. 𒊌 𒅤 ꗜ |
| [L29.456](#l29456) | Article opening an abstract feeling phrase: felt the pull | style | medium | 18.6 | 6.4 | 10.9 |  polymer  insistent &lt;unused359>  dibawah ꗜ |
| [L30.2039](#l302039) | 'felt' or a clause comma before a bodily emotion phrase | predictive | high | 9.6 | 3.1 | 5.9 |  Bernardo  Abdel  Gh &lt;unused2169> Marcus |
| [L32.388](#l32388) | Opening of a felt bodily reaction (a flush, a jolt) | construction | medium | 15.6 | 4.5 | 7.4 | '? ?... "? ?).  maids |
| [L33.1099](#l331099) | Article opening a physical-emotion phrase like 'a flicker of' | construction | high | 9.9 | 2.2 | 4.6 |  ವ್ಯವ  जलाश Tính  કંપની  აღმასრულ |

## L4.119

**Physical signs of emotion (a pang, eyes widened, face flushed)** (content, medium confidence)

Fires on bodily emotion words such as pang, sob, tears, widened, flushed and watered; at 9.5% density it covers much more besides. Gemma book scenes fire 2.6 times more than human ones and nearly four times more than Claude.

Fires on (% of tokens): wp/human 7.4, wp/gemma 12.8, wp/claude 4.9, wp/glm 4.6, books/human 7.2, books/gemma 19.1, books/haiku 8.7, books/gpt 8.0, books/glm 9.0, wp/gemma_plain 6.8, wp/gemma_lit 14.9, wp/gemma_greedy 12.4, wp/gemma_raw 12.8, wp/human_raw 7.1.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 3.0/2.88 (11.9 pts); books_gemma_vs_llm 2.89/2.97 (10.6 pts).

Constructions: bookism, slop_word.

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒅤` `&lt;unused338>` `MalayMarks` `ꗐ` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused1170>`

- *human* (252):  best."⏎⏎"Uh, I'mheretosell, sellyousome cookies - please, if you want them." Her face**[ flushed]** bright pink as she finished the
- *human* (244): "Wow, you're paying me this much for this mission!" Gabe exclaimed. His eyes**[ widened]** at the sight of the amount
- *Gemma* (264): ; a child who’d learned to appreciate the beauty of imperfection from watching Silas’s hands shape the clay.⏎⏎Elias felt a**[ pang]**, a familiar, dull ache
- *other LLM* (270):  and felt something lurch in his chest, a door in a dark house swinging on its hinge. He stared at the letter until his eyes**[ watered]**. N. N. Nothing
- *other* (260):  window at the rain. “Sometimes, it’s good to have company, even if just for a little while.”⏎⏎Peter felt a**[ pang]** of sympathy for Agnes. He
- *other* (258):  of rain that made the world look dull and gray. She had a blanket around her shoulders and was just watching. ⏎⏎I felt a**[ pang]** of something in my chest.

## L8.332

**Mood and emotion words: amused, wonder, melancholic, giddy** (lexical, high confidence)

Fires on words naming a mood or emotional tone, such as amused, cheerful, wonder, thrill, boredom and melancholic. Gemma fires about three times as often as humans and other LLMs, its literary mode three times its plain mode, and it also fires in Gemma's notes about a story's tone.

Fires on (% of tokens): wp/human 4.2, wp/gemma 10.5, wp/claude 2.6, wp/glm 2.6, books/human 3.6, books/gemma 11.9, books/haiku 3.9, books/gpt 3.0, books/glm 4.2, wp/gemma_plain 4.5, wp/gemma_lit 12.9, wp/gemma_greedy 10.7, wp/gemma_raw 9.2, wp/human_raw 3.9.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.32/2.05 (6.3 pts); books_gemma_vs_human 3.56/3.54 (8.3 pts); wp_gemma_vs_llm 2.99/3.24 (7.9 pts); books_gemma_vs_llm 3.92/3.7 (8.2 pts); plain_vs_default -1.94/-2.19 (-5.9 pts); raw_gemma_vs_human 1.71/1.74 (5.4 pts).

Promotes: `ꗜ` `𒉶` ` PLDNN` `MalayMarks` `𒅤` `&lt;unused338>` `ꗐ` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` `&lt;unused192>` ` cercando`

- *human* (615):  words. The only option he had now was to oblige, and try to figure out what was happening without having a panic attack.⏎⏎An**[ excited]** round of applause came from the
- *human* (603):  a city as big as this, there's bound to be callers from the same neighborhood.⏎⏎"Hello?" said Frasier almost**[ cheerfully]**. And although he was far
- *human* (591): ⏎⏎Next to him, a young man appeared. He had slicked back hair with a sharp black suit to match. And with an almost**[ mischievous]** grin, and piercing hazel eyes
- *Gemma* (659): , a subtle, persistent tang that clung to the back of your throat. I'd almost grown used to it, almost found a certain**[ melanch]**olic comfort in the grey skies
- *Gemma* (659):  understand the societal nuances of this era. The technology was… rudimentary. The pace of life was slower, less frantic. There was a certain**[ charm]** to it, a tangible connection
- *Gemma* (647): ’s fantastical tale. ⏎⏎As he read further, the stories revealed a remarkable consistency. They were all imbued with a potent blend of**[ wonder]**, fear, and a profound

## L20.1213

**Opening of an emotion noun phrase after 'felt a' or 'only'** (predictive, high confidence)

Fires on the article or first modifier that starts a named feeling (a sudden, a profound, a dull) and promotes intensifiers such as sheer and overwhelmingly. It fires about five times more often in Gemma's prose than in human prose (wp 0.205 vs 0.044), and most in Gemma's literary mode.

Fires on (% of tokens): wp/human 4.4, wp/gemma 20.5, wp/claude 8.2, wp/glm 9.1, books/human 9.8, books/gemma 27.7, books/haiku 15.7, books/gpt 12.6, books/glm 17.3, wp/gemma_plain 13.0, wp/gemma_lit 30.2, wp/gemma_greedy 19.6, wp/gemma_raw 11.9, wp/human_raw 3.0.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.39/2.52 (17.8 pts); books_gemma_vs_llm 2.13/2.14 (12.4 pts); lit_vs_default 1.48/1.75 (10.8 pts).

Constructions: emotion_pack.

Promotes: `完全に` ` sheer` `圧倒` `&lt;unused108>` ` ভীষণ` ` теат` ` 완전히` ` extraordinarily` `şk` ` drain`  
Suppresses: ` protruding` ` Ji` ` evaporator` ` greets` ` 江` `jeet`

- *human* (803): , the love of my life, only she wasn't there.⏎⏎The scene I was presented with filled me with confusion, and then**[ sudden]** panic. I stumbled backward and
- *Gemma* (939):  and something about the static, impersonal gaze of the camera, combined with the unyielding focus of the audience, triggered something in me. A**[ profound]**, crushing sense of isolation.
- *Gemma* (931): , and his eyes burned with an unnerving intelligence. Elias didn't feel fear, not exactly. He felt…something else entirely.**[ A]** sharp, disconcerting awareness of
- *other* (891):  simple instruction a tiny, ridiculous anchor in the swirling chaos of my thoughts. I felt a surge of anger, quickly followed by a bone-**[deep]** weariness. Why me?
- *other* (875):  tapestry pulled thread by thread until only the underlying weave remains.”⏎⏎I felt a prickle of something – not fear, exactly, but a**[ deep]**, unsettling disorientation. “But
- *other* (867):  polite indifference. ⏎⏎He felt a familiar pressure in his chest. It wasn’t anger. It wasn’t frustration. It was**[ a]** dull ache. He’d

## L25.65

**Connector inside an emotion noun phrase (sense of, fear and)** (construction, medium confidence)

Fires on 'of', 'and' or 'with' right after an abstract emotion noun, as in feeling of betrayal, fear and suspicion, sense of helplessness. Fires about twice as often in Gemma's prose as in human or other LLM prose, and four times more in Gemma's literary mode than its plain mode; decoder is junk.

Fires on (% of tokens): wp/human 7.3, wp/gemma 15.7, wp/claude 5.4, wp/glm 7.0, books/human 7.2, books/gemma 16.5, books/haiku 7.3, books/gpt 6.0, books/glm 8.2, wp/gemma_plain 4.5, wp/gemma_lit 20.0, wp/gemma_greedy 15.6, wp/gemma_raw 10.7, wp/human_raw 6.7.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.69/2.26 (9.3 pts); wp_gemma_vs_llm 2.79/2.66 (9.4 pts); books_gemma_vs_llm 2.94/2.78 (9.3 pts); lit_vs_plain 4.26/4.02 (15.5 pts); plain_vs_default -3.06/-2.94 (-11.2 pts).

Promotes: `ꗜ` ` PLDNN` `𒉶` `𒅤` `𒂷` `ꗐ` `MalayMarks` `DenovoMis` `odikwa` `&lt;unused338>`  
Suppresses: `&lt;unused1166>` `�` `&lt;unused687>` `&lt;unused201>` `&lt;unused1077>` ` cercando`

- *human* (2144):  be the last twenty years of my life with my feet firmly planted in the atheist camp. So, I will admit to not a little bit**[ of]** shock, and frankly, a
- *human* (1856):  what he had done. He didn't want to see that. He didn't want to see her look at him with the hate**[ and]** fear she would have when she
- *human* (1728): “May the saints forgive” he said out loud, not really expecting a response. Maybe it was his cultures tradition that gave him this feeling**[ of]** concern and guilt? Sure,
- *Gemma* (1776):  from broken homes, children deemed ‘unsuitable’ for their parents. Families, desperate for a reprieve, for a way to avoid the shame**[ and]** the struggle, would sell their
- *Gemma* (1760): overflowing with potential, yet fractured by internal conflict and driven by a singular, unsustainable pursuit: growth. ⏎⏎The initial reaction was one**[ of]** profound sadness. The White Ones
- *Gemma* (1744):  Then they’d grown louder, coalescing into a chilling chorus: “The Prophet.”⏎⏎They called me that. Not with affection.**[ With]** a mixture of fear and superstitious

## L25.662

**Article opening a named feeling after 'felt' (felt a flicker...)** (predictive, high confidence)

Fires on 'a' or 'the' that begins a noun phrase naming a feeling, usually after 'felt' or a comma, as in a cold knot or a flicker of alarm, and promotes feeling, joy, feel. Gemma fires over three times as often as humans in WritingPrompts stories, most of all in its literary mode.

Fires on (% of tokens): wp/human 5.8, wp/gemma 19.6, wp/claude 9.9, wp/glm 10.8, books/human 10.4, books/gemma 26.9, books/haiku 16.0, books/gpt 13.9, books/glm 17.2, wp/gemma_plain 10.1, wp/gemma_lit 27.8, wp/gemma_greedy 18.8, wp/gemma_raw 13.3, wp/human_raw 4.4.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.69/2.82 (16.5 pts); books_llm_vs_human 1.51/1.45 (5.3 pts); books_gemma_vs_llm 2.24/2.31 (11.2 pts); lit_vs_default 1.51/1.55 (9.5 pts).

Constructions: emotion_pack.

Writes toward: sense_of “ sense” (rank 6).

Promotes: ` feeling` ` exhilar` ` joy` ` feel` `Feel` ` feels` ` feelings` `feel` ` sentimento` ` чувство`  
Suppresses: `Federal` `ૐ` ` tín` ` Fingers` `obil` ` Federal`

- *Gemma* (1684): , and his eyes burned with an unnerving intelligence. Elias didn't feel fear, not exactly. He felt…something else entirely.**[ A]** sharp, disconcerting awareness of
- *other* (1564): ’t just a planet, but an anomaly. Captain Elias Thorne, a man who carried the weight of decades spent chasing impossible dreams, felt**[ a]** tremor of something akin to reverence
- *other* (1540): I know you don't like big surprises, but I wanted to do something special for you."⏎⏎I hug him back tightly, feeling**[ a]** warmth spread through my chest.
- *other* (1532):  in the smooth, programmed rhythm of our lives. It was a forbidden thought, a dangerous deviation. ⏎⏎I turned to her, a**[ strange]**, unfamiliar flicker in my eyes

## L26.147

**About to name an unsettling feeling (strange, eerie, uneasy)** (predictive, high confidence)

Fires on 'a', 'with', 'something' or a comma just before a noun phrase of vague dread or strangeness, and promotes unsettling, strange, eerie, uneasy, disconcerting. Gemma fires about five times more often than humans in WritingPrompts stories, most of all in literary mode.

Fires on (% of tokens): wp/human 3.5, wp/gemma 18.4, wp/claude 6.5, wp/glm 7.5, books/human 8.5, books/gemma 21.9, books/haiku 10.3, books/gpt 8.5, books/glm 12.3, wp/gemma_plain 5.4, wp/gemma_lit 27.0, wp/gemma_greedy 18.1, wp/gemma_raw 12.3, wp/human_raw 2.7.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.99/3.18 (14.9 pts); books_gemma_vs_human 2.89/2.57 (13.3 pts); wp_gemma_vs_llm 2.74/2.79 (11.3 pts); books_gemma_vs_llm 2.99/2.74 (11.5 pts); lit_vs_plain 4.16/4.12 (21.6 pts); lit_vs_default 2.15/1.95 (9.2 pts); plain_vs_default -2.44/-2.67 (-12.4 pts); raw_gemma_vs_human 1.36/1.62 (9.6 pts).

Writes toward: sense_of “ sense” (rank 13).

Promotes: ` bewild` ` unsettling` ` strange` ` disconcert` ` perplexing` ` eerie` ` uneasy` ` weird` ` nagging` ` inquiet`  
Suppresses: `Passed` `Tan` `繕` ` bytes` ` gummies` `પુર`

- *human* (1592): , the Mitchell boy with his godforsaken muffler.) Ross was a name she didn't know. But she knew, with a sense**[ of]** dread, that there was something
- *human* (1416): At first it was fascinating, but the strange technical glitch gradually became**[ an]** obsession for Grant until it consumed
- *Gemma* (1704):  helper, a perfectly polite conversationalist, a silent, reliable presence. But as the years passed, the novelty had worn off, replaced by**[ a]** creeping loneliness. I’d
- *Gemma* (1688): y were complex geometric shapes, interlocking circles and lines, pulsing with an almost imperceptible energy. I photographed them obsessively, feeling**[ a]** prickling sensation on my skin
- *Gemma* (1656):  stories as the ramblings of small-town folk, steeped in superstition. But the longer I spent in the manor, the more a sense**[ of]** unease began to settle over
- *other* (1616): ing clay; they were *injecting* it with something designed to promote specific morphological changes.”⏎⏎The air thickened with disbelief and a growing**[,]** prickling fear.⏎⏎“

## L26.10210

**Imagery of inner emptiness, dull ache and heavy silence** (content, medium confidence)

Fires on words leading into phrases about a hollow ache, a void to fill or a stretching silence, and promotes 'emptiness', 'hole' and 'emptying'. About 2.6 times more frequent in Gemma's prose than human prose, and highest in literary-prompted Gemma.

Fires on (% of tokens): wp/human 5.2, wp/gemma 13.6, wp/claude 6.3, wp/glm 6.9, books/human 4.5, books/gemma 12.6, books/haiku 6.9, books/gpt 5.7, books/glm 7.4, wp/gemma_plain 7.1, wp/gemma_lit 16.9, wp/gemma_greedy 13.6, wp/gemma_raw 6.7, wp/human_raw 3.7.

Constructions: air_silence.

Promotes: ` ખા` ` sm` ` emptiness` ` оправ` `FIX` ` fester` `ชัย` ` 앉` ` hole` ` corrosive`  
Suppresses: ` código` ` Código` `IEEE` `莼` `жная` `لون`

- *human* (1520):  over a loud speaker as I sat down⏎⏎"Shit" I said, as all speaking stopped and everyone turned to me. There was**[ death]** in their stares.⏎⏎Liter
- *human* (1424):  through Hume’s life history to help fill out his grief. The tragedy of Hume deserved more than a cold recitation of the facts. The**[ silence]** stretched on for seconds before he
- *human* (1368): ⏎⏎I am confined in a silver and steel place whose edges rest just beyond my ability to comprehend them. All I have is the gray,**[ that]** frigid lonesomeness:
- *Gemma* (1720):  a slow, insidious erosion of decency, built on lies and fueled by a desperate need to feel…something. Anything, really, besides the**[ dull]** ache of being unremarkable.⏎⏎
- *Gemma* (1688):  I’d bought it at a dusty estate sale, drawn to its unsettling beauty, a desperate attempt to find something, anything, to fill**[ the]** echoing emptiness in my life.
- *Gemma* (1544): . ⏎⏎The money, predictably, didn’t solve anything. It didn't bring her back. It certainly didn't fill**[ the]** aching void in my chest.

## L28.165

**Preposition before an emotion noun (mixture of, look of, out of)** (predictive, high confidence)

Fires on 'of', 'in' or 'to' in frames like 'a mixture of awe' or 'out of pure spite', and promotes 'pure', 'disbelief', 'annoyance' and 'relief'. Rates are similar across writers.

Fires on (% of tokens): wp/human 9.6, wp/gemma 11.6, wp/claude 8.8, wp/glm 9.4, books/human 6.8, books/gemma 11.1, books/haiku 7.5, books/gpt 7.7, books/glm 7.8, wp/gemma_plain 4.8, wp/gemma_lit 10.2, wp/gemma_greedy 11.8, wp/gemma_raw 11.9, wp/human_raw 9.5.

Constructions: pre:emotion_pack.

Promotes: ` pure` `pure` `Pure` ` Pure` ` disbelief` ` annoyance` ` pura` ` प्योर` `纯` ` amazement`  
Suppresses: `AutoSize` `unistd` `onka` `paces` `askell` ` און`

- *human* (2788):  unnatural at the same time, that I almost panicked. He suddenly stood upright. My heartbeat instantly rose and my short panick attack quickly shifted**[ to]** a sense of healthy wonder.
- *human* (2740):  destabilize and throw off radiation. He tried to shut it down, but he lost control of the mini black hole. He saw the look**[ of]** horror on the board of director
- *human* (2708):  the air as she went to volley it at Reaper, but her eyes locked with someone at the last moment "HONEY!?" she exclaimed**[ in]** shock and pulled her leg away
- *Gemma* (2532):  become one of them.⏎⏎“She’s… magnificent,” my wife, Hana, whispered, holding Rin close, her face a mixture**[ of]** awe and apprehension. Hana was
- *Gemma* (2516): . “Though I’d appreciate it if you didn’t announce the rather obvious.”⏎⏎I cautiously approached the mirror again, a mixture**[ of]** terror and morbid curiosity warring wit
- *Gemma* (2500): -eight years in the future. And you’re currently inhabiting my ten-year-old body.”⏎⏎I stared, a ridiculous combination**[ of]** horror and disbelief warring within me

## L28.448

**Linking verbs of appearance (felt, looked, sounded) before a description** (construction, medium confidence)

Fires on 'felt', 'looked', 'sounded' and 'feel' just before an adjective or a like/as-if comparison. About twice as frequent in Gemma's prose as human prose; it is dense (19%) with a junk decoder, so it may also fire beyond the verb itself.

Fires on (% of tokens): wp/human 10.3, wp/gemma 22.4, wp/claude 17.4, wp/glm 17.0, books/human 15.8, books/gemma 29.9, books/haiku 22.5, books/gpt 20.3, books/glm 23.5, wp/gemma_plain 22.9, wp/gemma_lit 26.0, wp/gemma_greedy 22.1, wp/gemma_raw 14.9, wp/human_raw 8.4.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.58/2.99 (14.1 pts); books_llm_vs_human 1.8/1.84 (6.3 pts).

Constructions: pre:as_if.

Writes toward: voice_barely “ barely” (rank 7).

Promotes: `&lt;unused338>` `ꗜ` `&lt;unused429>` `&lt;unused1102>` `&lt;unused1716>` `𒉶` `𒅤` ` PLDNN` `&lt;unused974>` ` തിരഞ്ഞെടു`  
Suppresses: ` эко` `扇` ` seva` `čnog` ` leachate` ` በ`

- *human* (2713):  thought we were pretty prepared for it. Did you think so?”⏎⏎“Yeah, I guess it went fine,” Violet said. Her voice**[ sounded]** like it had run out of
- *human* (2617):  and felt something crinkle underneath him. Reaching down, he felt a thin sheet of paper resting atop a hard cushion. His whole body**[ felt]** stiff, like he had been
- *human* (2521):  but not before gently touching the other woman on the shoulder. "The doctor says it really will help."⏎⏎In the bed there, he**[ looked]** so weak. Slender,
- *other LLM* (2777):  job, new kid."⏎⏎I did my job. I inspected boxes for warped flaps and bad glue lines, and the whole shift the plant**[ felt]** like it was holding its breath
- *other* (2745):  bizarre declaration of something utterly beyond my comprehension. ⏎⏎I got out of bed slowly, each movement a deliberate act of will. The room**[ felt]** unfamiliar, almost alien. My
- *other* (2617):  office. Sarah was there too, scrolling through her phone. We didn't say much. There was nothing to say. The whole country**[ felt]** off-kilter. It

## L28.538

**Start of a noun phrase naming a felt sensation (a familiar ache)** (construction, medium confidence)

Fires on the article or adjective opening phrases like 'a constant, dull ache' or 'a flicker of something'. Three times more frequent in Gemma's WritingPrompts stories than human ones and highest under literary prompts; decoder output is junk.

Fires on (% of tokens): wp/human 5.8, wp/gemma 16.9, wp/claude 9.3, wp/glm 12.3, books/human 9.2, books/gemma 19.0, books/haiku 12.3, books/gpt 10.6, books/glm 12.9, wp/gemma_plain 10.3, wp/gemma_lit 26.5, wp/gemma_greedy 16.6, wp/gemma_raw 10.5, wp/human_raw 4.7.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.16/2.25 (11.1 pts); books_gemma_vs_human 2.94/2.6 (9.8 pts); books_gemma_vs_llm 2.31/2.23 (7.1 pts); lit_vs_plain 3.57/3.8 (16.2 pts); lit_vs_default 2.94/2.56 (10.3 pts); raw_gemma_vs_human 1.15/1.19 (5.8 pts).

Writes toward: sense_of “ sense” (rank 3).

Promotes: `ꗜ` `𒅤` `𒉶` `ꗐ` ` PLDNN` `DenovoMis` ` wist` `&lt;unused1102>` `𒅿` ` ControlMissense`  
Suppresses: `原始内容存档` ` 이동` ` ത` ` वास्तविक` ` Go` `elijke`

- *other* (2138):  smelled of salt and something older, something of seaweed and drowned secrets. I watched it fall, a silent, solemn observer, and felt a**[ familiar]**, unsettling flatness bloom in my
- *other* (2122):  to the structure. I watched it fall, tracing the patterns with a fingertip that still felt strangely alien on my own skin, and a**[ familiar]** ache settled in my chest –
- *other* (2058):  course. I haven’t moved on. Not really. The thought of him moving on, of building a life without me, is a**[ constant]**, dull throb beneath the

## L29.189

**'a' opening an emotion phrase: felt a flicker of** (predictive, high confidence)

Fires on 'a' after 'felt', 'with' or a dialogue tag when a named emotion follows, as in 'a flicker of curiosity' or 'a tremor of unease'. It fires three times as often in Gemma's prose (0.21 in book scenes, 0.20 literary) as in human prose (0.05 to 0.07).

Fires on (% of tokens): wp/human 4.7, wp/gemma 16.6, wp/claude 6.7, wp/glm 7.1, books/human 6.8, books/gemma 21.0, books/haiku 9.5, books/gpt 7.9, books/glm 10.1, wp/gemma_plain 5.9, wp/gemma_lit 20.1, wp/gemma_greedy 16.1, wp/gemma_raw 10.1, wp/human_raw 3.6.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.59/2.55 (11.9 pts); books_gemma_vs_human 3.7/3.52 (14.3 pts); wp_gemma_vs_llm 2.56/2.68 (9.5 pts); books_gemma_vs_llm 3.5/3.45 (11.9 pts); lit_vs_plain 3.11/2.86 (14.2 pts); plain_vs_default -2.25/-2.27 (-10.1 pts); raw_gemma_vs_human 1.43/1.7 (6.6 pts).

Constructions: emotion_pack.

Promotes: `նել` `}'.` `𒊌` `𒅤` `ꗜ` ` अंडर` `positroids` `𒁼` ` تحت` `ꗨ`  
Suppresses: ` ecstasy` `Ther` ` لاکھ` `țiilor` `pham` `ather`

- *human* (2432):  a voice buried in the echoes, a whisper on the wind. There was something dark in the voice, something angry, and the boy felt**[ a]** sharp fear in his gut.
- *human* (2416):  that it could very well be a battlefield. But nature is constantly at war with itself, including its inhabitants. Very interesting.”⏎⏎I felt**[ a]** bit sheepish. “Yeah
- *human* (2400):  To be completely frank: I looked like shit, and I knew it. I thought I saw my reflection grimace at the sight and felt**[ a]** surge of anger towards myself.
- *Gemma* (2768):  tendencies, a task Seraphina had deemed vital to our operation. Isolde’s expression was a carefully neutral mask, but I detected**[ a]** flicker of something akin to apprehensi
- *other* (2656): I’d seen the effect it had on other people. The way they’d stop, look around, then glance at each other with**[ a]** brief, puzzled expression. Like
- *other* (2624): , almost hollow. A faint scent, like damp moss and distant rain, emanated from it. “What is it?” I asked,**[ a]** tremor of unease prickling

## L29.456

**Article opening an abstract feeling phrase: felt the pull** (style, medium confidence)

Fires on 'the' or 'a' after felt, filled with or against, before an abstract sensation like the weight or the ache of something. It is Gemma's literary register: 0.34 in its literary prose vs 0.08 plain and 0.06 for human stories.

Fires on (% of tokens): wp/human 6.4, wp/gemma 18.6, wp/claude 9.1, wp/glm 12.7, books/human 10.8, books/gemma 22.6, books/haiku 14.3, books/gpt 11.9, books/glm 15.3, wp/gemma_plain 7.5, wp/gemma_lit 33.7, wp/gemma_greedy 18.4, wp/gemma_raw 11.0, wp/human_raw 5.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.0/2.08 (12.2 pts); books_gemma_vs_human 2.79/2.73 (11.8 pts); books_gemma_vs_llm 2.54/2.61 (8.8 pts); lit_vs_plain 5.4/5.81 (26.2 pts); lit_vs_default 3.66/3.09 (15.6 pts); plain_vs_default -2.1/-2.06 (-10.6 pts).

Promotes: ` polymer` ` insistent` `&lt;unused359>` ` dibawah` `ꗜ` ` Polymer` ` 現在` `ꗐ` ` under` ` दुबई`  
Suppresses: ` школова` ` infot` `হাত` ` mė` `bishop` `prefs`

- *other* (2037):  from obsidian and regret. Its eyes, when they finally focused on Silas, were not bright or malevolent, but infinitely sad, filled with**[ the]** weight of millennia. ⏎⏎
- *other* (1989):  fabric seeming to absorb rather than reflect light. His face was etched with a melancholic serenity, his eyes the color of polished obsidian, holding**[ a]** depth of observation that felt both
- *other* (1989):  caught in the strands of her hair. It wasn't an attempt to capture her beauty, not exactly. It was an attempt to understand**[ the]** weight she carried. ⏎⏎

## L30.2039

**'felt' or a clause comma before a bodily emotion phrase** (predictive, high confidence)

Fires on 'felt' after a name ('Linus felt') and on the comma after an 'As X happened' clause, just before a phrase like 'a prickle of unease' or 'his stomach twist'. Gemma uses it three times as often as human Reddit writers (9.6% versus 3.1%), and most in its literary mode.

Fires on (% of tokens): wp/human 3.1, wp/gemma 9.6, wp/claude 6.0, wp/glm 5.8, books/human 5.9, books/gemma 10.8, books/haiku 9.0, books/gpt 8.2, books/glm 9.4, wp/gemma_plain 4.1, wp/gemma_lit 12.5, wp/gemma_greedy 9.2, wp/gemma_raw 6.7, wp/human_raw 2.2.

Writer contrasts (paired effect size on each half, change in firing rate): books_llm_vs_human 1.34/1.55 (2.9 pts); raw_gemma_vs_human 1.2/1.25 (4.5 pts).

Constructions: pre:emotion_pack.

Promotes: ` Bernardo` ` Abdel` ` Gh` `&lt;unused2169>` `Marcus` ` பொருளாதார` ` bartenders` `Barb` ` ದ` ` Marcus`  
Suppresses: `ҝ` ` sid` ` ausz` `睹` `돋` `駆`

- *human* (1423):  the product of another sentient creature. That was all about to end…⏎⏎As I placed the bowl of oatmeal within the microwave and pressed start**[,]** I heard a sound that will
- *Gemma* (1543):  salvage what they could, the growing desperation as the landslides continued to worsen. He heard the cries for help, the pleas for deliverance, and**[ felt]** a strange, unfamiliar tug
- *Gemma* (1479): , the slight downturn of his mouth when he spoke – it was all… wrong. And yet, utterly, undeniably *right*.⏎⏎Then**[,]** it hit me. Like a
- *Gemma* (1431):  getting sucked into the simulation.”⏎⏎I examined the display, focusing my mental awareness. The colours shifted, and for a fleeting moment, I**[ felt]** a sharp pang of sadness,
- *other* (1447):  a lavender hue, a color utterly alien to the muted grays and whites of the surrounding snow. When I knelt to examine it, I**[ felt]** a tremor, not of cold
- *other* (1431):  writhe in the dim light. ⏎⏎He reached out a tentative finger and traced one of the symbols. As his fingertip made contact**[,]** a low hum filled the room

## L32.388

**Opening of a felt bodily reaction (a flush, a jolt)** (construction, medium confidence)

Fires on the article or word just before a physical sign of emotion (sent a jolt, felt a flicker, a blush rose). About three times more frequent in Gemma's prose than human prose; the decoder promotes question-mark tokens, which does not fit the examples.

Fires on (% of tokens): wp/human 4.5, wp/gemma 15.6, wp/claude 7.4, wp/glm 7.3, books/human 7.6, books/gemma 23.8, books/haiku 13.9, books/gpt 12.5, books/glm 14.0, wp/gemma_plain 8.3, wp/gemma_lit 20.7, wp/gemma_greedy 15.1, wp/gemma_raw 12.4, wp/human_raw 3.5.

Writer contrasts (paired effect size on each half, change in firing rate): books_gemma_vs_human 2.57/2.6 (16.2 pts); books_llm_vs_human 1.62/1.46 (5.9 pts).

Constructions: emotion_pack.

Writes toward: sense_of “ sense” (rank 22).

Promotes: `'?` `?...` `"?` `?).` ` maids` `..?` `cl` `?),` `”?` `?-`  
Suppresses: `产业` `ﻳ` ` adenocarcinoma` `YA` `्रोत` ` Somit`

- *human* (2087):  that it could very well be a battlefield. But nature is constantly at war with itself, including its inhabitants. Very interesting.”⏎⏎I felt**[ a]** bit sheepish. “Yeah
- *other* (2287):  unexpected. He reached out and gently brushed the charcoal smudge from Cas’s cheek. The contact was fleeting, almost hesitant, but it sent**[ a]** jolt through Cas’s
- *other* (2271):  she'd loved.⏎⏎Mary didn't answer. She simply reached across the table, placing her hand over his. Her touch sent**[ a]** jolt through him.⏎⏎
- *other* (2255): 's just... embarrassing." ⏎⏎"Oh, come on. You're a natural." He turned to face me fully, his**[ eyes]** sparkling with amusement. "You

## L33.1099

**Article opening a physical-emotion phrase like 'a flicker of'** (construction, high confidence)

Fires on 'A' or 'a' that begins a bodily emotion phrase (a shiver ran through, a knot of, a wave of, a hint of). Gemma uses it about four times as often as humans (0.14 vs 0.035 in books, 0.16 in literary mode); the decoder promotes unrelated tokens.

Fires on (% of tokens): wp/human 2.2, wp/gemma 9.9, wp/claude 4.3, wp/glm 4.8, books/human 3.5, books/gemma 14.1, books/haiku 6.4, books/gpt 4.7, books/glm 6.4, wp/gemma_plain 5.0, wp/gemma_lit 15.9, wp/gemma_greedy 9.7, wp/gemma_raw 5.5, wp/human_raw 1.6.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.22/2.5 (7.8 pts); books_gemma_vs_human 3.59/3.67 (10.5 pts); books_llm_vs_human 1.63/1.36 (2.3 pts); books_gemma_vs_llm 3.01/3.19 (8.2 pts); lit_vs_plain 3.25/3.13 (10.9 pts); lit_vs_default 2.2/1.93 (6.4 pts); raw_gemma_vs_human 1.31/1.42 (3.9 pts).

Constructions: emotion_pack.

Promotes: ` ವ್ಯವ` ` जलाश` `Tính` ` કંપની` ` აღმასრულ` `arriv` ` Stakes` `mineral` `Respondent` ` ص`  
Suppresses: `ꗜ` `Cs` ` Mira` ` Kes` ` PLDNN` ` Kumar`

- *human* (3216):  a voice buried in the echoes, a whisper on the wind. There was something dark in the voice, something angry, and the boy felt**[ a]** sharp fear in his gut.
- *other* (3600):  cool to the touch. Turning it over in his hand, he saw an inscription etched into the back: "Always find your way."⏎⏎**[A]** wave of unexpected emotion washed over
- *other* (3568):  flickered over her, assessing. “You remember,” he said, his voice low and gravelly. “After all these years.”⏎⏎**[A]** cold wave washed over her,
- *other* (3568):  to feed on the very essence of a person’s despair. ⏎⏎“Grandpa, what are you talking about?” I asked,**[ a]** knot forming in my stomach.
