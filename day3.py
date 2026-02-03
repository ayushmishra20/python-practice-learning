class person():
    name = "Ayush Mishra"
    occupation = "ai engineer"
    sallary = 400

    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
# a.name = "Harsh Mishra"
a.occupation = "AI Engineer"


c = person()
c.name = "Vaibhav"
c.occupation = "Game Developer"
b = person()
b.name = "Shubhm"
b.occupation = "Tax Collector"


a.info()
c.info()
b.info()


class person():

    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is an {self.occupation} in this firm")

a = person("Ayush Mishra", "AI Engineer")
a.info()        

# Decorator 

def greet(fx):
    def mfx(*args, **kwargs):
        print("Jai Hind")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def add(a,b):
    sum = a+b
    print("The addition of two number is :", sum )
add(6, 7)


# ---------random function---------- #
@greet
def hello():
    print("hello someone born with glorious perpose")
hello()




class student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print(f"{self.name}'s grade ")

    def get_grade(self):
        if self.marks>90:
            return "A"
        elif self.marks>85:
            return "B"
        elif self.marks>80:
            return "C"
        
        

stud = student("Ayush" , 91)
print(stud.get_grade())

class bankaccount:
    def __init__(self, accountholder, balance):
        self.accountholder = accountholder
        self.balance = balance

    def deposit(self, ammount):
        if ammount> 0:
            self.balance += ammount
            print(f"{ammount} Credited to your Account XX4770")
        elif ammount < 0:
            print("Invalid transaction")
    
    def withdrwa(self, ammount):
        if ammount <=0 :
            print("The transacion could not be proceeded")
        elif ammount < self.balance:
            self.balance -= ammount
            print(f" After deduction the Remaining Balance is {self.balance}")
        elif ammount >= self.balance:
            print("the ammount could not deduct you should enter low ammount")

    def show_balance(self):
        print(f"The fetched balance of {self.accountholder} is {self.balance}")
        

s1 = bankaccount("Ayush", 1000)
s1.deposit(20)
s1.withdrwa(20)
s1.show_balance()

        
# # 3️⃣ Book

# title, author, price

# method: apply_discount()

class book:
    def __init__(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
    
    def apply_discount(self, discount_percentage):
        if 0 < discount_percentage <= 100:
            discount_amount = (discount_percentage/100) *self.price
            self.price -= discount_amount
            print(f"{discount_percentage} percent applied")
        else:
            print("Invalid!!!")
    def show_details(self):
        print(f"{self.title} book's title")
        print(f"{self.author} is the Author of the book")
        print(f"{self.price } is the book's price")


b = book("House Of The Dragons", 3000, "Ayush")
b.apply_discount(10)
b.show_details()




