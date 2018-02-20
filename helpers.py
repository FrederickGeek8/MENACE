from GameManager import GameManager
from Game2Manager import Game2Manager
import math


def test_p1(subject):
    temp = GameManager(prev_player=subject, train=False)
    loss = 0
    wins = 0
    for i in range(10000):
        temp.simulate()

        if temp.check_win() == 2:
            loss += 1
        else:
            wins += 1
        temp.reset()

    return (wins / (wins + loss)) * 100


def test_p2(subject):
    temp = Game2Manager(prev_player=subject, train=False)
    loss = 0
    wins = 0
    for i in range(10000):
        temp.simulate()

        if temp.check_win() == 1:
            loss += 1
        else:
            wins += 1
        temp.reset()

    return (wins / (wins + loss)) * 100


def prune(menance):
    done = 0
    for key in menance.moves:
        done += 1
        state = menance.moves[key].state
        if len(state) > 0:
            unique = list(set(state))
            unique_count = [state.count(num) for num in unique]
            mmin = min(unique_count)
            new_count = [math.ceil(count / mmin) for count in unique_count]

            tmp = []
            for i in range(len(new_count)):
                orig = unique[i]
                for j in range(new_count[i]):
                    tmp.append(orig)

            menance.moves[key].state = tmp
