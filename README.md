# MENACE
Basic ML Playground with Matchboxes. This repository was not really supposed to be public, however, recently I have decided that it might as well be out there. Sorry for the mess with the files, if I have time I will redo the directory structure.

## Requirements
Run `pip install -r requirements.txt` to install dependencies.
This is meant to run with Python ~3.6 (I personally use 3.6.3)

## Contributing
Feel free to submit issues or pull requests! I would ask that you please keep this code private (unless you have my express permission).

Pull requests do not have to fix bugs or improve existing architecture! Feel free to contribute cool new features or experiments! Add your voice to the project!

## Interactive Files
1. train.py
  - Train a "Player 1" instance. Can load or generate a new instance.
2. train2.py
  - Train a "Player 2" instance Can load or generate a new instance.
3. play.py
  - Play against your trained "Player 1" instance. (loads `./instance.p`)
4. play2.py
  - Play again your trained "Player 2" instance. (loads `./instance2.p`)
5. fight.py
  - Make Player 1 and Player 2 fight against each other. Can generate a new instance of each, or can load previous instances. There is an option at the end of training to save the instances as well!
6. prune.py
  - A utility for "pruning" a saved instance of a player. Uses statistical reduction. Definitely saves on memory usage and sometimes improves learning rate later in life.
7. plot.py
  - A program that will plot incremental training results of Player 1. Currently compares `uniform` and `random` initializations.
8. plot2.py
  - A program that will plot incremental training results of Player 2. Currently compares `uniform` and `random` initializations.
9. pruneplot.py
  - A program that will plot incremental training results of a "vanilla" given instance versus an instance that utilizes automatic pruning. Currently configured to compare a pruned Player 1 initialized uniformly and a Player 1 initialized randomly.
10. fightplot.py
  - A **expensive** program that will compare training performance of an Adversarial instance, as well as compare testing performance of each model against random data. Has support for pruning as well! Due to old testing results, there is no option via the command-line interface to disable pruning for Player 2. Player 1 pruning, on the other hand, can be disabled via the command-line.

## Classes
1. Box.py
  - Represents a box filled with beads
2. MENANCE.py
  - Represents a MENANCE instance. i.e. a pile of matchboxes
3. GameManager.py
  - Interface for training a Player 1 instance.
4. Game2Manager.py
  - Interface for training a Player 2 instance.
5. PlayManager.py
  - Interface for playing with a MENANCE instance.
6. AdversarialManager.py
  - Interface for Adversarial training/testing.
7. helpers.py
  - Random helpers. Currently includes testing functions for Player 1 and 2 as well as the prune function.
