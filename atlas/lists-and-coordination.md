# Lists and coordination

7 features. [Back to the index](../ATLAS.md)

| Feature | Label | Kind | Conf. | G | H | L | Promotes |
|---|---|---|---|---|---|---|---|
| [L2.38](#l238) | 'and' or 'or' joining a pair of nouns, often abstract pairs | construction | high | 2.4 | 2.3 | 2.8 | ꗜ 𒉶 &lt;unused338>  PLDNN 𒅤 |
| [L11.166](#l11166) | Separators deep inside long repetitive enumerations | construction | high | 0.0 | 0.0 | 0.1 | � &lt;unused687> &lt;unused1166> &lt;unused201> .&lt;/ |
| [L14.452](#l14452) | And or or joining coordinated nouns or verbs | construction | high | 4.9 | 2.9 | 3.8 | ꗜ 𒉶  PLDNN 𒅤 ꗐ |
| [L19.292](#l19292) | Final adjective in a stacked or intensified adjective run | construction | high | 5.1 | 1.6 | 1.0 | &lt;unused687> &lt;unused1166> &lt;unused201> � &lt;unused108> |
| [L19.3041](#l193041) | and before the final item of a list | construction | high | 4.5 | 2.1 | 3.9 | ..! 部份 部分  ziren  piernas |
| [L31.687](#l31687) | First adjective in a paired-adjective phrase like 'a slow, deliberate' | style | high | 6.2 | 1.5 | 1.3 | &lt;unused687>  도  افراد &lt;unused192>  apprezz |
| [L32.796](#l32796) | First item of a comma-separated list, before the comma | construction | high | 6.3 | 2.1 | 4.6 | &lt;unused87>  व्यक्ती سبب untamento Quién |

## L2.38

**'and' or 'or' joining a pair of nouns, often abstract pairs** (construction, high confidence)

Fires on the conjunction inside a noun pair or short list, strongest on abstract doublets like beauty and fragility or kindness and cruelty. Rates are similar across writers, but literary Gemma fires 2.5 times more than plain Gemma.

Fires on (% of tokens): wp/human 2.3, wp/gemma 2.4, wp/claude 2.8, wp/glm 2.8, books/human 2.3, books/gemma 1.9, books/haiku 2.9, books/gpt 2.0, books/glm 3.0, wp/gemma_plain 1.0, wp/gemma_lit 2.5, wp/gemma_greedy 2.4, wp/gemma_raw 2.3, wp/human_raw 2.3.

Constructions: list3.

Promotes: `ꗜ` `𒉶` `&lt;unused338>` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `DenovoMis` `𒂷` `posTocco`  
Suppresses: `�` `.&lt;/` `&lt;unused687>` ` cercando` `&lt;unused192>` `&lt;unused1077>`

- *human* (166):  say to his own defense. He skipped his 9-11 AM classes (*Botany II* and *Transcribing Voice: Applications**[ and]** Understanding*) precisely because it wa
- *human* (166):  with no success. I have become bored with every aspect of living. The technological wonders of this day and age no wonder amaze me. Relationships**[ and]** bonds I have formed over the
- *human* (158):  The. Food. It’s. Not. Me. I. Am. Completely. Normal.” Every word is loud and short, accent**[ and]** staccato. She repeats
- *Gemma* (176): . I’d witnessed the rise and fall of empires, the birth and death of religions. I’d seen beauty and horror, kindness**[ and]** cruelty, all with a detached
- *Gemma* (166): lways would be, the guardians of breakfast happiness. It also stipulated that any deviation from the established order – any hint of rivalry, dissent,**[ or]**, heaven forbid, *b
- *Gemma* (162): . I don’t publish them. I simply… keep them. I create these maps as a personal archive, a testament to the beauty**[ and]** fragility of human experience. I

## L11.166

**Separators deep inside long repetitive enumerations** (construction, high confidence)

Fires very strongly on commas, STOP, ellipses and bullets late in long runs of parallel items: lists of years, places, names or countdown numbers. Rare in all writers; its taste-set rate (0.009 approved, 0.012 rejected) is one token per text: it fires on the first text token after BOS, which only taste texts expose, so the rejected/approved gap reflects shorter rejected texts.

Fires on (% of tokens): wp/human 0.0, wp/gemma 0.0, wp/claude 0.1, wp/glm 0.1, books/human 0.1, books/gemma 0.0, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.1, wp/gemma_lit 0.0, wp/gemma_greedy 0.1, wp/gemma_raw 0.1, wp/human_raw 0.0.

Promotes: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused1077>` ` cercando` `&lt;unused1170>` `&lt;unused366>` `&lt;unused192>`  
Suppresses: `ꗜ` `𒉶` ` PLDNN` `𒅤` `&lt;unused338>` `MalayMarks`

- *human* (1568): C....0.8C (a new record)....0.81C....0.82C.....0.83C**[....]**then disaster. Alarms went
- *human* (1520): , 18th place, 14th place, 13th place, 9th place, 7th place**[,]** 6th place, 
- *human* (1440): huicxitia nican", "tlamachhuicxitia nican", "tlamachhuicxitia nican**[",]** "tlamachhuic
- *Gemma* (448):  Processing – specifically, the meticulous arrangement of nutrient paste. It came in five shades of beige: Pale, Mid-Tone, Standard, Rich**[,]** and Umber. Each shade
- *Gemma* (400): , chaotic, like a broken record skipping across multiple grooves. Sometimes it’s a single, isolated word – “Frederick,” “lost,”**[ “]**remember.” Other times it’
- *Gemma* (376):  birthday. Everyone in the world, every single person, received it. The day and month of their death. No year, no hour,**[ no]** minute. Just the 1

## L14.452

**And or or joining coordinated nouns or verbs** (construction, high confidence)

Fires on and or or linking two nouns or verbs in a pair or list (tools and techniques, sort and stack). Gemma uses it more than humans (0.049 vs 0.029 wp, 0.034 vs 0.020 books), and its literary mode about twice its plain mode.

Fires on (% of tokens): wp/human 2.9, wp/gemma 4.9, wp/claude 3.7, wp/glm 3.8, books/human 2.0, books/gemma 3.4, books/haiku 3.1, books/gpt 2.2, books/glm 3.0, wp/gemma_plain 2.6, wp/gemma_lit 5.1, wp/gemma_greedy 4.9, wp/gemma_raw 4.1, wp/human_raw 2.7.

Constructions: list3.

Promotes: `ꗜ` `𒉶` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `&lt;unused338>` `𒂷` `DenovoMis` `posTocco`  
Suppresses: `�` `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` `.&lt;/` `&lt;unused1077>`

- *human* (2594): . People used to chat, laugh, even exchange witty and sometimes flirty banter. Not anymore. It was a common misconception for the cops**[ and]** civilians to assume that new hires
- *human* (2514):  me. My soul wasn't dead, just wounded. I was so tired of seeing dead friends. The worst part was the more friends**[ and]** soldiers I gathered, the more
- *human* (2498): since a symbiosis of sorts had developed between organic and cybernetic tissue.⏎⏎These people were ruthless, inventing entirely new methods of torture**[ and]** execution to find the most efficient
- *Gemma* (2274): reconstructions of bustling palace walls and solemn rituals. I’d even lectured on them, gesturing at projected images, confidently outlining the tools**[ and]** techniques of a people whose language
- *Gemma* (2274): d they could trigger emotional responses without resorting to manipulative slogans. Corporations learned to harness the mimetic power to build loyalty**[ and]** encourage consumption.⏎⏎The shift
- *Gemma* (2178):  the GZC’s managed zoos – the Regent’s Park, the Tokyo Dome, even the notoriously competitive Serengeti Plains – in visitor numbers**[ and]**, more importantly, in breeding

## L19.292

**Final adjective in a stacked or intensified adjective run** (construction, high confidence)

Fires on the last adjective of a stacked run, often after an intensifier, as in a chaotic, vibrant, utterly overwhelming. Gemma uses it about five times as often as Claude, GPT or GLM, and three times as often as humans.

Fires on (% of tokens): wp/human 1.6, wp/gemma 5.1, wp/claude 1.0, wp/glm 1.1, books/human 1.4, books/gemma 4.3, books/haiku 1.0, books/gpt 1.0, books/glm 1.2, wp/gemma_plain 2.1, wp/gemma_lit 5.8, wp/gemma_greedy 5.1, wp/gemma_raw 3.1, wp/human_raw 1.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.53/2.33 (3.6 pts); books_gemma_vs_human 2.5/2.51 (2.9 pts); wp_gemma_vs_llm 3.42/3.69 (4.1 pts); books_gemma_vs_llm 2.96/3.15 (3.2 pts); plain_vs_default -2.28/-2.19 (-2.9 pts); raw_gemma_vs_human 1.25/1.35 (1.7 pts); chat_vs_raw_gemma 1.3/1.15 (2.1 pts).

Promotes: `&lt;unused687>` `&lt;unused1166>` `&lt;unused201>` `�` `&lt;unused108>` `&lt;unused1170>` `&lt;unused1077>` `Referências` `&lt;unused2040>` `&lt;unused366>`  
Suppresses: `ꗜ` `&lt;unused338>` `𒉶` `𒅤` ` PLDNN` `ꗐ`

- *human* (897): , using one of the in-game emotes. I panned the camera around my character and admired the beautifully-coloured, albeit low-**[polygon]**, models of the surrounding landscape
- *human* (889):  Jeremy Matthew Fink, age 30," the Judge announced. Screens in front of us lit up, showing us the face of a moderately**[ attractive]** man whose features belied his
- *human* (881):  yes dear all very melodramatic, boo hoo and all that.⏎⏎When she'd finally composed herself, she said a few more equally**[ banal]** things about love and life and
- *Gemma* (1089): . The Great Spoon is watching over us.”⏎⏎This was the reality of Cornflake City – a meticulously organized, relentlessly cheerful, and utterly**[ bizarre]** metropolis governed by the mascots
- *Gemma* (1049): , cataloging, analyzing.  Like a particularly unsettling insect under a microscope.  ⏎⏎Across from me, Kai Volkov, a ridiculously**[ handsome]**, perpetually tanned second-year
- *Gemma* (1001):  I hadn’t thought about this game in… well, a decade. Back then, it was my entire world. A sprawling, ridiculously**[ complicated]** MMORPG filled with gobl

## L19.3041

**and before the final item of a list** (construction, high confidence)

Fires on and, or an ampersand, before the last item of a list, especially triads of noun phrases. Literary-mode Gemma uses it most (0.052), about two and a half times the human rate.

Fires on (% of tokens): wp/human 2.1, wp/gemma 4.5, wp/claude 3.7, wp/glm 4.2, books/human 1.9, books/gemma 2.5, books/haiku 3.2, books/gpt 2.1, books/glm 3.3, wp/gemma_plain 1.9, wp/gemma_lit 5.2, wp/gemma_greedy 4.5, wp/gemma_raw 2.5, wp/human_raw 1.8.

Constructions: list3.

Promotes: `..!` `部份` `部分` ` ziren` ` piernas` ` töö` ` altid` `amenti` ` Hunde` ` ვერ`  
Suppresses: ` स्टैट` ` സാമൂഹ` ` Hatter` ` علاوه` ` mobile` ` تكون`

- *human* (545): I'd been traveling for days, flickering upon a sand covered beach one day, a desert the next**[ and]** once through a city of the
- *human* (529): ifer Morningstar rolled his eyes and licked his thin, red lips. They were together in a room of brimstone, black smoke,**[ and]** floating flames, Kaldon seated
- *human* (525):  the heater wafted past me I caught a whiff of the stench that I carried on me like a bad story. Cigarettes, whiskey,**[ and]** masculine sweat; the current story
- *Gemma* (585):  A small town nestled deep in the Appalachian Mountains, it offered a startling lack of ambition, a general disinterest in anything remotely exciting,**[ and]** a population that seemed permanently re
- *Gemma* (581):  joyous shower. It was a viscous, grey film that perpetually coated everything, clinging to the impossibly perfect white lilies, the sculpted clouds,**[ and]**, most persistently, to my
- *Gemma* (577):  I’d hunted him. Twenty years of tracking his malice, of witnessing the slow, agonizing decay he’d leave in his wake,**[ and]** twenty years of steel against shadow

## L31.687

**First adjective in a paired-adjective phrase like 'a slow, deliberate'** (style, high confidence)

Fires on the first adjective after 'a' or 'the' when a second adjective follows ('a frantic, desperate', 'a dull, repetitive'). A Gemma habit: 6% of Gemma's tokens versus 1-1.5% for humans, Claude, GLM, GPT and Haiku, and 9% in its literary mode.

Fires on (% of tokens): wp/human 1.5, wp/gemma 6.2, wp/claude 1.1, wp/glm 1.5, books/human 1.4, books/gemma 6.2, books/haiku 1.3, books/gpt 1.0, books/glm 1.7, wp/gemma_plain 1.6, wp/gemma_lit 8.6, wp/gemma_greedy 6.0, wp/gemma_raw 3.5, wp/human_raw 1.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.77/2.67 (4.7 pts); books_gemma_vs_human 3.17/2.78 (4.9 pts); wp_gemma_vs_llm 3.5/3.25 (4.9 pts); books_gemma_vs_llm 3.25/2.99 (4.9 pts); lit_vs_plain 4.5/4.25 (7.0 pts); lit_vs_default 1.49/1.35 (2.5 pts); plain_vs_default -3.11/-2.81 (-4.6 pts); raw_gemma_vs_human 1.29/1.43 (2.2 pts); chat_vs_raw_gemma 1.36/1.18 (2.7 pts).

Promotes: `&lt;unused687>` ` 도` ` افراد` `&lt;unused192>` ` apprezz` `&lt;unused366>` ` ক্রয়` ` অন্য` `�` ` शरद`  
Suppresses: `&lt;unused1716>` `&lt;unused338>` `ꗜ` `𒉶` `∣` `&lt;unused1640>`

- *human* (1736):  the wing to her right rustling papers on the low table before her. She read through the reports they'd brought her and ignored the**[ quiet]** echoing steps of visitors come to
- *Gemma* (2200):  helmet, and continued hacking mushrooms.⏎⏎The first few years had been… amusing. A slow, methodical dismantling of my own power, a**[ quiet]**, defiant rebellion against the inevitab
- *Gemma* (2040):  the slick cobblestones and reflecting the neon glow of the Rowdy Raccoon with a sickly, iridescent sheen. Joker watched it fall, a**[ slow]**, deliberate trickle of observation,
- *Gemma* (2040):  it wasn’t *big*. Maybe a kilometer across at its widest point. ⏎⏎I’d spent the first few days in a**[ frantic]**, adrenaline-fueled search for
- *other LLM* (1992):  a notebook. Over two years I logged twenty-three residents of that hospice, each with a prognosis, most delivered by Pruett in his**[ gentle]**, apologetic voice. Twenty
- *other LLM* (1920): e, by every metric the Accord cared about, unremarkable. Their propulsion was chemical. Their computation was clever but brittle. Their medicine was a**[ frantic]** mix of brilliance and superstition,

## L32.796

**First item of a comma-separated list, before the comma** (construction, high confidence)

Fires on the first noun of a list just before its comma (their faces, their voices). Seven times more frequent in Gemma's literary mode than plain mode, and about twice as frequent in LLM prose as human prose.

Fires on (% of tokens): wp/human 2.1, wp/gemma 6.3, wp/claude 4.7, wp/glm 4.6, books/human 3.8, books/gemma 6.0, books/haiku 5.5, books/gpt 5.5, books/glm 5.5, wp/gemma_plain 1.0, wp/gemma_lit 7.1, wp/gemma_greedy 6.3, wp/gemma_raw 3.7, wp/human_raw 1.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human 2.88/2.75 (4.2 pts); wp_llm_vs_human 1.66/1.9 (2.5 pts); books_llm_vs_human 1.47/1.37 (1.7 pts); lit_vs_plain 5.08/5.4 (6.1 pts); plain_vs_default -4.07/-4.11 (-5.4 pts); raw_gemma_vs_human 1.67/1.56 (2.4 pts); chat_vs_raw_gemma 1.51/1.49 (2.6 pts).

Promotes: `&lt;unused87>` ` व्यक्ती` `سبب` `untamento` `Quién` ` tubuh` `isempty` `apsible` `椥` ` ঘোষণা`  
Suppresses: `》，` ` !,` `®,` `》` `!` `!”,`

- *human* (1000):  I'm so terrified right now.⏎⏎With all the money I had to spare, I bought excessive amounts of security devices; alarms,**[ cameras]**, fences around the house,
- *Gemma* (1476): ’d specialized in the study of conflict and cooperation – a subject now suddenly considered tragically vital. He, along with a rotating team of lingu**[ists]**, psychologists, sociologists,
- *Gemma* (1404):  it.”⏎⏎“You curate it,” Lust corrected, the shimmer intensifying around his edges. “You pre-select the ingredients – the attractive**[ faces]**, the compatible interests, the
- *Gemma* (1364):  haze that clung to everything – our suits, the habitat, even the inside of my nostrils. Mars. It was real. After decades of**[ planning]**, billions of dollars, and
- *other LLM* (1224):  a bound Captain Solstice, gesturing at the skyline, explaining his plan to seize the city's tide buffers in exhaustive detail — dates,**[ codes]**, fail-safes —
- *other LLM* (1204):  away. They haven't expelled me because of the Halcyan Exam.⏎⏎Every applicant takes it. The Halcyan measures heroic potential —**[ courage]**, instinct, the deep wiring
