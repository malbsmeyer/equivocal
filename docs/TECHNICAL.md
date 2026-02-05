\# Technical Documentation



\## Architecture Overview



Equivocal consists of three main components:



1\. \*\*Feature Extraction\*\* - Converting audio to semantic representations

2\. \*\*Scene Composition\*\* - Blending atomic sounds into complex scenes

3\. \*\*Internal Interpretation\*\* - Translating latent space to human understanding



---



\## 1. Feature Extraction



\### The Semantic Feature Space



Instead of traditional acoustic features (MFCCs, spectrograms), Equivocal extracts \*\*semantic features\*\* that capture meaning:



| Feature | Range | Meaning |

|---------|-------|---------|

| `emotional\_valence` | \[-1, 1] | Positive vs negative feeling |

| `energy\_level` | \[0, 1] | Calm vs intense |

| `temporal\_complexity` | \[0, 1] | Predictable vs chaotic rhythm |

| `harmonic\_richness` | \[0, 1] | Tonal vs noisy |

| `spectral\_trajectory` | \[-1, 1] | Darkening vs brightening |

| `textural\_density` | \[0, 1] | Sparse vs layered |

| `spatial\_openness` | \[0, 1] | Enclosed vs open |

| `timbre\_vector` | ℝ¹³ | Characteristic sound quality (MFCCs) |

| `pitch\_profile` | {mean, range, variance} | Melodic characteristics |

| `onset\_pattern` | {mean\_ioi, variance, count} | Event timing structure |



\### Implementation

```python

def \_extract\_semantic\_features(self, audio, sr):

&nbsp;   """

&nbsp;   Extract semantic features from audio waveform.

&nbsp;   

&nbsp;   Args:

&nbsp;       audio: numpy array of audio samples

&nbsp;       sr: sample rate (Hz)

&nbsp;   

&nbsp;   Returns:

&nbsp;       Dictionary of semantic features

&nbsp;   """

&nbsp;   features = {}

&nbsp;   

&nbsp;   # Emotional valence: Major vs minor harmony

&nbsp;   chroma = librosa.feature.chroma\_cqt(y=audio, sr=sr)

&nbsp;   major\_energy = chroma\[4].mean()  # Major third

&nbsp;   minor\_energy = chroma\[3].mean()  # Minor third

&nbsp;   features\['emotional\_valence'] = np.tanh(major\_energy - minor\_energy)

&nbsp;   

&nbsp;   # Energy level: RMS amplitude

&nbsp;   rms = librosa.feature.rms(y=audio)

&nbsp;   features\['energy\_level'] = float(np.mean(rms))

&nbsp;   

&nbsp;   # Temporal complexity: Entropy of onset distribution

&nbsp;   onset\_env = librosa.onset.onset\_strength(y=audio, sr=sr)

&nbsp;   onset\_prob = onset\_env / (np.sum(onset\_env) + 1e-10)

&nbsp;   entropy = -np.sum(onset\_prob \* np.log(onset\_prob + 1e-10))

&nbsp;   features\['temporal\_complexity'] = float(entropy / np.log(len(onset\_env)))

&nbsp;   

&nbsp;   # ... (additional features)

&nbsp;   

&nbsp;   return features

```



\### Why These Features?



\*\*Traditional approach:\*\*

\- Extract acoustic features (spectrum, MFCCs, etc.)

\- Train classifier on labeled data

\- Predict categories



\*\*Equivocal's approach:\*\*

\- Extract semantic features directly

\- Learn prototypes through averaging

\- Compose through blending



This allows \*\*compositional understanding\*\* - scenes can be built from primitives without requiring labeled examples of every combination.



---



\## 2. Scene Composition



\### Atomic Sound Prototypes



Each sound category is represented by an \*\*averaged prototype\*\*:

```python

\# Train on multiple samples

samples = \[

&nbsp;   extract\_features(whale\_call\_1.wav),

&nbsp;   extract\_features(whale\_call\_2.wav)

]



\# Create prototype by averaging

whale\_prototype = average\_features(samples)

```



This prototype captures the \*\*essence\*\* of "whale-ness" across multiple instances.



\### Semantic Blending



Scenes are composed by weighted averaging in feature space:

