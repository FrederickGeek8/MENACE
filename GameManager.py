from MENANCE import MENANCE
import random


class GameManager:
    """docstring for GameManager."""

    def __init__(self,
                 prev_player=None,
                 train=True,
                 init_method='uniform',
                 sizes=10):
        self.state = ["0" for i in range(9)]
        self.player = MENANCE(
            model=prev_player, init_method=init_method, sizes=sizes)
        self.resigned = False
        self.train = train

    def simulate(self):
        while not self.resigned:
            move = self.player.move(self.state)

            if move == -1:
                if self.train:
                    self.player.regress('loss')
                self.resigned = True
                break

            self.state[move] = "1"

            winner = self.check_win()
            # print(1, winner)
            # print(self)
            if winner == 1:
                if self.train:
                    self.player.regress('win')
                break
            elif winner == -1:
                if self.train:
                    self.player.regress('draw')
                break

            blank = [i for i, x in enumerate(self.state) if x == "0"]
            self.state[random.choice(blank)] = "2"

            winner = self.check_win()
            # print(2, winner)
            # print(self)
            if winner == 2:
                if self.train:
                    self.player.regress('loss')
                break
            elif winner == -1:
                if self.train:
                    self.player.regress('draw')
                break

    def check_win(self):
        if self.resigned:
            return 2

        for i in range(3):
            test = self.state[3 * i]
            if self.state[3 * i:3 * i + 3].count(test) == 3 and test != '0':
                return int(test)

        for i in range(3):
            first = self.state[i] == self.state[i + 3]
            second = self.state[i + 3] == self.state[i + 6]
            if first and second and self.state[i] != '0':
                return int(self.state[i])

        first = self.state[0] == self.state[4]
        second = self.state[4] == self.state[8]
        if first and second and self.state[0] != '0':
            return int(self.state[0])

        first = self.state[2] == self.state[4]
        second = self.state[4] == self.state[6]
        if first and second and self.state[2] != '0':
            return int(self.state[2])

        if self.state.count('0') == 0:
            return -1

        return 0

    def reset(self):
        self.state = ["0" for i in range(9)]

    def __str__(self):
        joined = " ".join(self.state)
        out = ""
        out += joined[0:6] + '\n'
        out += joined[6:12] + '\n'
        out += joined[12:18] + '\n'
        return out
