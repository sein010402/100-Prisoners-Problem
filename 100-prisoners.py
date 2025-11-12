import random

def main():
    NUM_DRAWERS = 10
    NUM_REPETITIONS = int(1E5)

    print('{:15}: {:5} ({})'.format('approach', 'wins', 'ratio'))
    for approach in PrisionersGame.approaches:
        num_victories = 0
        for _ in range(NUM_REPETITIONS):
            game = PrisionersGame(NUM_DRAWERS)
            num_victories += PrisionersGame.victory(game.play(approach))

        print('{:15}: {:5} ({:.2%})'.format(
            approach.__name__, num_victories, num_victories / NUM_REPETITIONS))


class PrisionersGame:
    def __init__(self):
        return
    def play_naive(self):
        return
    def play_naive_mem(self, play_number):
        not_attemped = self.drawer_ids[:]
        for attempt in range(self.max_attempts):
                        guess = random.choice(not_attemped)
            not_attemped.remove(guess)

            if self.drawers[guess] == player_number:
                return True

        return False
    def play_optimum(self):
        return
    @classmethod
    def victory(csl):
        return
    def play(self):
        return

if __name__ == '__main__':
    main()
