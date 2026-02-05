"""
Equivocal GUI - Graphical interface for semantic audio understanding
Built with tkinter (Python standard library - no extra dependencies)
"""

import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
from pathlib import Path
import threading
import sys
import os

# Add parent directory to path to import equivocal
sys.path.insert(0, str(Path(__file__).parent.parent))
from equivocal import SceneAudioEngine


class EquivocalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Equivocal - Semantic Audio Understanding")
        self.root.geometry("800x700")
        self.root.resizable(True, True)
        
        # State
        self.engine = None
        self.is_trained = False
        
        # Paths
        self.tier1_path = tk.StringVar(value="data/training_samples/Tier_1")
        self.tier2_path = tk.StringVar(value="data/training_samples/Tier_2")
        self.tier3_path = tk.StringVar(value="data/training_samples/Tier_3")
        
        # Build UI
        self.create_widgets()
        
    def create_widgets(self):
        """Build the interface"""
        
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # ===== HEADER =====
        header = ttk.Label(
            main_frame, 
            text="🎵 Equivocal", 
            font=('Arial', 18, 'bold')
        )
        header.grid(row=0, column=0, columnspan=3, pady=(0, 5))
        
        subtitle = ttk.Label(
            main_frame,
            text="Semantic audio understanding without rendering",
            font=('Arial', 10, 'italic')
        )
        subtitle.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # ===== STEP 1: TRAINING DATA =====
        row = 2
        step1_label = ttk.Label(
            main_frame,
            text="Step 1: Select Training Data",
            font=('Arial', 12, 'bold')
        )
        step1_label.grid(row=row, column=0, columnspan=3, sticky=tk.W, pady=(10, 10))
        
        # Tier 1
        row += 1
        ttk.Label(main_frame, text="Tier 1 (Base Layers):").grid(
            row=row, column=0, sticky=tk.W, pady=5
        )
        tier1_entry = ttk.Entry(main_frame, textvariable=self.tier1_path, width=50)
        tier1_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(
            main_frame, text="Browse...", 
            command=lambda: self.browse_folder(self.tier1_path)
        ).grid(row=row, column=2)
        
        # Tier 2
        row += 1
        ttk.Label(main_frame, text="Tier 2 (Events):").grid(
            row=row, column=0, sticky=tk.W, pady=5
        )
        tier2_entry = ttk.Entry(main_frame, textvariable=self.tier2_path, width=50)
        tier2_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(
            main_frame, text="Browse...",
            command=lambda: self.browse_folder(self.tier2_path)
        ).grid(row=row, column=2)
        
        # Tier 3
        row += 1
        ttk.Label(main_frame, text="Tier 3 (Textures):").grid(
            row=row, column=0, sticky=tk.W, pady=5
        )
        tier3_entry = ttk.Entry(main_frame, textvariable=self.tier3_path, width=50)
        tier3_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5)
        ttk.Button(
            main_frame, text="Browse...",
            command=lambda: self.browse_folder(self.tier3_path)
        ).grid(row=row, column=2)
        
        # Train button
        row += 1
        self.train_button = ttk.Button(
            main_frame,
            text="Train Model",
            command=self.train_model
        )
        self.train_button.grid(row=row, column=0, columnspan=3, pady=20)
        
        # Progress bar
        row += 1
        self.progress = ttk.Progressbar(
            main_frame,
            mode='indeterminate',
            length=400
        )
        self.progress.grid(row=row, column=0, columnspan=3, pady=(0, 10))
        
        # Status label
        row += 1
        self.status_label = ttk.Label(
            main_frame,
            text="Ready to train",
            foreground="gray"
        )
        self.status_label.grid(row=row, column=0, columnspan=3)
        
        # ===== SEPARATOR =====
        row += 1
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).grid(
            row=row, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20
        )
        
        # ===== STEP 2: EXPLORATION =====
        row += 1
        step2_label = ttk.Label(
            main_frame,
            text="Step 2: Explore Scenes",
            font=('Arial', 12, 'bold')
        )
        step2_label.grid(row=row, column=0, columnspan=3, sticky=tk.W, pady=(10, 10))
        
        # Prompt entry
        row += 1
        ttk.Label(main_frame, text="Enter prompt:").grid(
            row=row, column=0, sticky=tk.W, pady=5
        )
        self.prompt_var = tk.StringVar(value="peaceful underwater whale")
        self.prompt_entry = ttk.Entry(
            main_frame,
            textvariable=self.prompt_var,
            width=50,
            state='disabled'
        )
        self.prompt_entry.grid(row=row, column=1, sticky=(tk.W, tk.E), padx=5)
        
        # Generate button
        self.generate_button = ttk.Button(
            main_frame,
            text="Generate Scene",
            command=self.generate_scene,
            state='disabled'
        )
        self.generate_button.grid(row=row, column=2)
        
        # Example prompts button
        row += 1
        ttk.Button(
            main_frame,
            text="Show Example Prompts",
            command=self.show_examples,
            state='disabled'  # Enable after training
        ).grid(row=row, column=0, columnspan=3, pady=5)
        
        # Results output
        row += 1
        ttk.Label(main_frame, text="Results:").grid(
            row=row, column=0, sticky=tk.W, pady=(10, 5)
        )
        
        row += 1
        self.output_text = scrolledtext.ScrolledText(
            main_frame,
            width=80,
            height=15,
            wrap=tk.WORD,
            font=('Courier', 9),
            state='disabled'
        )
        self.output_text.grid(
            row=row, column=0, columnspan=3,
            sticky=(tk.W, tk.E, tk.N, tk.S),
            pady=(0, 10)
        )
        
        # Configure text tags for colored output
        self.output_text.tag_config('header', foreground='blue', font=('Courier', 9, 'bold'))
        self.output_text.tag_config('prompt', foreground='green', font=('Courier', 9, 'bold'))
        self.output_text.tag_config('component', foreground='purple')
        self.output_text.tag_config('result', foreground='darkgreen')
        
        # Bottom buttons
        row += 1
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=row, column=0, columnspan=3, pady=(10, 0))
        
        self.save_button = ttk.Button(
            button_frame,
            text="Save Model",
            command=self.save_model,
            state='disabled'
        )
        self.save_button.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Clear Output",
            command=self.clear_output
        ).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(
            button_frame,
            text="Help",
            command=self.show_help
        ).pack(side=tk.LEFT, padx=5)
        
        # Make output text expandable
        main_frame.rowconfigure(row-1, weight=1)
    
    def browse_folder(self, path_var):
        """Open folder browser"""
        folder = filedialog.askdirectory(
            title="Select Folder",
            initialdir=path_var.get() if Path(path_var.get()).exists() else "."
        )
        if folder:
            path_var.set(folder)
    
    def train_model(self):
        """Train the model in background thread"""
        # Validate paths
        tier1 = self.tier1_path.get()
        tier2 = self.tier2_path.get()
        tier3 = self.tier3_path.get()
        
        if not all(Path(p).exists() for p in [tier1, tier2, tier3]):
            messagebox.showerror(
                "Error",
                "One or more training data paths do not exist.\nPlease check the paths and try again."
            )
            return
        
        # Disable controls
        self.train_button.config(state='disabled')
        self.prompt_entry.config(state='disabled')
        self.generate_button.config(state='disabled')
        
        # Start progress bar
        self.progress.start()
        self.status_label.config(text="Training model... (this may take 30-60 seconds)", foreground="blue")
        
        # Run training in background
        def train_thread():
            try:
                self.engine = SceneAudioEngine()
                self.engine.train_atomic_sounds(tier1, tier2, tier3)
                
                # Update UI on success (must use after() for thread safety)
                self.root.after(0, self.training_complete)
                
            except Exception as e:
                self.root.after(0, lambda: self.training_error(str(e)))
        
        threading.Thread(target=train_thread, daemon=True).start()
    
    def training_complete(self):
        """Called when training finishes successfully"""
        self.progress.stop()
        self.status_label.config(text="✅ Training complete! Ready to explore.", foreground="green")
        self.is_trained = True
        
        # Enable exploration controls
        self.train_button.config(state='normal')
        self.prompt_entry.config(state='normal')
        self.generate_button.config(state='normal')
        self.save_button.config(state='normal')
        
        # Enable example button
        for widget in self.root.winfo_children():
            self._enable_examples_recursive(widget)
        
        # Show success message
        self.write_output("="*70 + "\n", 'header')
        self.write_output("TRAINING COMPLETE\n", 'header')
        self.write_output("="*70 + "\n\n", 'header')
        self.write_output(f"Learned {len(self.engine.atomic_sounds)} atomic sounds:\n")
        for sound in self.engine.atomic_sounds.keys():
            self.write_output(f"  • {sound}\n", 'component')
        self.write_output("\nEnter a prompt above to begin exploring!\n\n")
        
        # Focus prompt entry
        self.prompt_entry.focus()
    
    def _enable_examples_recursive(self, widget):
        """Recursively enable 'Show Example Prompts' button"""
        if isinstance(widget, ttk.Button) and 'Show Example' in widget.cget('text'):
            widget.config(state='normal')
        for child in widget.winfo_children():
            self._enable_examples_recursive(child)
    
    def training_error(self, error_msg):
        """Called when training fails"""
        self.progress.stop()
        self.status_label.config(text="❌ Training failed", foreground="red")
        self.train_button.config(state='normal')
        
        messagebox.showerror(
            "Training Error",
            f"Failed to train model:\n\n{error_msg}\n\nPlease check:\n"
            "- Training data paths are correct\n"
            "- Folders contain .wav files\n"
            "- Files are not corrupted"
        )
    
    def generate_scene(self):
        """Generate and interpret a scene from prompt"""
        if not self.is_trained:
            messagebox.showwarning("Not Ready", "Please train the model first.")
            return
        
        prompt = self.prompt_var.get().strip()
        if not prompt:
            messagebox.showwarning("Empty Prompt", "Please enter a prompt.")
            return
        
        self.write_output("\n" + "="*70 + "\n", 'header')
        self.write_output(f"PROMPT: '{prompt}'\n", 'prompt')
        self.write_output("="*70 + "\n\n", 'header')
        
        try:
            # Generate scene
            scene = self.engine.generate_scene_from_text(prompt)
            
            if not scene:
                self.write_output("⚠️  No matching sounds found for this prompt.\n")
                self.write_output("Try different words or use 'Show Example Prompts'.\n\n")
                return
            
            # Show components
            self.write_output("Matched components:\n", 'component')
            for comp in scene['components']:
                self.write_output(f"  • {comp}\n", 'component')
            self.write_output("\n")
            
            # Interpret
            interpretation = self.engine.listen_internal(scene)
            
            # Format interpretation results
            self.write_output("🧠 What the model 'hears':\n", 'result')
            for key, value in interpretation.items():
                self.write_output(f"   {key.capitalize():12s}: {value}\n", 'result')
            
            self.write_output("\n📊 Raw latent values:\n", 'result')
            latent = scene['latent']
            for key, value in list(latent.items())[:7]:
                if isinstance(value, (int, float)):
                    self.write_output(f"   {key:25s}: {value:7.4f}\n", 'result')
                elif hasattr(value, '__len__') and len(value) > 0:
                    self.write_output(f"   {key:25s}: [{value[0]:.3f}, ...]\n", 'result')
            
            self.write_output("\n")
            
        except Exception as e:
            self.write_output(f"❌ Error: {str(e)}\n\n")
    
    def save_model(self):
        """Save the trained model"""
        if not self.is_trained:
            return
        
        filename = filedialog.asksaveasfilename(
            title="Save Model As",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            initialfile="equivocal_model.json"
        )
        
        if filename:
            try:
                self.engine.save_model(filename)
                messagebox.showinfo("Success", f"Model saved to:\n{filename}")
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save model:\n{str(e)}")
    
    def show_examples(self):
        """Show example prompts in a popup"""
        examples_window = tk.Toplevel(self.root)
        examples_window.title("Example Prompts")
        examples_window.geometry("500x600")
        
        # Header
        ttk.Label(
            examples_window,
            text="🎨 Example Prompts",
            font=('Arial', 14, 'bold')
        ).pack(pady=10)
        
        # Scrollable text
        text = scrolledtext.ScrolledText(
            examples_window,
            width=60,
            height=30,
            wrap=tk.WORD,
            font=('Arial', 10)
        )
        text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Add examples
        examples = {
            "Natural Scenes": [
                "peaceful forest morning",
                "dramatic ocean storm",
                "calm wind through trees",
                "gentle rain in forest"
            ],
            "Underwater": [
                "deep ocean with whale song",
                "dolphin clicking underwater",
                "quiet underwater cave",
                "seal calls with shrimp"
            ],
            "Urban/Indoor": [
                "busy coffee shop",
                "quiet morning cafe",
                "espresso machine steaming",
                "people talking in cafe"
            ],
            "Dramatic Events": [
                "intense thunderstorm",
                "powerful whale call",
                "thunder in forest",
                "storm with rain and wind"
            ]
        }
        
        for category, prompts in examples.items():
            text.insert(tk.END, f"{category}:\n", 'category')
            for prompt in prompts:
                text.insert(tk.END, f"  → {prompt}\n")
            text.insert(tk.END, "\n")
        
        text.tag_config('category', font=('Arial', 10, 'bold'), foreground='blue')
        text.config(state='disabled')
        
        # Close button
        ttk.Button(
            examples_window,
            text="Close",
            command=examples_window.destroy
        ).pack(pady=10)
    
    def show_help(self):
        """Show help dialog"""
        help_text = """
🎵 EQUIVOCAL - HELP

GETTING STARTED:
1. Select your training data folders (Tier 1, 2, 3)
2. Click 'Train Model' and wait 30-60 seconds
3. Enter a prompt and click 'Generate Scene'
4. Explore different prompts to see what the model 'hears'

TRAINING DATA:
- Tier 1: Base environments (cafe, forest, underwater)
- Tier 2: Distinctive events (birds, whales, thunder, espresso)
- Tier 3: Textures (chatter, clicks, ambient sounds)

WRITING PROMPTS:
Combine these elements for rich scenes:
- Environments: cafe, forest, underwater, ocean
- Animals: whale, dolphin, bird, seal
- Events: thunder, storm, espresso, chatter
- Qualities: peaceful, calm, dramatic, busy, quiet

EXAMPLES:
- "peaceful underwater whale"
- "busy cafe with espresso"
- "dramatic forest thunderstorm"

Click 'Show Example Prompts' for more ideas!
"""
        messagebox.showinfo("Help", help_text)
    
    def clear_output(self):
        """Clear the output text"""
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state='disabled')
    
    def write_output(self, text, tag=None):
        """Write text to output window"""
        self.output_text.config(state='normal')
        if tag:
            self.output_text.insert(tk.END, text, tag)
        else:
            self.output_text.insert(tk.END, text)
        self.output_text.see(tk.END)  # Auto-scroll
        self.output_text.config(state='disabled')


def main():
    root = tk.Tk()
    app = EquivocalGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()