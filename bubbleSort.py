# 1. Comparaciones de elementos subyacentes
# 2. Repetir hasta tener una pasada completa sin ningun Suap
# 3. (opcional) Contar cuantos bucles o recorridos utilizamos
cambios = 0

def bubbleSort(array, ):
    n = len(array)
    for i in range(n):
        #Declaramos los cambios en False para iniciar
        changes = False
        #Imprimimos el array con los cambios 
        print(array)

        for j in range(0, n-i-1):

            if array[j] > array[j + 1]:
                #Cambiamos los valores de lugar
                array[j], array[j + 1] = array[j + 1], array[j]
                #Asignamos cambios a True para decir que si se generaron cambios
                changes = True
            else:
                #Asignamos cambios a False rompiendo el bucle diciendo que no hay mas cambios por hacer
                changes = False
        
        #Si al volver a hacer el bucle se detecta que no hubieron cambios, se rompe el ciclo 
        if changes == False:

            break




def main():
    array = [190, 200, 1, 2, 5, 55, 1000, 6, -80, 55]

    bubbleSort(array)
    for i in range(len(array)):
        print("%d"%array[i]),


if __name__ == "__main__":
    main()