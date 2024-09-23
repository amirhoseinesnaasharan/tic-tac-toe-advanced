import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

# Initialize main window
window = tk.Tk()
window.title("بازی دوز حرفه‌ای")
window.configure(bg='#222222')  # Dark background for modern look

current_player = "X"
# Update scores dictionary to use the icons as keys
scores = {"❤️": 0, "⭐": 0}
buttons = []

# Add player icons
player_icons = {
    "X": "❤️",
    "O": "⭐"
}

def switch_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"

def check_winner():
    # Define winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for combo in winning_combinations:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] and buttons[combo[0]]["text"] != "":
            for idx in combo:
                buttons[idx].config(bg="#00FF00")  # Highlight winning combination in green
            return buttons[combo[0]]["text"]
    
    if all(button["text"] != "" for button in buttons):
        return "Tie"
    
    return None

def button_click(index):
    if buttons[index]["text"] == "":
        buttons[index]["text"] = player_icons[current_player]
        # Set button color based on current player
        if current_player == "X":
            buttons[index].configure(bg='#FF6347', fg='white')  # X player's color (tomato)
        else:
            buttons[index].configure(bg='#4682B4', fg='white')  # O player's color (steel blue)

        winner = check_winner()
        
        if winner:
            if winner == "Tie":
                messagebox.showinfo("بازی دوز", "بازی مساوی شد!")
            else:
                scores[winner] += 1  # Use winner to access correct score
                update_scores()
                messagebox.showinfo("بازی دوز", f"بازیکن {winner} برنده شد!")
            reset_board()
        else:
            switch_player()

def reset_board():
    for button in buttons:
        button["text"] = ""
        button.configure(bg='#333333')  # Reset button background color to dark

def update_scores():
    point_player_one["text"] = scores["❤️"]
    point_player_two["text"] = scores["⭐"]

def points():
    # Create a frame for player labels
    board_frame = tk.Frame(window, bg='#222222')  # Set background color for the frame
    board_frame.grid(row=0, pady=10)
    
    # Label for player 1
    label_player_one = tk.Label(
        board_frame, 
        text="بازیکن شماره 1 (❤️)", 
        font=("Aviny", 18, "bold"),  # Added bold style
        padx=10,
        bg='#222222',  # Background color for label
        fg='#FF6347'  # Text color for label
    )
    
    # Label for player 2
    label_player_two = tk.Label(
        board_frame, 
        text="بازیکن شماره 2 (⭐)", 
        font=("Aviny", 18, "bold"),  # Added bold style
        padx=10,
        bg='#222222',  # Background color for label
        fg='#4682B4'  # Text color for label
    )
    
    # Place the labels in the frame
    label_player_one.grid(row=0, column=0, padx=20)
    label_player_two.grid(row=0, column=1, padx=20)

    # Create a frame for player scores
    point_frame = tk.Frame(window, bg='#222222')  # Set background color for the frame
    point_frame.grid(row=1, pady=10)
    
    # Score label for player 1
    global point_player_one
    point_player_one = tk.Label(
        point_frame,
        text="0",  # Initial score
        padx=20, 
        font=("BYekan", 20, "bold"),  # Added bold style
        bg='#222222',  # Background color for label
        fg='#FF6347'  # Text color for label
    )
    
    # Score label for player 2
    global point_player_two
    point_player_two = tk.Label(
        point_frame,
        text="0",  # Initial score
        padx=20, 
        font=("BYekan", 20, "bold"),  # Added bold style
        bg='#222222',  # Background color for label
        fg='#4682B4'  # Text color for label
    )
    
    # Place the score labels in the frame
    point_player_one.grid(row=0, column=0, padx=10)
    point_player_two.grid(row=0, column=1, padx=10)

def board():
    global buttons
    buttons = []
    counter = 0
    board_frame = tk.Frame(window, bg='#222222')  # Set background color for the frame
    board_frame.grid(row=2, pady=20)
    
    for row in range(3):
        for column in range(3):
            index = counter
            button = tk.Button(
                board_frame, 
                text="", 
                width=10, 
                height=4, 
                font=("Arial", 18, "bold"), 
                bg='#333333',  # Initial button background color
                fg='white',
                command=lambda idx=index: button_click(idx),
                relief="groove",  # Added groove effect for button border
                bd=3  # Added border width
            )
            button.grid(row=row, column=column, padx=5, pady=5)  # Added padding between buttons
            buttons.append(button)
            counter += 1

# Call the function to create the GUI
points()
board()

# Start the main event loop
window.mainloop()
