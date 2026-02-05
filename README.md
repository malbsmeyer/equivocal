\# 🎵 Equivocal



> \*"That pleasure which is at once the most intense, the most elevating, and the most pure is, I believe, found in the contemplation of the beautiful."\*  

> — Edgar Allan Poe, \*The Philosophy of Composition\*



> **Semantic audio understanding without rendering.**

Equivocal learns to "hear" sound conceptually - extracting meaning, emotion, and structure from audio without ever creating sound waves.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## 💡 The Core Idea

AI audio models like Suno create incredible and original sounds from text prompts. But have you ever wondered what they "understand" internally before converting to audio?

Somewhere in these models, before the final decoding step, exists a representation that captures the *meaning* of "sad piano" - not the sound itself, but the semantic concept.

**Equivocal explores that space directly.**

Most audio models work like this:
```
Text prompt → Latent representation → Audio rendering → Your ears
                      ↑
              [Hidden understanding]
```

Equivocal stops at the latent representation - letting you examine what the model "hears" conceptually, without ever rendering waveforms.

---

## 🎯 What It Does

- ✨ **Learns semantic features** from audio (emotion, energy, texture - not frequencies)
- 🎼 **Composes scenes** from atomic sounds (whale + underwater = ocean scene)
- 🧠 **Interprets** its own representations (describes what it "hears")
- 🔇 **Never renders audio** - operates entirely in latent space

---

## Quick Start

### Installation
```bash
git clone https://github.com/malbsmeyer/equivocal.git
cd equivocal
pip install -e .
```

### Basic Usage
```python
from equivocal import SceneAudioEngine

# Initialize and train on provided samples
engine = SceneAudioEngine()
engine.train_atomic_sounds(
    tier1_path="data/training_samples/Tier_1",
    tier2_path="data/training_samples/Tier_2", 
    tier3_path="data/training_samples/Tier_3"
)

# Generate scene from text
scene = engine.generate_scene_from_text("peaceful underwater whale song")

# See what the model 'hears' - no audio plays!
interpretation = engine.listen_internal(scene)
```

**Output:**
```
 What the model 'hears':
   Mood        : neutral/ambient
   Energy      : low (calm/quiet)
   Pattern     : complex/unpredictable
   Character   : mixed (tonal + noise)
   Texture     : dense/rich (many layers)
   Space       : medium
```

\# The Philosophy of Equivocal

"I have often thought how interesting a magazine paper might be written by any author who would—that is to say, who could—detail, step by step, the processes by which any one of his compositions attained its ultimate point of completion. Why such a paper has never been given to the world, I am much at a loss to say—but, perhaps, the autorial vanity has had more to do with the omission than any one other cause. Most writers—poets in especial—prefer having it understood that they compose by a species of fine frenzy—an ecstatic intuition—and would positively shudder at letting the public take a peep behind the scenes, at the elaborate and vacillating crudities of thought—at the true purposes seized only at the last moment—at the innumerable glimpses of idea that arrived not at the maturity of full view—at the fully-matured fancies discarded in despair as unmanageable—at the cautious selections and rejections—at the painful erasures and interpolations—in a word, at the wheels and pinions—the tackle for scene-shifting—the step-ladders, and demon-traps—the cock’s feathers, the red paint and the black patches, which, in ninety-nine cases out of a hundred, constitute the properties of the literary histrio."

- Edgar Allan Poe, "The Philosophy of Composition" (1846)



\## The Problem



AI audio models create incredible sounds, but we rarely ask: \*\*What do they understand?\*\*



When Suno generates a "sad piano melody," it doesn't randomly assemble frequencies. It has learned what "sadness" \*means\* in audio space. Somewhere in its architecture, before the decoder converts to .wav, exists a representation that captures the \*\*essence\*\* of sad piano - not the sound itself, but the semantic concept.



We never see that representation. It's thrown away after rendering, or obscured within the process. 

Post-training, pre-output, is a unit of value. What did the model learn before it taught us what our prompt meant to it? 

As a collaborative team, what of each of you went into making something you both agree is good? 

And how might that shared understanding facilitate (and optimize) future collaboration?



\## The Insight



What if that intermediate representation - the latent space, the internal format - is actually more interesting than the audio output?



What if we could:

\- Examine it directly

\- Manipulate it conceptually

