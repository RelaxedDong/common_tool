from math import sin, cos, pow, pi, asin, sqrt


EARTH_REDIUS = 6378.137


def rad(d):
    return float(d) * pi / 180.0


def getDistance(lat1, lng1, lat2, lng2):
    rad_lat1 = rad(lat1)
    rad_lat2 = rad(lat2)
    a = rad_lat1 - rad_lat2
    b = rad(lng1) - rad(lng2)
    s = 2 * asin(sqrt(pow(sin(a / 2), 2) + cos(rad_lat1) * cos(rad_lat2) * pow(sin(b / 2), 2)))
    s = s * EARTH_REDIUS
    if s < 1:
        return "%s m" % int(s * 1000)
    return "%skm" % round(s, 1)
