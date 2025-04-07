import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from dotenv import load_dotenv

# Load environment if needed
load_dotenv()

# You can customize this Photoshop path
PHOTOSHOP_PATH = r"C:\Program Files\Adobe\Adobe Photoshop 2024\Photoshop.exe"
JSX_SCRIPT = "scripts/insert_design.jsx"

def select_file(title, filetypes):
    return filedialog.askopenfilename(title=title, filetypes=filetypes)

def run_photoshop(svg_path, mockup_path, output_path):
    # Set environment variables to pass to Photoshop
    os.environ["SVG_DESIGN"] = os.path.abspath(svg_path)
    os.environ["MOCKUP_FILE"] = os.path.abspath(mockup_path)
    os.environ["OUTPUT_FILE"] = os.path.abspath(output_path)

    command = f'"{PHOTOSHOP_PATH}" -r "{JSX_SCRIPT}"'
    subprocess.run(command, shell=True)

class MockupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Jersey Mockup Generator")

        # File selections
        self.svg_path = tk.StringVar()
        self.mockup_path = tk.StringVar()
        self.output_path = tk.StringVar()

        # Layout
        self.build_gui()

    def build_gui(self):
        tk.Label(self.root, text="1. Select SVG Design:").pack()
        tk.Entry(self.root, textvariable=self.svg_path, width=60).pack(padx=5)
        tk.Button(self.root, text="Browse", command=self.select_svg).pack()

        tk.Label(self.root, text="2. Select 3D Mockup PSD/TIF:").pack()
        tk.Entry(self.root, textvariable=self.mockup_path, width=60).pack(padx=5)
        tk.Button(self.root, text="Browse", command=self.select_mockup).pack()

        tk.Label(self.root, text="3. Output Preview Path:").pack()
        tk.Entry(self.root, textvariable=self.output_path, width=60).pack(padx=5)
        tk.Button(self.root, text="Save As...", command=self.select_output).pack()

        tk.Button(self.root, text="🎯 Generate 3D Preview", command=self.generate_mockup, bg="green", fg="white", padx=10, pady=5).pack(pady=10)

    def select_svg(self):
        file = select_file("Select SVG Design", [("SVG files", "*.svg")])
        if file:
            self.svg_path.set(file)

    def select_mockup(self):
        file = select_file("Select Mockup PSD/TIF", [("Photoshop files", "*.psd *.tif")])
        if file:
            self.mockup_path.set(file)

    def select_output(self):
        file = filedialog.asksaveasfilename(title="Save Output", defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if file:
            self.output_path.set(file)

    def generate_mockup(self):
        if not all([self.svg_path.get(), self.mockup_path.get(), self.output_path.get()]):
            messagebox.showwarning("Missing Info", "Please select all files.")
            return

        try:
            run_photoshop(self.svg_path.get(), self.mockup_path.get(), self.output_path.get())
            messagebox.showinfo("Done!", "✅ 3D Preview generated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MockupApp(root)
    root.mainloop()