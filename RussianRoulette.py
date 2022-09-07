import random

class RussianRoulette:
    def __init__(self, num_of_players, chamber_size):
        self.num_of_players = num_of_players
        self.chamber_size = chamber_size

    def shuffle(self):
        self.gun_chamber = [False for x in range(self.chamber_size)]
        self.gun_chamber[random.randint(0, self.chamber_size - 1)] = True

    def play(self):
        counter = 0
        someone_shot = False
        while not someone_shot:
            if self.gun_chamber[counter % self.chamber_size]:
                someone_shot = True
            else:
                counter += 1
        return counter % self.num_of_players

    def play_verbose(self):
        counter = 0
        someone_shot = False
        print("Gun: %s" % (self.gun_chamber))
        while not someone_shot:
            if self.gun_chamber[counter % self.chamber_size]:
                print("Player %s was shot at %s" % (counter % self.num_of_players, counter))
                someone_shot = True
            else:
                print("Player %s was not shot at %s" % (counter % self.num_of_players, counter))
                counter += 1
        print("\n\n")
        return counter % self.num_of_players
