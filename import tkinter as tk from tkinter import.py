import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("XO Game")
root.geometry("320x380")
root.resizable(False, False)

# Variables
current_player = "X"
board = ["" for _ in range(9)]
buttons = []

# Winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Status label
status_label = tk.Label(root, text="Player X Turn", font=("Arial", 18))
status_label.pack(pady=10)

# Frame for game board
frame = tk.Frame(root)
frame.pack()


def check_winner():
    global current_player

    for combo in winning_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c] != "":
            messagebox.showinfo("Winner", f"🎉 Player {current_player} Wins!")
            disable_buttons()
            return

    if "" not in board:
        messagebox.showinfo("Draw", "🤝 Match Draw!")
        return

    # Switch player
    current_player = "O" if current_player == "X" else "X"
    status_label.config(text=f"Player {current_player} Turn")


def button_click(index):
    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)
        check_winner()


def disable_buttons():
    for button in buttons:
        button.config(state="disabled")


# Restart game
def restart_game():
    global current_player, board

    current_player = "X"
    board = ["" for _ in range(9)]

    status_label.config(text="Player X Turn")

    for button in buttons:
        button.config(text="", state="normal")


# Create buttons
for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 24),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Restart button
restart_btn = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14),
    command=restart_game,
    bg="orange",
    fg="white"
)

restart_btn.pack(pady=20)

# Run application
root.mainloop()