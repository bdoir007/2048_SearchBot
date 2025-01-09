import main
from random import randint

def evaluation(weights):
    sum = 0
    high_score = 0
    for i in range(10):
        score = main.main(weights)
        high_score = max(high_score, score)
        sum += score

    print("Average score: " + str(sum/10) + " Highest score: " + str(high_score))

def initialization():
    weights = []
    for i in range(5):
        weights.append(randint(0,50))

    return weights

def


simulation()
