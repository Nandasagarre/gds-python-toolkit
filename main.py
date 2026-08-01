from pathlib import Path

from src.gdstool.io import load_layout
from src.gdstool.layout import get_layout_info
from src.gdstool.layers import get_layers


def main():

    gds_path = Path("data/input/inv.gds")

    layout = load_layout(gds_path)

    info = get_layout_info(layout)

    print("\nLayout Information")
    print("------------------")

    for key, value in info.items():
        print(f"{key:12}: {value}")
    
    layers = get_layers(layout)

    print("\nLayers")
    print("------")

    for layer in layers:
        print(
            f"Layer {layer['layer']}/{layer['datatype']}"
            + (f" ({layer['name']})" if layer["name"] else "")
    )


if __name__ == "__main__":
    main()