menu ="""
Escoja una opción:
    1)Metodo de Regula Falsi.
    2)Metodo de la Secante.
    3)Salir
Solo utilice los numeros correspondientes a las opciones.
: """

print("Conversor de diferentes bases")

while True:
    opcion=input(menu)

    if opcion=="1":
        while True:
            
            #funcion
            def f(x):
                return x**3-5*x-9

            #Regula falsi
            def regulafalsi(x0,x1,e):
                step = 1
                condicion = True
                while condicion:
                    x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
                    print('Iteraciones %d, x = %0.6f  f(x) = %0.6f' % (step, x2, f(x2)))

                    if f(x0) * f(x2) < 0:
                        x1 = x2
                    else:
                        x0 = x2

                    step = step + 1
                    condicion = abs(f(x2)) > e

                print('\nSolucion encontrada x= %0.8f \n' % x2)


            #Valores de entrada
            x0 = input('Primera suposicion: ')
            x1 = input('Segunda suposicion: ')
            e = input('Tolerancia: ')

            #Conversion de int a float
            x0 = float(x0)
            x1 = float(x1)
            e = float(e)
            


            # verificar si el intevalo escogido no funciona
            if f(x0) * f(x1) > 0.0:
                print('El intervalo no funciona.')
                print('Pruebe con un valor diferente.')
            else:
                regulafalsi(x0,x1,e)

            

            continuar = input("Desea continuar? S / N :")

            if continuar.lower() in "s si y yes":
                continue

            else:
                break

    elif opcion=="2":
        while True:
            
            #funcion
            def f(x):
                return x**3 - 2*x - 5

            #Secante

            def secante(x0,x1,e,N):
                iteracion = 1
                condicion = True
                while condicion:
                    if f(x0) == f(x1):
                        print('Division entre 0 no es permitido')
                        break
                    
                    x2 = x0 - (x1-x0)*f(x0)/( f(x1) - f(x0) ) 
                    print('Iteracion %d, x = %0.6f f(x) = %0.6f' % (iteracion, x2, f(x2)))
                    x0 = x1
                    x1 = x2
                    iteracion = iteracion + 1
                    
                    if iteracion > N:
                        print('No convergencia')
                        break
                    
                    condicion = abs(f(x2)) > e
                print('\nLa raiz requerida es = %0.8f \n' % x2)


            #Valores de entrada
            x0 = input('Primera suposición: ')
            x1 = input('Segunda suposición: ')
            e = input('Tolerancia: ')
            N = input('Maximo de iteraciones: ')

            #Conversion de int a float
            x0 = float(x0)
            x1 = float(x1)
            e = float(e)

            #N a int
            N = int(N)


            #Se inicia el metodo
            secante(x0,x1,e,N)

            continuar = input("Desea continuar? S / N :")

            if continuar.lower() in "s si y yes":
                continue

            else:
                break

    elif opcion == "3":
        print("\nChao que te vi")
        break

    else:
        print("Ha escogido una opcion invalida, intentelo de nuevo.")