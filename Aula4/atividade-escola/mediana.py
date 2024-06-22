import statistics   
from dados import ensino_fundamental
from dados import ensino_medio

def mediana_fund():
    mediana_fund = statistics.mean(ensino_fundamental)
    print ("Mediana Ensino Fundamental:" , mediana_fund)

def mediana_med():
    mediana_med = statistics.mean(ensino_medio)
    print ("Mediana Ensino Médio:" , mediana_med)

mediana_fund()
mediana_med()