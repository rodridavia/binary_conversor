""" 
    File with all the functions that store the 
    logic and the algorithms for the program.

    @author: rodrids

 """

def decimalToBinary(dec):
    coeficiente = dec / 2
    resto = dec % 2
    num_convertido = []
    num_convertido.append(resto)

    while coeficiente >= 1 :
        resto = int(coeficiente) % 2
        num_convertido.append(resto)
        
        coeficiente = int(coeficiente) / 2

    num_convertido.reverse()
    num_str = [str(x) for x in num_convertido]

    resultado = "".join(num_str)

    return resultado

def binaryToDecimal(bin):
    num_conver = [int(x) for x in bin]
    num_conver.reverse()
    num_lista = []

    for pos, value in enumerate(num_conver):
        op = value * (pow(2,pos))
        num_lista.append(op)
                        
    def sum_result(myList):
        result = 0
        for x in myList:
            result = result + x
        return result

    final = sum_result(num_lista)
    return final

def decimalToOctal(dec):
    coeficiente = dec / 8
    resto = dec % 8
    num_convertido = []
    num_convertido.append(resto)

    while coeficiente >= 1 :
        resto = int(coeficiente) % 8
        num_convertido.append(resto)
                
        coeficiente = int(coeficiente) / 8

    num_convertido.reverse()
    num_str = [str(x) for x in num_convertido]

    resultado = "".join(num_str)

    return resultado

def octalToDecimal(oct):
    num_conver = [int(x) for x in oct]
    num_conver.reverse()
            
    num_lista = []
            
    for pos, value in enumerate(num_conver):
        op = value * (pow(8,pos))
        num_lista.append(op)
                
    def sum_result(myList):
        result = 0
        for x in myList:
            result = result + x
        return result

    final = sum_result(num_lista)

    return final

def decimalToHexadecimal(dec):
    coeficiente = num_conversor / 16
    resto = num_conversor % 16
    num_convertido = []
    num_convertido.append(resto)

    while coeficiente >= 1 :
        resto = int(coeficiente) % 16
        num_convertido.append(resto)
                
        coeficiente = int(coeficiente) / 16
            
    num_convertido.reverse()
    num_str = [str(x) for x in num_convertido]
            
    for index, value in enumerate(num_str):
        if value == "10":
            num_str[index] = "A"
        if value == "11":
            num_str[index] = "B"
        if value == "12":
            num_str[index] = "C"
        if value == "13":
            num_str[index] = "D"
        if value == "14":
            num_str[index] = "E"
        if value == "15":
            num_str[index] = "F"
        
    resultado = "".join(num_str)
    
    return resultado

def hexadecimalToDecimal(hex):
    num_str = [str(x) for x in hex]
    for index, value in enumerate(hex):
        if value =="A":
            hex[index] = 10
        if value =="B":
            hex[index] = 11
        if value =="C":
            hex[index] = 12
        if value =="D":
             hex[index] = 13
        if value =="E":
            hex[index] = 14
        if value =="F":
            hex[index] = 15
            
    num_conver = [int(x) for x in hex]  
    num_conver.reverse()
            
    num_lista = []
            
    for pos, value in enumerate(num_conver):
        op = value * (pow(16,pos))
        num_lista.append(op)
            
    def sum_result(myList):
        result = 0
        for x in myList:
            result = result + x
        return result

    final = sum_result(num_lista)
    
    return final
