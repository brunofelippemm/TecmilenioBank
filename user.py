class User:

    credentials = {
        "john": "gato",
        "pepe": "vaca",
        'name':'password',
    }

    def init(self):
        self.balance=0

    def deposit(self):
        print("======== Welcome to TecmiBank ========")
        print("Select 0 to end all the processes.")
        print("what action do you want to do")

        answer = input()
        print("Enter the money")
        deposit=float (input())
        self.balance += deposit 

        print(f"your balance is: {self.balance}")
    
    def login(self):
        email = input()
        password = input()
        stored_password = User.credentials.get(email, False)
        return password == stored_password

    def delete(self, name, password):
        if self.login(name, password) and not self.balance:
            self.credentials.pop(name)
        return
    
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