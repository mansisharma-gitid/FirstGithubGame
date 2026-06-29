def welcome():
    print("===== CALCULATOR =====")

welcome()
class Calculator:

 def inputs(self):
     while True:
         try:
             a = float(input("Enter first number: "))
             break
         except:
             print("Enter a valid number!!")
     c = input("Enter operation to perform: ")
     while True:
         if c not in ["+", "-", "*", "/"]:
             print("Invalid operator!  ")
             c = input("Please Enter valid operator: ")
         else:
             break 
     while True:
         try:    
              b =  float(input("Enter second number: "))
              break
         except:
              print("Enter valid number!! ")

     return a,c,b

 def TakeInput(self):
     a, c, b = self.inputs()

     while True:

         if c == '+':
             result = self.add(a,b)
             print('The sum of', a, 'and', b, 'is:', result)
         elif c == '-':
             result = self.subtract(a,b)
             print('The difference of', a, 'and', b, 'is:', result)
         elif c == '*':
             result = self.multiply(a,b)
             print('The product of', a, 'and', b, 'is:', result)
         elif c == '/':
             result = self.division(a,b)
             print('The division of', a, 'and', b, 'is:', result)

         
         ans = input("Would you like to continue?? Y/N: ")
         if ans == 'y' or ans == 'Y':
            a = result
            while True:
                 try:    
                     b =  float(input("Enter second number: "))
                     break
                 except:
                     print("Enter valid number!! ")
            
            while True:
                      if c not in ["+", "-", "*", "/"]:
                         print("Invalid operator!  ")
                         c = input("Please Enter valid operator: ")
                      else:
                         break 
         elif ans == 'n' or ans == 'N':
            break
     print("Calculation Completed!!")   
     
    

 def add(self,a,b):
    res = a + b
    return res

 def subtract(self,a,b):
    res = a - b
    return res


 def multiply(self,a,b):
    res = a * b
    return res

 def division(self,a,b):
     while True:
             if b == 0: 
                 print("Division not possible")
                 b = float(input("Enter valid number: "))
             if b != 0:
                 break
                           
     res = a / b
     return res

obj = Calculator()
obj.TakeInput()