```python

def \_blend\_sounds(self, sound\_names, weights=None):

&nbsp;   """

&nbsp;   Blend multiple sound prototypes into unified scene.

&nbsp;   

&nbsp;   Example:

&nbsp;       blend(\['underwater\_ambience', 'whale\_song'], \[0.6, 0.4])

&nbsp;       → 60% underwater ambience + 40% whale characteristics

&nbsp;   """

&nbsp;   if weights is None:

&nbsp;       weights = \[1.0 / len(sound\_names)] \* len(sound\_names)

&nbsp;   

&nbsp;   latents = \[self.atomic\_sounds\[name] for name in sound\_names]

&nbsp;   

&nbsp;   blended = {}

&nbsp;   for key in all\_feature\_keys:

&nbsp;       values = \[lat\[key] for lat in latents if key in lat]

&nbsp;       weights\_for\_key = \[w for lat, w in zip(latents, weights) if key in lat]

&nbsp;       

&nbsp;       blended\[key] = np.average(values, weights=weights\_for\_key)

&nbsp;   

&nbsp;   return blended

```



\### Why Averaging Works



In semantic space, averaging creates \*\*meaningful interpolations\*\*:



\- `forest\_ambience` + `bird\_chirp` = forest with birds

\- `cafe\_ambience` + `espresso\_machine` = coffee shop atmosphere

\- `underwater\_ambience` + `whale\_song` = ocean with marine life



This is \*\*compositional semantics\*\* - meaning emerges from combination.



---



\## 3. Internal Interpretation



\### Latent Space → Human Language



The model translates its internal representation to qualitative descriptions:

```python

def listen\_internal(self, scene\_representation):

&nbsp;   """

&nbsp;   Interpret latent representation in human terms.

&nbsp;   

&nbsp;   Thresholds are calibrated based on training data distribution:

&nbsp;   - energy > 0.15 → "high"

&nbsp;   - 0.05 < energy < 0.15 → "medium"  

&nbsp;   - energy < 0.05 → "low"

&nbsp;   """

&nbsp;   latent = scene\_representation\['latent']

&nbsp;   

&nbsp;   interpretation = {}

&nbsp;   

&nbsp;   # Map continuous values to discrete categories

&nbsp;   energy = latent.get('energy\_level', 0)

&nbsp;   if energy > 0.15:

&nbsp;       interpretation\['energy'] = 'high (active/intense)'

&nbsp;   elif energy > 0.05:

&nbsp;       interpretation\['energy'] = 'medium (moderate)'

&nbsp;   else:

&nbsp;       interpretation\['energy'] = 'low (calm/quiet)'

&nbsp;   

&nbsp;   # ... (additional interpretations)

&nbsp;   

&nbsp;   return interpretation

```



\### Calibration



Thresholds were determined empirically:

\- Training on BBC Sound Effects samples

\- Observing feature value distributions

\- Setting boundaries that separate perceptually distinct categories



\*\*Future work:\*\* Could be learned from human ratings.



---



\## Technical Specifications



\### Dependencies



\- \*\*librosa\*\* (0.10.0+): Audio analysis, feature extraction

\- \*\*numpy\*\* (1.20.0+): Numerical operations

\- \*\*soundfile\*\* (0.12.0+): Audio file I/O

\- \*\*scikit-learn\*\* (1.0.0+): Used by librosa for some operations



\### Performance



\*\*Training:\*\*

\- 10 audio files (5-10 sec each): ~30 seconds on CPU

\- Scales linearly with number of files

\- Feature extraction is the bottleneck



\*\*Inference:\*\*

\- Scene generation: <100ms (dictionary lookup + averaging)

\- Real-time capable for interactive use



\### Memory Requirements



\- Model size: ~50KB (JSON format, 10 sound categories)

\- Runtime memory: <100MB (depends on audio file sizes during training)

\- Scales with number of sound categories and audio duration



---



\## File Formats



\### Training Audio

\- \*\*Supported:\*\* .wav, .mp3, .flac, .ogg, .m4a

\- \*\*Recommended:\*\* .wav (lossless)

\- \*\*Sample rate:\*\* Any (resampled to 22050 Hz)

\- \*\*Channels:\*\* Mono or stereo (converted to mono)

\- \*\*Duration:\*\* 3-15 seconds per sample



\### Model Storage

\- \*\*Format:\*\* JSON

\- \*\*Contents:\*\* 

&nbsp; - Atomic sound prototypes (feature dictionaries)

&nbsp; - Metadata (version, sample rate, etc.)

\- \*\*Size:\*\* ~5KB per sound category



---



\## Extending Equivocal



\### Adding New Semantic Features



1\. \*\*Define feature in `\_extract\_semantic\_features()`:\*\*

