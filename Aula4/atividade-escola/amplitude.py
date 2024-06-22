import statistics
from dados import ensino_fundamental
from dados import ensino_medio

def amplitude_fund():
    amplitude_fund = max(ensino_fundamental) - min(ensino_fundamental)
    print("Amplitude Ensino Fundamental:" , amplitude_fund)


def amplitude_med():
    amplitude_med = max(ensino_medio) - min(ensino_medio)
    print("Amplitude Ensino Médio:" , amplitude_med)

amplitude_fund()
amplitude_med()