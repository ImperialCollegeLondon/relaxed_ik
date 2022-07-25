from typing import Tuple

CYLINDER_SHAPES = {
       # radius factor, length
    0: (1.5, 0.27),
    1: (1.5, 0.33),
    2: (1.1, 0.74),
    3: (1.5, 0.68),
    4: (1.5, 0.26),
    5: (1.5, 0.22),
    6: (1.5, 0.17),
    7: (1.5, 0.15),
}

def adapt_cylinder_shapes_to_amiga(link_id: int) -> Tuple[float, float]:
    return CYLINDER_SHAPES[link_id]

def fix_tansforms_amiga():
    pass