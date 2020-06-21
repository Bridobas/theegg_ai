#Tarea 21 Joseba Andreu

#Dato de entrada
inputNum = 0.9931

#Función que calcula pasándole el denominador si existe un numerador de menor valor que haga que la división
# entre ambos sea el número de entrada
def calcModulus(i) : 
    retCont = [False, 0]
    for j in range(1,i):        
        if j / i == inputNum: 
            retCont = [True, j] 
            break
    return retCont

#Comprueba que el número de entrada no tiene más de 4 decimales o si no está entre 0 y 1
if str(inputNum)[::-1].find('.') > 4 or inputNum <= 0 or inputNum >= 1:
    print("Número de entrada incorrecto.")
else:
    for i in range(1, 10001):
        ret = calcModulus(i) #Llamada a la función de cálculo      
        if ret[0] is True :
            print ("Resultado: " + str(ret[1]) + "/" + str(i))
            break
        if i == 10000 and ret[0] is False:
            print ("Resultado no encontrado.")

        


    



