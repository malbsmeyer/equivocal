\# Training Data Sources



All training audio for Equivocal comes from the \*\*BBC Sound Effects Archive\*\*, used under the RemArc license.



\## BBC Sound Effects Archive



\- \*\*URL:\*\* https://sound-effects.bbcrewind.co.uk/

\- \*\*License:\*\* RemArc License (free for personal, educational, research, and commercial use with attribution)

\- \*\*Collection Size:\*\* 33,000+ high-quality sound effects

\- \*\*Format:\*\* WAV files, various sample rates



\### License Terms



The BBC Sound Effects are made available under the RemArc License:



\- ✅ Free to use for personal projects

\- ✅ Free to use for educational purposes

\- ✅ Free to use for research

\- ✅ Free to use commercially

\- ✅ Attribution required



\*\*Attribution:\*\* "Sound effects courtesy of the BBC"



Full license: https://sound-effects.bbcrewind.co.uk/licensing



---



\## Equivocal Training Set



The default Equivocal model was trained on carefully curated samples:



\### Tier 1: Base Layers (Acoustic Environments)



| Category | File | Description |

|----------|------|-------------|

| `cafe\_ambience` | Morocco Rabat cafe atmosphere | Interior cafe with traffic, TV, espresso machine |

| `forest\_ambience` | Wind blowing in Banyan tree | Natural wind through leaves |

| `underwater\_ambience` | Rockpool atmosphere | Underwater hydrophone recording |



\### Tier 2: Distinctive Events



| Category | File | Description |

|----------|------|-------------|

| `bird\_chirp` | Puerto Rican Tody warble | Medium close-up bird calls |

| `whale\_song` | Northern Right Whale calls | Underwater whale vocalizations (stereo) |

| `espresso\_machine` | Espresso coffee machine | Person preparing coffee, steam sounds |

| `thunder` | Single crack of thunder | Dramatic thunder rumble |



\### Tier 3: Textures



| Category | File | Description |

|----------|------|-------------|

| `cafe\_chatter` | Tangier tourist cafe | General atmosphere with Arabic conversation |

| `dolphin\_clicks` | Bottle-nosed Dolphin echolocation | Underwater hydrophone recording |

| `sealion\_shrimp` | Galapagos Sealion with snapping shrimp | Marine life composite |



For ease of use during training, the audio filenames were updated to match the descriptions of the sound file, as provided by the publisher.

---



\## Using Your Own Training Data



Equivocal can be trained on any audio sources. To use custom data:



\### Organize Your Files

```

my\_training\_data/

&nbsp; Tier\_1/           # Base environments

&nbsp;   kitchen/

&nbsp;     sample1.wav

&nbsp;     sample2.wav

&nbsp;   garden/

&nbsp;     sample1.wav

&nbsp; Tier\_2/           # Distinctive events  

&nbsp;   dog\_bark/

&nbsp;     sample1.wav

&nbsp; Tier\_3/           # Textures

&nbsp;   wind\_chimes/

&nbsp;     sample1.wav

```



\### Recommendations



\- \*\*Duration:\*\* 3-15 seconds per sample

\- \*\*Format:\*\* WAV (lossless) preferred

\- \*\*Quality:\*\* Clean recordings without artifacts

\- \*\*Labeling:\*\* Use descriptive folder names (they become sound categories)



\### Free Audio Sources



\- \*\*Freesound.org\*\* - Creative Commons audio library

\- \*\*BBC Sound Effects\*\* - As described above  

\- \*\*YouTube Audio Library\*\* - Google's free collection

\- \*\*Internet Archive\*\* - Public domain recordings



Always check and respect licenses when using others' work. Poe is watching.



---



\## Attribution



Equivocal's default training data:



\*\*"Sound effects courtesy of the BBC Sound Effects Archive"\*\*



If you train on different data, please attribute accordingly in your project.



---



\## Questions?



If you have questions about licensing or training data, please open an issue on GitHub.

