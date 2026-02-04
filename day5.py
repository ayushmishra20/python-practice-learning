# inharitance 
class employee():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"Employee name is {self.name} and id is {self.id}")

e1 = employee("Ayush", 21)
e1.showdetails()

class programmer (employee):
    def programmer_lang(self, lang):
        self.lang = lang
        print(f"{self.id} id employee writing code in {self.lang} language")

e2 = programmer("Ayush", 21)
e2.programmer_lang("java")
        