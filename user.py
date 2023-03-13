class User:

    credentials = {'name':'password'}

    def init(self):
        self.balance=0

    def play(self):
        print("======== Welcome to TecmiBank ========")
        print("Select 0 to end all the processes.")
        print("what action do you want to do")

        answer = input()
        print("Enter the money")
        deposit=float (input())
        self.balance += deposit 

        print(f"your balance is: {self.balance}")
    
    def delete(self, name, password):
        if self.login(name, password) and not self.balance:
            self.credentials.pop(name)
        return