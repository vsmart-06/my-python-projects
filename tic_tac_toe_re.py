import tkinter as tk
import random as rd

play = 1
user_score = 0
comp_score = 0

while play == 1:
    window_game = tk.Tk()
    window_game.title("Tic-Tac-Toe")
    window_end = tk.Tk()
    window_end.title("Tic-Tac-Toe")
    window_end.withdraw()
    screen1 = 1
    user_symbol = ""
    comp_symbol = ""
    choice_list = [11, 12, 13, 21, 22, 23, 31, 32, 33]
    symbol_list = ["", "", "", "", "", "", "", "", ""]
    symbol_choice = ["X", "O"]
    row_1 = [symbol_list[0], symbol_list[1], symbol_list[2]]
    row_2 = [symbol_list[3], symbol_list[4], symbol_list[5]]
    row_3 = [symbol_list[6], symbol_list[7], symbol_list[8]]
    column_1 = [symbol_list[0], symbol_list[3], symbol_list[6]]
    column_2 = [symbol_list[1], symbol_list[4], symbol_list[7]]
    column_3 = [symbol_list[2], symbol_list[5], symbol_list[8]]
    diagonal_1 = [symbol_list[0], symbol_list[4], symbol_list[8]]
    diagonal_2 = [symbol_list[2], symbol_list[4], symbol_list[6]]
    turn = "user"
    comp_choice = 0
    turns_over = 0
    game_over = 0

    def symbol_press_x():
        global screen1, user_symbol, comp_symbol
        if screen1 == 1:
            user_symbol = "X"
            comp_symbol = "O"
        screen1 = 0
        remove_and_place_screen(screen1)

    def symbol_press_o():
        global screen1, user_symbol, comp_symbol
        if screen1 == 1:
            user_symbol = "O"
            comp_symbol = "X"
        screen1 = 0
        remove_and_place_screen(screen1)

    def symbol_press_xo():
        global screen1, user_symbol, comp_symbol, symbol_choice
        if screen1 == 1:
            user_symbol = rd.choice(symbol_choice)
            symbol_choice.remove(user_symbol)
            comp_symbol = symbol_choice[0]
            symbol_choice.remove(comp_symbol)
        screen1 = 0
        remove_and_place_screen(screen1)

    def remove_and_place_screen(a):
        if a == 0:
            x_button.grid_remove()
            o_button.grid_remove()
            button_11.grid(row = 0, column = 0)
            button_12.grid(row = 0, column = 1)
            button_13.grid(row = 0, column = 2)
            button_21.grid(row = 1, column = 0)
            button_22.grid(row = 1, column = 1)
            button_23.grid(row = 1, column = 2)
            button_31.grid(row = 2, column = 0)
            button_32.grid(row = 2, column = 1)
            button_33.grid(row = 2, column = 2)

    def play_again():
        global play
        window_end.destroy()
        play = 1

    def end_game():
        global play
        window_end.destroy()
        play = 0    

    def is_game_over():
        global symbol_list, user_symbol, comp_symbol, game_over, turns_over, user_score, comp_score, row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2
        row_1 = [symbol_list[0], symbol_list[1], symbol_list[2]]
        row_2 = [symbol_list[3], symbol_list[4], symbol_list[5]]
        row_3 = [symbol_list[6], symbol_list[7], symbol_list[8]]
        column_1 = [symbol_list[0], symbol_list[3], symbol_list[6]]
        column_2 = [symbol_list[1], symbol_list[4], symbol_list[7]]
        column_3 = [symbol_list[2], symbol_list[5], symbol_list[8]]
        diagonal_1 = [symbol_list[0], symbol_list[4], symbol_list[8]]
        diagonal_2 = [symbol_list[2], symbol_list[4], symbol_list[6]]
        if row_1==[user_symbol, user_symbol, user_symbol] or row_2==[user_symbol, user_symbol, user_symbol] or row_3==[user_symbol, user_symbol, user_symbol] or column_1==[user_symbol, user_symbol, user_symbol] or column_2==[user_symbol, user_symbol, user_symbol] or column_3==[user_symbol, user_symbol, user_symbol] or diagonal_1==[user_symbol, user_symbol, user_symbol] or diagonal_2==[user_symbol, user_symbol, user_symbol]:
            game_over = 1
            user_score += 1
            window_game.destroy()
            window_end.deiconify()
            label_finish = tk.Label(window_end, text = "You win!")
            label_finish.grid(row = 0, column = 0)
            label_user_score = tk.Label(window_end, text = "Your score:")
            label_user_score.grid(row = 1, column = 0)
            label_user_number = tk.Label(window_end, text = user_score)
            label_user_number.grid(row = 1, column = 1)
            label_comp_score = tk.Label(window_end, text = "Computer's score:")
            label_comp_score.grid(row = 2, column = 0)
            label_comp_number = tk.Label(window_end, text = comp_score)
            label_comp_number.grid(row = 2, column = 1)
            play_again_button = tk.Button(window_end, text = "Play Again", command = play_again)
            play_again_button.grid(row = 3, column = 0)
            end_button = tk.Button(window_end, text = "End Game", command = end_game)
            end_button.grid(row = 4, column = 0)
        elif row_1==[comp_symbol, comp_symbol, comp_symbol] or row_2==[comp_symbol, comp_symbol, comp_symbol] or row_3==[comp_symbol, comp_symbol, comp_symbol] or column_1==[comp_symbol, comp_symbol, comp_symbol] or column_2==[comp_symbol, comp_symbol, comp_symbol] or column_3==[comp_symbol, comp_symbol, comp_symbol] or diagonal_1==[comp_symbol, comp_symbol, comp_symbol] or diagonal_2==[comp_symbol, comp_symbol, comp_symbol]:
            game_over = 1
            comp_score += 1
            window_game.destroy()
            window_end.deiconify()
            label_finish = tk.Label(window_end, text = "You lost :(")
            label_finish.grid(row = 0, column = 0)
            label_user_score = tk.Label(window_end, text = "Your score:")
            label_user_score.grid(row = 1, column = 0)
            label_user_number = tk.Label(window_end, text = user_score)
            label_user_number.grid(row = 1, column = 1)
            label_comp_score = tk.Label(window_end, text = "Computer's score:")
            label_comp_score.grid(row = 2, column = 0)
            label_comp_number = tk.Label(window_end, text = comp_score)
            label_comp_number.grid(row = 2, column = 1)
            play_again_button = tk.Button(window_end, text = "Play Again", command = play_again)
            play_again_button.grid(row = 3, column = 0)
            end_button = tk.Button(window_end, text = "End Game", command = end_game)
            end_button.grid(row = 4, column = 0)
        elif turns_over == 9:
            window_game.destroy()
            window_end.deiconify()
            label_finish = tk.Label(window_end, text = "It's a tie!")
            label_finish.grid(row = 0, column = 0)
            label_user_score = tk.Label(window_end, text = "Your score:")
            label_user_score.grid(row = 1, column = 0)
            label_user_number = tk.Label(window_end, text = user_score)
            label_user_number.grid(row = 1, column = 1)
            label_comp_score = tk.Label(window_end, text = "Computer's score:")
            label_comp_score.grid(row = 2, column = 0)
            label_comp_number = tk.Label(window_end, text = comp_score)
            label_comp_number.grid(row = 2, column = 1)
            play_again_button = tk.Button(window_end, text = "Play Again", command = play_again)
            play_again_button.grid(row = 3, column = 0)
            end_button = tk.Button(window_end, text = "End Game", command = end_game)
            end_button.grid(row = 4, column = 0)

    def button_press(loc):
        global choice_list, symbol_list, turn, comp_choice, user_symbol, comp_symbol, turns_over, game_over, row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2
        choice_list.remove(loc)
        if turn == "user":
            if loc == 11:
                button_11.grid_remove()
                label_11 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_11.grid(row = 0, column = 0)
                symbol_list[0] = user_symbol
            elif loc == 12:
                button_12.grid_remove()
                label_12 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_12.grid(row = 0, column = 1)
                symbol_list[1] = user_symbol
            elif loc == 13:
                button_13.grid_remove()
                label_13 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_13.grid(row = 0, column = 2)
                symbol_list[2] = user_symbol
            elif loc == 21:
                button_21.grid_remove()
                label_21 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_21.grid(row = 1, column = 0)
                symbol_list[3] = user_symbol
            elif loc == 22:
                button_22.grid_remove()
                label_22 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_22.grid(row = 1, column = 1)
                symbol_list[4] = user_symbol
            elif loc == 23:
                button_23.grid_remove()
                label_23 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_23.grid(row = 1, column = 2)
                symbol_list[5] = user_symbol
            elif loc == 31:
                button_31.grid_remove()
                label_31 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_31.grid(row = 2, column = 0)
                symbol_list[6] = user_symbol
            elif loc == 32:
                button_32.grid_remove()
                label_32 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_32.grid(row = 2, column = 1)
                symbol_list[7] = user_symbol
            elif loc == 33:
                button_33.grid_remove()
                label_33 = tk.Label(window_game, text = user_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_33.grid(row = 2, column = 2)
                symbol_list[8] = user_symbol
            turns_over += 1
            is_game_over()
            if turns_over < 9 and game_over == 0:
                turn = "comp"
                if row_1 == [comp_symbol, comp_symbol, ""] or column_3 == ["", comp_symbol, comp_symbol] or diagonal_2 == ["", comp_symbol, comp_symbol]:
                    comp_choice = 13
                elif row_1 == [comp_symbol, "", comp_symbol] or column_2 == ["", comp_symbol, comp_symbol]:
                    comp_choice = 12
                elif row_1 == ["", comp_symbol, comp_symbol] or column_1 == ["", comp_symbol, comp_symbol] or diagonal_1 == ["", comp_symbol, comp_symbol]:
                    comp_choice = 11
                elif row_2 == [comp_symbol, comp_symbol, ""] or column_3 == [comp_symbol, "", comp_symbol]:
                    comp_choice = 23
                elif row_2 == [comp_symbol, "", comp_symbol] or column_2 == [comp_symbol, "", comp_symbol] or diagonal_1 == [comp_symbol, "", comp_symbol] or diagonal_2 == [comp_symbol, "", comp_symbol]:
                    comp_choice = 22
                elif row_2 == ["", comp_symbol, comp_symbol] or column_1 == [comp_symbol, "", comp_symbol]:
                    comp_choice = 21
                elif row_3 == [comp_symbol, comp_symbol, ""] or column_3 == [comp_symbol, comp_symbol, ""] or diagonal_1 == [comp_symbol, comp_symbol, ""]:
                    comp_choice = 33
                elif row_3 == [comp_symbol, "", comp_symbol] or column_2 == [comp_symbol, comp_symbol, ""]:
                    comp_choice = 32
                elif row_3 == ["", comp_symbol, comp_symbol] or column_1 == [comp_symbol, comp_symbol, ""] or diagonal_2 == [comp_symbol, comp_symbol, ""]:
                    comp_choice = 31
                elif row_1 == [user_symbol, user_symbol, ""] or column_3 == ["", user_symbol, user_symbol] or diagonal_2 == ["", user_symbol, user_symbol]:
                    comp_choice = 13
                elif row_1 == [user_symbol, "", user_symbol] or column_2 == ["", user_symbol, user_symbol]:
                    comp_choice = 12
                elif row_1 == ["", user_symbol, user_symbol] or column_1 == ["", user_symbol, user_symbol] or diagonal_1 == ["", user_symbol, user_symbol]:
                    comp_choice = 11
                elif row_2 == [user_symbol, user_symbol, ""] or column_3 == [user_symbol, "", user_symbol]:
                    comp_choice = 23
                elif row_2 == [user_symbol, "", user_symbol] or column_2 == [user_symbol, "", user_symbol] or diagonal_1 == [user_symbol, "", user_symbol] or diagonal_2 == [user_symbol, "", user_symbol]:
                    comp_choice = 22
                elif row_2 == ["", user_symbol, user_symbol] or column_1 == [user_symbol, "", user_symbol]:
                    comp_choice = 21
                elif row_3 == [user_symbol, user_symbol, ""] or column_3 == [user_symbol, user_symbol, ""] or diagonal_1 == [user_symbol, user_symbol, ""]:
                    comp_choice = 33
                elif row_3 == [user_symbol, "", user_symbol] or column_2 == [user_symbol, user_symbol, ""]:
                    comp_choice = 32
                elif row_3 == ["", user_symbol, user_symbol] or column_1 == [user_symbol, user_symbol, ""] or diagonal_2 == [user_symbol, user_symbol, ""]:
                    comp_choice = 31
                else:                    
                    comp_choice = rd.choice(choice_list)
                button_press(comp_choice)
        if turn == "comp":
            if loc == 11:
                button_11.grid_remove()
                label_11 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_11.grid(row = 0, column = 0)
                symbol_list[0] = comp_symbol
            elif loc == 12:
                button_12.grid_remove()
                label_12 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_12.grid(row = 0, column = 1)
                symbol_list[1] = comp_symbol
            elif loc == 13:
                button_13.grid_remove()
                label_13 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_13.grid(row = 0, column = 2)
                symbol_list[2] = comp_symbol
            elif loc == 21:
                button_21.grid_remove()
                label_21 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_21.grid(row = 1, column = 0)
                symbol_list[3] = comp_symbol
            elif loc == 22:
                button_22.grid_remove()
                label_22 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_22.grid(row = 1, column = 1)
                symbol_list[4] = comp_symbol
            elif loc == 23:
                button_23.grid_remove()
                label_23 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_23.grid(row = 1, column = 2)
                symbol_list[5] = comp_symbol
            elif loc == 31:
                button_31.grid_remove()
                label_31 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_31.grid(row = 2, column = 0)
                symbol_list[6] = comp_symbol
            elif loc == 32:
                button_32.grid_remove()
                label_32 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_32.grid(row = 2, column = 1)
                symbol_list[7] = comp_symbol
            elif loc == 33:
                button_33.grid_remove()
                label_33 = tk.Label(window_game, text = comp_symbol, height = 3, width = 6, borderwidth = 1, relief = "solid")
                label_33.grid(row = 2, column = 2)
                symbol_list[8] = comp_symbol
            turn = "user"
            turns_over += 1
            is_game_over()

    x_button = tk.Button(window_game, text = "X", height = 3, width = 6, command = symbol_press_x)
    x_button.grid(row = 1, column = 0)

    o_button = tk.Button(window_game, text = "O", height = 3, width = 6, command = symbol_press_o)
    o_button.grid(row = 1, column = 1)

    xo_button = tk.Button(window_game, text = "Random", height = 3, width = 6, command = symbol_press_xo)
    xo_button.grid(row = 1, column = 2)

    button_11 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 11: button_press(loc))
    button_12 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 12: button_press(loc))
    button_13 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 13: button_press(loc))
    button_21 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 21: button_press(loc))
    button_22 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 22: button_press(loc))
    button_23 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 23: button_press(loc))
    button_31 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 31: button_press(loc))
    button_32 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 32: button_press(loc))
    button_33 = tk.Button(window_game, height = 3, width = 6, command = lambda loc = 33: button_press(loc))

    window_game.mainloop()
    window_end.mainloop()