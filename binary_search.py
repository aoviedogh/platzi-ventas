import random

def busqueda_binaria(data, num_buscar, i_inicial, i_final):
  if (i_inicial > i_final):
    return False
  
  mitad = (i_inicial + i_final) // 2

  if (num_buscar == data[mitad]):
    return True
  elif (num_buscar < data[mitad]):
    return busqueda_binaria(data, num_buscar, i_inicial, mitad - 1)
  else:
    return busqueda_binaria(data, num_buscar, mitad + 1, i_final)

def busqueda_binaria_while(data, num_buscar, i_inicial, i_final):
  while (i_inicial <= i_final):
    mitad = (i_inicial + i_final) // 2

    if (num_buscar == data[mitad]):
      return True
    elif (num_buscar < data[mitad]):
      i_final = mitad - 1
    else:
      i_inicial = mitad + 1

if __name__ == "__main__":
  data = [random.randint(0, 100) for numero in range(10)]
  data.sort()
  print(data)

  num_buscar = int(input("Número a buscar: "))
  encontro = busqueda_binaria_while(data, num_buscar, 0, len(data) - 1)

  if (encontro):
    print("Número {} encontrado".format(num_buscar))
  else:
    print("Número {} no encontrado".format(num_buscar))