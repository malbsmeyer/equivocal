import numpy as np
import librosa
from pathlib import Path
import json

class SceneAudioEngine:
    """
    Learns compositional scene understanding from atomic sounds.
    Operates entirely in latent/semantic space.
    """
    
    def __init__(self, sample_rate=22050):
        self.sr = sample_rate
        
        # Three levels of memory
        self.atomic_sounds = {}      # Individual sound concepts
        self.soundscapes = {}         # Composed scenes
        self.semantic_vocabulary = {}  # High-level descriptors
        
        print("="*70)
        print("EQUIVOCAL - Scene Audio Engine")
        print("Semantic audio understanding without rendering")
        print("="*70)
    
    def train_atomic_sounds(self, tier1_path="Tier_1", tier2_path="Tier_2", tier3_path="Tier_3"):
        """
        Level 1: Learn individual sound primitives
        """
        print("\n" + "="*70)
        print("LEVEL 1: LEARNING ATOMIC SOUNDS")
        print("="*70)
        
        all_tiers = [
            (tier1_path, "base layers"),
            (tier2_path, "distinctive events"),
            (tier3_path, "texture")
        ]
        
        total_learned = 0
        
        for tier_path, tier_name in all_tiers:
            print(f"\nProcessing {tier_name} ({tier_path})...")
            
            tier_dir = Path(tier_path)
            if not tier_dir.exists():
                print(f"  ⚠️  Directory not found: {tier_path}")
                continue
            
            # Each subdirectory is a sound category
            for category_dir in tier_dir.iterdir():
                if not category_dir.is_dir():
                    continue
                
                category_name = category_dir.name
                print(f"\n  Learning: {category_name}")
                
                samples = []
                for audio_file in category_dir.glob('*.wav'):
                    print(f"    • {audio_file.name}")
                    
                    try:
                        audio, sr = librosa.load(audio_file, sr=self.sr, mono=True)
                        features = self._extract_semantic_features(audio, sr)
                        samples.append(features)
                    except Exception as e:
                        print(f"      ⚠️  Error loading: {e}")
                        continue
                
                if samples:
                    # Average samples to get prototype
                    self.atomic_sounds[category_name] = self._average_features(samples)
                    print(f"    ✓ Learned from {len(samples)} sample(s)")
                    total_learned += 1
        
        print(f"\n{'='*70}")
        print(f"✅ LEVEL 1 COMPLETE: Learned {total_learned} atomic sounds")
        print(f"{'='*70}")
        
        return self.atomic_sounds
    
    def _extract_semantic_features(self, audio, sr):
        """
        Extract the MEANING of audio, not just acoustic properties.
        This creates the latent representation.
        """
        
        features = {}
        
        # === EMOTIONAL/PERCEPTUAL DIMENSIONS ===
        
        # 1. Emotional valence (positive/negative feeling)
        features['emotional_valence'] = self._compute_valence(audio, sr)
        
        # 2. Energy level (calm vs intense)
        features['energy_level'] = self._compute_energy(audio)
        
        # 3. Temporal complexity (predictable vs chaotic)
        features['temporal_complexity'] = self._compute_rhythm_complexity(audio, sr)
        
        # 4. Harmonic content (tonal vs noisy)
        features['harmonic_richness'] = self._compute_harmonic_content(audio, sr)
        
        # 5. Spectral trajectory (brightening vs darkening)
        features['spectral_trajectory'] = self._compute_spectral_motion(audio, sr)
        
        # 6. Textural density (sparse vs layered)
        features['textural_density'] = self._compute_texture(audio, sr)
        
        # === TIMBRAL QUALITIES ===
        
        # 7. Timbre signature (what makes it recognizable)
        features['timbre_vector'] = self._compute_timbre(audio, sr)
        
        # === STRUCTURAL UNDERSTANDING ===
        
        # 8. Onset pattern (how events are distributed)
        features['onset_pattern'] = self._compute_onset_structure(audio, sr)
        
        # 9. Pitch characteristics
        features['pitch_profile'] = self._compute_pitch_profile(audio, sr)
        
        # 10. Spatial quality (open vs enclosed)
        features['spatial_openness'] = self._compute_spatial_quality(audio, sr)
        
        return features
    
    def _compute_valence(self, audio, sr):
        """Emotional positivity/negativity"""
        chroma = librosa.feature.chroma_cqt(y=audio, sr=sr)
        
        # Major vs minor intervals
        major_energy = chroma[4].mean()  # Major third
        minor_energy = chroma[3].mean()  # Minor third
        
        valence = (major_energy - minor_energy)
        return np.tanh(valence)  # [-1, 1]
    
    def _compute_energy(self, audio):
        """Overall intensity"""
        rms = librosa.feature.rms(y=audio)
        return float(np.mean(rms))
    
    def _compute_rhythm_complexity(self, audio, sr):
        """Predictability of temporal patterns"""
        onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
        
        if len(onset_env) > 1:
            onset_prob = onset_env / (np.sum(onset_env) + 1e-10)
            entropy = -np.sum(onset_prob * np.log(onset_prob + 1e-10))
            return float(entropy / np.log(len(onset_env)))
        return 0.0
    
    def _compute_harmonic_content(self, audio, sr):
        """Tonality vs noisiness"""
        harmonic, percussive = librosa.effects.hpss(audio)
        ratio = np.sum(harmonic**2) / (np.sum(audio**2) + 1e-10)
        return float(ratio)
    
    def _compute_spectral_motion(self, audio, sr):
        """Brightness change over time"""
        centroid = librosa.feature.spectral_centroid(y=audio, sr=sr)[0]
        
        if len(centroid) > 1:
            x = np.arange(len(centroid))
            slope = np.polyfit(x, centroid, 1)[0]
            return float(np.tanh(slope / 100))
        return 0.0
    
    def _compute_texture(self, audio, sr):
        """Density of spectral content"""
        flatness = librosa.feature.spectral_flatness(y=audio)
        return float(1 - np.mean(flatness))
    
    def _compute_timbre(self, audio, sr):
        """Characteristic sound quality"""
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)
        return np.mean(mfccs, axis=1)
    
    def _compute_onset_structure(self, audio, sr):
        """Pattern of sound attacks"""
        onset_frames = librosa.onset.onset_detect(y=audio, sr=sr)
        
        if len(onset_frames) > 1:
            iois = np.diff(onset_frames)
            return {
                'mean_ioi': float(np.mean(iois)),
                'ioi_variance': float(np.var(iois)),
                'num_onsets': int(len(onset_frames))
            }
        return {'mean_ioi': 0.0, 'ioi_variance': 0.0, 'num_onsets': 0}
    
    def _compute_pitch_profile(self, audio, sr):
        """Melodic characteristics"""
        pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
        
        pitch_track = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_track.append(pitch)
        
        if len(pitch_track) > 0:
            return {
                'mean_pitch': float(np.mean(pitch_track)),
                'pitch_range': float(np.max(pitch_track) - np.min(pitch_track)),
                'pitch_variance': float(np.var(pitch_track))
            }
        return {'mean_pitch': 0.0, 'pitch_range': 0.0, 'pitch_variance': 0.0}
    
    def _compute_spatial_quality(self, audio, sr):
        """Sense of acoustic space"""
        # Spectral rolloff indicates openness
        rolloff = librosa.feature.spectral_rolloff(y=audio, sr=sr, roll_percent=0.85)
        
        # Zero-crossing rate indicates space
        zcr = librosa.feature.zero_crossing_rate(audio)
        
        openness = float(np.mean(rolloff) / (sr/2) + np.mean(zcr))
        return np.clip(openness, 0, 1)
    
    def _average_features(self, feature_list):
        """Average multiple feature dictionaries"""
        if not feature_list:
            return {}
        
        averaged = {}
        
        all_keys = set()
        for f in feature_list:
            all_keys.update(f.keys())
        
        for key in all_keys:
            values = []
            for f in feature_list:
                if key in f:
                    val = f[key]
                    if isinstance(val, dict):
                        values.append(val)
                    elif isinstance(val, np.ndarray):
                        values.append(val)
                    else:
                        values.append(val)
            
            if values:
                if isinstance(values[0], dict):
                    averaged[key] = self._average_features(values)
                elif isinstance(values[0], np.ndarray):
                    averaged[key] = np.mean(values, axis=0)
                else:
                    averaged[key] = float(np.mean(values))
        
        return averaged
    
    def generate_scene_from_text(self, prompt):
        """
        Improved semantic matching for scene generation.
        Uses semantic mapping + fallback substring matching.
        """
        print(f"\n{'='*70}")
        print(f"GENERATING SCENE: '{prompt}'")
        print(f"{'='*70}")
        
        words = prompt.lower().split()
        
        # Semantic mapping: words → sound categories
        semantic_map = {
            # Environments
            'cafe': ['cafe_ambience', 'cafe_chatter', 'espresso_machine'],
            'coffee': ['cafe_ambience', 'espresso_machine'],
            'coffeeshop': ['cafe_ambience', 'cafe_chatter', 'espresso_machine'],
            'restaurant': ['cafe_ambience', 'cafe_chatter'],
            'indoor': ['cafe_ambience'],
            'inside': ['cafe_ambience'],
            
            'forest': ['forest_ambience', 'bird_chirp'],
            'woods': ['forest_ambience', 'bird_chirp'],
            'trees': ['forest_ambience'],
            'nature': ['forest_ambience', 'bird_chirp'],
            'outdoor': ['forest_ambience'],
            'outside': ['forest_ambience'],
            'wind': ['forest_ambience'],
            'breeze': ['forest_ambience'],
            'leaves': ['forest_ambience'],
            
            'underwater': ['underwater_ambience', 'whale_song', 'dolphin_clicks'],
            'ocean': ['underwater_ambience', 'whale_song', 'dolphin_clicks'],
            'sea': ['underwater_ambience', 'whale_song'],
            'aquatic': ['underwater_ambience', 'whale_song', 'dolphin_clicks'],
            'deep': ['underwater_ambience', 'whale_song'],
            'water': ['underwater_ambience'],
            'marine': ['underwater_ambience', 'whale_song', 'dolphin_clicks'],
            
            # Animals
            'whale': ['whale_song'],
            'whales': ['whale_song'],
            'humpback': ['whale_song'],
            'dolphin': ['dolphin_clicks'],
            'dolphins': ['dolphin_clicks'],
            'seal': ['sealion_shrimp'],
            'sealion': ['sealion_shrimp'],
            'sea-lion': ['sealion_shrimp'],
            'bird': ['bird_chirp'],
            'birds': ['bird_chirp'],
            'chirp': ['bird_chirp'],
            'chirping': ['bird_chirp'],
            'singing': ['bird_chirp', 'whale_song'],
            'song': ['bird_chirp', 'whale_song'],
            
            # Events/Actions
            'thunder': ['thunder'],
            'thunderstorm': ['thunder', 'forest_ambience'],
            'storm': ['thunder', 'forest_ambience'],
            'lightning': ['thunder'],
            'rain': ['forest_ambience'],
            'raining': ['forest_ambience'],
            'espresso': ['espresso_machine'],
            'steam': ['espresso_machine'],
            'hiss': ['espresso_machine'],
            'machine': ['espresso_machine'],
            'brewing': ['espresso_machine'],
            'chatter': ['cafe_chatter'],
            'talking': ['cafe_chatter'],
            'conversation': ['cafe_chatter'],
            'voices': ['cafe_chatter'],
            'people': ['cafe_chatter'],
            'crowd': ['cafe_chatter'],
            'clicks': ['dolphin_clicks'],
            'clicking': ['dolphin_clicks'],
            'echolocation': ['dolphin_clicks'],
            
            # Qualities (adjectives that suggest environments/sounds)
            'peaceful': ['underwater_ambience', 'forest_ambience'],
            'calm': ['forest_ambience', 'underwater_ambience'],
            'quiet': ['forest_ambience', 'underwater_ambience'],
            'serene': ['forest_ambience', 'underwater_ambience'],
            'tranquil': ['forest_ambience', 'underwater_ambience'],
            'busy': ['cafe_ambience', 'cafe_chatter'],
            'active': ['cafe_chatter', 'bird_chirp'],
            'lively': ['cafe_ambience', 'cafe_chatter', 'bird_chirp'],
            'dramatic': ['thunder', 'whale_song'],
            'intense': ['thunder', 'whale_song'],
            'powerful': ['thunder', 'whale_song'],
            'gentle': ['forest_ambience', 'bird_chirp'],
            'soft': ['forest_ambience'],
            'loud': ['thunder', 'espresso_machine'],
        }
        
        # Match words to sounds
        matched_sounds = set()
        matched_by_word = {}
        
        for word in words:
            # Direct semantic mapping
            if word in semantic_map:
                for sound in semantic_map[word]:
                    if sound in self.atomic_sounds:  # Verify sound exists
                        matched_sounds.add(sound)
                        if sound not in matched_by_word:
                            matched_by_word[sound] = []
                        matched_by_word[sound].append(word)
            
            # Fallback: substring matching in sound names
            for sound_name in self.atomic_sounds:
                if word in sound_name:
                    matched_sounds.add(sound_name)
                    if sound_name not in matched_by_word:
                        matched_by_word[sound_name] = []
                    matched_by_word[sound_name].append(word)
        
        if not matched_sounds:
            print("  ⚠️  No matching sounds found")
            print(f"  Try words like: cafe, forest, underwater, whale, bird, thunder, espresso")
            print(f"  Available sounds: {', '.join(self.atomic_sounds.keys())}")
            return None
        
        # Convert to list
        matched_sounds = list(matched_sounds)
        
        print(f"\n  Matched components:")
        for sound in matched_sounds:
            trigger_words = matched_by_word.get(sound, [])
            print(f"    • {sound:25s} (from: {', '.join(trigger_words)})")
        
        # Blend matched sounds
        latent = self._blend_sounds(matched_sounds)
        
        return {
            'latent': latent,
            'components': matched_sounds,
            'prompt': prompt
        }
    
    def _blend_sounds(self, sound_names, weights=None):
        """Compositionally blend multiple learned sounds"""
        
        if weights is None:
            weights = [1.0 / len(sound_names)] * len(sound_names)
        
        latents = [self.atomic_sounds[name] for name in sound_names]
        
        blended = {}
        all_keys = set()
        for lat in latents:
            all_keys.update(lat.keys())
        
        for key in all_keys:
            values = []
            valid_weights = []
            
            for lat, weight in zip(latents, weights):
                if key in lat:
                    values.append(lat[key])
                    valid_weights.append(weight)
            
            if values:
                if isinstance(values[0], dict):
                    # Recursive blend for nested dicts
                    blended[key] = self._blend_dict_values(values, valid_weights)
                elif isinstance(values[0], np.ndarray):
                    blended[key] = np.average(values, axis=0, weights=valid_weights)
                else:
                    blended[key] = float(np.average(values, weights=valid_weights))
        
        return blended
    
    def _blend_dict_values(self, dicts, weights):
        """Blend nested dictionary values"""
        blended = {}
        all_keys = set()
        for d in dicts:
            all_keys.update(d.keys())
        
        for key in all_keys:
            values = [d[key] for d in dicts if key in d]
            if values:
                if isinstance(values[0], np.ndarray):
                    blended[key] = np.average(values, axis=0, weights=weights[:len(values)])
                else:
                    blended[key] = float(np.average(values, weights=weights[:len(values)]))
        
        return blended
    
    def listen_internal(self, scene_representation):
        """
        'Hear' the latent representation without rendering audio.
        This is the model experiencing sound conceptually.
        """
        
        if not scene_representation:
            return None
        
        print(f"\n{'='*70}")
        print("INTERNAL LISTENING")
        print("(No audio rendered - pure semantic interpretation)")
        print(f"{'='*70}")
        
        latent = scene_representation['latent']
        components = scene_representation['components']
        prompt = scene_representation['prompt']
        
        print(f"\nPrompt: \"{prompt}\"")
        print(f"Components: {', '.join(components)}")
        
        # Interpret the latent representation
        interpretation = {}
        
        # Emotional dimension
        valence = latent.get('emotional_valence', 0)
        if valence > 0.3:
            interpretation['mood'] = 'positive/uplifting'
        elif valence < -0.3:
            interpretation['mood'] = 'negative/melancholic'
        else:
            interpretation['mood'] = 'neutral/ambient'
        
        # Energy dimension
        energy = latent.get('energy_level', 0)
        if energy > 0.15:
            interpretation['energy'] = 'high (active/intense)'
        elif energy > 0.05:
            interpretation['energy'] = 'medium (moderate)'
        else:
            interpretation['energy'] = 'low (calm/quiet)'
        
        # Complexity
        complexity = latent.get('temporal_complexity', 0)
        if complexity > 0.5:
            interpretation['pattern'] = 'complex/unpredictable'
        else:
            interpretation['pattern'] = 'simple/regular'
        
        # Tonality
        harmonic = latent.get('harmonic_richness', 0)
        if harmonic > 0.6:
            interpretation['character'] = 'tonal/melodic'
        elif harmonic > 0.3:
            interpretation['character'] = 'mixed (tonal + noise)'
        else:
            interpretation['character'] = 'noisy/percussive'
        
        # Spectral evolution
        motion = latent.get('spectral_trajectory', 0)
        if motion > 0.1:
            interpretation['evolution'] = 'brightening (rising energy)'
        elif motion < -0.1:
            interpretation['evolution'] = 'darkening (falling energy)'
        else:
            interpretation['evolution'] = 'stable (unchanging)'
        
        # Texture
        texture = latent.get('textural_density', 0)
        if texture > 0.6:
            interpretation['texture'] = 'dense/rich (many layers)'
        elif texture > 0.3:
            interpretation['texture'] = 'moderate'
        else:
            interpretation['texture'] = 'sparse/simple (few elements)'
        
        # Spatial quality
        space = latent.get('spatial_openness', 0)
        if space > 0.6:
            interpretation['space'] = 'open/expansive (outdoor feeling)'
        elif space > 0.3:
            interpretation['space'] = 'medium'
        else:
            interpretation['space'] = 'enclosed/intimate (indoor feeling)'
        
        # Print interpretation
        print(f"\n🧠 What the model 'hears':")
        for key, value in interpretation.items():
            print(f"   {key.capitalize():12s}: {value}")
        
        # Print raw latent values (for debugging)
        print(f"\n📊 Raw latent representation (excerpt):")
        for key, value in list(latent.items())[:7]:
            if isinstance(value, (int, float, np.number)):
                print(f"   {key:25s}: {value:7.4f}")
            elif isinstance(value, np.ndarray):
                print(f"   {key:25s}: [{value[0]:.3f}, {value[1]:.3f}, ...]")
            elif isinstance(value, dict):
                first_subkey = list(value.keys())[0]
                print(f"   {key:25s}: {{{first_subkey}: {value[first_subkey]:.3f}, ...}}")
        
        print(f"{'='*70}\n")
        
        return interpretation
    
    def save_model(self, filepath="equivocal_model.json"):
        """Save learned representations"""
        # Convert numpy arrays to lists for JSON
        def make_serializable(obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {k: make_serializable(v) for k, v in obj.items()}
            elif isinstance(obj, (np.integer, np.floating)):
                return float(obj)
            return obj
        
        data = {
            'atomic_sounds': make_serializable(self.atomic_sounds),
            'soundscapes': make_serializable(self.soundscapes)
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Model saved to {filepath}")


# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    
    # Initialize engine
    engine = SceneAudioEngine()
    
    # LEVEL 1: Train on atomic sounds
    engine.train_atomic_sounds()
    
    # Save the learned model
    engine.save_model()
    
    print("\n" + "="*70)
    print("🎓 TRAINING COMPLETE")
    print("="*70)
    print("\nThe model has learned the semantic meaning of:")
    for sound_name in engine.atomic_sounds.keys():
        print(f"  • {sound_name}")
    
    print("\n" + "="*70)
    print("🧪 TESTING INTERNAL LISTENING")
    print("="*70)
    
    # Test prompts (including "calm wind" which should now work!)
    test_prompts = [
        "peaceful underwater scene with whale",
        "cafe with espresso machine",
        "forest with bird and thunder",
        "dolphin underwater",
        "calm wind",  # This should work now!
        "dramatic storm",
        "quiet ocean",
        "busy coffee shop"
    ]
    
    for prompt in test_prompts:
        scene = engine.generate_scene_from_text(prompt)
        engine.listen_internal(scene)
        input("Press Enter to continue to next prompt...")
    
    print("\n" + "="*70)
    print("✨ EQUIVOCAL ENGINE READY")
    print("="*70)
    print("\nThe model can now 'hear' scenes without rendering audio!")
    print("Try your own prompts by modifying the test_prompts list.")