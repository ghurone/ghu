import math


def p_norm(media:float, desv_pad:float, a:float=-math.inf, b:float=math.inf) -> float:
    return (math.erf((media-a)/(math.sqrt(2)*desv_pad)) - math.erf((media-b)/(math.sqrt(2)*desv_pad))) / 2

