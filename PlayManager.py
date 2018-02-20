from GameManager import GameManager


class PlayManager(GameManager):
    """docstring for PlayManager."""

    def __init__(self, prev_player):
        super(PlayManager, self).__init__(prev_player=prev_player, train=False)

    def simulate(self):
        move = self.player.move(self.state)

        if move == -1:
            self.resigned = True
            return

        self.state[move] = "1"

    def move(self, x, y=None):
        if y is not None:
            x = x + 3 * y
        if self.state[x] == "0":
            self.state[x] = "2"
            return True

        return False

    def __str__(self):
        out = super(PlayManager, self).__str__()
        out = out.replace('1', 'X')
        out = out.replace('2', 'O')
        out = out.replace('0', '□')
        return out
