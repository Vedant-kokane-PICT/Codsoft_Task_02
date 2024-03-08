import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = 'O'

        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.buttons[row][col]['text'] == '' and not self.check_winner():
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner():
                messagebox.showinfo(
                    "Game Over", f"{self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.window.title(
                    f"Tic-Tac-Toe - {self.current_player}'s turn")

    def check_winner(self):
        for i in range(3):
            if all(self.buttons[i][j]['text'] == self.current_player for j in range(3)) or \
               all(self.buttons[j][i]['text'] == self.current_player for j in range(3)):
                return True
        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)) or \
           all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3))

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''
        self.current_player = 'O'
        self.window.title("Tic-Tac-Toe")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    TicTacToeGUI().run()
