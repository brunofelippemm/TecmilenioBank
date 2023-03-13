class User:
    credentials = {'':''}
    def register(self):
        print("-----Bienvenido al Banco Tecmilenio-----")

        print("Ingresa su correo")
        email = input()
       
        if (User.credentials.get(email,False)):
            print("Este correo ya está en uso")
        else:
            print("ingrese su contraseña")
            password=input()
            if(User.credentials.get(email,False)):
                print("Su cuenta se ha creado correctamente")
                User.credentials[email] = password
        

pepe = User()
pepe.register() 
#add commit push -u origin 