'''
A série de Fibonacci é uma sequência de números na qual 
cada número é a soma dos dois anteriores. A sequência começa geralmente com os números 
0 e 1, e os próximos números são calculados a partir daí. Por exemplo, a sequência de Fibonacci 
começa assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Um algoritmo para gerar a série de Fibonacci até um determinado número de elementos seria 
o seguinte:
'''

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
  print(fibonacci(i))

'''
Este algoritmo imprime os primeiros 10 elementos da série de Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 
21, 34.

Se você quiser um algoritmo mais avançado, posso tentar adaptar este algoritmo para utilizar 
uma abordagem iterativa em vez de recursiva, o que pode ser mais eficiente para gerar a série 
até um número maior de elementos. Isso também pode ser útil se você precisar gerar a série de 
Fibonacci para um número muito grande de elementos.
'''