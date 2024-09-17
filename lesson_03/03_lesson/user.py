class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName(self):
        print(self.first_name)

    def getLastName(self):
        print(self.last_name)

    def getFullName(self):
        print("fFirst name: {self.first_name}, last name: {self.last_name}")
