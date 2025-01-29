import random

user = ""
pc_choises = ["rock", "paper", "scissors"]
while True:
   user = input("Rock, Paper, Scissors : ").lower()
   pc = random.choice(pc_choises)
   if(user == "q"):
      break
   if(user == "rock" or user == "paper" or user == "scissors"):
      print(f"You = {user.title()}")
      print(f"PC = {pc.title()}")
      if((user == "rock" and pc == "scissors") or (user == "scissors" and pc == "paper") or (user == "paper" and pc == "rock")):
         print("You wins")  
      elif(pc == user):
         print("Draw")    
      else:
         print("PC wins")   
     

      

