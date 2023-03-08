class User:
    
    
    credentials = {
        "john": "gato",
        "pepe": "vaca"
    }
    
    def login(self):
        email = input()
        password = input()
        stored_password = User.credentials.get(email, False)
        return password == stored_password

    
usuario_1 = User()
usuario_1.login()
        