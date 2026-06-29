def title():
   print(" ")
   print("Let's Play!")
   print("TIC TAC TOE   ")



board = [[" "," "," "],
         [" "," "," "],
         [" "," "," "],]


def box():
    for rows in board:
       print(" | ".join(rows))
       print("-"*10)
    

def input_():
    while True:
     r =  int(input("enter row: "))
     c = int(input("enter coloumn: "))         
     board[r][c] = input("Enter your symbol '0' or '*' : ")
     if board[r][c] != '0' and board[r][c] != '*':
         print("Invalid input! Please enter valid input;)")
         board[r][c] = input("Enter your symbol '0' or '*' : ")
     box()
     condition()
     
     
     
def condition():
    
      if board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0':
          print ("0 wins") 
          return True
      elif board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0':
          print ("0 wins")
          return True
      elif board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0': 
          print ("0 wins")
          return True
      elif board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0':
          print ("0 wins")
          return True
      elif board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0':
       print ("0 wins")
       return True
      elif board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0': 
          print ("0 wins")
          return True
      elif board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0': 
          print ("0 wins")
          return True
      elif board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0':
          print ("0 wins")
          return True

      elif board[0][0] == '*' and board[0][1] == '*' and board[0][2] == '*':
          print("* wins")
          return True
      elif board[1][0] == '*' and board[1][1] == '*' and board[1][2] == '*':
          print("* wins")
          return True
      elif board[2][0] == '*' and board[2][1] == '*' and board[2][2] == '*': 
          print("* wins")
          return True 
      elif board[0][0] == '*' and board[1][0] == '*' and board[2][0] == '*':
          print("* wins")
          return True 
      elif board[0][1] == '*' and board[1][1] == '*' and board[2][1] == '*':
          print("* wins")
          return True 
      elif board[0][2] == '*' and board[1][2] == '*' and board[2][2] == '*':
          print("* wins")
          return True 
      elif board[0][0] == '*' and board[1][1] == '*' and board[2][2] == '*':
          print("* wins")
          return True 
      elif board[0][2] == '*' and board[1][1] == '*' and board[2][0] == '*':
          print("* wins")
          return True
      
      return False
 
   

title()    
box()
input_()