```python

def \_compute\_my\_feature(self, audio, sr):

&nbsp;   """

&nbsp;   Compute my custom semantic feature.

&nbsp;   

&nbsp;   Should return a scalar or numpy array.

&nbsp;   """

&nbsp;   # Your implementation here

&nbsp;   return feature\_value



\# Add to feature extraction:

features\['my\_feature'] = self.\_compute\_my\_feature(audio, sr)

```



2\. \*\*Add interpretation in `listen\_internal()`:\*\*

```python

my\_value = latent.get('my\_feature', 0)

if my\_value > threshold:

&nbsp;   interpretation\['my\_aspect'] = 'description'

```



\### Training on New Domains



To train on different types of sounds:



1\. \*\*Organize by semantic category:\*\*

```

my\_sounds/

&nbsp; Tier\_1/

&nbsp;   rain/

&nbsp;   traffic/

&nbsp; Tier\_2/

&nbsp;   dog\_bark/

&nbsp;   car\_horn/

&nbsp; Tier\_3/

&nbsp;   wind/

&nbsp;   voices/

```



2\. \*\*Update semantic mapping in `generate\_scene\_from\_text()`:\*\*

```python

semantic\_map = {

&nbsp;   'rain': \['rain'],

&nbsp;   'wet': \['rain'],

&nbsp;   'traffic': \['traffic'],

&nbsp;   'car': \['car\_horn', 'traffic'],

&nbsp;   # ...

}

```



3\. \*\*Train:\*\*

```python

engine.train\_atomic\_sounds(

&nbsp;   tier1\_path="my\_sounds/Tier\_1",

&nbsp;   tier2\_path="my\_sounds/Tier\_2",

&nbsp;   tier3\_path="my\_sounds/Tier\_3"

)

```



---



\## Limitations \& Future Work



\### Current Limitations



1\. \*\*No temporal modeling\*\* - Features are averaged over entire clip

2\. \*\*Fixed vocabulary\*\* - Semantic mapping is hand-coded

3\. \*\*No hierarchy\*\* - All sounds treated equally (no "sub-sounds")

4\. \*\*Linear blending\*\* - Simple averaging, no learned composition rules



\### Potential Improvements



1\. \*\*Temporal modeling:\*\*

&nbsp;  - Extract features in sliding windows

&nbsp;  - Model how scenes evolve over time

&nbsp;  - Enable generation of dynamic soundscapes



2\. \*\*Learned semantics:\*\*

&nbsp;  - Train word embeddings from text descriptions

&nbsp;  - Learn semantic mappings from data

&nbsp;  - Support free-form language input



3\. \*\*Hierarchical composition:\*\*

&nbsp;  - Model relationships (e.g., "bird is part of forest")

&nbsp;  - Enable nested scenes ("cafe inside building on street")

&nbsp;  - Support varying levels of detail



4\. \*\*Neural blending:\*\*

&nbsp;  - Learn composition rules from examples

&nbsp;  - Non-linear interactions between sounds

&nbsp;  - Context-dependent blending



5\. \*\*Cross-modal grounding:\*\*

&nbsp;  - Image → sound prediction

&nbsp;  - Video → soundscape generation

&nbsp;  - Multi-modal semantic space



---



\## Research Context



Equivocal draws on:



\- \*\*Audio feature extraction\*\* (MFCCs, chromagrams, onset detection)

\- \*\*Semantic audio analysis\*\* (emotion recognition, scene classification)

\- \*\*Compositional semantics\*\* (meaning as combination of primitives)

\- \*\*Interpretable ML\*\* (making model decisions understandable)



Related work:

\- Audio tagging and classification (AudioSet, ESC-50)

\- Sound event detection (DCASE challenges)

\- Cross-modal learning (audio-visual correspondence)

\- Generative audio models (WaveNet, Jukebox, MusicLM, Suno)



\*\*Equivocal's contribution:\*\* Focuses on \*\*understanding\*\* rather than generation, making the semantic layer explicit and interpretable.



---



\## Citation



If you use Equivocal in research, please cite:

```bibtex

@software{equivocal2026,

&nbsp; author = {Albsmeyer, Max},

&nbsp; title = {Equivocal: Semantic Audio Understanding Without Rendering},

&nbsp; year = {2026},

&nbsp; url = {https://github.com/maxalbsmeyer/equivocal},

&nbsp; note = {Open source project for compositional audio semantics}

}

```

