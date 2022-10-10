import math


def teste_Z(x:float, y:float, sx:float, sy:float) -> float:
    """
        Dado duas medidas e suas respectivas incertezas, calcula
        o critério de compatibiliade.
        se Z <= 1 Compativeis ao nível de 1 \sigma
           1 <= Z <= 2 Compativeis ao nível de 2 \sigma
           2 <= Z <= 3 Compativeis ao nível de 3 \sigma
           Z > 3 Discrepantes.
    """
    
    return abs(x-y) / math.sqrt(math.pow(sx,2) + math.pow(sy,2))

