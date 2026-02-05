"""
Basic Usage Example for Equivocal

This script demonstrates the fundamental workflow:
1. Initialize the engine
2. Train on audio samples
3. Generate scenes from text
4. Interpret internal representations
"""

from equivocal import SceneAudioEngine
from pathlib import Path

def main():
    print("="*70)
    print("EQUIVOCAL - Basic Usage Example")
    print("="*70)
    print()
    
    # Step 1: Initialize the engine
    print("Step 1: Initializing Scene Audio Engine...")
    engine = SceneAudioEngine()
    print("✓ Engine initialized\n")
    
    # Step 2: Train on audio samples
    print("Step 2: Training on audio samples...")
    print("(This will take 30-60 seconds)")
    print()
    
    # Check if training data exists
    data_path = Path("data/training_samples")
    if not data_path.exists():
        print("❌ Training data not found!")
        print(f"   Expected path: {data_path.absolute()}")
        print("   Please run from project root directory.")
        return
    
    try:
        engine.train_atomic_sounds(
            tier1_path="data/training_samples/Tier_1",
            tier2_path="data/training_samples/Tier_2",
            tier3_path="data/training_samples/Tier_3"
        )
        print("\n✓ Training complete!\n")
    except Exception as e:
        print(f"❌ Training failed: {e}")
        return
    
    # Step 3: Generate scenes from text prompts
    print("="*70)
    print("Step 3: Generating Scenes")
    print("="*70)
    print()
    
    # Example prompts
    prompts = [
        "peaceful underwater whale song",
        "busy cafe with espresso",
        "dramatic forest thunderstorm"
    ]
    
    for prompt in prompts:
        print(f"\nPrompt: '{prompt}'")
        print("-" * 70)
        
        # Generate scene
        scene = engine.generate_scene_from_text(prompt)
        
        if scene:
            # Show components
            print(f"Components: {', '.join(scene['components'])}")
            
            # Step 4: Interpret internal representation
            print("\n🧠 Internal Listening:")
            interpretation = engine.listen_internal(scene)
            
            # Print interpretation (already done by listen_internal)
            # But you could also access the data:
            if interpretation:
                print("\nYou can also access interpretation data programmatically:")
                print(f"  Mood: {interpretation.get('mood', 'N/A')}")
                print(f"  Energy: {interpretation.get('energy', 'N/A')}")
        else:
            print("⚠️  No matching sounds found")
        
        print()
    
    # Step 5: Save the trained model (optional)
    print("="*70)
    print("Step 5: Saving Model")
    print("="*70)
    print()
    
    model_path = "my_equivocal_model.json"
    engine.save_model(model_path)
    print(f"✓ Model saved to: {model_path}\n")
    
    # Conclusion
    print("="*70)
    print("EXAMPLE COMPLETE")
    print("="*70)
    print()
    print("Next steps:")
    print("  • Try your own prompts in the code above")
    print("  • Run interactive_demo.py for a conversational interface")
    print("  • Run gui_demo.py for a graphical interface")
    print("  • Train on your own audio samples")
    print()

if __name__ == "__main__":
    main()