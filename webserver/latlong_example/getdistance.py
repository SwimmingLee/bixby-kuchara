from math import sin, cos, pi, sqrt, atan2
import numbers

def degree2radius(degree):
    return degree * (pi / 180)

def get_harversion_distance(x1, y1, x2, y2, round_decimal_digits=6):
    R = 6371
    dlong = degree2radius(x2-x1)
    dlat = degree2radius(y2-y1)

    a = sin(dlat/2) ** 2 + \
        cos(degree2radius(y1)) * cos(degree2radius(y2)) * \
        sin(dlong/2) ** 2
    b = 2 * atan2(sqrt(a), sqrt(1-a))

    return round(R*b, round_decimal_digits)

def get_euclidean_distance(x1, y1, x2, y2, round_decimal_digits=6):
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return None
    
    dlong = abs(x2-x1)
    if dlong >= 180:
        dlong -= 360
    dlat = y2 - y1

    return round(sqrt(pow(dlong, 2)+pow(dlat, 2)), round_decimal_digits)


x1 = 126.910008
x2 = 126.915780

y1 = 37.499989
y2 = 37.499955

ans1 = get_harversion_distance(x1, y1, x2, y2)

ans2 = get_euclidean_distance(x1, y1, x2, y2)

print('{} , {}'.format(ans1, ans2))