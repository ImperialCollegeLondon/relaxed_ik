from typing import Tuple
import copy

CYLINDER_SHAPES = {
       # radius factor, urdf length * adjustment factor
    0: (1.6, 0.038 * 5),  # base
    1: (1.5, 0.178 * 1.2),  # shoulder
    2: (1.5, 0.613 * 1.3),  # upper arm
    3: (1.3, 0.571 * 1.1),  # forearm
    4: (1.3, 0.12  * 1.4),  # wrist 1
    5: (1.3, 0.12  * 1.4),  # wrist 2
    6: (0.9, 0.05  * 1.7),  # wrist 3
    7: (1.5, 0.28),  # ?
}

def adapt_cylinder_shapes_to_amiga(link_id: int) -> Tuple[float, float]:
    return CYLINDER_SHAPES[link_id]

def fix_tansforms_amiga(ptA, ptB, link_id, all_frames):
    ptA, ptB = copy.deepcopy(ptA), copy.deepcopy(ptB)
    # link67_offset = [-0.13, -0.1, -0.13]

    # Fix elbow offset defined in ur10e urdf
    if link_id == 2:
        rot = all_frames[0][1][3]
        ptB = ptB + rot.dot([0, 0.137 ,0])

    # elif link_id == 6:
    #     rot = all_frames[0][1][7]
    #     ptB = ptB + rot.dot(link67_offset)

    # elif link_id == 7:
    #     rot = all_frames[0][1][7]
    #     ptA = ptA + rot.dot(link67_offset)
        
    #     rot = all_frames[0][1][8]
    #     ptB = ptB + rot.dot([-0.22, 0.23, -0.23])

    return ptA, ptB