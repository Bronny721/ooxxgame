import random

print("歡迎來到井字遊戲")
print("**************")

possibleNumbers = [1,2,3,4,5,6,7,8,9]
gameBoard = [[1,2,3], [4,5,6], [7,8,9]]
rows = 3
cols = 3

def printGameBoard():
  for x in range(rows):
    print("\n*************")
    print("|", end="")
    for y in range(cols):
      print("", gameBoard[x][y], end=" |")
  print("\n*************")

def modifyArray(num, turn):
  num -= 1
  if(num == 0):
    gameBoard[0][0] = turn
  elif(num == 1):
    gameBoard[0][1] = turn
  elif(num == 2):
    gameBoard[0][2] = turn
  elif(num == 3):
    gameBoard[1][0] = turn
  elif(num == 4):
    gameBoard[1][1] = turn
  elif(num == 5):
    gameBoard[1][2] = turn
  elif(num == 6):
    gameBoard[2][0] = turn
  elif(num == 7):
    gameBoard[2][1] = turn
  elif(num == 8):
    gameBoard[2][2] = turn

def checkForWinner(gameBoard):
  if(gameBoard[0][0] == 'X' and gameBoard[0][1] == 'X' and gameBoard[0][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[0][1] == 'O' and gameBoard[0][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[1][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[1][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[1][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[1][2] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[2][0] == 'X' and gameBoard[2][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[2][0] == 'O' and gameBoard[2][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return "O"

  if(gameBoard[0][0] == 'X' and gameBoard[1][0] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][0] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][1] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][1] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][1] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][1] == 'O'):
    print("O has won!")
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][2] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][2] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")
    return "O"

  elif(gameBoard[0][0] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][2] == 'X'):
    print("X has won!")
    return "X"
  elif(gameBoard[0][0] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][2] == 'O'):
    print("O has won!")  
    return "O"
  elif(gameBoard[0][2] == 'X' and gameBoard[1][1] == 'X' and gameBoard[2][0] == 'X'):
    print("X has won!")  
    return "X"
  elif(gameBoard[0][2] == 'O' and gameBoard[1][1] == 'O' and gameBoard[2][0] == 'O'):
    print("O has won!") 
    return "O" 
  else:
    return "N"

leaveLoop = False
turnCounter = 0

while(leaveLoop == False):
  if(turnCounter % 2 == 0):
    printGameBoard()
    numberPicked = int(input("\n請選擇數字[1-9]: "))
    if(numberPicked >= 1 or numberPicked <= 9):
      modifyArray(numberPicked, 'X')
      possibleNumbers.remove(numberPicked)
    else:
      print("無效指令 請再試一次")
    turnCounter += 1
  else:
    while(True):
      cpuChoice = random.choice(possibleNumbers)
      print("\n電腦選擇: ", cpuChoice)
      if(cpuChoice in possibleNumbers):
        modifyArray(cpuChoice, 'O')
        possibleNumbers.remove(cpuChoice)
        turnCounter += 1
        break
  
  winner = checkForWinner(gameBoard)
  if(winner != "N"):
    print("\n遊戲結束!!!")
    break
