import random
choice = ''
stop = "q"
print ("Welcome to your personal computer assistant. ")



print ("Enter 1 to Generate a Design." )
print ("Enter 2 to Activate Budget Mode ." )
print ("Enter 3 to Project Futer Income." )
print ("Enter q to quit." )
choice = input("What would you like to do? ")

if choice == '1':
    rows= (random.randint(3,7))
    for i in range (rows + 1, 0, -1):
      for j in range (0, i - 1):
        print ("*", end='')
      print (" ") 
      if i == 1: 
        print("Look how pretty! ") 
while 
elif choice == '2':
  budget = int(input("How much did you budget for this month? "))
  expone = int(input("Amount of expense #1?, (type -1 to quit."))