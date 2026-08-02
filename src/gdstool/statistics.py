from collections import defaultdict


def layer_statistics(shapes: list[dict]) -> dict:
    """Generate statistics for each layer."""

    stats = defaultdict(int)

    for shape in shapes:
        key = (shape.layer, shape.datatype)
        stats[key] += 1

    return stats