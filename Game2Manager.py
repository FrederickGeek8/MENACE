from GameManager import GameManager
import random


class Game2Manager(GameManager):
    """docstring for Game2Manager."""

    def __init__(self,
                 prev_player=None,
                 train=True,
                 init_method='uniform',
                 sizes=10):
        super(Game2Manager, self).__init__(prev_player, train, init_method,
                                           sizes)

    def simulate(self):
        while not self.resigned:
            blank = [i for i, x in enumerate(self.state) if x == "0"]
            self.state[random.choice(blank)] = "1"

            winner = self.check_win()
            # print(2, winner)
            # print(self)
            if winner == 1:
                if self.train:
                    self.player.regress('loss')
                break
            elif winner == -1:
                if self.train:
                    self.player.regress('draw')
                break

            move = self.player.move(self.state)

            if move == -1:
                if self.train:
                    self.player.regress('loss')
                self.resigned = True
                break

            self.state[move] = "2"

            winner = self.check_win()
            # print(1, winner)
            # print(self)
            if winner == 2:
                if self.train:
                    self.player.regress('win')
                break
            elif winner == -1:
                if self.train:
                    self.player.regress('draw')
                break
