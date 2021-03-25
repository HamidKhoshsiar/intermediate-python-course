import random
def main():
  #print('You rolled a die')
  dice = random.randrange(1, 7)

  if dice == 6:
    dice = random.randrange(1, 7)
    print(dice)
  else:
    print(dice)

if __name__== "__main__":
  main()
