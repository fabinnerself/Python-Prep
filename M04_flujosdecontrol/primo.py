def es_primo(num):
  """Determina si un número es primo.

  Args:
    num: El número a evaluar.

  Returns:
    True si el número es primo, False si no lo es.
  """

  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def encontrar_siguiente_primo(num):
  """Encuentra el siguiente número primo a partir de un número dado.

  Args:
    num: El número a partir del cual se buscará el siguiente primo.

  Returns:
    El siguiente número primo.
  """

  while True:
    num += 1
    if es_primo(num):
      return num

while True:
  try:
    num = int(input("Ingrese un número entero positivo (o 0 para salir): "))
    if num == 0:
      break
    if es_primo(num):
      print(num, "es un número primo.")
    else:
      print(num, "no es un número primo.")
      siguiente_primo = encontrar_siguiente_primo(num)
      print("El siguiente número primo es:", siguiente_primo)
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")