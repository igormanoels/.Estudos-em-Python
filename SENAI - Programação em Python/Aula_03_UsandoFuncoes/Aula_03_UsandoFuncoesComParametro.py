import os 
os.system('cls')

def seqFibonnaci(n):
    if (n <= 1):
        return [0]*n
    else:
        fibs = [0,1]
        for i in range(2,n):
            fibs.append(fibs[i-1]+fibs[i-2])
        return fibs
        
valor = int(input("Digite um número: "))
num = seqFibonnaci(valor)
print(num)