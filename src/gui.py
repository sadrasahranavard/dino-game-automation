import tkinter as tk
from tkinter import ttk, messagebox
import threading
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.controller import DinoController

class DinoGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🦖 Dino Game Bot Controller")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        self.controller = DinoController()
        self.bot_thread = None
        
        self.bg = "#2b2b2b"
        self.fg = "#ffffff"
        self.accent = "#B4B239"
        
        self.root.configure(bg=self.bg)
        
        self.setup_ui()
    
    def setup_ui(self):
        title = tk.Label(
            self.root,
            text="🦖 DINO GAME BOT",
            font=("Arial", 20, "bold"),
            bg=self.bg,
            fg=self.accent
        )
        title.pack(pady=20)
        
        instructions = tk.Label(
            self.root,
            text="1. Open https://elgoog.im/t-rex/\n"
                 "2. Position the game window\n"
                 "3. Set detection zone below\n"
                 "4. Click Start",
            font=("Arial", 10),
            bg=self.bg,
            fg=self.fg,
            justify=tk.LEFT
        )
        instructions.pack(pady=10)
        
        zone_frame = tk.LabelFrame(
            self.root,
            text="Detection Zone",
            font=("Arial", 11),
            bg=self.bg,
            fg=self.fg,
            padx=10,
            pady=10
        )
        zone_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(zone_frame, text="X:", bg=self.bg, fg=self.fg).grid(row=0, column=0, sticky=tk.W)
        self.x_entry = tk.Entry(zone_frame, width=10)
        self.x_entry.insert(0, "350")
        self.x_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(zone_frame, text="Y:", bg=self.bg, fg=self.fg).grid(row=0, column=2, sticky=tk.W)
        self.y_entry = tk.Entry(zone_frame, width=10)
        self.y_entry.insert(0, "400")
        self.y_entry.grid(row=0, column=3, padx=5)
        
        tk.Label(zone_frame, text="Width:", bg=self.bg, fg=self.fg).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.w_entry = tk.Entry(zone_frame, width=10)
        self.w_entry.insert(0, "150")
        self.w_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(zone_frame, text="Height:", bg=self.bg, fg=self.fg).grid(row=1, column=2, sticky=tk.W, pady=5)
        self.h_entry = tk.Entry(zone_frame, width=10)
        self.h_entry.insert(0, "80")
        self.h_entry.grid(row=1, column=3, padx=5, pady=5)
        
        btn_frame = tk.Frame(self.root, bg=self.bg)
        btn_frame.pack(pady=20)
        
        self.start_btn = tk.Button(
            btn_frame,
            text="▶ START",
            command=self.start_bot,
            font=("Arial", 12, "bold"),
            bg=self.accent,
            fg="white",
            padx=20,
            pady=10,
            cursor="hand2"
        )
        self.start_btn.pack(side=tk.LEFT, padx=10)
        
        self.stop_btn = tk.Button(
            btn_frame,
            text="⏹ STOP",
            command=self.stop_bot,
            font=("Arial", 12, "bold"),
            bg="#ce3429",
            fg="white",
            padx=20,
            pady=10,
            state=tk.DISABLED,
            cursor="hand2"
        )
        self.stop_btn.pack(side=tk.LEFT, padx=10)
        
        self.status_label = tk.Label(
            self.root,
            text="Ready",
            font=("Arial", 10),
            bg=self.bg,
            fg="#888888"
        )
        self.status_label.pack(pady=10)
        
        self.stats_label = tk.Label(
            self.root,
            text="Jumps: 0 | Ducks: 0",
            font=("Arial", 10),
            bg=self.bg,
            fg=self.fg
        )
        self.stats_label.pack()
        
        warning = tk.Label(
            self.root,
            text="⚠ Move mouse to top-left corner to emergency stop",
            font=("Arial", 8),
            bg=self.bg,
            fg="#ff9800"
        )
        warning.pack(pady=20)
    
    def start_bot(self):
        try:
            x = int(self.x_entry.get())
            y = int(self.y_entry.get())
            w = int(self.w_entry.get())
            h = int(self.h_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return
        
        self.controller.configure(x, y, w, h)
        
        self.bot_thread = threading.Thread(target=self._run_bot, daemon=True)
        self.bot_thread.start()
        
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_label.config(text="Bot running... Switch to game window!")
    
    def _run_bot(self):
        self.controller.run()
        self.root.after(0, self._bot_stopped)
    
    def _bot_stopped(self):
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Stopped")
        self.stats_label.config(
            text=f"Jumps: {self.controller.jump_count} | "
                 f"Ducks: {self.controller.duck_count}"
        )
    
    def stop_bot(self):
        """Stop the bot."""
        self.controller.stop()
        self.status_label.config(text="Stopping...")

def main():
    root = tk.Tk()
    app = DinoGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()