import abc


def divisors(num):
    divisors = []
    for i in range(1, num + 1 ):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run ():
    try:
        num = int(input("ingrese un numero: "))
        if num < 0:
            raise ValueError
            
        print (divisors(num))
        print("termino")
    except ValueError: 
      print ("debes ingresar un numero positivo")
    

if __name__=="__main__":
    run()