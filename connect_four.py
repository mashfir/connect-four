import numpy as np
from scipy.signal import convolve2d

BOARD_ROWS = 6
BOARD_COLS = 7


class ConnectFour:
    def __init__(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        self.player_turn = 2

    def initialize(self):
        self.board = np.zeros((BOARD_ROWS, BOARD_COLS))
        print("New game started")
        print(self.board)

    def check_allowed(self, column):
        if 0 <= column <= BOARD_COLS - 1:
            if (self.board[:, column] == 0).all() or (
                self.board[:, column] == 0
            ).argmin() > 0:
                return True
            else:
                print("Column full, try again")
                return False  # TODO add more precise exit routine to loop back to take_turn
        else:
            print("Out of range, try again")
            return False

    def check_win(self):
        """
        Taken from StackOverflow
        https://stackoverflow.com/a/63991845
        """
        h_kernel = np.array([[1, 1, 1, 1]])
        v_kernel = np.transpose(h_kernel)
        d1_kernel = np.eye(4)
        d2_kernel = np.fliplr(d1_kernel)
        detection_kernels = [h_kernel, v_kernel, d1_kernel, d2_kernel]
        detection_board = np.where(self.board == self.player_turn, self.player_turn, 0)

        for kernel in detection_kernels:
            if (
                convolve2d(detection_board == self.player_turn, kernel, mode="valid")
                == 4
            ).any():
                return True
        return False

    def check_full(self):
        return np.all(self.board != 0)

    def take_turn(self):
        col = input(
            "Player " + str(self.player_turn) + ", select column to place checker: "
        )
        col = int(col)
        self.check_allowed(col)
        free_row = (self.board[:, col] == 0).argmin() - 1
        self.board[free_row, col] = self.player_turn
        print(self.board)
        print("Checker placed in column " + str(col))

    def play(self):
        self.initialize()
        while not self.check_win() and not self.check_full():
            if self.player_turn == 1:
                self.player_turn = 2
            else:
                self.player_turn = 1
            self.take_turn()
        if self.check_full():
            print("Game is a draw")
        else:
            print("Player " + str(self.player_turn) + " wins!")
        exit()


def main():
    game = ConnectFour()
    game.play()


if __name__ == "__main__":
    main()
