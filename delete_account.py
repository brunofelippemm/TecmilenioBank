class User:
    
    def __init__(self):
        self.balance = None
        pass
    
    credentials = {'name':'password'}
    balance = float(0)
    
    def delete(self, name, password):
        if self.login(name, password) and not self.balance:
            self.credentials.pop(name)
        return