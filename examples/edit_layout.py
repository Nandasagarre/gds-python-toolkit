from pathlib import Path

from src.gdstool.io import load_layout
from src.gdstool.edit import (
    create_layer,
    insert_box,
    copy_cell,
)
from src.gdstool.writer import write_layout


layout = load_layout("data/input/inv.gds")

top = layout.top_cell()

layer = create_layer(layout, 100, 0)

insert_box(
    top,
    layer,
    -1000,
    -1000,
    -500,
    -500,
)

copy_cell(layout, top.name, "inv_copy")

write_layout(layout, Path("data/output/inv_edit.gds"))

print("Edited GDS written.")