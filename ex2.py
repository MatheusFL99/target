def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número: "))

i = 0
while fibonacci(i) <= num:
    if fibonacci(i) == num:
        print(f"O número {num} pertence à sequência de Fibonacci.")
        break
    i += 1
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
