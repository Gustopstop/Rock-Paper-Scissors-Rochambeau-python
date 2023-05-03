import random
import time
while True:
    a = random.choice(["rock", "paper", "Scissors"])
    b = input("rock, Scissors, paper?:")
    if b == "Scissors" and a == "paper":
        print("...")
        time.sleep(0.5)
        print("win")
    elif b == "paper" and a == "rock":
        print("...")
        time.sleep(0.5)
        print("win")
    elif b == "rock" and a == "Scissors":
        print("...")
        time.sleep(0.5)
        print("win")
    elif b == a:
        print("...")
        time.sleep(0.5)
        print("tie")
    elif b == "exit":
        break
    else:
        print("...")
        time.sleep(0.5)
        print("lose")
    print(a)
