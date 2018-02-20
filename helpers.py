from GameManager import GameManager
from Game2Manager import Game2Manager


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
