import utils


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0

    def __str__(self):
        return f"{self.name} ({self.symbol})"

    @staticmethod
    def symbol_of(player):
        return player.symbol if player is not None else " "


class TicTacToe:
    def __init__(self, players):
        self.players = players
        self.field = utils.new_field()
        self.curr_player = 0

    def pretty_print_field(self):
        print("  1 2 3")
        for i in range(3):
            print(i + 1,
                  " ".join(map(Player.symbol_of, self.field[i])))

    @staticmethod
    def print_players(players):
        print("#", "Players:", ", ".join(map(str, players)))

    @staticmethod
    def play_set(players, wins=5):
        print("#", f"Playing a set (wins={wins}).")
        TicTacToe.print_players(players)

        ttt = TicTacToe(players)
        while all([player.score < wins for player in players]):
            winner = ttt._play_round()
            if winner:
                winner.score += 1
            # print scores
            # print("# Scores:")
            for player in players:
                print(f"{player}: {player.score} / {wins} wins")
            print()  # newline to seperate rounds
            ttt.field = utils.new_field()

        # never none
        winner = list(filter(lambda player: player.score == wins, players))[0]
        print(f"{winner} won this set!")
        return winner

    @staticmethod
    def play_round(players):
        print("#", "Playing a round.")
        TicTacToe.print_players(players)
        winner = TicTacToe(players)._play_round()
        return winner  # possibly None

    def _play_round(self):
        while True:
            # play moves as long as there is no winner
            winner = self._check_win()
            if winner or self._check_full():
                break

            self.pretty_print_field()  # print field
            self._play_move()
            print()  # newline to seperate moves

        # when win or draw
        self.pretty_print_field()
        if winner:
            print("#", f"{winner} won this round!")
        else:
            print("#", "This round was a draw!")
        return winner

    def _play_move(self):
        # currently active player
        player = players[self.curr_player]
        # input coordinates
        coords = utils.input_coords(f"{player}, please select coordinates: ")
        # assert that selected cell is not filled yet
        if self.field[coords[0]][coords[1]]:
            print("This cell is already filled! Please try again!")
            self._play_move()  # retry
            return  # stop - do not overwrite cell
        self.field[coords[0]][coords[1]] = player
        self._switch_player()

    def _switch_player(self):
        self.curr_player = 1 - self.curr_player

    # checks if any player has won, if true then return that player
    def _check_win(self):
        for player in players:
            pfield = [[cell is player for cell in row] for row in self.field]
            row = any(map(all, pfield))  # any row, all cell (in a row)
            column = any(map(all, zip(*pfield)))  # any column, all cells
            diagonal = pfield[0][0] and pfield[1][1] and pfield[2][2] or \
                pfield[0][2] and pfield[1][1] and pfield[2][0]
            # result
            if row or column or diagonal:
                return player
        return None

    def _check_full(self):
        return all(map(all, self.field))  # all cells are filled


# setup players
player1 = Player("Player 1", "O")
player2 = Player("Player 2", "X")
players = [player1, player2]

# ttt = TicTacToe(players)
TicTacToe.play_set(players)
