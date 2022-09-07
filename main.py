import sys, random
from RussianRoulette import RussianRoulette

if __name__ == "__main__":

    # Check if the user has supplied a number of players argument
    if not sys.argv[1]:
        print("Invalid arguments, needs an integer for number of players")
        sys.exit(0)

    # Check if the user has supplied a chamber size argument
    if not sys.argv[2]:
        print("Invalid arguments, needs an integer for the chamber size for the gun")
        sys.exit(0)

    # Check if the user has supplied an iterations argument
    if not sys.argv[3]:
        print("Invalid arguments, needs an integer for the number of iterations")
        sys.exit(0)

    # Use the command line argument to define the number of players
    num_of_players = int(sys.argv[1])

    # Use the command line argument to define the chamber size of the gun
    chamber_size = int(sys.argv[2])

    # Use the command line argument to define the number of iterations of the game
    iters = int(sys.argv[3])
    
    # Count the number of deaths for each player
    player_deaths = [0 for x in range(num_of_players)]

    # Define the game
    game = RussianRoulette(num_of_players, chamber_size)

    # Define a loop for the number of iterations of the game
    for i in range(iters):
        game.shuffle()
        death = game.play()
        player_deaths[death] += 1

    # Print percentage of deaths for each player
    for i, death_count in enumerate(player_deaths):
        print("Player %s has died %s times with a percentage deaths of %s%%" % (str(i + 1), str(death_count), str((death_count / iters) * 100)))
