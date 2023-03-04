from data import data
import random
from art import tprint

def ran_num():
    """Choses a random number between 0 and 49"""
    num = random.randint(0, 49)
    return num

def choosing(num):
    """Choosing a celebrity from the list and returning name and description"""
    choise = data[num]['name']
    descrip = data[num]['description']
    return choise + ' ' + descrip

def follower_count(num):
    """Reads and returns the follower count"""
    follow = data[num]['follower_count']
    return follow

def scoring(follow_one, follow_two):
    """Sees who has the most followers"""
    if follow_one > follow_two:
        return 'a'
    else:
        return 'b'

points = 0
game_over = False
chosen_numb = ran_num()
celeb_one = choosing(chosen_numb)
while not game_over:
    followers = follower_count(chosen_numb)
    chosen_numb_two = ran_num()
    celeb_two = choosing(chosen_numb_two)
    followers_two = follower_count(chosen_numb_two)
    print(f"\nCompare A: {celeb_one}")
    tprint('VS')
    print(f"Against B: {celeb_two}")

    asking = input("Who has the most followers? Type 'A' or 'B': ").lower().strip()
    result = scoring(followers, followers_two)

    if result == asking:
        points += 1
        print(f"Correct. Your score is {points}.")
        celeb_one = celeb_two
    else:
        game_over = True
print(f"\nSorry, that's wrong. Your final score was {points}.")
