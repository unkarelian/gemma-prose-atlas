# Informal human texture

18 features. [Back to the index](../ATLAS.md)

| Feature | Label | Kind | Conf. | G | H | L | Promotes |
|---|---|---|---|---|---|---|---|
| [L3.4140](#l34140) | Completion of 'some-' words, strongest in dialect forms like somethin' | lexical | medium | 0.4 | 0.4 | 0.5 | on  noget  yerde crafted  else |
| [L4.3884](#l43884) | Orthographic slips: lowercase 'i' pronoun or a switched quote style | lexical | low | 0.4 | 0.1 | 0.0 | ꗜ 𒂷 ꗐ &lt;unused593> odikwa |
| [L11.2054](#l112054) | Mixed; strongest on it in Reddit author notes | unclear | low | 0.1 | 0.1 | 0.1 | ꗜ &lt;unused338>  PLDNN 𒉶 MalayMarks |
| [L16.2323](#l162323) | Grammatical slips: doubled, missing or mismatched words | construction | high | 0.1 | 4.3 | 1.1 |  tipo  trabajado  예를 륭  無 |
| [L16.5815](#l165815) | Human WritingPrompts prose; silent on nearly all LLM text | style | high | 0.0 | 58.3 | 2.3 |  ചു  በ  ಮತ್ತು � \uf069 |
| [L20.1373](#l201373) | Mid-utterance words in casual or dialect spoken dialogue | style | medium | 2.5 | 11.5 | 12.8 |  RID  Mad  कर्ण 맟  drives |
| [L21.1135](#l211135) | Broad marker of human WritingPrompts text; absent in LLM prose | style | medium | 0.0 | 35.9 | 1.5 |  derivs पचारिक  소비자 ल्लिंग 更好的 |
| [L25.1452](#l251452) | Plain colloquial wording, mostly in casual dialogue | style | medium | 6.2 | 13.5 | 24.6 | polished  `>=`,  Practice  Practices  hagg |
| [L26.2282](#l262282) | Amateur online human prose; almost silent on any model's text | style | medium | 0.0 | 60.2 | 0.5 |  aswell  allong appendText  stomp  कदम |
| [L27.738](#l27738) | Human-register text outside chat replies; near zero in Gemma's stories | style | medium | 0.4 | 46.2 | 6.4 |    。... ?...           |
| [L28.12980](#l2812980) | Casual British spoken register in dialogue; promotes 'bit' | style | medium | 0.8 | 1.0 | 3.0 |  bit  bits  Bit bit Bit |
| [L29.231](#l29231) | Emphatic speech slot where an expletive could go; promotes damn | predictive | medium | 21.3 | 18.0 | 30.6 |  god  bloody  damn  damned  fucking |
| [L31.402](#l31402) | Phrase-final word in colloquial or dialect speech | style | medium | 1.5 | 2.6 | 3.7 |  them them  Them  something  theſe |
| [L31.985](#l31985) | Amateur web-fiction register; fires on half of human Reddit tokens | style | high | 0.0 | 47.5 | 2.0 |  BECAUSE  बिकॉज !!!!!!! !.. !!!!!! |
| [L32.3885](#l323885) | Clause-final word in human prose; promotes ASCII double-hyphen dashes | style | medium | 0.0 | 47.1 | 3.5 | --“  "-- “- 、“ "-- |
| [L32.5959](#l325959) | Sentence end after a comic or self-deprecating beat | style | low | 4.7 | 7.2 | 6.7 |  U U  u u  У |
| [L33.212](#l33212) | Human-text marker, peaking on apostrophes in contractions | confidence | medium | 0.9 | 52.4 | 4.0 | ꗜ &lt;unused338> 𒉶  PLDNN 𒅤 |
| [L33.2461](#l332461) | Plain, simple spoken register; suppresses formal Latinate words | style | high | 4.1 | 14.4 | 19.3 | োপাধ্যায়  tenéis  .,  cierra ². |

## L3.4140

**Completion of 'some-' words, strongest in dialect forms like somethin'** (lexical, medium confidence)

Fires on the token completing some- words, strongest on dialect spellings (somethin', sumpin, sumbuddy) and on somehow, with weaker hits on 'some kind of'. Rates are flat across writers.

Fires on (% of tokens): wp/human 0.4, wp/gemma 0.4, wp/claude 0.6, wp/glm 0.5, books/human 0.4, books/gemma 0.5, books/haiku 0.6, books/gpt 0.4, books/glm 0.6, wp/gemma_plain 0.5, wp/gemma_lit 0.4, wp/gemma_greedy 0.4, wp/gemma_raw 0.5, wp/human_raw 0.4.

Constructions: something.

Promotes: `on` ` noget` ` yerde` `crafted` ` else` `href` ` variation` ` Styled` `بق` `ب`  
Suppresses: `써` `mış` `இய` ` pabbaj` ` PBMCs` `கு`

- *human* (150):  huff and leaned onto one hip much like an overweight horse did. "Remind me why again you're here? Somethin**[']** about your ma?" He stared
- *human* (124):  a human would have thought of as a deep sigh. I KNEW THAT LAW WAS GOING TO CAUSE ME A HEADACHE SOME**[HOW]**. I SHOULD HAVE VETO
- *Gemma* (85): iness that seemed to span centuries. ⏎⏎“Dr. Alistair Finch?” he asked, his voice strained, filtered through some kind**[ of]** modulator. ⏎⏎“That
- *Gemma* (80): nto something ancient and profoundly unsettling.⏎⏎I posted the images on an online forum dedicated to obscure historical symbols, hoping for some kind**[ of]** identification. The responses were…
- *Gemma* (79):  break the rules – jaywalking, shouting obscenities, attempting to start a small fire with a discarded newspaper – hoping to trigger some kind**[ of]** system error. Nothing. The
- *other LLM* (106):  ALONE. WHO WALKS YOU TO YOUR CAR.⏎⏎And underneath: I'M SORRY. I SHOULD HAVE SAID SOMETH**[ING]** WEEKS AGO.⏎⏎

## L4.3884

**Orthographic slips: lowercase 'i' pronoun or a switched quote style** (lexical, low confidence)

Fires on a lowercase i used as a pronoun in casual human and forum text, and on a straight quote opening speech after curly-quoted text in Gemma. The two cases may share a 'nonstandard character' signal, but that is a guess; Gemma, especially raw, fires most.

Fires on (% of tokens): wp/human 0.1, wp/gemma 0.4, wp/claude 0.0, wp/glm 0.0, books/human 0.0, books/gemma 0.2, books/haiku 0.0, books/gpt 0.0, books/glm 0.0, wp/gemma_plain 0.3, wp/gemma_lit 0.2, wp/gemma_greedy 0.0, wp/gemma_raw 0.9, wp/human_raw 0.1.

Writer contrasts (paired effect size on each half, change in firing rate): greedy_vs_sampled -1.22/-1.23 (-0.4 pts); raw_gemma_vs_human 1.2/1.2 (0.8 pts).

Promotes: `ꗜ` `𒂷` `ꗐ` `&lt;unused593>` `odikwa` `𒅤` `𒉶` `ُ` ` PLDNN` `טאטורק`  
Suppresses: `&lt;unused201>` `&lt;unused1166>` `&lt;unused1088>` `&lt;unused187>` `icions` `。...`

- *human* (98):  stepped outside those solid steel doors.. they slam behind me. The first thing I notice is my breathing.. for some reason I feel as though**[ i]**'m trying to breathe through
- *human* (91):  from our destination. I'd been here about 500 years, I only had 1500 to go, and**[ i]**'d developed quite the system
- *human* (90):  dunno. I don't know."⏎⏎"You were! Aw, you sick fuck!"⏎⏎"No, I might have, but**[ i]**-it just felt like vertigo
- *Gemma* (106): , a flicker of something akin to pity crossing his face. “It lacks… resonance,” he’d finally said, his voice flat.**[ "]**It's… functional.
- *Gemma* (101):  The language, while fundamentally English, was laced with a bewildering array of slang and colloquialisms. "Howdy," they kept saying.**[ “]**That’s mighty fine,”
- *Gemma* (96): ’t want a blank slate,” I’d argued, surprised by the intensity of my own conviction. “He’s…he'**[s]** becoming *himself*.  

## L11.2054

**Mixed; strongest on it in Reddit author notes** (unclear, low confidence)

Top human examples are it referring to the story in Reddit author notes (hope you like it), and raw Gemma fires ten times more than other sets (0.012 vs 0.001), but LLM examples look unrelated. Its taste-set rate (0.009 approved, 0.012 rejected) is one token per text: it fires on the first text token after BOS, which only taste texts expose, so the rejected/approved gap reflects shorter rejected texts.

Fires on (% of tokens): wp/human 0.1, wp/gemma 0.1, wp/claude 0.1, wp/glm 0.1, books/human 0.1, books/gemma 0.1, books/haiku 0.1, books/gpt 0.1, books/glm 0.1, wp/gemma_plain 0.1, wp/gemma_lit 0.1, wp/gemma_greedy 0.1, wp/gemma_raw 1.2, wp/human_raw 0.2.

Promotes: `ꗜ` `&lt;unused338>` ` PLDNN` `𒉶` `MalayMarks` `𒅤` `ꗐ` `DenovoMis` `odikwa` `posTocco`  
Suppresses: `&lt;unused687>` `&lt;unused1166>` `&lt;unused192>` `&lt;unused366>` `&lt;unused2040>` `&lt;unused201>`

- *human* (277):  one of these writing prompts (also my first reddit post.) I am a little late to this one, but hopefully some one out there enjoys**[ it]**!⏎⏎-- -- -- --
- *human* (207): My first time posting a story, hope you like**[ it]**.⏎⏎The Xeneria
- *human* (185): This is a little long, so I'm going to put**[ it]** in two comments.⏎⏎Before
- *Gemma* (279):  Pratchett. Author.  Specifically, of the Discworld series. A surprisingly popular collection of anthropomorphic animals and improbable adventures. He**[’]**d shuffled off this mortal coil
- *Gemma* (172):  rain hammered against the windows, a relentless, mournful rhythm. I was trying to read, attempting to lose myself in the predictable plot of**[ a]** detective novel, but the atmosphere
- *Gemma* (147):  grey light, reflecting the panic rising in my throat.⏎⏎The connection. It was finally here.⏎⏎Everyone in Havenwood, and probably**[ the]** world, experienced it on their

## L16.2323

**Grammatical slips: doubled, missing or mismatched words** (construction, high confidence)

Fires on tokens that break grammar, such as a doubled 'in', a missing subject, 'a unsettling' or 'a greasy overalls'. Human WritingPrompts text hits it on 4.3% of tokens against 0.1% for Gemma and about 1% for other LLMs.

Fires on (% of tokens): wp/human 4.3, wp/gemma 0.1, wp/claude 0.8, wp/glm 1.4, books/human 1.9, books/gemma 0.1, books/haiku 0.6, books/gpt 0.6, books/glm 0.7, wp/gemma_plain 0.1, wp/gemma_lit 0.1, wp/gemma_greedy 0.0, wp/gemma_raw 0.4, wp/human_raw 2.9.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -3.47/-3.33 (-4.2 pts); books_gemma_vs_human -2.38/-1.98 (-1.8 pts); wp_llm_vs_human -2.45/-2.46 (-3.2 pts); books_llm_vs_human -1.69/-1.3 (-1.3 pts); wp_gemma_vs_llm -2.17/-2.01 (-1.0 pts); books_gemma_vs_llm -1.78/-1.76 (-0.5 pts); raw_gemma_vs_human -2.01/-2.17 (-2.5 pts).

Promotes: ` tipo` ` trabajado` ` 예를` `륭` ` 無` `মাম` `மிருந்து` `𒊺` `μένο` ` விதைகள்`  
Suppresses: `inflate` `เอก` `alignment` `character` `곱` ` IFC`

- *human* (581):  were gone, now, both speed and heavy. The ring had been removed, piece by piece. It lay, a disassembled ruin, in**[ in]** the basement, bags and stands
- *human* (541):  himself slowly up the counter to have a look in the mirror.⏎⏎No flesh on his face, either, dammit.⏎⏎He realised**[ was]** probably going to have to call
- *human* (533): ’t recognize. The heavy silence turned into a whispered murmur as people stepped aside one-by-one to form a path to the stairs**[.]**⏎⏎Making my way through the
- *Gemma* (483):  spent every afternoon reading tattered paperbacks and nursing a single cup of chamomile tea. There was George, a mechanic who always wore a greasy**[ overalls]** and complained about the price of
- *Gemma* (325):  hand trembling. The chain is stiff, coated in years of accumulated grime and neglect. It resists, a stubborn refusal to yield. My breath**[ hit]**ches in my chest. This
- *Gemma* (313): y *rearranged* them. They ‘optimized’ them. They replaced perfectly functional wells with holographic fountains that spouted iridescent water, turning**[ into]** instant tourist traps. They gutted

## L16.5815

**Human WritingPrompts prose; silent on nearly all LLM text** (style, high confidence)

Fires on 58% of tokens in human WritingPrompts stories and 16% in human book scenes, but 0% for Gemma, 1% for Claude and 3.5% for GLM. Peaks fall on clause-final words and punctuation, so it reads as a broad detector of amateur human prose.

Fires on (% of tokens): wp/human 58.3, wp/gemma 0.0, wp/claude 1.1, wp/glm 3.5, books/human 15.8, books/gemma 0.1, books/haiku 1.2, books/gpt 1.7, books/glm 1.4, wp/gemma_plain 0.1, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 1.2, wp/human_raw 39.9.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -3.3/-2.89 (-58.3 pts); books_gemma_vs_human -1.5/-1.22 (-15.8 pts); wp_llm_vs_human -3.16/-2.85 (-56.2 pts); books_llm_vs_human -1.42/-1.17 (-14.4 pts); raw_gemma_vs_human -2.17/-1.87 (-38.7 pts).

Promotes: ` ചു` ` በ` ` ಮತ್ತು` `�` `\uf069` `&lt;unused2040>` ` বিরাট` `escens` ` ম্যাজিস্ট` ` dwarves`  
Suppresses: ` розгля` `𒉶` ` iba` `𒅤` `apetiti` ` pedestrian`

- *human* (771):  *adore* this dress…” noted the woman.⏎⏎"I'll buy you another.” said the man, kissing her on the neck**[ as]** he fondled her pale body
- *human* (723):  The desk I sat behind was a dark wood, the surface tattered and stained by blood and tears and had fingernail marks all over the**[ top]**.⏎⏎Between the judge'
- *human* (687):  coming conflict. In the end, I was the only one left, standing on that bleak hillside, left to stare at the object and brood**[.]**⏎⏎Unlike the surrounding hillside,
- *Gemma* (153):  a liability, a useless adolescent clinging to the edges of an adventure I wasn’t equipped to handle.⏎⏎The drive to go on this**[ trip]** stemmed from a strange restlessness wit
- *other LLM* (475):  table and waited to find out if I was having a stroke. I smiled at the window to check whether both sides of my face worked.**[ I]** said "Walter Dennis Okafor
- *other LLM* (407):  launch window moved up or my clock didn't. The inquiry will decide. We'll hear the findings, I think. It turned**[ out]** we'd hear everything.

## L20.1373

**Mid-utterance words in casual or dialect spoken dialogue** (style, medium confidence)

Fires inside colloquial or dialect speech (ain't, folks tryin', must be) on verbs and function words, and suppresses filler words like vraiment and Hmmm. Human and other LLM text fire on it far more than Gemma (wp human 0.115 vs Gemma 0.025, literary Gemma 0.004), and approved edits fire more than rejected drafts.

Fires on (% of tokens): wp/human 11.5, wp/gemma 2.5, wp/claude 14.3, wp/glm 11.3, books/human 17.0, books/gemma 6.8, books/haiku 15.5, books/gpt 15.2, books/glm 16.4, wp/gemma_plain 8.1, wp/gemma_lit 0.4, wp/gemma_greedy 2.4, wp/gemma_raw 4.7, wp/human_raw 10.3.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_default -0.93/-0.89 (-1.9 pts).

Promotes: ` RID` ` Mad` ` कर्ण` `맟` ` drives` ` plays` `Mad` ` cf` ` Cf` ` fa`  
Suppresses: ` opravdu` ` ça` `ちょっと` ` เดี๋ยว` `どんどん` ` vraiment`

- *other* (509):  herself than I was.⏎⏎“This is my nana, Shirley, she’s the only one I got and some days she doesn’**[t]** know who I am. The
- *other* (469):  it, and “That’s gon na come in handy some day when you’ve got yourself a wife and don’t feel like**[ tak]**in ’ out the trash every
- *other* (465):  as soon as I heard, I wanted to meet this fancy-schmancy highfalutin Ay-Eye thingamabob that'**[s]** been given so much leeway to

## L21.1135

**Broad marker of human WritingPrompts text; absent in LLM prose** (style, medium confidence)

Fires on ordinary mid-sentence words throughout human WritingPrompts stories and the taste texts, with no clear shared word. It fires on 36 percent of human WritingPrompts tokens and almost none of Gemma's, Claude's or GLM's, and less on human novels (0.093).

Fires on (% of tokens): wp/human 35.9, wp/gemma 0.0, wp/claude 0.9, wp/glm 2.0, books/human 9.3, books/gemma 0.0, books/haiku 0.7, books/gpt 0.9, books/glm 0.7, wp/gemma_plain 0.1, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 5.0, wp/human_raw 46.3.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -3.09/-2.88 (-35.9 pts); books_gemma_vs_human -1.51/-1.25 (-9.2 pts); wp_llm_vs_human -2.95/-2.87 (-34.5 pts); books_llm_vs_human -1.43/-1.19 (-8.5 pts); raw_gemma_vs_human -4.13/-3.5 (-41.4 pts).

Promotes: ` derivs` `पचारिक` ` 소비자` `ल्लिंग` `更好的` ` নির্বাচিত` ` которыми` ` praktische` `ക്കാൻ` `🏷`  
Suppresses: ` Hone` ` Package` `CZ` ` Since` `Since` `比利`

- *human* (456): Hypergullibility Syndrome" (only a hypothesis so far), which meant that either a) John just believed whatever was told to him without**[ spending]** any time mulling over it
- *human* (444):  don't want to hear that" *His training supervisor Frank had told him. "*Try something more upbeat, something inspiring, so that**[ as]** soon as they call, they
- *human* (436):  who told me the same thing: "Just start writing!" But I can't! I'm trapped here. The only time it**[ had]** felt like I wasn't
- *Gemma* (204):  balance, and tasked me with a singular, brutal duty: to purge the human race. ⏎⏎And the criteria? Simple. I would**[ only]** remember the names of those I
- *Gemma* (178): , devoid of any discernible emotion – had stated. “It will be recorded, analyzed, and studied by the brightest minds on the planet.**[ Do]** you understand?”⏎⏎I’
- *Gemma* (176):  a piercing, unsettling blue, held a disconcerting knowledge, a sense of having witnessed things that shouldn’t be seen.⏎⏎“I**[ understand]** your skepticism, Doctor,” Silas

## L25.1452

**Plain colloquial wording, mostly in casual dialogue** (style, medium confidence)

Fires on everyday words ending casual spoken phrases, including dialect speech (gets on my nerves, all the time). Nearly silent in Gemma's literary mode and high in its plain mode, Claude and GLM, and higher in the taste approved edits than in the rejected drafts.

Fires on (% of tokens): wp/human 13.5, wp/gemma 6.2, wp/claude 26.5, wp/glm 22.7, books/human 15.1, books/gemma 7.9, books/haiku 16.2, books/gpt 15.6, books/glm 16.7, wp/gemma_plain 21.1, wp/gemma_lit 0.8, wp/gemma_greedy 6.3, wp/gemma_raw 7.9, wp/human_raw 11.6.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_llm -1.99/-2.0 (-18.5 pts); lit_vs_default -1.19/-1.24 (-5.5 pts).

Promotes: `polished` ` `>=`,` ` Practice` ` Practices` ` hagg` ` practice` `practice` `capacity` ` Bayes` `емости`  
Suppresses: ` right` `Right` ` Right` `right` `RIGHT` ` RIGHT`

- *human* (1266): "Are you sure? It's hella**[ boring]** mayne, really nothing worth
- *Gemma* (1098):  appointments and endless rounds of antibiotics. I’d always attributed it to a particularly nasty bout of childhood illness. “Yeah. I remember being**[ sick]** a lot.”⏎⏎“Well
- *other LLM* (1354): Sometimes the ordinary days are the heaviest ones."⏎⏎"Yeah." A pause. "That's exactly it. Nothing happened. Nothing ever**[ happens]**. I just keep thinking I
- *other LLM* (1242): engine shop," I said. "Forty-one years. Kovacs Small Engine, out on Route 9. My dad used to come**[ by]** Saturdays after he retired, and
- *other LLM* (1234):  finally noticed her. She looked Comet up and down and turned back to her father with fresh ammunition. "Great. Now the city's**[ here]**. Is this what the satellite
- *other* (1282):  boy, whose name was Leo, surprisingly understood. He pointed to a nearby shed, overflowing with garden tools. “My grandpa uses an extension**[ cord]** to power his lights. You

## L26.2282

**Amateur online human prose; almost silent on any model's text** (style, medium confidence)

Fires on about 60% of tokens in human WritingPrompts stories and near zero for Gemma, Claude and GLM, but only 4.5% in published human novels. Top examples are 'as' in 'as if', and it promotes misspelled forms like 'aswell' and 'allong', so it reads as a casual-web register detector.

Fires on (% of tokens): wp/human 60.2, wp/gemma 0.0, wp/claude 0.3, wp/glm 0.8, books/human 4.5, books/gemma 0.0, books/haiku 0.2, books/gpt 0.2, books/glm 0.2, wp/gemma_plain 0.1, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 5.6, wp/human_raw 66.8.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -3.02/-2.81 (-60.2 pts); wp_llm_vs_human -3.0/-2.83 (-59.9 pts); books_llm_vs_human -1.11/-0.89 (-4.3 pts); raw_gemma_vs_human -2.88/-2.81 (-61.1 pts).

Promotes: ` aswell` ` allong` `appendText` ` stomp` ` कदम` ` antics` ` pertain` ` फेल` `闡` ` acom`  
Suppresses: ` ==>` ` &lt;` `чному` ` થયા` `portivo` `/&lt;`

- *human* (1363): ing shit!" I exclaimed thinking without repercussion. Rage and anger immediately took hold and I spoke without remorse or fear of consequence. It felt**[ as]** if I couldn't stop
- *human* (1283): .⏎⏎"I would like to know before we do this do you wish to be alone?" everyone at once began to talk. It sounded**[ as]** if everyone in the building or
- *human* (1179):  no questions asked, and run as the fugitive he is.⏎⏎"Sure... Let's go with that," He sighs. Its almost**[ as]** if I can hear the mechanical
- *Gemma* (287):  you busy. Pays enough for a crust and a corner.”⏎⏎He hadn't asked about my past. No one did. It was**[ as]** if my arrival was a random
- *Gemma* (247): ⏎⏎Elias paused, seemingly struggling to articulate something beyond words. “It’s… wrong,” he finally said, his voice distant,**[ as]** if speaking through a thick veil
- *Gemma* (245): ,” the reflection replied, a dry, cynical inflection in its tone. “Though I’d appreciate it if you didn’t announce the**[ rather]** obvious.”⏎⏎I cautiously approached

## L27.738

**Human-register text outside chat replies; near zero in Gemma's stories** (style, medium confidence)

Fires on 46-63% of human WritingPrompts tokens and about half of both taste sets, but under 1% of Gemma's chat-template stories (14% when Gemma writes without the template). Examples are plain, run-on amateur narration; it promotes whitespace runs and suppresses the junk tokens that dense model-prose features promote.

Fires on (% of tokens): wp/human 46.2, wp/gemma 0.4, wp/claude 4.8, wp/glm 8.0, books/human 15.8, books/gemma 0.5, books/haiku 3.5, books/gpt 3.3, books/glm 3.9, wp/gemma_plain 1.0, wp/gemma_lit 0.3, wp/gemma_greedy 0.3, wp/gemma_raw 14.2, wp/human_raw 63.0.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -3.57/-3.26 (-45.8 pts); books_gemma_vs_human -1.78/-1.57 (-15.2 pts); wp_llm_vs_human -3.14/-2.87 (-39.7 pts); books_llm_vs_human -1.61/-1.45 (-12.2 pts); wp_gemma_vs_llm -1.89/-1.81 (-6.0 pts); raw_gemma_vs_human -4.21/-4.01 (-48.8 pts); chat_vs_raw_gemma -1.49/-1.4 (-13.8 pts).

Promotes: `  ` `。...` `?...` `     ` `   ` `              ` `                 ` `             ` `    ` `        `  
Suppresses: `ꗜ` ` PLDNN` `𒉶` `odikwa` `ꗐ` `∣`

- *human* (676):  doors leading to bedrooms on the left side and two doors on the right, the closest one that leads to the garage is painted red on both**[ sides]**, the farthest of the two
- *human* (664):  on top as they pull me back closer to the ER. The doctor next me was screaming to the greeter to call down to the ER**[ ahead]** of us.⏎⏎At this
- *human* (646): 45 AM. This was the case, he reasoned, because by leaving slightly earlier he dodged both the stop-light timings adjustment as**[ well]** as a majority of morning rush
- *other LLM* (530):  so item twelve makes sense. When our mother was dying, I handled everything, and "everything" included lying to my brother on our Sunday**[ calls]**. *She's stable
- *other LLM* (516):  addressed the same way: To the one who receives this. Do you remember the lighthouse at Vesterø? Did the surgery take? Write**[ back]**. Someone always wrote back,
- *other LLM* (506):  and also very sad. He eat the sun because he was cold and also because nobody liked him. This was because of the eating of the**[ sun]**. It was a big problem

## L28.12980

**Casual British spoken register in dialogue; promotes 'bit'** (style, medium confidence)

Fires in colloquial dialogue, much of it in a British school voice, at slots like 'A lot of us' or 'He's got', and promotes 'bit'. It fires twice as often in the reader's approved edits (0.18) as in the rejected drafts (0.08), and more in human book scenes (0.11) than Gemma's (0.05).

Fires on (% of tokens): wp/human 1.0, wp/gemma 0.8, wp/claude 3.5, wp/glm 2.6, books/human 11.2, books/gemma 4.9, books/haiku 10.1, books/gpt 8.2, books/glm 10.0, wp/gemma_plain 1.6, wp/gemma_lit 0.3, wp/gemma_greedy 0.8, wp/gemma_raw 0.7, wp/human_raw 1.1.

Promotes: ` bit` ` bits` ` Bit` `bit` `Bit` ` Bits` `bits` `Bits` ` BIT` ` aswell`  
Suppresses: ` كثير` ` سول` ` تصير` ` butts` `讓你` ` அதிகமாக`

- *other* (1517):  in the fingerless gloves we all wore would sound a tone in our ear when full contact was made, and we could move on. The**[ difficult]** part was the actual finding.

## L29.231

**Emphatic speech slot where an expletive could go; promotes damn** (predictive, medium confidence)

Fires on determiners and possessives in angry or exasperated speech, as in 'Get out of my house', and promotes damn, bloody, god and similar. It fires more in the approved edits (0.17) than the rejected drafts (0.11), and most in Claude and GLM stories (about 0.3).

Fires on (% of tokens): wp/human 18.0, wp/gemma 21.3, wp/claude 31.8, wp/glm 29.4, books/human 17.6, books/gemma 15.7, books/haiku 19.0, books/gpt 16.7, books/glm 21.2, wp/gemma_plain 10.3, wp/gemma_lit 13.5, wp/gemma_greedy 21.2, wp/gemma_raw 11.9, wp/human_raw 14.6.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_default -1.35/-1.57 (-7.9 pts).

Promotes: ` god` ` bloody` ` damn` ` damned` ` fucking` `God` ` God` `god` `damn` ` Damn`  
Suppresses: `ลักษณ์` `োঁ` `妥` `atoti` ` Winkel` `मेटिक`

- *human* (2780): ? That watching my mother go through her cancer and die slowly was supposed to be some great experience?.... Who the fuck are you?! Show**[ your]** goddamned face!"⏎⏎
- *human* (2748):  in front, and seemingly plastic in how perfectly it’s groomed. And the clothes. Who wears a suit and tie at 1 in**[ the]** morning on a deserted desert road
- *human* (2732):  the small moral victory of being asleep and dodging that bullet this one time felt... who the hell am I kidding? I wish I had answered**[ the]** call.⏎⏎Film was always
- *Gemma* (2428):  every single pigeon in the city seemed to be staring directly at me, tilting their heads with an unsettlingly deliberate curiosity. And the books.**[ So]** many books.⏎⏎Not just
- *Gemma* (2284):  cycles, a slow, relentless bleed that coated everything in a grey sheen. I didn’t bother to bother with an umbrella. What was**[ the]** point? The atmosphere was still
- *Gemma* (2204):  he’d just nodded, retreating to the sofa with a book and a vow of solitary darkness.⏎⏎It had become our routine. Every**[.]** Single. Morning. Leo,

## L31.402

**Phrase-final word in colloquial or dialect speech** (style, medium confidence)

Fires at the end of idiomatic, regional or slangy spoken phrases ('keep his cool', 'a bit whiffy', 'had a go at her'). More frequent in human and other-LLM prose than in Gemma's, nearly absent from Gemma's literary mode, and higher in approved edits (4.3%) than rejected drafts (2.5%).

Fires on (% of tokens): wp/human 2.6, wp/gemma 1.5, wp/claude 3.5, wp/glm 4.0, books/human 4.4, books/gemma 2.3, books/haiku 4.2, books/gpt 3.5, books/glm 4.3, wp/gemma_plain 1.7, wp/gemma_lit 0.7, wp/gemma_greedy 1.4, wp/gemma_raw 0.8, wp/human_raw 1.9.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_default -1.03/-0.87 (-0.9 pts).

Promotes: ` them` `them` ` Them` ` something` ` theſe` ` southbound` ` conic` ` breathable` ` confortable` ` these`  
Suppresses: `&lt;unused338>` `𒉶` `𒅤` `ꗜ` `ꗨ` `&lt;unused429>`

- *human* (1618):  fellow walking over furiously nodding and staring directly at her made her assume he was addressing her.⏎⏎“Aye been shovling shite outta the**[ pens]** dis morning. What the bug
- *Gemma* (1426):  I grumbled, adjusting the strap of my waterproof satchel, “couldn’t you have predicted this? It’s been steadily**[ escalating]** for the last hour.”⏎⏎
- *other LLM* (1666):  "I'll make it right, Meg, no charge—"⏎⏎"Break? It cuts through rock. I hit the old boundary**[ stone]** at the bottom field, the
- *other* (1570):  fellow walking over furiously nodding and staring directly at her made her assume he was addressing her.⏎⏎“Aye been shovling shite outta the**[ pens]** dis morning. What the bug
- *other* (1538):  prime target. This one brute of a kid decided he didn't like me and thought it'd be fun to knock me around a**[ bit]**. It only took two incidents

## L31.985

**Amateur web-fiction register; fires on half of human Reddit tokens** (style, high confidence)

Fires on 47-51% of human Reddit story tokens, 15% of human book tokens and 0% of Gemma's prose, with other LLMs at 1-3%. Top examples are plain, slightly awkward amateur sentences, and it promotes 'Because' and runs of exclamation marks.

Fires on (% of tokens): wp/human 47.5, wp/gemma 0.0, wp/claude 0.8, wp/glm 3.1, books/human 15.3, books/gemma 0.0, books/haiku 0.8, books/gpt 1.1, books/glm 1.2, wp/gemma_plain 0.0, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 3.7, wp/human_raw 51.2.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -4.09/-3.74 (-47.5 pts); books_gemma_vs_human -2.05/-1.69 (-15.2 pts); wp_llm_vs_human -3.94/-3.59 (-45.6 pts); books_llm_vs_human -2.0/-1.62 (-14.2 pts); raw_gemma_vs_human -4.05/-4.09 (-47.5 pts).

Promotes: ` BECAUSE` ` बिकॉज` `!!!!!!!` `!..` `!!!!!!` `Because` `!!.` ` Thereafter` `!!` `!!!!!`  
Suppresses: ` ศ` ` ра` `Bl` ` l` ` bl` ` li`

- *human* (1115):  with radiation, we could not keep ourselves or the plants alive for more than a month. We realised that the ozone is the real protector of**[ life]**. Thus, mars project was
- *human* (1067):  consisted of his'real body' remained inside an amulet. The spell wasn't reversible by the castor as the amulet couldn't be**[ harmed]** by his hands, yet that
- *human* (1035):  the current population plus two generations. By this time of course the world had created a clock that kept track of the amount of time they were**[ given]** somewhere in the quintillions.
- *other LLM* (751):  and forever.⏎⏎So the Founder made two decisions that explained everything after. The pearl would be hidden, in time beneath Mount Paektu**[ itself]**, under the sacred mountain,
- *other LLM* (739):  suggested it, originally, so the real Biscuit would stop scratching at the kitchen door during Monday readings — but the boy kept him on out of**[ loyalty]** long after the trick was needed
- *other LLM* (731):  then the next night you do it again."⏎⏎The jogger went by us just then and hung in the air, one foot never coming**[ down]**, a leaf standing still beside

## L32.3885

**Clause-final word in human prose; promotes ASCII double-hyphen dashes** (style, medium confidence)

Fires on the word that closes a clause or idiom (ahead of time, denying the truth) in human prose and promotes typed dashes such as -- and "--. It fires on 47% of human WritingPrompts tokens, 0% of Gemma's and 2-5% of other LLMs'.

Fires on (% of tokens): wp/human 47.1, wp/gemma 0.0, wp/claude 1.8, wp/glm 5.2, books/human 20.9, books/gemma 0.0, books/haiku 2.3, books/gpt 2.9, books/glm 2.9, wp/gemma_plain 0.0, wp/gemma_lit 0.0, wp/gemma_greedy 0.0, wp/gemma_raw 3.9, wp/human_raw 50.1.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -4.1/-3.96 (-47.1 pts); books_gemma_vs_human -2.81/-2.05 (-20.8 pts); wp_llm_vs_human -3.82/-3.66 (-43.7 pts); books_llm_vs_human -2.6/-1.89 (-18.2 pts); raw_gemma_vs_human -4.26/-4.16 (-46.2 pts); chat_vs_raw_gemma -0.93/-0.92 (-3.9 pts).

Promotes: `--“` ` "--` `“-` `、“` `"--` ` --` ` "-` `--` `"/` `\t\t\t\t\t\t`  
Suppresses: `䔧` ` мм` `照片` `ographs` `MalayMarks` ` भारतीय`

- *human* (1536): ."⏎⏎"They started worshipping her instead of me. My temple has been deserted for three years." Mom falls silent now after completing the**[ explanation]**. Her arms are folded across
- *human* (1496):  heavy. He was appalled at the lack of exercise routines for the comatose.⏎⏎Little by little did his eyes adjust to the real**[ world]**, the *bright* real
- *human* (1488):  come before you today as a citizen of this city, a friend, a scientist, a neighbor." He clearly rehearsed his speech ahead of**[ time]**. I didn't know
- *other LLM* (1176):  so item twelve makes sense. When our mother was dying, I handled everything, and "everything" included lying to my brother on our Sunday**[ calls]**. *She's stable
- *other LLM* (1160):  the room a slow look like a man choosing a table at a restaurant. Then the line. Every post got its own; he never repeated**[ himself]**. *You boys picked the
- *other LLM* (1128):  the real Biscuit would stop scratching at the kitchen door during Monday readings — but the boy kept him on out of loyalty long after the trick was**[ needed]**, into every century and climate

## L32.5959

**Sentence end after a comic or self-deprecating beat** (style, low confidence)

Fires on the period or question mark closing a punchy, humorous first-person line (drunk confessions, small indignities) and promotes U/u, possibly the start of Ugh. Human and Claude rates are similar (7%); Gemma's literary mode fires least (1.7%) and its plain mode more (5%).

Fires on (% of tokens): wp/human 7.2, wp/gemma 4.7, wp/claude 7.3, wp/glm 6.1, books/human 3.8, books/gemma 3.5, books/haiku 4.3, books/gpt 4.5, books/glm 4.0, wp/gemma_plain 5.1, wp/gemma_lit 1.7, wp/gemma_greedy 4.7, wp/gemma_raw 4.0, wp/human_raw 6.1.

Writer contrasts (paired effect size on each half, change in firing rate): lit_vs_default -1.43/-1.48 (-3.1 pts).

Promotes: ` U` `U` ` u` `u` ` У` `𝑈` ` उ` `𝑢` ` உ` `Ｕ`  
Suppresses: `Se` ` Se` `льти` ` dishonest` ` disagreeable` ` dishonesty`

- *human* (1441): God I was drunk last night. Stupid giggly drunk. Slutty drunk**[.]** Titania you suck. You
- *human* (1401): anging" in front of Megan. I'm sure she'd be thrilled that I just referred to our magical moment as "banging**[."]**⏎⏎I really can't
- *human* (1401):  a very funny joke to give me a⏎⏎copy of "How to train your Dragon" after a particularly nasty Wyvern burnt my hand black**[.]** That's it. A
- *Gemma* (1225):  Star Wars pajamas. Then, the insistent drone of the morning cartoon – *The New Adventures of Winnie the Pooh* – assaulted my ears**[.]** I groaned, a small,
- *Gemma* (1185):  up, but my limbs felt thick, unresponsive, coated in a layer of leaden resistance. A throbbing pain exploded in my lower back**[.]** I was… I was sixteen
- *Gemma* (1177):  Me? I was eighteen, obsessed with video games, and arguing about pizza toppings. I was supposed to be the embodiment of disease and decay**[?]** ⏎⏎“Don’t

## L33.212

**Human-text marker, peaking on apostrophes in contractions** (confidence, medium confidence)

Top hits are the apostrophe in I'm, that's and I'd, plus a few hyphens and colons inside tokens. It fires on 52% of human tokens (94% raw) against 1% of Gemma's and 2-5% of other LLMs'.

Fires on (% of tokens): wp/human 52.4, wp/gemma 0.9, wp/claude 3.2, wp/glm 4.9, books/human 33.7, books/gemma 0.7, books/haiku 2.0, books/gpt 2.4, books/glm 3.0, wp/gemma_plain 0.6, wp/gemma_lit 0.7, wp/gemma_greedy 1.0, wp/gemma_raw 12.4, wp/human_raw 94.4.

Writer contrasts (paired effect size on each half, change in firing rate): wp_gemma_vs_human -3.67/-3.37 (-51.5 pts); books_gemma_vs_human -1.97/-2.01 (-33.0 pts); wp_llm_vs_human -3.61/-3.13 (-48.7 pts); books_llm_vs_human -1.92/-1.93 (-31.2 pts); raw_gemma_vs_human -10.41/-7.6 (-82.0 pts); chat_vs_raw_gemma -1.47/-1.31 (-11.6 pts).

Promotes: `ꗜ` `&lt;unused338>` `𒉶` ` PLDNN` `𒅤` `ꗐ` `MalayMarks` `𒂷` `DenovoMis` `&lt;unused1716>`  
Suppresses: `&lt;unused687>` `�` `&lt;unused1166>` `&lt;unused201>` `&lt;unused1077>` `&lt;unused192>`

- *human* (10014):  the shoes were about the same mixture of "tomboyish with a few girly things" so I grabbed a few things. A blink**[ ]**182 t shirt,
- *human* (9854): rophobia and just wanted out.⏎⏎"Hold on, Explorer. Commander Ryan's having some O2 issues with his suit and I**[']**m just about to fix it
- *human* (9534):  it. S'probably Buck, the southern boy just down the hall. Why am I saying it that way, I know exactly that that**[']**s his hat, a cute
- *Gemma* (6398): There was a British-made Harrier jump jet, its wings crumpled and blackened, half-buried in the dust. A sleek, Russian An**[-]**2 biplane, its propeller
- *Gemma* (5566):  of the Charles Bridge looming above me. My hand instinctively went to my palm, feeling the cool metal of the clock. 364**[:]**03. Panic began to
- *Gemma* (4222):  New Orleans. I'd seen the printing press change the world, electricity illuminate cities, and the first tentative steps on the moon. I**[’]**d drunk wine with emperors and

## L33.2461

**Plain, simple spoken register; suppresses formal Latinate words** (style, high confidence)

Fires on everyday words inside simple, childlike or dialect speech (don't like, going to get me, Thank you for). Suppresses formal words (Subsequently, concomitant, exacerbated); plain-mode Gemma fires on 41% of tokens vs 1% in literary mode, and approved taste edits fire more than rejected drafts (0.42 vs 0.28).

Fires on (% of tokens): wp/human 14.4, wp/gemma 4.1, wp/claude 19.4, wp/glm 19.3, books/human 23.1, books/gemma 9.9, books/haiku 26.2, books/gpt 25.7, books/glm 24.6, wp/gemma_plain 40.6, wp/gemma_lit 1.2, wp/gemma_greedy 3.9, wp/gemma_raw 11.9, wp/human_raw 20.2.

Promotes: `োপাধ্যায়` ` tenéis` ` .,` ` cierra` `².` `📪` ` cuaderno` ` calent` ` puerta` ` ${{`  
Suppresses: ` Extensive` `Subsequently` ` Subsequently` ` concomitant` ` extensive` ` exacerbated`

- *Gemma* (2590): s there!” she’d shriek, pointing a sticky finger towards the darkness beneath the bed. “The monster! He’s going**[ to]** get me!”⏎⏎I didn
- *Gemma* (2398):  can leave.”⏎⏎She shook her head, her dark hair falling across her face. “No. I have to. Grandma… she needs**[ to]** remember.” ⏎⏎I gest
- *other* (2766): s pain. But it was also incredibly touching. ⏎⏎"Thank you," I said, my voice choked with emotion.⏎⏎"My**[ grandma]** always says flowers make everything bet
- *other* (2494):  out a single, perfect wildflower.⏎⏎"You're the kind one," she said, her voice barely a whisper. "Thank you**[ for]** helping my father.”⏎⏎I
- *other* (2206):  spaceship. A silver spaceship. With wings.⏎⏎“What are you drawing?” I asked.⏎⏎“A spaceship,” he said. “**[It]** goes to another world.”⏎⏎
