"""
Interactive Equivocal Demo
Explore semantic audio understanding through conversational prompts
"""

from equivocal import SceneAudioEngine
from pathlib import Path
import sys

def print_banner():
    """Welcome message"""
    print("\n" + "="*70)
    print("🎵 EQUIVOCAL - Interactive Demo")
    print("="*70)
    print("\nExplore semantic audio understanding without rendering sound.")
    print("Type prompts to see what the model 'hears' conceptually.\n")

def print_help():
    """Show available commands and tips"""
    print("\n" + "="*70)
    print("📖 HELP")
    print("="*70)
    
    print("\n🎯 Commands:")
    print("  help       - Show this help message")
    print("  examples   - Show example prompts")
    print("  sounds     - List available sounds")
    print("  save       - Save current model")
    print("  quit/exit  - Exit the demo")
    
    print("\n✨ Prompt Tips:")
    print("  Environments: cafe, forest, underwater, ocean")
    print("  Animals: whale, dolphin, bird, seal")
    print("  Events: thunder, storm, espresso, chatter")
    print("  Qualities: peaceful, calm, dramatic, busy, quiet")
    
    print("\n💡 Try combining them:")
    print("  'peaceful underwater whale'")
    print("  'busy cafe with espresso'")
    print("  'dramatic forest storm'")
    print()

def print_examples():
    """Show curated example prompts"""
    print("\n" + "="*70)
    print("🎨 EXAMPLE PROMPTS")
    print("="*70)
    
    examples = {
        "Natural Scenes": [
            "peaceful forest morning",
            "dramatic ocean storm", 
            "calm wind through trees",
            "gentle rain"
        ],
        "Underwater": [
            "deep ocean with whale song",
            "dolphin clicking underwater",
            "quiet underwater cave",
            "marine life ambience"
        ],
        "Urban/Indoor": [
            "busy coffee shop",
            "quiet morning cafe",
            "espresso machine steaming",
            "people talking in restaurant"
        ],
        "Dramatic Events": [
            "intense thunderstorm",
            "powerful whale call",
            "thunder in forest",
            "storm over ocean"
        ]
    }
    
    for category, prompts in examples.items():
        print(f"\n{category}:")
        for prompt in prompts:
            print(f"  → {prompt}")
    print()

def print_available_sounds(engine):
    """Show what sounds the model knows"""
    print("\n" + "="*70)
    print("🔊 AVAILABLE SOUNDS")
    print("="*70)
    print("\nThe model has learned these atomic sounds:\n")
    
    for sound in sorted(engine.atomic_sounds.keys()):
        print(f"  • {sound}")
    print()

def run_interactive_session():
    """Main interactive loop"""
    print_banner()
    
    # Check if training data exists
    data_path = Path("data/training_samples")
    if not data_path.exists():
        print("⚠️  Training data not found at 'data/training_samples/'")
        print("   Please run from the project root directory, or")
        print("   provide training data paths.\n")
        
        use_custom = input("Provide custom training paths? (y/n): ").lower()
        if use_custom == 'y':
            tier1 = input("Tier 1 path: ").strip()
            tier2 = input("Tier 2 path: ").strip()
            tier3 = input("Tier 3 path: ").strip()
        else:
            print("Exiting. Please run from project root.")
            sys.exit(1)
    else:
        tier1 = "data/training_samples/Tier_1"
        tier2 = "data/training_samples/Tier_2"
        tier3 = "data/training_samples/Tier_3"
    
    # Initialize and train
    print("\n🎓 Training model on audio samples...")
    print("(This will take 30-60 seconds)\n")
    
    engine = SceneAudioEngine()
    
    try:
        engine.train_atomic_sounds(tier1, tier2, tier3)
    except Exception as e:
        print(f"\n❌ Error during training: {e}")
        print("Please check that training data exists and is accessible.")
        sys.exit(1)
    
    print("\n✅ Training complete!")
    print("\nType 'help' for commands, or enter a prompt to begin.")
    print("Type 'quit' or 'exit' to end the session.\n")
    
    # Main interaction loop
    while True:
        try:
            # Get user input
            prompt = input("🎵 Equivocal> ").strip()
            
            # Handle empty input
            if not prompt:
                continue
            
            # Handle commands
            if prompt.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thanks for exploring Equivocal!")
                print("The song that plays in the mind of the machine,")
                print("before it learns to sing.\n")
                break
            
            elif prompt.lower() == 'help':
                print_help()
                continue
            
            elif prompt.lower() == 'examples':
                print_examples()
                continue
            
            elif prompt.lower() == 'sounds':
                print_available_sounds(engine)
                continue
            
            elif prompt.lower() == 'save':
                filename = input("Save as (default: equivocal_model.json): ").strip()
                if not filename:
                    filename = "equivocal_model.json"
                engine.save_model(filename)
                continue
            
            # Process as scene generation prompt
            scene = engine.generate_scene_from_text(prompt)
            
            if scene:
                engine.listen_internal(scene)
            
            # Offer to continue
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Exiting gracefully...")
            break
        
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Try 'help' for guidance or 'quit' to exit.\n")

if __name__ == "__main__":
    run_interactive_session()