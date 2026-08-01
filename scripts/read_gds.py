from src.gdstool.io import load_layout

layout = load_layout("data/input/inv.gds")
print("Layout loaded successfully!")
print(f"Top cell name: {layout.top_cell().name}")
