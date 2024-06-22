import statistics   
from dados import ensino_fundamental
from dados import ensino_medio

def moda_fund():
    moda_fund = statistics.mode(ensino_fundamental)
    print ("Moda Ensino Fundamental:" , moda_fund)

def moda_med():
    moda_med = statistics.mode(ensino_medio)
    print ("Moda Ensino Fundamental:" , moda_med)

moda_fund()
moda_med()