from pathlib import Path

from src.gdstool.io import load_layout

layout = load_layout(Path("data/input/inv.gds"))

cell = layout.top_cell()

print(type(cell))
print()

for name in dir(cell):
    if not name.startswith("_"):
        print(name)