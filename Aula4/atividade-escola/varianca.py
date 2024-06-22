import statistics   
from dados import ensino_fundamental
from dados import ensino_medio


variancia_fund = statistics.variance(ensino_fundamental)
print(f"Variança Ensino Fundamental: {variancia_fund:.2f}")


variancia_med = statistics.variance(ensino_medio)
print(f"Variança Ensino Médio: {variancia_med:.2f}")

