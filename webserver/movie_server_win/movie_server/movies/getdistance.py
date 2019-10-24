import math
import numbers

def get_euclidean_distance(x1, y1, x2, y2, round_decimal_digits=6):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return None
    
    dlong = abs(x2-x1)
    if dlong >= 180:
        dlong -= 360
    dlat = y2 - y1

    distance = round(math.sqrt(pow(dlong, 2)+pow(dlat, 2)), round_decimal_digits)
    distance_meter = int(distance * (10 ** 5))
    return distance_meter