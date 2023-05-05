import random

moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.score = 0

        self.their_move = ''
        self.my_move = ''

    def move(self):
        return 'Rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move
        self.my_move = my_move


class ReflectPlayer(Player):

    def move(self):
        if self.their_move not in moves:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):

    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return random.choice(moves)


class RandomPlayer(Player):

    def move(self):

        return random.choice(moves)


class HumanPlayer(Player):

    def move(self):
        return input('what is your move ? rock'
                     ' or paper or scissors?or Q to Quit \n').lower()


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.score = 0

    def beats(self, one, two):
        if one == 'rock' and two == 'scissors' or one == 'scissors' \
         and two == 'paper' or one == 'paper' and two == 'rock':
            self.p1.score += 1
            print('you lose!')
        elif one == two:

            print('its a draw!')
        else:

            self.p2.score += 1
            print('you win!')
        print(f'the score is {self.p1.score} for player 1'
              f'And {self.p2.score} for player 2')

    def play_round(self):
        move1 = self.p1.move()
        while True:
            move2 = self.p2.move()
            if move2 == 'q':
                print('goodbye')
                exit()

            if move2 in moves:
                print(f'Player 1 : {move1}  Player: {move2}')
                self.beats(move1, move2)
                self.p1.learn(move1, move2)
                self.p2.learn(move1, move2)

                break

    def play_game(self):
        print('Game start!')
        round = 0
        while self.p2.score < 3 and self.p1.score < 3:
            round += 1
            print(f'Round {round}:')
            self.play_round()

        print('Game over!')

        if self.p1.score < self.p2.score:
            print('Player1 is the winner ')
        else:
            print('Player2 is the winner ')


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
