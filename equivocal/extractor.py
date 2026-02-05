import librosa
import soundfile as sf
import numpy as np
from pathlib import Path

class CleanAudioExtractor:
    """Extract samples with minimal, clean processing"""
    
    def __init__(self, target_sr=22050):
        self.target_sr = target_sr
    
    def extract_clean_sample(self, 
                            input_file, 
                            output_file, 
                            start_time, 
                            duration,
                            fade_duration=0.01,
                            normalize=True,
                            trim_silence=False):
        """
        Extract with clean, minimal processing
        """
        print(f"\n📥 Processing: {Path(input_file).name}")
        
        # Load audio
        audio, sr = librosa.load(input_file, sr=self.target_sr, mono=True)
        
        # Extract time segment
        start_sample = int(start_time * sr)
        end_sample = int((start_time + duration) * sr)
        
        if end_sample > len(audio):
            print(f"  ⚠️  Requested end time exceeds file length")
            end_sample = len(audio)
        
        segment = audio[start_sample:end_sample]
        
        # Optional: Trim silence from edges
        if trim_silence:
            segment, _ = librosa.effects.trim(segment, top_db=40)
            print(f"  ✂️  Trimmed silence")
        
        # Apply gentle fade in/out (prevents clicks)
        fade_samples = int(fade_duration * sr)
        if len(segment) > 2 * fade_samples:
            fade_in = np.linspace(0, 1, fade_samples)
            segment[:fade_samples] *= fade_in
            
            fade_out = np.linspace(1, 0, fade_samples)
            segment[-fade_samples:] *= fade_out
            
            print(f"  🎚️  Applied {fade_duration*1000:.0f}ms fades")
        
        # Normalize volume
        if normalize:
            peak = np.max(np.abs(segment))
            if peak > 0:
                segment = segment / peak * 0.8
                print(f"  📊 Normalized (peak was {peak:.3f})")
        
        # Save
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        sf.write(output_file, segment, sr)
        
        actual_duration = len(segment) / sr
        print(f"  ✅ Saved: {actual_duration:.2f}s → {output_path.name}")
        
        return segment, sr
    
    def find_interesting_moments(self, input_file, duration=5, n_moments=5):
        """
        Auto-detect good extraction points
        """
        print(f"\n🔍 Analyzing: {Path(input_file).name}")
        
        audio, sr = librosa.load(input_file, sr=self.target_sr, mono=True)
        total_duration = len(audio) / sr
        
        # Calculate onset strength
        onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
        onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr)
        onset_times = librosa.frames_to_time(onset_frames, sr=sr)
        
        # Calculate RMS energy in windows
        hop_length = int(sr * 0.5)
        window_size = int(duration * sr)
        
        segments = []
        for i in range(0, len(audio) - window_size, hop_length):
            window = audio[i:i+window_size]
            start_time = i / sr
            
            rms = np.sqrt(np.mean(window**2))
            
            onsets_in_window = np.sum((onset_times >= start_time) & 
                                     (onset_times < start_time + duration))
            
            score = rms * (1 + 0.5 * onsets_in_window)
            
            segments.append({
                'start': start_time,
                'score': score,
                'rms': rms,
                'onsets': onsets_in_window
            })
        
        # Sort by score
        segments.sort(key=lambda x: x['score'], reverse=True)
        top_segments = segments[:n_moments]
        top_segments.sort(key=lambda x: x['start'])
        
        print(f"  Total duration: {total_duration:.1f}s")
        print(f"  Found {len(onset_times)} onset events")
        print(f"\n  Top {n_moments} moments:")
        
        for i, seg in enumerate(top_segments, 1):
            print(f"    {i}. {seg['start']:6.1f}s - "
                  f"energy: {seg['rms']:.3f}, "
                  f"events: {seg['onsets']}")
        
        return [seg['start'] for seg in top_segments]
    
    def extract_stereo_channels(self, input_file, output_left, output_right, 
                               start_time, duration):
        """
        Special extractor for stereo files like the whale recording
        (Left = underwater, Right = surface)
        """
        print(f"\n📥 Processing STEREO: {Path(input_file).name}")
        
        # Load WITHOUT forcing mono
        audio, sr = librosa.load(input_file, sr=self.target_sr, mono=False)
        
        if len(audio.shape) == 1:
            print("  ⚠️  File is mono, not stereo")
            return None
        
        print(f"  Channels: {audio.shape[0]}")
        
        start_sample = int(start_time * sr)
        end_sample = int((start_time + duration) * sr)
        
        left_channel = audio[0, start_sample:end_sample]
        right_channel = audio[1, start_sample:end_sample]
        
        # Save both channels
        for channel, output_file, name in [
            (left_channel, output_left, "underwater"),
            (right_channel, output_right, "surface")
        ]:
            # Normalize
            peak = np.max(np.abs(channel))
            if peak > 0:
                channel = channel / peak * 0.8
            
            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            sf.write(output_file, channel, sr)
            print(f"  ✅ Saved {name}: {output_path.name}")


