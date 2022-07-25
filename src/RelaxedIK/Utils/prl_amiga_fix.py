from typing import Tuple
import copy

CYLINDER_SHAPES = {
       # radius factor, length
    0: (1.5, 0.29),
    1: (1.5, 0.30),
    2: (1.1, 0.74),
    3: (1,   0.68),
    4: (1,   0.26),
    5: (1,   0.22),
    6: (1,   0.17),
    7: (1,   0.15),
}

def adapt_cylinder_shapes_to_amiga(link_id: int) -> Tuple[float, float]:
    return CYLINDER_SHAPES[link_id]

def fix_tansforms_amiga(ptA, ptB, link_id, all_frames):
    ptA, ptB = copy.deepcopy(ptA), copy.deepcopy(ptB)
    if link_id == 0:
        ptA = [0.0, 0.0, 0.3]
        
        pt = all_frames[0][0][0]
        rot = all_frames[0][2][1]
        ptB = pt + rot.dot([0, 0, -1.5705])
    elif link_id == 1:
        # pt = all_frames[0][0][0]
        # rot = all_frames[0][2][1]
        # ptA = pt + rot.dot([0.0,-0.13585, 0.0])
        
        # pt = all_frames[0][0][1]
        # rot = all_frames[0][2][2]
        # ptB = pt + rot.dot([-0.425,0, 0.13585])
        pass

    elif link_id == 2:
        # pt = all_frames[0][0][1]
        # rot = all_frames[0][2][2]
        # ptA = pt + rot.dot([-0.425,0, 0.015])

        # pt = all_frames[0][0][2]
        # rot = all_frames[0][2][3]
        # ptB = pt + rot.dot([-0.39225, 0.0, 0.10915-0.093])
        pass

    elif link_id == 3:
        # pt = all_frames[0][0][2]
        # rot = all_frames[0][2][3]
        # ptA = pt + rot.dot([-0.39225, 0.0, 0.10915])
        pass

    elif link_id == 4:
        # pt = all_frames[0][0][4]
        # rot = all_frames[0][2][5]
        # ptB = pt + rot.dot([0.0, 0.0823 + 0.02, -1.68800121668e-11])
        pass

    elif link_id == 5:
        # pt = all_frames[0][0][4]
        # rot = all_frames[0][2][5]
        # ptA = pt + rot.dot([0.0, 0.0823 + 0.065, -1.68800121668e-11])
        
        # pt = all_frames[0][0][5]
        # rot = all_frames[0][2][6]
        # ptB = pt + rot.dot([0.0, 0.0, 0.23])
        pass

    elif link_id == 6:
        # pt = all_frames[0][0][4]
        # rot = all_frames[0][2][5]
        # ptA = pt + rot.dot([0.0, 0.0823 + 0.065, -1.68800121668e-11])
        
        # pt = all_frames[0][0][5]
        # rot = all_frames[0][2][6]
        # ptB = pt + rot.dot([0.0, 0.0, 0.23])
        pass

    elif link_id == 7:
        # pt = all_frames[0][0][4]
        # rot = all_frames[0][2][5]
        # ptA = pt + rot.dot([0.0, 0.0823 + 0.065, -1.68800121668e-11])
        
        # pt = all_frames[0][0][5]
        # rot = all_frames[0][2][6]
        # ptB = pt + rot.dot([0.0, 0.0, 0.23])
        pass

    return ptA, ptB