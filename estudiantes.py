import core
import os
diccEstudiantes ={"data":[]}

def LoadInfoEstudiantes():
    global diccEstudiantes
    if (core.checkFile('estudiantes.json')):
        diccEstudiantes = core.LoadInfo('estudiantes.json')
    else:
        core.crearInfo('estudiantes.json',diccEstudiantes)

def MainMenu():
    os.system('cls')
    isMainMenu = True
    print('+','-'*55,'+')
    print("|{:^14}{}{:^14}|".format(' ','ADMINISTRACION DE ESTUDIANTES',' '))
    print('+','-'*55,'+')
    print("Bienvenido al sistema de gestión de estudiantes")
    print("1. Registrar Estudiante")
    print("2. Buscar Estudiante")
    print("3. Modificar Estudiante")
    print("4. Eliminar Estudiante")
    print("5. Listar Estudiantes")
    print("6. Salir al menu principal")
    opcion = int(input("Ingrese una opción: "))
    if (opcion == 1):
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^18}{}{:^18}|".format(' ','REGRISTRAR ESTUDIANTES',' '))
        print('+','-'*55,'+')
        print("Completar la siguiente información: ")
        id=input("Ingresa el id del estudiante: ").upper()
        contador=len(diccEstudiantes['data'])
        if (len(diccEstudiantes['data'])==0):
            nombres=input("Nombres del estudiante:" ).upper()
            apellidos=input("Apellidos del estudiante: ").upper()
            edadEstudiante=int(input("Edad: "))
            correoElectronico=input("Correo Electronico:").upper()
            ciudadDeOrigen=input("Ciudad de origen: ").upper()
            print("Escoge tu estado civil:")
            print("1. Soltero")
            print("2. Casado")
            print("3. Otro")
            opcionEstado=int(input("Ingrese una opción: "))
            if(opcionEstado==1):
                estadoCivil="SOLTERO"
            elif(opcionEstado==2):
                estadoCivil="CASADO"
            elif(opcionEstado==3):
                estadoCivil=input("Indica cual: ").upper()
            print("Escoge tu genero: ")
            print("1. Masculino")
            print("2. Femenino")
            print("3. Otro")
            opcionGenero=int(input("Ingrese una opción: "))
            if(opcionGenero==1):
                genero="MASCULINO"
            elif(opcionGenero==2):
                genero="FEMENINO"
            elif(opcionGenero==3):
                genero=input("Indica cual: ").upper()
            numeroTelefonico=input("NumeroTelefonico:")
            data ={
                "id":id,
                "nombres":nombres,
                "apellidos":apellidos,
                "edadEstudiante":edadEstudiante,
                "correoElectronico":correoElectronico,
                "ciudadDeOrigen":ciudadDeOrigen,
                "estadoCivil":estadoCivil,
                "genero":genero,
                "numeroTelefonico":numeroTelefonico
            }
            diccEstudiantes["data"].append(data)
            core.crearInfo("estudiantes.json",data)
        elif (len(diccEstudiantes['data'])!=0):
            for i,item in enumerate(diccEstudiantes["data"]):
                if(id in item['id']):
                    print("Cliente ya está registrado...")
                    os.system('pause')
                    break
                elif(contador==i+1):
                    nombres=input("Nombres del estudiante:" ).upper()
                    apellidos=input("Apellidos del estudiante: ").upper()
                    edadEstudiante=int(input("Edad: "))
                    correoElectronico=input("Correo Electronico:").upper()
                    ciudadDeOrigen=input("Ciudad de origen: ").upper()
                    print("Escoge tu estado civil:")
                    print("1. Soltero")
                    print("2. Casado")
                    print("3. Otro")
                    opcionEstado=int(input("Ingrese una opción: "))
                    if(opcionEstado==1):
                        estadoCivil="SOLTERO"
                    elif(opcionEstado==2):
                        estadoCivil="CASADO"
                    elif(opcionEstado==3):
                        estadoCivil=input("Indica cual: ").upper()
                    print("Escoge tu genero: ")
                    print("1. Masculino")
                    print("2. Femenino")
                    print("3. Otro")
                    opcionGenero=int(input("Ingrese una opción: "))
                    if(opcionGenero==1):
                        genero="MASCULINO"
                    elif(opcionGenero==2):
                        genero="FEMENINO"
                    elif(opcionGenero==3):
                        genero=input("Indica cual: ").upper()

                    numeroTelefonico=input("NumeroTelefonico:")
                    data ={
                        "id":id,
                        "nombres":nombres,
                        "apellidos":apellidos,
                        "edadEstudiante":edadEstudiante,
                        "correoElectronico":correoElectronico,
                        "ciudadDeOrigen":ciudadDeOrigen,
                        "estadoCivil":estadoCivil,
                        "genero":genero,
                        "numeroTelefonico":numeroTelefonico
                    }
                    if(edadEstudiante<18):
                        idAcudiente=input("Ingresa el id del acudiente:").upper()
                        nombreAcudiente=input("Ingresa el nombre del acudiente:").upper()
                        parentesco=input("Parentesco con el estudiante:").upper()
                        data = {
                            "id":id,
                            "nombres":nombres,
                            "apellidos":apellidos,
                            "edadEstudiante":edadEstudiante,
                            "correoElectronico":correoElectronico,
                            "ciudadDeOrigen":ciudadDeOrigen,
                            "estadoCivil":estadoCivil,
                            "genero":genero,
                            "numeroTelefonico":numeroTelefonico,
                            "idAcudiente":idAcudiente,
                            "nombreAcudiente":nombreAcudiente,
                            "parentesco":parentesco,
                        }
                    diccEstudiantes["data"].append(data)
                    core.crearInfo("estudiantes.json",data)
                    break
        #REVISAR LA FORMA DE HACERLE UPDATE AL DICCIONARIO DEL CAMPERO Y REDUCIR LAS LINEAS DE CODIGO
    elif (opcion == 2):
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^19}{}{:^18}|".format(' ','BUSCAR ESTUDIANTE',' '))
        print('+','-'*55,'+')
        numeroId=input("Ingresa Id a buscar:")
        for i,item in enumerate(diccEstudiantes["data"]):
            if numeroId in item["id"]:
                if (item['edadEstudiante']>=18):
                    print(f"Numero de Id: {item['id']}")
                    print(f"Nombres: {item['nombres']}")
                    print(f"Apellidos: {item['apellidos']}")
                    print(f"Edad Estudiante: {item['edadEstudiante']}")
                    print(f"Correo electronico: {item['correoElectronico']}")
                    print(f"Ciudad de Origen: {item['ciudadDeOrigen']}")
                    print(f"Estado Civil: {item['estadoCivil']}")
                    print(f"Genero: {item['genero']}")
                    print(f"Numero Telefonico: {item['numeroTelefonico']}")
                    os.system("pause")
                else:
                    print(f"Numero de Id: {item['id']}")
                    print(f"Nombres: {item['nombres']}")
                    print(f"Apellidos: {item['apellidos']}")
                    print(f"Edad Estudiante: {item['edadEstudiante']}")
                    print(f"Correo electronico: {item['correoElectronico']}")
                    print(f"Ciudad de Origen: {item['ciudadDeOrigen']}")
                    print(f"Estado Civil: {item['estadoCivil']}")
                    print(f"Genero: {item['genero']}")
                    print(f"Numero Telefonico: {item['numeroTelefonico']}")
                    print(f"Numero Id Acudiente: {item['idAcudiente']}")
                    print(f"Nombre Acudiente: {item['nombreAcudiente']}")
                    print(f"Parentesco: {item['parentesco']}")
                    os.system("pause")
    elif (opcion == 3):
        os.system('cls')
        print('+','-'*55,'+')
        print("|{:^20}{}{:^19}|".format(' ','EDITAR ESTUDIANTES',' '))
        print('+','-'*55,'+')
        numeroId=input("Ingresar el numero Id:")
        for i,item in enumerate(diccEstudiantes["data"]):
            if numeroId in item['id']:
                if (item['edadEstudiante']>=18):
                    item['id']=input("Ingresar nuevo Id o Enter para continuar..").upper() or item['id']
                    item['nombres']=input("Ingresar nuevo nombres o Enter para continuar..").upper() or item['nombres']
                    item['apellidos']=input("Ingresar nuevo apellidos o Enter para continuar..").upper() or item['apellidos']
                    item['edadEstudiante']=int(input("Ingresar edad"))
                    item['correoElectronico']=input("Ingresar nuevo correo electronico o Enter para continuar..").upper() or item['correoElectronico']
                    print("Escoge tu estado civil:")
                    print("1. SOLTERO")
                    print("2. CASADO")
                    print("3. OTRO")
                    opcionEstado=int(input("Ingrese una opción: "))
                    if(opcionEstado==1):
                        estadoCivil="SOLTERO"
                    elif(opcionEstado==2):
                        estadoCivil="CASADO"
                    elif(opcionEstado==3):
                        estadoCivil=input("Indica cual: ").upper()
                    print("Escoge tu genero: ")
                    print("1. MASCULINO")
                    print("2. FEMENINO")
                    print("3. OTRO")
                    opcionGenero=int(input("Ingrese una opción: "))
                    if(opcionGenero==1):
                        genero="MASCULINO"
                    elif(opcionGenero==2):
                        genero="FEMENINO"
                    elif(opcionGenero==3):
                        genero=input("Indica cual: ").upper()
                    item['estadoCivil']=estadoCivil
                    item['genero']=genero
                    item['numeroTelefonico']=input("Ingresar nuevo telefono o Enter para continuar..") or item['numeroTelefonico']
                    core.EditarData('estudiantes.json',diccEstudiantes)
                else:
                    item['id']=input("Ingresar nuevo Id o Enter para continuar..").upper() or item['id']
                    item['nombres']=input("Ingresar nuevo nombres o Enter para continuar..").upper() or item['nombres']
                    item['apellidos']=input("Ingresar nuevo apellidos o Enter para continuar..").upper() or item['apellidos']
                    item['edadEstudiante']=int(input("Ingresar edad"))
                    item['correoElectronico']=input("Ingresar nuevo correo electronico o Enter para continuar..").upper() or item['correoElectronico']
                    print("Escoge tu estado civil:")
                    print("1. SOLTERO")
                    print("2. CASADO")
                    print("3. OTRO")
                    opcionEstado=int(input("Ingrese una opción: "))
                    if(opcionEstado==1):
                        estadoCivil="SOLTERO"
                    elif(opcionEstado==2):
                        estadoCivil="CASADO"
                    elif(opcionEstado==3):
                        estadoCivil=input("Indica cual: ").upper()
                    print("Escoge tu genero: ")
                    print("1. MASCULINO")
                    print("2. FEMENINO")
                    print("3. OTRO")
                    opcionGenero=int(input("Ingrese una opción: "))
                    if(opcionGenero==1):
                        genero="MASCULINO"
                    elif(opcionGenero==2):
                        genero="FEMENINO"
                    elif(opcionGenero==3):
                        genero=input("Indica cual: ").upper()
                    item['estadoCivil']=estadoCivil
                    item['genero']=genero
                    item['numeroTelefonico']=input("Ingresar nuevo telefono o Enter para continuar..") or item['numeroTelefonico']
                    item['idAcudiente']=input("Ingresar nuevo id acudiente o Enter para continuar..") or item['idAcudiente']
                    item['nombreAcudiente']=input("Ingresar nombre acudiente o Enter para continuar..") or item['nombreAcudiente']
                    item['parentesco']=input("Ingresar parentesco o Enter para continuar..") or item['parentesco']
                    core.EditarData('estudiantes.json',diccEstudiantes)
    elif (opcion == 4):
        pass
    elif (opcion == 5):
        isMainMenu = False
    elif(isMainMenu):
        MainMenu()