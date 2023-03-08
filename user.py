class User:
    credentials = dict()
    def register(self):
        print("-----Bienvenido al Banco Tecmilenio-----")

        print("Ingresa su correo")
        email = input()
        if (email==User.credentials):
            print("Este correo ya está en uso")
        else:
            print("ingrese su contraseña")
            password=input()
            if(password==User.credentials):
                print("Esta contraseña ya está en uso")
            else:
                print("Su cuenta se ha creado correctamente")
            User.credentials[email] = password
        #    if (User.credentials[email]==password):
         #       print("esta contraseña ya está en uso")
          #  else:
           #     print("Confirme su contraseña")
            #    confirmpassword = input()
            
               
             ##      print("Se ha creado correctamente la cuenta")
            print(User.credentials)
pepe = User()
pepe.register()     
#add commit push -u origin 