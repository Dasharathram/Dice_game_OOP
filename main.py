import random


class Die:

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self._player = player
        self._computer = computer

    def play(self):
        print("+++++++++++++++++++++++++")
        print("Welcome to Roll the Dice!")
        print("+++++++++++++++++++++++++\n")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break

    def play_round(self):
        # Welcome the user
        print("=========== This is the New round ===========")
        input("Please press any key to start the game!!!!!!\n")

        # rolling the dice
        player_value = self._player.roll_die()
        computer_value = self._computer.roll_die()

        #  showing the die values
        print(f"Your Die: {player_value}")
        print(f"Computer's Die: {computer_value}")

        #  compare the values
        if player_value > computer_value:
            print("You won this round")
            self._player.decrement_counter()
            self._computer.increment_counter()
        elif computer_value > player_value:
            print("You lost this round")
            self._computer.decrement_counter()
            self._player.increment_counter()
        else:
            print("It's a tie bruhh")

        # display counters as well
        print(f"You counter is at {self._player.counter}")
        print(f"Computer's counter is at {self._computer.counter}")

    def check_game_over(self):
        if self._player.counter == 0:
            print("Your counter reached Zero, YOU WON. yay")
            return True
        elif self._computer.counter == 0:
            print("Your score reached the limit, you lost. psst")
            return True
        else:
            return False


# assigning dice for each player
player_die = Die()
computer_die = Die()
# creating instances of players
my_player = Player(player_die, is_computer=False)
comp_player = Player(computer_die, is_computer=True)
# start the game with those instances
game = DiceGame(my_player, comp_player)
# game
game.play()
