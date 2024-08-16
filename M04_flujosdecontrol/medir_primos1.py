import time

def calcular_tiempo_ejecucion(funcion, *args, **kwargs):
    start_time = time.time()
    resultado = funcion(*args, **kwargs)
    end_time = time.time()
    return resultado, end_time - start_time
 
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
 

 

resultado, tiempo_ejecucion = calcular_tiempo_ejecucion(es_primo, 10000)
print("Tiempo de ejecución:", tiempo_ejecucion, "segundos")