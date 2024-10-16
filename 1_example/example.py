import random
import ipdb


random.seed(42)


x = 0  
tries = 0  
while x < 3:  
    coin_flip = random.choice([0, 1])  
    decision = random.choice([0, 1])  
    # ipdb.set_trace()
    tries += 1
    if decision == coin_flip:
        print(f"Correct guess! Consecutive wins: {x+1} ")
        x += 1  
       
    else:
        print("Wrong guess, resetting streak!")
        x = 0  




print(f"It took {tries} tries for the computer to win 3 times in a row!")