import os

alumnos = []
notas = []

isActive = True

menu = "1. Ingresa el nombre del alumno\n2. Registrar nota\n3. Busqueda de alumno\n0. Salir\n:>"
menuNotas = ["Parciales", "Quicez", "Trabajos", "Volver al menu principal"]
opMenu = 0

while isActive:
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Ha ocurrido un error al ingresar la opcion")
        os.system("pause")
    else:
        if opMenu == 1:
            rta = "S"
            while rta in ["S", "s"]:
                codigo = int(input("Ingresa el codigo del estudiante: "))
                nombre = str(input("Ingresa el nombre del estudiante: "))
                edad = int(input(f"Ingresa el edad de {nombre}: "))

                alumno = [codigo, nombre, edad, [],[],[]]
                alumnos.append(alumno)

                os.system("pause")
                rta = input("Desea ingresar otro alumno? (S o N): ")

        elif opMenu == 2:
            isActiveGrade = True
            opNotas = 0
            
            while isActiveGrade:
                for i, item in enumerate(menuNotas):
                    print(f"{i+1}. {item}")
                try:
                    opNotas = int(input("=>"))
                except ValueError:
                    print("Error en el ingreso del dato")
                    os.system("pause")
                else:
                    if (opNotas == 1):
                        opParciales = 0
                        isActiveParciales = True

                        while isActiveParciales:
                            cod = int(input("Ingresa el codigo del estudiante: "))

                            for item in alumnos[0]:
                                if item in alumnos[0]:
                                    print("El alumnno existe")


                    elif (opNotas == 2):
                        pass
                    elif (opNotas == 3):
                        pass
                    elif (opNotas == 0):
                        print("Gracias por usar nuestro sistema!")
                        isActiveGrade = False
                
        elif opMenu == 3:
            cod = int(input("Ingresa el codigo del estudiante: "))
            for item in alumnos:
                if cod in item:
                    print(item)
        os.system("pause")
