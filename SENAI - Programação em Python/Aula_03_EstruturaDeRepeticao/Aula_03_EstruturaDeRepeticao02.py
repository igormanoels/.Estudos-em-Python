import os 
os.system('cls')

c = 1
total = 0

while c <= 10:
    num = int(input(f"Informe o {c}º número: "))
    if num % 2 == 0:
        total += num
    c += 1

print(f"\nA soma dos números pares é {total}")
