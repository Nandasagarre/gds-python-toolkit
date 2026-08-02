import pya


def list_cells(layout: pya.Layout):
    for cell in layout.each_cell():
        print(f"\nCell: {cell.name}")

        for inst in cell.each_inst():
            print(f"  -> {inst.cell.name}")

import pya


def count_shapes_recursive(cell: pya.Cell, layer_index: int) -> int:
    """Count shapes in a cell and all its children."""

    count = 0

    # Shapes in this cell
    for _ in cell.shapes(layer_index):
        count += 1

    # Shapes in child cells
    for inst in cell.each_inst():
        count += count_shapes_recursive(inst.cell, layer_index)

    return count