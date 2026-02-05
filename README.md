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

## 🚀 Quick Start

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
🧠 What the model 'hears':
   Mood        : neutral/ambient
   Energy      : low (calm/quiet)
   Pattern     : complex/unpredictable
   Character   : mixed (tonal + noise)
   Texture     : dense/rich (many layers)
   Space       : medium
```

---

## 🎓 Why This Matters

### For AI Research
- Reveals what models learn about audio semantics
- Separates understanding from generation
- Enables compositional reasoning about sound

### For Artists & Producers
- Semantic audio search: "find sounds that *feel* like this"
- Compose with meanings, not just waveforms
- Bridge modalities: what should this image sound like?

### For Philosophy
- What does it mean to "hear" without ears?
- Can meaning exist independent of physical sensation?
- How do we validate understanding without perception?

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
- **Claude (Anthropic)** - For collaborative development and foundational teaching

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
```

---

*"The song that plays in the mind of the machine, before it learns to sing."*