# ============================================
# EXTRACTION PLAN FOR YOUR FILES
# ============================================

if __name__ == "__main__":
    
    extractor = CleanAudioExtractor()
    
    print("="*70)
    print("EQUIVOCAL - Audio Sample Extraction")
    print("="*70)
    
    # ========================================
    # TIER 1: BASE LAYERS
    # ========================================
    
    print("\n" + "="*70)
    print("TIER 1: BASE LAYERS")
    print("="*70)
    
    # 1. CAFE AMBIENCE (Morocco - has everything!)
    print("\n[1/3] Cafe Ambience (Morocco)")
    moments = extractor.find_interesting_moments(
        "Africa Morocco - Morocco Rabat, cafe atmosphere with audible traffic, TV & expresso machine.wav",
        duration=10,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Africa Morocco - Morocco Rabat, cafe atmosphere with audible traffic, TV & expresso machine.wav",
        output_file="Tier_1/cafe_ambience/morocco_cafe.wav",
        start_time=moments[0],
        duration=10
    )
    
    # 2. FOREST AMBIENCE (Sacred Banyan)
    print("\n[2/3] Forest Ambience (Wind through Banyan)")
    moments = extractor.find_interesting_moments(
        "Wind Atmosphere - Wind blowing in leaves & branches of tree. N.B. This is the worlds largest Banyam, a sacred tree.wav",
        duration=10,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Wind Atmosphere - Wind blowing in leaves & branches of tree. N.B. This is the worlds largest Banyam, a sacred tree.wav",
        output_file="Tier_1/forest_ambience/banyan_wind.wav",
        start_time=moments[0],
        duration=10
    )
    
    # 3. UNDERWATER AMBIENCE (Rockpool)
    print("\n[3/3] Underwater Ambience (Rockpool)")
    moments = extractor.find_interesting_moments(
        "Rockpool Atmosphere - underwater atmosphere within rockpool [rec with hydrophone].wav",
        duration=10,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Rockpool Atmosphere - underwater atmosphere within rockpool [rec with hydrophone].wav",
        output_file="Tier_1/underwater_ambience/rockpool.wav",
        start_time=moments[0],
        duration=10
    )
    
    # ========================================
    # TIER 2: DISTINCTIVE EVENTS
    # ========================================
    
    print("\n" + "="*70)
    print("TIER 2: DISTINCTIVE EVENTS")
    print("="*70)
    
    # 4. BIRD CHIRP (Puerto Rican Tody - melodic warble)
    print("\n[1/4] Bird: Puerto Rican Tody")
    moments = extractor.find_interesting_moments(
        "Puerto Rican Tody (Todus Mexicanus) - medium close-up tody warble. Forest atmosphere & light wind in background.wav",
        duration=5,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Puerto Rican Tody (Todus Mexicanus) - medium close-up tody warble. Forest atmosphere & light wind in background.wav",
        output_file="Tier_2/bird_chirp/tody_warble.wav",
        start_time=moments[0],
        duration=5
    )
    
    # 5. WHALE SONG (Right Whale - extract underwater channel)
    print("\n[2/4] Whale Song (Northern Right Whale - STEREO)")
    print("  Extracting BOTH channels (underwater + surface)")
    moments = extractor.find_interesting_moments(
        "Northern Right Whale (Eubalaena Glacialis Glacialis) - close-up 'blowing' Fin and slaps on surface and underwater. Song and calls underwater, Left track underwater, right track on surface, 2 whales mating, Sei and mink.wav",
        duration=10,
        n_moments=2
    )
    extractor.extract_stereo_channels(
        input_file="Northern Right Whale (Eubalaena Glacialis Glacialis) - close-up 'blowing' Fin and slaps on surface and underwater. Song and calls underwater, Left track underwater, right track on surface, 2 whales mating, Sei and mink.wav",
        output_left="Tier_2/whale_song/right_whale_underwater.wav",
        output_right="Tier_2/whale_song/right_whale_surface.wav",
        start_time=moments[0],
        duration=10
    )
    
    # 6. ESPRESSO MACHINE (Extract from Morocco cafe)
    print("\n[3/4] Espresso Machine (from Morocco cafe)")
    print("  Manually finding espresso burst...")
    # This will require listening - espresso machines make distinctive sounds
    # For now, extract a likely moment (you can adjust after listening)
    extractor.extract_clean_sample(
        input_file="Africa Morocco - Morocco Rabat, cafe atmosphere with audible traffic, TV & expresso machine.wav",
        output_file="Tier_2/espresso_machine/steam_hiss.wav",
        start_time=60,  # Guess - you may need to adjust
        duration=6
    )
    
    # 7. THUNDER (Single crack)
    print("\n[4/4] Thunder (Single crack)")
    moments = extractor.find_interesting_moments(
        "Thunder - Single crack of thunder.wav",
        duration=7,
        n_moments=1
    )
    extractor.extract_clean_sample(
        input_file="Thunder - Single crack of thunder.wav",
        output_file="Tier_2/thunder/crack.wav",
        start_time=moments[0],
        duration=7
    )
    
    # ========================================
    # TIER 3: TEXTURE
    # ========================================
    
    print("\n" + "="*70)
    print("TIER 3: TEXTURE")
    print("="*70)
    
    # 8. CAFE CHATTER (Arabic)
    print("\n[1/3] Cafe Chatter (Arabic)")
    moments = extractor.find_interesting_moments(
        "Arabic Crowds Tangier - Tangier, tourist cafe general atmosphere..wav",
        duration=8,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Arabic Crowds Tangier - Tangier, tourist cafe general atmosphere..wav",
        output_file="Tier_3/cafe_chatter/arabic_murmur.wav",
        start_time=moments[0],
        duration=8
    )
    
    # 9. DOLPHIN CLICKS (Bottle-nosed)
    print("\n[2/3] Dolphin Clicks (Echo-location)")
    moments = extractor.find_interesting_moments(
        "Bottle-nosed Dolphin (Tursiops Truncatus) - Echo-location sounds recorded underwater with hydrophone.wav",
        duration=5,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Bottle-nosed Dolphin (Tursiops Truncatus) - Echo-location sounds recorded underwater with hydrophone.wav",
        output_file="Tier_3/dolphin_clicks/echolocation.wav",
        start_time=moments[0],
        duration=5
    )
    
    # 10. BONUS: SEALION + SNAPPING SHRIMP
    print("\n[3/3] BONUS: Sealion with Snapping Shrimp")
    moments = extractor.find_interesting_moments(
        "Galapagos Sealion (Zalophus Californianus Wollebakei) - Calls underwater from a bull, With snapping shrimp and underwater sounds.wav",
        duration=6,
        n_moments=3
    )
    extractor.extract_clean_sample(
        input_file="Galapagos Sealion (Zalophus Californianus Wollebakei) - Calls underwater from a bull, With snapping shrimp and underwater sounds.wav",
        output_file="Tier_3/sealion_shrimp/galapagos.wav",
        start_time=moments[0],
        duration=6
    )
    
    print("\n" + "="*70)
    print("✅ EXTRACTION COMPLETE!")
    print("="*70)
    print("\nExtracted samples are in:")
    print("  - Tier_1/ (base layers)")
    print("  - Tier_2/ (distinctive events)")
    print("  - Tier_3/ (texture)")
    print("\nNext: Listen to samples and verify quality!")