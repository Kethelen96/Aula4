import statistics   
from dados import ensino_fundamental
from dados import ensino_medio

def media_fund():
    media_fund = statistics.median(ensino_fundamental)
    print("Média Ensino Fundamental: ", media_fund)

def media_med():
    media_med = statistics.median(ensino_medio)
    print("Média Ensino Médio: ", media_med)

media_fund()
media_med()