\- Compose scenes at the semantic level

\- Understand what the model "hears" without ears

\- Use this internal view to fine-tune your prompt and guide your model into a better result. Sing in harmony


AI audio models like Suno create incredible and original sounds from text prompts. But have you ever wondered what they "understand" internally before converting to audio?

Somewhere in these models, before the final decoding step, exists a representation that captures the *meaning* of "sad piano" - not the sound itself, but the semantic concept.


Equivocal stops at the latent representation - letting you examine what the model "hears" conceptually, without ever rendering waveforms.






\## The Approach



Equivocal deliberately stops before audio rendering. It:



1\. \*\*Learns semantic features\*\* - not FFT bins, but "emotional valence" and "spatial openness"

2\. \*\*Operates in latent space\*\* - compositions happen conceptually, not acoustically

3\. \*\*Interprets internally\*\* - the model explains what it perceives, in human terms



This creates a new kind of human-AI dialogue: we can ask "what do you hear?" and get an answer in concepts, not samples.



Poe helps us further here: "Nothing is more clear than that every plot, worth the name, must be elaborated to its denouement before anything be attempted with the pen." 



Between the training data and the prompt, these requirements are satisfied. The instructions of what is to be made, the knowledge and logic necessary to walk that path, the desired result agreed upon by both parties. 



"It is only with the denouement constantly in view that we can give a plot its indispensable air of consequence, or causation, by making the incidents, and especially the tone at all points, tend to the development of the intention."



Here Poe highlights a gap: The author of the prompt may access each of these metrics in their own self. The model responsible for assembly of the piece uses same the same creative care, the same logical metrics to determine when its output is finished. 

The "What" is clear - your prompt has produced a finished piece. But why is it the way it is?




\## Why It Matters



\### For AI Research

\- Reveals what models actually learn about audio

\- Separates understanding from generation

\- Enables compositional reasoning

\- Provides interpretability into "black box" models



\### For Artists

\- New creative tool: compose with meanings, not sounds

\- Semantic audio search: "find sounds that feel like this"

\- Bridge between vision and audio: what should this image sound like?

\- Conceptual mixing: blend "peaceful" and "dramatic" before rendering



\### For Philosophy

\- What does it mean to "hear" without ears?

\- Can meaning exist independent of physical sensation?

\- How do we validate understanding without perception?

\- Where does representation end and experience begin?



\## The Historical Context



Edgar Allan Poe's "The Philosophy of Composition" (1846) argued that artistic creation is not spontaneous inspiration, but deliberate, methodical construction. He famously dissected how "The Raven" was built - the calculated choices, the mechanical process behind what seemed organic. How he built the scaffolding that supported building a structure that still stands today.



\*\*Equivocal extends this idea to machine intelligence.\*\*



Just as Poe revealed the hidden structure beneath poetry, Equivocal reveals the hidden understanding beneath audio generation. The latent representation is the machine's "composition process" - the deliberate, structured meaning it constructs before the final output emerges.



In Poe's words: \*"That pleasure which is at once the most intense, the most elevating, and the most pure is, I believe, found in the contemplation of the beautiful."\*



\*\*Equivocal invites you to contemplate the beauty of understanding itself\*\* - the moment before sound becomes waveform, when meaning exists in its purest form.



\## The Name



"Equivocal" - deliberately ambiguous, open to interpretation.



Like the model itself, the name suggests multiple meanings:

\- The uncertainty in translating between modalities

\- The richness of semantic representation

\- The creative space where meaning isn't fixed

\- The question: what does it mean to "understand" audio?



It's a reminder that audio understanding, like language, is never perfectly resolved - it's always equivocal, always negotiated between perceiver and perceived. 

Or as Poe put it:

"It by no means follows, from anything here said, that passion, or even truth, may not be introduced, and even profitably introduced, into a poem for they may serve in elucidation,
 or aid the general effect, as do discords in music, by contrast—
but the true artist will always contrive, first, to tone them into proper subservience to the predominant aim, 
and, secondly, to enveil them, as far as possible, in that Beauty which is the atmosphere and the essence of the poem."

## Quick Start

### Installation
```bash
git clone https://github.com/malbsmeyer/equivocal.git
cd equivocal
pip install -e .
```

