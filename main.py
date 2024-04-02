# A simple Instagram follower guessing game where players are presented with two random profiles and 
# must guess which one has a higher follower count. The game utilizes a predefined dataset of 
# profile details, including follower counts, and ASCII art for the "vs" display. Players can choose to 
# continue playing to increase their score.
from data import data
from logo import logo, vs
import random

print(logo)

score = 0
total_questions = 0  

while True:
    abc = input("Type Y to play and N to break:").lower()
    if abc == "n":
        print("Your Total Score is {} from {} questions.".format(score, total_questions))
        break
    
    elif abc == "y":
        random_item1 = random.choice(data)
        random_item2 = random.choice(data)
        count1 = random_item1["follower_count"]
        count2 = random_item2["follower_count"]
        detail1 = random_item1["name"]
        detail2 = random_item2["name"]
        print("Who has more followers:\n{} or {}".format(detail1, detail2))
        print(vs)
        guess = int(input("Type 1 for 1st Choice and Type 2 for 2nd Choice:"))
        total_questions += 1 
        
        if guess == 1:
            if count1 > count2:
                score += 1
                print("Correct! Current score is: {} out of {}".format(score, total_questions))
            else:
                print("Incorrect! Current score is: {} out of {}".format(score, total_questions))
        elif guess == 2:
            if count2 > count1:
                score += 1
                print("Correct! Current score is: {} out of {}".format(score, total_questions))
            else:
                print("Incorrect! Current score is: {} out of {}".format(score, total_questions))
        else:
            print("Invalid Input.")
    else:
        print("Invalid Input.")

