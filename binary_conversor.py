"""
    File with the "interface" of the program and the
    function calls.

    @author: rodrids
    
"""
from conversions import *
import time

print("#########################################")
print("######   Conversor de Binarios   ######")
print("#########################################")
print("")

while True:
    
    conversiones = {
        1 : "De Decimal a Binario",
        2 : "De Binario a Decimal",
        3 : "De Decimal a Octal",
        4 : "De Octal a Decimal",
        5 : "De Decimal a Hexadecimal",
        6 : "De Hexadecimal a Decimal",
        0 : "Salir"
    }

    print("----------------------------------------")
    for clave in conversiones:
        print(f"{clave} - {conversiones[clave]}")
    
    print("----------------------------------------")
    print("")
    
    conversión = int(input("Que conversión quieres hacer: "))
    
    print("")

    match conversión:
        case 1 :
            print("----------------------------------------")
            num_conversor = int(input("Introduce el número a convertir: "))    
            print("")
            print("               Calculando               ")
            time.sleep(2)
            print("")
            print(f"{num_conversor} es {decimalToBinary(num_conversor)} en binario")
            print("----------------------------------------")
            print("\n")

        case 2 :
            print("----------------------------------------")
            num_conversor = list(input("Introduce el número a convertir: "))
            num_org = "".join(num_conversor)
            print("")
            print("               Calculando               ")
            time.sleep(2)
            print("")
            print(f"El número {num_org} es {binaryToDecimal(num_conversor)} en decimal")
            print("----------------------------------------")
            print("\n")

        case 3 :
            print("----------------------------------------")
            num_conversor = int(input("Introduce el número a convertir: "))
            print("")
            print("               Calculando               ")
            time.sleep(2)
            print("")
            print(f"{num_conversor} es {decimalToOctal(num_conversor)} en octal")
            print("----------------------------------------")
            print("\n")

        case 4 :
            print("----------------------------------------")
            num_conversor = list(input("Introduce el número a convertir: "))
            num_org = "".join(num_conversor)
            print("")
            print("               Calculando               ")
            time.sleep(2)
            print("")
            print(f"El número {num_org} es {octalToDecimal(num_conversor)} en decimal")
            print("----------------------------------------")
            print("\n")

        case 5 :
            print("----------------------------------------")
            num_conversor = int(input("Introduce el número a convertir: "))
            print("")
            print("               Calculando               ")
            time.sleep(2)
            print("")
            print(f"{num_conversor} es {decimalToHexadecimal(num_conversor)} en hexadecimal")
            print("----------------------------------------")
            print("\n")

        case 6 :
            print("----------------------------------------")
            num_conversor = list(input("Introduce el número a convertir: "))
            num_org = "".join(num_conversor)
            print("")
            print("               Calculando               ")
            time.sleep(2)
            print("")
            
            print(f"El número {num_org} es {hexadecimalToDecimal(num_conversor)} en decimal")
            print("----------------------------------------")
            print("\n")
        case 0 :
            print("----------------------------------------")
            print("")           
            print("Espero que te haya servido - Rodrigo Davia")
            print("")
            print("----------------------------------------")

            exit()
