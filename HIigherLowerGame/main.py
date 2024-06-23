from game_data import data
from art import logo , vs
import random

# print(data)
# print(logo)
# print(vs)
YourScore = 0
for i in range(0,len(data)):
    # for j in range(0,len(data[i])):
        print(data[i]['name'])
        print(data[i]['description'])
        print(data[i]['country'])
        print(vs)
        print(data[i+1]['name'])
        print(data[i+1]['description'])
        print(data[i+1]['country'])
        Guess = input("Who has more follower: A or B ")
        if Guess == 'A':
            if data[i]['follower_count'] > data[i+1]['follower_count']:
                YourScore +=1
            elif data[i]['follower_count'] < data[i+1]['follower_count']:
                print(YourScore)
                break
        elif Guess == 'B':
            if data[i+1]['follower_count'] > data[i]['follower_count']:
                YourScore +=1       
            elif data[i+1]['follower_count'] < data[i]['follower_count']:
                print(YourScore)
                break
                