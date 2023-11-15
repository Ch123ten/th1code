import tkinter as tk
from tkinter import messagebox

def check_winner():
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

def on_click(row, col):
    global player
    if buttons[row][col]['text'] == '':
        buttons[row][col]['text'] = player
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {player} wins!")
            reset_board()
        elif all(buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_board()
        else:
            player = 'O' if player == 'X' else 'X'

def reset_board():
    global player
    player = 'X'
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[0]*3 for _ in range(3)]
player = 'X'

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Arial', 20), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text='Reset', font=('Arial', 14), command=reset_board)
reset_button.grid(row=3, columnspan=3)

root.mainloop()