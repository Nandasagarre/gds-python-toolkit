from pathlib import Path

from src.gdstool.io import load_layout

layout = load_layout(Path("data/input/inv.gds"))

print(type(layout))
print()

for name in dir(layout):
    if not name.startswith("_"):
        print(name)