import random
min = 1
max = 7
choices = []
def main():
  #print('You rolled a die')
  dice = random.randrange(min, max)
  print(dice)
  choices.append(dice)

# if __name__== "__main__":
#   main()
def dice_size():
  try:
    min_changer = int(input('Define the minimum of dice'))
    global min
    min = min_changer
  except:print('Only integer')
  try:
    max_changer = int(input('Define the maximum of dice'))
    global max
    max = max_changer + 1
  except:print('Only integer')



print(min)
cntr = 0
while cntr ==0:
  user = input("roll the dice?(y/n)\n O for option")
  if user == 'y' or user == 'Y':
    main()
  elif user == 'n' or user =='N':
    cntr=1
    print('the sum of all choices are: ',sum(choices))
    print(choices)
  elif user == 'o' or user == 'O':
    dice_size()
  else:
    print('Yes or No or option please!')
