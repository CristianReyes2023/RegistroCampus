import os
import estudiantes

# El centro de entrenamiento en software campus land desea realizar un programa que le permita llevar el control de los candidatos interesados a participar en su programa de entrenamiento.Campus desea realizar un registro previo de los participantes; la información que se contempla por cada participantes es la siguiente:
# Numero de Id,Nombres,Apellidos,edad,correo electronico,ciudad de origen,estado civil,genero,numero telefonico.
# Los campers que son menores de edad deben registrar información de acudientes con la siguiente informaicón: Id del acudiente, nombre del acudiente y parentesco 
# La información ingresada debe ser almacenada de forma local 

if __name__ == '__main__':
    isAddPrincipal = True
    while(isAddPrincipal):
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^23}|".format(' ','MENU PRINCIPAL',' '))
        print('+','-'*55,'+')
        print("1. Registro de estudiantes.")
        print("2. Terminar")
        opcion = int(input("Ingrese una opcion: "))
        if ( opcion ==1):
            estudiantes.LoadInfoEstudiantes()
            estudiantes.MainMenu()
        elif ( opcion ==2):
            isAddPrincipal = False
        else:
            print("Opcion no valida")