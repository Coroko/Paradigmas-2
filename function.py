from functools import reduce
def es_palindromo(list):    
    true_palindromo=map(lambda x:True if x[::-1]==x else False, list)
    return(true_palindromo)        
    
def impares_de(list):
    vector_impares = filter(lambda x: x%2==0,list)
    return(vector_impares)

def cuadrados_sumados(n):
    suma_cuadrados=reduce(lambda acc,suma:acc+pow(suma,2),range(1,n+1))
    return(suma_cuadrados)

def factorial(n):
    fact_num = reduce(lambda acc,suma:acc*suma,range(1,n+1))
    return(fact_num)

def es_primo(n):
    num=n/2
    primo= filter(lambda x: n % x ==0 ,range(1,int(num)+1))
    print(len(list(primo)))
    if len(list(primo))==1:
        return(True)
    else:
        return(False)
