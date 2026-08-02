import pya


def create_layer(layout: pya.Layout, layer: int, datatype: int = 0):
    """Create a layer if it does not already exist."""
    return layout.layer(layer, datatype)


def insert_box(
    cell: pya.Cell,
    layer_index: int,
    left: int,
    bottom: int,
    right: int,
    top: int,
):
    """Insert a rectangular box."""
    box = pya.Box(left, bottom, right, top)
    cell.shapes(layer_index).insert(box)


def move_cell(cell: pya.Cell, dx: int, dy: int):
    """Move every shape in a cell."""

    trans = pya.Trans(dx, dy)

    for layer_index in cell.layout().layer_indexes():
        cell.shapes(layer_index).transform(trans)


def delete_layer_shapes(cell: pya.Cell, layer_index: int):
    """Delete every shape on a layer."""

    cell.shapes(layer_index).clear()


def copy_cell(layout: pya.Layout, source: str, new_name: str):
    """Duplicate a cell."""

    src = layout.cell(source)

    if src is None:
        raise ValueError(f"Cell '{source}' not found.")

    new_cell = layout.create_cell(new_name)
    new_cell.copy_tree(src)

    return new_cell