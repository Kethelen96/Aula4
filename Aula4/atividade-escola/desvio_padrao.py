import statistics   
from dados import ensino_fundamental
from dados import ensino_medio

def desvio_padrao_fund():
    desvio = statistics.stdev(ensino_fundamental)
    print("Desvio Padrão Ensino Fundamental: ", desvio)

def desvio_padrao_med():
    desvio = statistics.stdev(ensino_medio)
    print("Desvio Padrão Ensino Médio: ", desvio)

desvio_padrao_fund()
desvio_padrao_med()
