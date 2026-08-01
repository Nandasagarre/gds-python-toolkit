import pya

def get_layers(layout: pya.Layout) -> List[dict]:
    """Return basic layout information."""

    layer = []

    for layer_info in layout.layer_infos():
        layer.append(
            {
                "layer": layer_info.layer,
                "datatype": layer_info.datatype,
                "name": layer_info.name,
            }
        )
    return layer