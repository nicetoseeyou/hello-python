class People:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail

    def info(self):
        print(f"Name {self.name}, mail {self.mail}")
        return None
