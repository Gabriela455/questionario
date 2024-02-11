def fibonacci(n):
 
  fib = [0, 1]
  while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])
  return fib

def main():
 
  while True:
    # Entrada do usuário
    entrada = input("Digite um número para verificar se pertence à sequência de Fibonacci (ou 'end' para encerrar): ")

    # Verificação de 'sair'
    if entrada.lower() == "sair":
      print("Programa encerrado.")
      break

    if not entrada.isdigit():
      print("Entrada inválida. Por favor, insira apenas números inteiros positivos.")
      continue

    numero = int(entrada)

    fib_seq = fibonacci(numero)

    if numero in fib_seq:
      print(f"O número {numero} pertence à sequência de Fibonacci!")
    else:
      print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
  main()