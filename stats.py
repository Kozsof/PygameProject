

class Stats:
    """Отслеживание текущей игры"""

    def __init__(self):
        self.reset_stats()
        self.run_game = True
        with open("high_score.txt", 'r') as f:
             self.high_score = int(f.readline())


    def reset_stats(self):
        self.guns_life = 3
        self.score = 0

