import random
cash = 1000
def littledevil(bet_per_run, number_of_rolls, cash):
  if bet_per_run * number_of_rolls <= cash:
    for i in range(0, number_of_rolls):
      r1 = random.randint(1, 6)
      r2 = random.randint(1, 6)
      r3 = random.randint(1, 6)
      if r1 and r2 and r3 == 1:
        cash = cash + (bet_per_run * 3)
        print("Snake Eyes", cash)
      elif r1 and r2 and r3 == 6:
        cash = cash + (bet_per_run * 6)
        print("Little Devil", cash)
      else:
        cash = cash - bet_per_run
    q = str(input("Do you want to continue? [y/N] "))
    if "y" in q:
      q_y_1 = input("how much per roll, how many rolls? ")
      q_y_1_l = q_y_1.split(",")
      littledevil(int(q_y_1_l[0]), int(q_y_1_l[1]), cash)
    if "Y" in q:
      q_y_1 = input("how much per roll, how many rolls? ")
      q_y_1_l = q_y_1.split(",")
      littledevil(int(q_y_1_l[0]), int(q_y_1_l[1]), cash)
  else:
    print("Insufficent funds.")
    print(cash)
    q_y_1 = input("how much per roll, how many rolls? ")
    q_y_1_l = q_y_1.split(",")
    littledevil(int(q_y_1_l[0]), int(q_y_1_l[1]), cash)
littledevil(10, 20, cash)
"""
wrote this in like 20 minutes, so it's kinda bad, but it works
"""
