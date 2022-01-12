import function as f

def main():
    palindromos = ["ana","pepe","otto","carmen","reconocer","granaino","orejero","hugo","javi","leila"]
    print(palindromos)
    palin=f.es_palindromo(palindromos)
    print(list(palin))
    impares=[1,22,34,43,55,6,123,8,90,120]
    print(impares)
    impares=f.impares_de(impares)
    print(list(impares))
    n=12
    cuadrados_sumados=f.cuadrados_sumados(n)
    print("el cuadrado sumado de {num} es {cuadrado}".format(num=n,cuadrado=cuadrados_sumados))
    n=10
    fact=f.factorial(n)
    print("el factorial sumado de {num} es {fact}".format(num=n,fact=fact))
    n=12
    primo=f.es_primo(n)
    print("Es {primo} que el numero {num} es primo".format(num=n,primo=primo))

if __name__ == '__main__':
    main()