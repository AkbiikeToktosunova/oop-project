class calculator():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def multiplication(self):
        return self.x*self.y
    def division(self):
        if y==0:
            return "Division by 0"
        else: self.x//self.y
    def add(self):
        return self.x+self.y
    def subtraction(self):
        return self.x-self.y
    def percentage(self):
        return self.x*self.y/100
x=int(input("Enter first number: "))
y=int(input("Enter second number: "))
object=calculator(x,y)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Multiplication")
    print("2. Division") 
    print("3. Add")
    print("4. Subtraction")
    print("5. Percentage")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",object.multiplication())
    elif choice==2:
        print("Result: ",object.division())
    elif choice==3:
        print("Result: ",object.add())
    elif choice==4:
        print("Result: ",object.subtraction())
    elif choice==5:
        print("Result: ",object.percentage())
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
print()
