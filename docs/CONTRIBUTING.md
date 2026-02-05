\# Contributing to Equivocal



Thank you for your interest in contributing! Equivocal is built for the community, and all contributions are welcome.



\## Ways to Contribute



\### 🐛 Report Bugs

Found a bug? \[Open an issue](https://github.com/maxalbsmeyer/equivocal/issues) with:

\- Description of the problem

\- Steps to reproduce

\- Expected vs actual behavior

\- Your environment (OS, Python version)



\### 💡 Suggest Features

Have an idea? \[Open an issue](https://github.com/maxalbsmeyer/equivocal/issues) with:

\- Description of the feature

\- Why it would be useful

\- Potential implementation approach (optional)



\### 📚 Improve Documentation

\- Fix typos or unclear explanations

\- Add examples and tutorials

\- Improve code comments

\- Create visualizations



\### 🎵 Contribute Training Data

\- Share curated sound collections

\- Document interesting use cases

\- Create example datasets for specific domains



\### 💻 Submit Code

See below for development guidelines.



---



\## Development Setup



\### 1. Fork and Clone

```bash

git fork https://github.com/malbsmeyer/equivocal.git

git clone https://github.com/YOUR\_USERNAME/equivocal.git

cd equivocal

```



\### 2. Install Development Dependencies

```bash

pip install -e ".\[dev]"

```



This installs:

\- Equivocal in editable mode

\- Testing tools (pytest)

\- Jupyter for notebooks

\- Matplotlib for visualization



\### 3. Create a Branch

```bash

git checkout -b feature/my-new-feature

\# or

git checkout -b fix/issue-123

```



---



\## Code Guidelines



\### Style



\- Follow \[PEP 8](https://pep8.org/) style guide

\- Use meaningful variable names

\- Add docstrings to all functions

\- Keep functions focused and small



\### Example

```python

def extract\_emotional\_valence(audio, sample\_rate):

&nbsp;   """

&nbsp;   Compute emotional valence from chromagram.

&nbsp;   

&nbsp;   Args:

&nbsp;       audio (np.ndarray): Audio waveform

&nbsp;       sample\_rate (int): Sample rate in Hz

&nbsp;   

&nbsp;   Returns:

&nbsp;       float: Valence in range \[-1, 1]

&nbsp;           -1 = negative (minor key)

&nbsp;           +1 = positive (major key)

&nbsp;   """

&nbsp;   chroma = librosa.feature.chroma\_cqt(y=audio, sr=sample\_rate)

&nbsp;   major\_energy = chroma\[4].mean()

&nbsp;   minor\_energy = chroma\[3].mean()

&nbsp;   return np.tanh(major\_energy - minor\_energy)

```



\### Testing



Add tests for new features:

```python

\# tests/test\_features.py

def test\_emotional\_valence():

&nbsp;   """Test that valence is in expected range"""

&nbsp;   # Generate test audio (e.g., sine wave)

&nbsp;   audio = generate\_test\_audio()

&nbsp;   

&nbsp;   valence = extract\_emotional\_valence(audio, 22050)

&nbsp;   

&nbsp;   assert -1 <= valence <= 1, "Valence must be in \[-1, 1]"

```



Run tests:

```bash

pytest tests/

```



---



\## Adding New Features



\### New Semantic Feature



1\. \*\*Add extraction method\*\* in `equivocal/engine.py`:

```python

def \_compute\_my\_feature(self, audio, sr):

&nbsp;   """

&nbsp;   Compute my new semantic feature.

&nbsp;   

&nbsp;   Describe what it measures and why it's useful.

&nbsp;   """

&nbsp;   # Implementation

&nbsp;   return feature\_value

```



2\. \*\*Add to feature extraction\*\*:

```python

def \_extract\_semantic\_features(self, audio, sr):

&nbsp;   # ... existing features ...

&nbsp;   features\['my\_feature'] = self.\_compute\_my\_feature(audio, sr)

&nbsp;   return features

```



3\. \*\*Add interpretation\*\*:

```python

def listen\_internal(self, scene\_representation):

&nbsp;   # ... existing interpretations ...

&nbsp;   

&nbsp;   my\_value = latent.get('my\_feature', 0)

&nbsp;   if my\_value > 0.5:

&nbsp;       interpretation\['my\_aspect'] = 'high'

&nbsp;   else:

&nbsp;       interpretation\['my\_aspect'] = 'low'

```



4\. \*\*Document\*\* in `docs/TECHNICAL.md`



5\. \*\*Add test\*\* in `tests/test\_features.py`



\### New Sound Domain



To add support for a new domain (e.g., industrial sounds, speech):



1\. \*\*Curate training data\*\* organized by category



2\. \*\*Update semantic mapping\*\* in `generate\_scene\_from\_text()`:

```python

semantic\_map = {

&nbsp;   # ... existing mappings ...

&nbsp;   'factory': \['machine\_hum', 'metal\_clang'],

&nbsp;   'speech': \['male\_voice', 'female\_voice'],

}

```



3\. \*\*Add example prompts\*\* to documentation



4\. \*\*Share your trained model\*\* (optional)



---



\## Pull Request Process



\### 1. Make Your Changes



\- Write clear, focused commits

\- Add tests for new features

\- Update documentation



\### 2. Test Locally

```bash

\# Run tests

pytest tests/



\# Test example scripts

python examples/interactive\_demo.py

python examples/gui\_demo.py



\# Check that basic usage works

python -c "from equivocal import SceneAudioEngine; print('OK')"

```



\### 3. Submit PR

```bash

git push origin feature/my-new-feature

```



Then open a pull request on GitHub with:

\- \*\*Clear title\*\* describing the change

\- \*\*Description\*\* of what you changed and why

\- \*\*Testing\*\* you performed

\- \*\*Breaking changes\*\* (if any)



\### 4. Code Review



\- Maintainers will review your code

\- Address feedback by pushing new commits

\- Once approved, your PR will be merged!



---



\## Areas We Need Help



\### High Priority



\- \[ ] Visualization of latent space (t-SNE, UMAP plots)

\- \[ ] More semantic features (brightness, roughness, etc.)

\- \[ ] Batch processing for large datasets

\- \[ ] Performance optimization for training

\- \[ ] Cross-modal examples (image → sound prediction)



\### Medium Priority



\- \[ ] Jupyter notebook tutorials

\- \[ ] Video documentation and walkthroughs

\- \[ ] Alternative GUI frameworks (web-based)

\- \[ ] Integration examples (DAWs, game engines)

\- \[ ] Pre-trained models for common domains



\### Nice to Have



\- \[ ] Audio playback in GUI (render for comparison)

\- \[ ] Real-time processing mode

\- \[ ] Plugin architecture for custom features

\- \[ ] Synthetic data generation for testing

\- \[ ] Benchmarking suite



---



\## Community Guidelines



\### Be Respectful



\- Treat everyone with kindness and respect

\- Assume good intentions

\- Welcome newcomers

\- Provide constructive feedback



\### Be Open



\- Share your ideas and experiments

\- Ask questions when stuck

\- Learn from others' contributions

\- Celebrate community successes



\### Be Collaborative



\- Help review pull requests

\- Answer questions in issues

\- Share your trained models

\- Document your learnings



---



\## Questions?



\- \*\*Technical questions:\*\* Open a \[GitHub issue](https://github.com/malbsmeyer/equivocal/issues)

\- \*\*General discussion:\*\* \[GitHub Discussions](https://github.com/malbsmeyer/equivocal/discussions) (if enabled)

\- \*\*Security issues:\*\* Email maxalbsmeyer@\[domain] (replace with actual contact)



---



\## License



By contributing, you agree that your contributions will be licensed under the MIT License.



---



\*\*Thank you for contributing to Equivocal!\*\* 🎵



Together we're building tools to understand how machines hear the world.

