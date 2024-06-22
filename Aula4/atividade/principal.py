from amplitude import amplitude
from desvio import desvio_padrao
from media import media
from mediana import mediana
from moda import moda
from variancia import variancia

from matplotlib import pyplot as plt


portugues = [10,9,7,6]
portugues.sort()
matematica = [1,4,5,6]
matematica.sort()
quimica = [6,7,8,6]
quimica.sort()
filosofia = [8,9,7,6]
filosofia.sort()

turma = ["Ensino Médio A", "Ensino Médio B", "Ensino Médio C", "Ensino Médio D"]

def substituir (lista, notas):
    print ("Mostrar notas")
    amplitude(lista)
    desvio_padrao(lista)
    media(lista)
    mediana(lista)
    moda(lista)
    variancia(lista)

substituir(portugues, portugues)
substituir(matematica, matematica)
substituir(quimica, quimica)
substituir(filosofia, filosofia)

plt.plot(turma, portugues)
plt.plot(turma, matematica)
plt.plot(turma, quimica)
plt.plot(turma, filosofia)

plt.title("Turmas e Notas")
plt.grid(True)
plt.show()

