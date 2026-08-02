import pya
from src.gdstool.cells import count_shapes_recursive
from src.gdstool.models import LayerInfo, LayerCount

def get_layers(layout: pya.Layout) -> List[dict]:
    """Return basic layout information."""

    layer = []

    for layer_info in layout.layer_infos():
        layer.append(
            LayerInfo(
                layer=layer_info.layer,
                datatype=layer_info.datatype,
                name=layer_info.name,
            )
        )
    return layer

def count_shapes(layout: pya.Layout) -> list[dict]:
    """Count shapes on each layer in the hierarchy."""

    top = layout.top_cell()
    results = []

    for layer_index in layout.layer_indexes():

        layer_info = layout.get_info(layer_index)

        count = count_shapes_recursive(top, layer_index)

        results.append(
            LayerCount(
                layer=layer_info.layer,
                datatype=layer_info.datatype,
                count=count,
            )
        )

    return results