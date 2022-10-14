
from typing import List
from collections import Counter

def moda(x: List[float]) -> List[float]:
  counts = Counter(x)
  max_count = max(counts.values())
  return [x_i for x_i, count in counts.items()
    if count == max_count]

def amplitude(xs: List[float]) -> float:
  return max(xs) - min(xs)


def media(xs: List[float]) -> float:
  return sum(xs) / len(xs)

def _med_impar(xs: List[float]) -> float:
  return sorted(xs)[len(xs) // 2]

def _med_par(xs: List[float]) -> float:
  sorted_xs = sorted(xs)
  meio_hi = len(xs) // 2
  return (sorted_xs[meio_hi-1] + sorted_xs[meio_hi]) / 2


def mediana(v: List[float]) ->float:
  return _med_par(v) if len(v) % 2 == 0 else _med_impar(v)

soma = 0 
contador = 0
lista = []
linha = input()

while(linha != ""):
  separado = linha.split("time=")

  if(len(separado)>1):
    tempo = separado[1]
    tempo = tempo.replace(" ms", "")
    soma = soma + float(tempo)
    lista.append(float(tempo))
    contador = contador + 1
  
  linha = input()

print("{:.2f}".format(soma/contador))

print(moda(lista))
print(media(lista))
print(amplitude(lista))


print(mediana(lista))
print(_med_par(lista))
print(_med_impar(lista))


