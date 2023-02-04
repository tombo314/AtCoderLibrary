def three_coords_one_line(x1, y1, x2, y2, x3, y3):
    """ 三点が同一直線上にあるか判定 O(1) """
    if (y2-y1)*(x3-x1)==(y3-y1)*(x2-x1):
        return True
    return False
