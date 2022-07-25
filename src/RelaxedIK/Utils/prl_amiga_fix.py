from typing import Tuple
import copy

CYLINDER_SHAPES = {
       # radius factor, urdf length * adjustment factor
    0: (1.5, 0.038 * 5),  # base
    1: (1.5, 0.178 * 1.2),  # shoulder
    2: (1.5, 0.613 * 1.3),  # upper arm
    3: (1.4, 0.571 * 1.2),  # forearm
    4: (1.4, 0.12  * 1.4),  # wrist 1
    5: (1.4, 0.12  * 1.4),  # wrist 2
    6: (0.9, 0.05  * 1.4),  # wrist 3
    7: (1.5, 0.15),  # ?
}

def adapt_cylinder_shapes_to_amiga(link_id: int) -> Tuple[float, float]:
    return CYLINDER_SHAPES[link_id]

def fix_tansforms_amiga(ptA, ptB, link_id, all_frames):
    ptA, ptB = copy.deepcopy(ptA), copy.deepcopy(ptB)

    # Fix elbow offset defined in ur10e urdf
    if link_id == 2:
        rot = all_frames[0][1][3]
        ptB = ptB + rot.dot([0, 0.137 ,0])

    if link_id == 6:
        rot = all_frames[0][1][7]
        ptB = ptB + rot.dot([-0.117, 0.117 ,0])

    return ptA, ptB