### Basic Usage
```python
from equivocal import SceneAudioEngine

# Initialize and train on provided samples
engine = SceneAudioEngine()
engine.train_atomic_sounds(
    tier1_path="data/training_samples/Tier_1",
    tier2_path="data/training_samples/Tier_2", 
    tier3_path="data/training_samples/Tier_3"
)

# Generate scene from text
scene = engine.generate_scene_from_text("peaceful underwater whale song")

# See what the model 'hears' - no audio plays!
interpretation = engine.listen_internal(scene)
```

**Output:**
```
 What the model 'hears':
   Mood        : neutral/ambient
   Energy      : low (calm/quiet)
   Pattern     : complex/unpredictable
   Character   : mixed (tonal + noise)
   Texture     : dense/rich (many layers)
   Space       : medium
```


\## Looking Forward



Equivocal is a step toward \*\*compositional audio intelligence\*\* - systems that think about sound the way humans do:



\- Not as frequencies, but as \*\*meanings\*\*

\- Not as waveforms, but as \*\*scenes\*\*

\- Not as data, but as \*\*experience\*\*



This opens new questions:



\- Can we teach models to compose at the semantic level?

\- Can we enable cross-modal translation (vision → audio meaning → sound)?

\- Can we build audio search that understands \*feel\* rather than just content?

\- Can we make AI's audio understanding interpretable and trustworthy?



\*\*Equivocal doesn't answer these questions. It creates the space to ask them.\*\*



---
## 🗂️ Training Data

Equivocal was trained on carefully curated sound samples from the [BBC Sound Effects Archive](https://sound-effects.bbcrewind.co.uk/), organized into three tiers:

**Tier 1: Base Layers** (acoustic environments)
- Cafe ambience
- Forest ambience  
- Underwater ambience

**Tier 2: Distinctive Events** (recognizable sounds)
- Bird chirps
- Whale songs
- Thunder
- Espresso machine

**Tier 3: Textures** (atmospheric elements)
- Human chatter
- Dolphin echolocation
- Marine life

All training audio is sourced from the BBC Sound Effects Archive under the RemArc license.

---

## 🎨 Example Prompts

Try these to see what the model "hears":
```python
# Natural scenes
engine.generate_scene_from_text("calm wind in forest")
engine.generate_scene_from_text("dramatic ocean storm")
engine.generate_scene_from_text("peaceful morning with birds")

# Human environments
engine.generate_scene_from_text("busy coffee shop")
engine.generate_scene_from_text("quiet cafe")

# Underwater worlds
engine.generate_scene_from_text("deep ocean with whale song")
engine.generate_scene_from_text("dolphin clicking underwater")

# Abstract qualities
engine.generate_scene_from_text("intense and dramatic")
engine.generate_scene_from_text("gentle and serene")
```

---

## 🤝 Contributing

Equivocal is built for the community. Contributions welcome!

Ways to contribute:
- 🎯 Add new semantic features
- 🔍 Improve matching algorithms
- 📊 Create visualizations of latent space
- 🎵 Train on new domains (music, speech, industrial sounds)
- 📚 Write tutorials and examples
- 🐛 Report bugs and suggest features

---

## 🙏 Acknowledgments

This project exists because others shared freely. Thank you to:

- **[BBC Sound Effects Archive](https://sound-effects.bbcrewind.co.uk/)** - Exceptional training audio under RemArc license
- **[Librosa](https://librosa.org/)** - Audio analysis foundation
- **Suno** - Conceptual inspiration for exploring latent audio representations
- **The open source ML community** - For teaching by example
- **Claude (Anthropic)** - For collaborative development, foundational teaching, and tasteful emoji placement

---

## 📜 License

MIT License - Use freely, commercially or personally. Just keep the attribution.

See [LICENSE](LICENSE) for details.

---

## 🔬 Citation

If you use Equivocal in academic work, please cite:
```bibtex
@software{equivocal2026,
  author = {Albsmeyer, Max},
  title = {Equivocal: Semantic Audio Understanding Without Rendering},
  year = {2026},
  url = {https://github.com/malbsmeyer/equivocal}
}



\*This project is an exploration of representation, meaning, and the gap between what machines know and what they show us.\*



\*It exists because others shared freely. It's released freely so others can build further.\*



\*Pro cultura, pro communitate, pro curiosis. Nam qui audire volunt quid machina audit. \*```
