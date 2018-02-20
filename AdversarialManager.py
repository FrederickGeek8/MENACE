from GameManager import GameManager
from MENANCE import MENANCE


class AdversarialManager(GameManager):
    """docstring for AdversarialManager."""

    def __init__(self,
                 players=[None, None],
                 train=False,
                 init_method=['uniform', 'uniform'],
                 sizes=[10, 10]):
        super(AdversarialManager, self).__init__(players[0], train,
                                                 init_method[0], sizes[0])
        self.player2 = MENANCE(
            model=players[1], init_method=init_method[1], sizes=sizes[1])
        self.resigned2 = False

    def simulate(self):
        while not self.resigned and not self.resigned2:
            move = self.player.move(self.state)

            if move == -1:
                if self.train:
                    self.player.regress('loss')
                    self.player2.regress('win')
                self.resigned = True
                break

            self.state[move] = "1"
            # print(self)

            winner = self.check_win()
            if winner == 1:
                if self.train:
                    self.player.regress('win')
                    self.player2.regress('loss')
                break
            elif winner == -1:
                if self.train:
                    self.player.regress('draw')
                    self.player2.regress('draw')
                break

            move = self.player2.move(self.state)

            if move == -1:
                if self.train:
                    self.player.regress('win')
                    self.player2.regress('loss')
                self.resigned2 = True
                break

            self.state[move] = "2"
            # print(self)

            winner = self.check_win()
            if winner == 2:
                if self.train:
                    self.player.regress('loss')
                    self.player2.regress('win')
                break
            elif winner == -1:
                if self.train:
                    self.player.regress('draw')
                    self.player2.regress('draw')
                break

    def check_win(self):
        if self.resigned2:
            return 1

        return super(AdversarialManager, self).check_win()

    def reset(self):
        super(AdversarialManager, self).reset()
        self.resigned2 = False
