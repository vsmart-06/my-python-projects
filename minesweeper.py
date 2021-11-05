import tkinter as tk
import random as rd
play = 1
while play == 1:
    row_1 = ["", "", "", "", "", "", "", ""]
    row_2 = ["", "", "", "", "", "", "", ""]
    row_3 = ["", "", "", "", "", "", "", ""]
    row_4 = ["", "", "", "", "", "", "", ""]
    row_5 = ["", "", "", "", "", "", "", ""]
    row_6 = ["", "", "", "", "", "", "", ""]
    row_7 = ["", "", "", "", "", "", "", ""]
    row_8 = ["", "", "", "", "", "", "", ""]
    choice_row = [1, 2, 3, 4, 5, 6, 7, 8]
    choice_column = [1, 2, 3, 4, 5, 6, 7, 8]
    bomb_list = []
    for count in range(1, 9):
        row_pos = str(rd.choice(choice_row))
        column_pos = str(rd.choice(choice_column))
        bomb_loc = int(row_pos + column_pos)
        for ind in range(0, len(bomb_list)):
            if bomb_loc == bomb_list[ind]:
                row_pos = str(rd.choice(choice_row))
                column_pos = str(rd.choice(choice_column))
                bomb_loc = int(row_pos + column_pos)
        bomb_list.append(bomb_loc)
    for loc in bomb_list:
        str_loc = str(loc)
        index = int(str_loc[1])-1
        if int(str_loc[0]) == 1:
            row_1[index] = "💣"
        elif int(str_loc[0]) == 2:
            row_2[index] = "💣"
        elif int(str_loc[0]) == 3:
            row_3[index] = "💣"
        elif int(str_loc[0]) == 4:
            row_4[index] = "💣"
        elif int(str_loc[0]) == 5:
            row_5[index] = "💣"
        elif int(str_loc[0]) == 6:
            row_6[index] = "💣"
        elif int(str_loc[0]) == 7:
            row_7[index] = "💣"
        elif int(str_loc[0]) == 8:
            row_8[index] = "💣"

    for row in choice_row:
        for column in choice_column:
            ind_col = column - 1
            ind_col_prev = ind_col - 1
            ind_col_next = ind_col + 1
            if row == 1:
                if row_1[ind_col] != "💣":
                    num = 0
                    if row_2[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_1[ind_col_prev] == "💣":
                            num += 1
                        if row_2[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_1[ind_col_next] == "💣":
                            num += 1
                        if row_2[ind_col_next] == "💣":
                            num += 1
                    row_1[ind_col] = num
            elif row == 2:
                if row_2[ind_col] != "💣":
                    num = 0
                    if row_1[ind_col] == "💣":
                        num += 1
                    if row_3[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_1[ind_col_prev] == "💣":
                            num += 1
                        if row_2[ind_col_prev] == "💣":
                            num += 1
                        if row_3[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_1[ind_col_next] == "💣":
                            num += 1
                        if row_2[ind_col_next] == "💣":
                            num += 1
                        if row_3[ind_col_next] == "💣":
                            num += 1
                    row_2[ind_col] = num
            elif row == 3:
                if row_3[ind_col] != "💣":
                    num = 0
                    if row_2[ind_col] == "💣":
                        num += 1
                    if row_4[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_2[ind_col_prev] == "💣":
                            num += 1
                        if row_3[ind_col_prev] == "💣":
                            num += 1
                        if row_4[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_2[ind_col_next] == "💣":
                            num += 1
                        if row_3[ind_col_next] == "💣":
                            num += 1
                        if row_4[ind_col_next] == "💣":
                            num += 1
                    row_3[ind_col] = num
            elif row == 4:
                if row_4[ind_col] != "💣":
                    num = 0
                    if row_3[ind_col] == "💣":
                        num += 1
                    if row_5[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_3[ind_col_prev] == "💣":
                            num += 1
                        if row_4[ind_col_prev] == "💣":
                            num += 1
                        if row_5[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_3[ind_col_next] == "💣":
                            num += 1
                        if row_4[ind_col_next] == "💣":
                            num += 1
                        if row_5[ind_col_next] == "💣":
                            num += 1
                    row_4[ind_col] = num
            elif row == 5:
                if row_5[ind_col] != "💣":
                    num = 0
                    if row_4[ind_col] == "💣":
                        num += 1
                    if row_6[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_4[ind_col_prev] == "💣":
                            num += 1
                        if row_5[ind_col_prev] == "💣":
                            num += 1
                        if row_6[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_4[ind_col_next] == "💣":
                            num += 1
                        if row_5[ind_col_next] == "💣":
                            num += 1
                        if row_6[ind_col_next] == "💣":
                            num += 1
                    row_5[ind_col] = num
            elif row == 6:
                if row_6[ind_col] != "💣":
                    num = 0
                    if row_5[ind_col] == "💣":
                        num += 1
                    if row_7[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_5[ind_col_prev] == "💣":
                            num += 1
                        if row_6[ind_col_prev] == "💣":
                            num += 1
                        if row_7[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_5[ind_col_next] == "💣":
                            num += 1
                        if row_6[ind_col_next] == "💣":
                            num += 1
                        if row_7[ind_col_next] == "💣":
                            num += 1
                    row_6[ind_col] = num
            elif row == 7:
                if row_7[ind_col] != "💣":
                    num = 0
                    if row_6[ind_col] == "💣":
                        num += 1
                    if row_8[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_6[ind_col_prev] == "💣":
                            num += 1
                        if row_7[ind_col_prev] == "💣":
                            num += 1
                        if row_8[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_6[ind_col_next] == "💣":
                            num += 1
                        if row_7[ind_col_next] == "💣":
                            num += 1
                        if row_8[ind_col_next] == "💣":
                            num += 1
                    row_7[ind_col] = num
            elif row == 8:
                if row_8[ind_col] != "💣":
                    num = 0
                    if row_7[ind_col] == "💣":
                        num += 1
                    if ind_col_prev >= 0:
                        if row_7[ind_col_prev] == "💣":
                            num += 1
                        if row_8[ind_col_prev] == "💣":
                            num += 1
                    if ind_col_next <= 7:
                        if row_7[ind_col_next] == "💣":
                            num += 1
                        if row_8[ind_col_next] == "💣":
                            num += 1
                    row_8[ind_col] = num
    

    window = tk.Tk()
    window.title("Minesweeper")
    window_end = tk.Tk()
    window_end.title("Minesweeper")
    window_end.withdraw()

    row_1_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_2_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_3_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_4_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_5_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_6_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_7_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]
    row_8_stat = ["alive", "alive", "alive", "alive", "alive", "alive", "alive", "alive"]

    flag_11 = 0
    flag_12 = 0
    flag_13 = 0
    flag_14 = 0
    flag_15 = 0
    flag_16 = 0
    flag_17 = 0
    flag_18 = 0
    flag_21 = 0
    flag_22 = 0
    flag_23 = 0
    flag_24 = 0
    flag_25 = 0
    flag_26 = 0
    flag_27 = 0
    flag_28 = 0
    flag_31 = 0
    flag_32 = 0
    flag_33 = 0
    flag_34 = 0
    flag_35 = 0
    flag_36 = 0
    flag_37 = 0
    flag_38 = 0
    flag_41 = 0
    flag_42 = 0
    flag_43 = 0
    flag_44 = 0
    flag_45 = 0
    flag_46 = 0
    flag_47 = 0
    flag_48 = 0
    flag_51 = 0
    flag_52 = 0
    flag_53 = 0
    flag_54 = 0
    flag_55 = 0
    flag_56 = 0
    flag_57 = 0
    flag_58 = 0
    flag_61 = 0
    flag_62 = 0
    flag_63 = 0
    flag_64 = 0
    flag_65 = 0
    flag_66 = 0
    flag_67 = 0
    flag_68 = 0
    flag_71 = 0
    flag_72 = 0
    flag_73 = 0
    flag_74 = 0
    flag_75 = 0
    flag_76 = 0
    flag_77 = 0
    flag_78 = 0
    flag_81 = 0
    flag_82 = 0
    flag_83 = 0
    flag_84 = 0
    flag_85 = 0
    flag_86 = 0
    flag_87 = 0
    flag_88 = 0

    game_over = 0
    turns = 0

    flag_on = 0
    def flag_press():
        global flag_on
        if flag_on == 0:
            button_flag.config(background = "Red")
            flag_on = 1
        elif flag_on == 1:
            button_flag.config(background = "Blue")
            flag_on = 0

    def game_end():
        global game_over, turns
        if game_over == 1:
            msg = "You lost :("
        elif turns == 56:
            msg = "You win!"
        window.destroy()
        window_end.deiconify()
        label = tk.Label(window_end, text = msg)
        label.pack()
        button_play = tk.Button(window_end, text = "Play Again", command = lambda m = "play": end_but(m))
        button_end = tk.Button(window_end, text = "End Game", command = lambda m = "end": end_but(m))
        button_play.pack()
        button_end.pack()

    def end_but(but):
        global play
        window_end.destroy()
        if but == "end":
            play = 0
        if but == "play":
            play = 1

    def button_press(loc):
        global flag_on, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_1_stat, row_2_stat, row_3_stat, row_4_stat, row_5_stat, row_6_stat, row_7_stat, row_8_stat, flag_11, flag_12, flag_13, flag_14, flag_15, flag_16, flag_17, flag_18, flag_21, flag_22, flag_23, flag_24, flag_25, flag_26, flag_27, flag_28, flag_31, flag_32, flag_33, flag_34, flag_35, flag_36, flag_37, flag_38, flag_41, flag_42, flag_43, flag_44, flag_45, flag_46, flag_47, flag_48, flag_51, flag_52, flag_53, flag_54, flag_55, flag_56, flag_57, flag_58, flag_61, flag_62, flag_63, flag_64, flag_65, flag_66, flag_67, flag_68, flag_71, flag_72, flag_73, flag_74, flag_75, flag_76, flag_77, flag_78, flag_81, flag_82, flag_83, flag_84, flag_85, flag_86, flag_87, flag_88, game_over, turns
        if flag_on == 0:
            loc_ind = int(str(loc-1)[1])
            if loc == 11:
                button_11.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_11 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_11 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[1] == "alive":
                        button_press(12)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_2_stat[0] == "alive":
                        button_press(21)
                else:
                    label_11 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_11.grid(row = 1, column = 0)
            
            elif loc == 12:
                button_12.grid_remove()     
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_12 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_12 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[0] == "alive":
                        button_press(11)
                    if row_2_stat[0] == "alive":
                        button_press(21)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_1_stat[2] == "alive":
                        button_press(13)
                else:
                    label_12 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_12.grid(row = 1, column = 1)

            elif loc == 13:
                button_13.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_13 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_13 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[1] == "alive":
                        button_press(12)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_1_stat[3] == "alive":
                        button_press(14)
                else:
                    label_13 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_13.grid(row = 1, column = 2)

            elif loc == 14:
                button_14.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_14 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_14 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[2] == "alive":
                        button_press(13)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_1_stat[4] == "alive":
                        button_press(15)
                else:
                    label_14 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_14.grid(row = 1, column = 3)

            elif loc == 15:
                button_15.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_15 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_15 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[3] == "alive":
                        button_press(14)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_1_stat[5] == "alive":
                        button_press(16)
                else:
                    label_15 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_15.grid(row = 1, column = 4)

            elif loc == 16:
                button_16.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_16 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_16 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[4] == "alive":
                        button_press(15)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_1_stat[6] == "alive":
                        button_press(17)
                else:
                    label_16 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_16.grid(row = 1, column = 5)

            elif loc == 17:
                button_17.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_17 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_17 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[5] == "alive":
                        button_press(16)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_2_stat[7] == "alive":
                        button_press(28)
                    if row_1_stat[7] == "alive":
                        button_press(18)
                else:
                    label_17 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_17.grid(row = 1, column = 6)

            elif loc == 18:
                button_18.grid_remove()
                row_1_stat[loc_ind] = "dead"
                obj = row_1[loc_ind]
                turns += 1
                if obj == "💣":
                    label_18 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_18 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[6] == "alive":
                        button_press(17)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_2_stat[7] == "alive":
                        button_press(28)
                else:
                    label_18 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_18.grid(row = 1, column = 7)

            elif loc == 21:
                button_21.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_21 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_21 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[0] == "alive":
                        button_press(11)
                    if row_1_stat[1] == "alive":
                        button_press(12)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_3_stat[0] == "alive":
                        button_press(31)
                else:
                    label_21 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_21.grid(row = 2, column = 0)

            elif loc == 22:
                button_22.grid_remove()     
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_22 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_22 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[0] == "alive":
                        button_press(11)
                    if row_2_stat[0] == "alive":
                        button_press(21)
                    if row_3_stat[0] == "alive":
                        button_press(31)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_1_stat[2] == "alive":
                        button_press(13)
                    if row_1_stat[1] == "alive":
                        button_press(12)
                else:
                    label_22 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_22.grid(row = 2, column = 1)

            elif loc == 23:
                button_23.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_23 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_23 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[1] == "alive":
                        button_press(12)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_1_stat[3] == "alive":
                        button_press(14)
                    if row_1_stat[2] == "alive":
                        button_press(13)
                else:
                    label_23 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_23.grid(row = 2, column = 2)

            elif loc == 24:
                button_24.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_24 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_24 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[2] == "alive":
                        button_press(13)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_1_stat[4] == "alive":
                        button_press(15)
                    if row_1_stat[3] == "alive":
                        button_press(14)
                else:
                    label_24 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_24.grid(row = 2, column = 3)

            elif loc == 25:
                button_25.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_25 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_25 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[3] == "alive":
                        button_press(14)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_1_stat[5] == "alive":
                        button_press(16)
                    if row_1_stat[4] == "alive":
                        button_press(15)
                else:
                    label_25 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_25.grid(row = 2, column = 4)

            elif loc == 26:
                button_26.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_26 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_26 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[4] == "alive":
                        button_press(15)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_1_stat[6] == "alive":
                        button_press(17)
                    if row_1_stat[5] == "alive":
                        button_press(16)
                else:
                    label_26 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_26.grid(row = 2, column = 5)

            elif loc == 27:
                button_27.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_27 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_27 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[5] == "alive":
                        button_press(16)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_3_stat[7] == "alive":
                        button_press(38)
                    if row_2_stat[7] == "alive":
                        button_press(28)
                    if row_1_stat[7] == "alive":
                        button_press(18)
                    if row_1_stat[6] == "alive":
                        button_press(17)
                else:
                    label_27 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_27.grid(row = 2, column = 6)

            elif loc == 28:
                button_28.grid_remove()
                row_2_stat[loc_ind] = "dead"
                obj = row_2[loc_ind]
                turns += 1
                if obj == "💣":
                    label_28 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_28 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_1_stat[6] == "alive":
                        button_press(17)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_3_stat[7] == "alive":
                        button_press(38)
                    if row_1_stat[7] == "alive":
                        button_press(18)
                else:
                    label_28 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_28.grid(row = 2, column = 7)

            elif loc == 31:
                button_31.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_31 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_31 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[0] == "alive":
                        button_press(21)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_4_stat[0] == "alive":
                        button_press(41)
                else:
                    label_31 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_31.grid(row = 3, column = 0)

            elif loc == 32:
                button_32.grid_remove()     
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_32 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_32 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[0] == "alive":
                        button_press(21)
                    if row_3_stat[0] == "alive":
                        button_press(31)
                    if row_4_stat[0] == "alive":
                        button_press(41)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_2_stat[1] == "alive":
                        button_press(22)
                else:
                    label_32 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_32.grid(row = 3, column = 1)

            elif loc == 33:
                button_33.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_33 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_33 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[1] == "alive":
                        button_press(22)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_2_stat[2] == "alive":
                        button_press(23)
                else:
                    label_33 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_33.grid(row = 3, column = 2)

            elif loc == 34:
                button_34.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_34 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_34 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[2] == "alive":
                        button_press(23)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_2_stat[3] == "alive":
                        button_press(24)
                else:
                    label_34 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_34.grid(row = 3, column = 3)

            elif loc == 35:
                button_35.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_35 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_35 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[3] == "alive":
                        button_press(24)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_2_stat[4] == "alive":
                        button_press(25)
                else:
                    label_35 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_35.grid(row = 3, column = 4)

            elif loc == 36:
                button_36.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_36 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_36 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[4] == "alive":
                        button_press(25)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_2_stat[5] == "alive":
                        button_press(26)
                else:
                    label_36 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_36.grid(row = 3, column = 5)

            elif loc == 37:
                button_37.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_37 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_37 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[5] == "alive":
                        button_press(26)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_4_stat[7] == "alive":
                        button_press(48)
                    if row_3_stat[7] == "alive":
                        button_press(38)
                    if row_2_stat[7] == "alive":
                        button_press(28)
                    if row_2_stat[6] == "alive":
                        button_press(27)
                else:
                    label_37 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_37.grid(row = 3, column = 6)

            elif loc == 38:
                button_38.grid_remove()
                row_3_stat[loc_ind] = "dead"
                obj = row_3[loc_ind]
                turns += 1
                if obj == "💣":
                    label_38 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_38 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_2_stat[6] == "alive":
                        button_press(27)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_4_stat[7] == "alive":
                        button_press(48)
                    if row_2_stat[7] == "alive":
                        button_press(28)
                else:
                    label_38 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_38.grid(row = 3, column = 7)

            elif loc == 41:
                button_41.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_41 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_41 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[0] == "alive":
                        button_press(31)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_5_stat[0] == "alive":
                        button_press(51)
                else:
                    label_41 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_41.grid(row = 4, column = 0)

            elif loc == 42:
                button_42.grid_remove()     
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_42 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_42 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[0] == "alive":
                        button_press(31)
                    if row_4_stat[0] == "alive":
                        button_press(41)
                    if row_5_stat[0] == "alive":
                        button_press(51)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_3_stat[1] == "alive":
                        button_press(32)
                else:
                    label_42 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_42.grid(row = 4, column = 1)

            elif loc == 43:
                button_43.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_43 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_43 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[1] == "alive":
                        button_press(32)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_3_stat[2] == "alive":
                        button_press(33)
                else:
                    label_43 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_43.grid(row = 4, column = 2)

            elif loc == 44:
                button_44.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_44 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_44 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[2] == "alive":
                        button_press(33)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_3_stat[3] == "alive":
                        button_press(34)
                else:
                    label_44 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_44.grid(row = 4, column = 3)

            elif loc == 45:
                button_45.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_45 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_45 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[3] == "alive":
                        button_press(34)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_3_stat[4] == "alive":
                        button_press(35)
                else:
                    label_45 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_45.grid(row = 4, column = 4)

            elif loc == 46:
                button_46.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_46 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_46 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[4] == "alive":
                        button_press(35)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_3_stat[5] == "alive":
                        button_press(36)
                else:
                    label_46 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_46.grid(row = 4, column = 5)

            elif loc == 47:
                button_47.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_47 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_47 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[5] == "alive":
                        button_press(36)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_5_stat[7] == "alive":
                        button_press(58)
                    if row_4_stat[7] == "alive":
                        button_press(48)
                    if row_3_stat[7] == "alive":
                        button_press(38)
                    if row_3_stat[6] == "alive":
                        button_press(37)
                else:
                    label_47 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_47.grid(row = 4, column = 6)

            elif loc == 48:
                button_48.grid_remove()
                row_4_stat[loc_ind] = "dead"
                obj = row_4[loc_ind]
                turns += 1
                if obj == "💣":
                    label_48 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_48 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_3_stat[6] == "alive":
                        button_press(37)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_5_stat[7] == "alive":
                        button_press(58)
                    if row_3_stat[7] == "alive":
                        button_press(38)
                else:
                    label_48 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_48.grid(row = 4, column = 7)

            elif loc == 51:
                button_51.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_51 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_51 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[0] == "alive":
                        button_press(41)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_6_stat[0] == "alive":
                        button_press(61)
                else:
                    label_51 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_51.grid(row = 5, column = 0)

            elif loc == 52:
                button_52.grid_remove()     
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_52 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_52 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[0] == "alive":
                        button_press(41)
                    if row_5_stat[0] == "alive":
                        button_press(51)
                    if row_6_stat[0] == "alive":
                        button_press(61)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_4_stat[1] == "alive":
                        button_press(42)
                else:
                    label_52 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_52.grid(row = 5, column = 1)

            elif loc == 53:
                button_53.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_53 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_53 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[1] == "alive":
                        button_press(42)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_4_stat[2] == "alive":
                        button_press(43)
                else:
                    label_53 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_53.grid(row = 5, column = 2)

            elif loc == 54:
                button_54.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_54 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_54 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[2] == "alive":
                        button_press(43)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_4_stat[3] == "alive":
                        button_press(44)
                else:
                    label_54 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_54.grid(row = 5, column = 3)

            elif loc == 55:
                button_55.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_55 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_55 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[3] == "alive":
                        button_press(44)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_4_stat[4] == "alive":
                        button_press(45)
                else:
                    label_55 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_55.grid(row = 5, column = 4)

            elif loc == 56:
                button_56.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_56 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_56 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[4] == "alive":
                        button_press(45)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_4_stat[5] == "alive":
                        button_press(46)
                else:
                    label_56 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_56.grid(row = 5, column = 5)

            elif loc == 57:
                button_57.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_57 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_57 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[5] == "alive":
                        button_press(46)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_6_stat[7] == "alive":
                        button_press(68)
                    if row_5_stat[7] == "alive":
                        button_press(58)
                    if row_4_stat[7] == "alive":
                        button_press(48)
                    if row_4_stat[6] == "alive":
                        button_press(47)
                else:
                    label_57 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_57.grid(row = 5, column = 6)

            elif loc == 58:
                button_58.grid_remove()
                row_5_stat[loc_ind] = "dead"
                obj = row_5[loc_ind]
                turns += 1
                if obj == "💣":
                    label_58 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_58 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_4_stat[6] == "alive":
                        button_press(47)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_6_stat[7] == "alive":
                        button_press(68)
                    if row_4_stat[7] == "alive":
                        button_press(48)
                else:
                    label_58 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_58.grid(row = 5, column = 7)

            elif loc == 61:
                button_61.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_61 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_61 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[0] == "alive":
                        button_press(51)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_7_stat[0] == "alive":
                        button_press(71)
                else:
                    label_61 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_61.grid(row = 6, column = 0)

            elif loc == 62:
                button_62.grid_remove()     
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_62 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_62 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[0] == "alive":
                        button_press(51)
                    if row_6_stat[0] == "alive":
                        button_press(61)
                    if row_7_stat[0] == "alive":
                        button_press(71)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_5_stat[1] == "alive":
                        button_press(52)
                else:
                    label_62 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_62.grid(row = 6, column = 1)

            elif loc == 63:
                button_63.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_63 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_63 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[1] == "alive":
                        button_press(52)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_5_stat[2] == "alive":
                        button_press(53)
                else:
                    label_63 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_63.grid(row = 6, column = 2)

            elif loc == 64:
                button_64.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_64 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_64 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[2] == "alive":
                        button_press(53)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_5_stat[3] == "alive":
                        button_press(54)
                else:
                    label_64 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_64.grid(row = 6, column = 3)

            elif loc == 65:
                button_65.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_65 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_65 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[3] == "alive":
                        button_press(54)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_5_stat[4] == "alive":
                        button_press(55)
                else:
                    label_65 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_65.grid(row = 6, column = 4)

            elif loc == 66:
                button_66.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_66 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_66 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[4] == "alive":
                        button_press(55)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_5_stat[5] == "alive":
                        button_press(56)
                else:
                    label_66 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_66.grid(row = 6, column = 5)

            elif loc == 67:
                button_67.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_67 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_67 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[5] == "alive":
                        button_press(56)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_7_stat[7] == "alive":
                        button_press(78)
                    if row_6_stat[7] == "alive":
                        button_press(68)
                    if row_5_stat[7] == "alive":
                        button_press(58)
                    if row_5_stat[6] == "alive":
                        button_press(57)
                else:
                    label_67 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_67.grid(row = 6, column = 6)

            elif loc == 68:
                button_68.grid_remove()
                row_6_stat[loc_ind] = "dead"
                obj = row_6[loc_ind]
                turns += 1
                if obj == "💣":
                    label_68 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_68 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_5_stat[6] == "alive":
                        button_press(57)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_7_stat[7] == "alive":
                        button_press(78)
                    if row_5_stat[7] == "alive":
                        button_press(58)
                else:
                    label_68 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_68.grid(row = 6, column = 7)

            elif loc == 71:
                button_71.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_71 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_71 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[0] == "alive":
                        button_press(61)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_8_stat[1] == "alive":
                        button_press(82)
                    if row_8_stat[0] == "alive":
                        button_press(81)
                else:
                    label_71 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_71.grid(row = 7, column = 0)

            elif loc == 72:
                button_72.grid_remove()     
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_72 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_72 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[0] == "alive":
                        button_press(61)
                    if row_7_stat[0] == "alive":
                        button_press(71)
                    if row_8_stat[0] == "alive":
                        button_press(81)
                    if row_8_stat[1] == "alive":
                        button_press(82)
                    if row_8_stat[2] == "alive":
                        button_press(83)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_6_stat[1] == "alive":
                        button_press(62)
                else:
                    label_72 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_72.grid(row = 7, column = 1)

            elif loc == 73:
                button_73.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_73 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_73 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[1] == "alive":
                        button_press(62)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_8_stat[1] == "alive":
                        button_press(82)
                    if row_8_stat[2] == "alive":
                        button_press(83)
                    if row_8_stat[3] == "alive":
                        button_press(84)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_6_stat[2] == "alive":
                        button_press(63)
                else:
                    label_73 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_73.grid(row = 7, column = 2)

            elif loc == 74:
                button_74.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_74 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_74 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[2] == "alive":
                        button_press(63)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_8_stat[2] == "alive":
                        button_press(83)
                    if row_8_stat[3] == "alive":
                        button_press(84)
                    if row_8_stat[4] == "alive":
                        button_press(85)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_6_stat[3] == "alive":
                        button_press(64)
                else:
                    label_74 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_74.grid(row = 7, column = 3)

            elif loc == 75:
                button_75.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_75 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_75 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[3] == "alive":
                        button_press(64)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_8_stat[3] == "alive":
                        button_press(84)
                    if row_8_stat[4] == "alive":
                        button_press(85)
                    if row_8_stat[5] == "alive":
                        button_press(86)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_6_stat[4] == "alive":
                        button_press(65)
                else:
                    label_75 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_75.grid(row = 7, column = 4)

            elif loc == 76:
                button_76.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_76 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_76 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[4] == "alive":
                        button_press(65)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_8_stat[4] == "alive":
                        button_press(85)
                    if row_8_stat[5] == "alive":
                        button_press(86)
                    if row_8_stat[6] == "alive":
                        button_press(87)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_6_stat[5] == "alive":
                        button_press(66)
                else:
                    label_76 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_76.grid(row = 7, column = 5)

            elif loc == 77:
                button_77.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_77 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_77 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[5] == "alive":
                        button_press(66)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_8_stat[5] == "alive":
                        button_press(86)
                    if row_8_stat[6] == "alive":
                        button_press(87)
                    if row_8_stat[7] == "alive":
                        button_press(88)
                    if row_7_stat[7] == "alive":
                        button_press(78)
                    if row_6_stat[7] == "alive":
                        button_press(68)
                    if row_6_stat[6] == "alive":
                        button_press(67)
                else:
                    label_77 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_77.grid(row = 7, column = 6)

            elif loc == 78:
                button_78.grid_remove()
                row_7_stat[loc_ind] = "dead"
                obj = row_7[loc_ind]
                turns += 1
                if obj == "💣":
                    label_78 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_78 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_6_stat[6] == "alive":
                        button_press(67)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_8_stat[6] == "alive":
                        button_press(87)
                    if row_8_stat[7] == "alive":
                        button_press(88)
                    if row_6_stat[7] == "alive":
                        button_press(68)
                else:
                    label_78 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_78.grid(row = 7, column = 7)

            elif loc == 81:
                button_81.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_81 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_81 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[0] == "alive":
                        button_press(71)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_8_stat[1] == "alive":
                        button_press(82)
                else:
                    label_81 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_81.grid(row = 8, column = 0)

            elif loc == 82:
                button_82.grid_remove()     
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]        
                turns += 1
                if obj == "💣":
                    label_82 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_82 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[0] == "alive":
                        button_press(71)
                    if row_8_stat[0] == "alive":
                        button_press(81)
                    if row_8_stat[2] == "alive":
                        button_press(83)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_7_stat[1] == "alive":
                        button_press(72)
                else:
                    label_82 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_82.grid(row = 8, column = 1)

            elif loc == 83:
                button_83.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_83 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_83 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[1] == "alive":
                        button_press(72)
                    if row_8_stat[1] == "alive":
                        button_press(82)
                    if row_8_stat[3] == "alive":
                        button_press(84)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_7_stat[2] == "alive":
                        button_press(73)
                else:
                    label_83 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_83.grid(row = 8, column = 2)

            elif loc == 84:
                button_84.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_84 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_84 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[2] == "alive":
                        button_press(73)
                    if row_8_stat[2] == "alive":
                        button_press(83)
                    if row_8_stat[4] == "alive":
                        button_press(85)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_7_stat[3] == "alive":
                        button_press(74)
                else:
                    label_84 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_84.grid(row = 8, column = 3)

            elif loc == 85:
                button_85.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_85 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_85 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[3] == "alive":
                        button_press(74)
                    if row_8_stat[3] == "alive":
                        button_press(84)
                    if row_8_stat[5] == "alive":
                        button_press(86)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_7_stat[4] == "alive":
                        button_press(75)
                else:
                    label_85 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_85.grid(row = 8, column = 4)

            elif loc == 86:
                button_86.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_86 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_86 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[4] == "alive":
                        button_press(75)
                    if row_8_stat[4] == "alive":
                        button_press(85)
                    if row_8_stat[6] == "alive":
                        button_press(87)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_7_stat[5] == "alive":
                        button_press(76)
                else:
                    label_86 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_86.grid(row = 8, column = 5)

            elif loc == 87:
                button_87.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_87 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_87 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[5] == "alive":
                        button_press(76)
                    if row_8_stat[5] == "alive":
                        button_press(86)
                    if row_8_stat[7] == "alive":
                        button_press(88)
                    if row_7_stat[7] == "alive":
                        button_press(78)
                    if row_7_stat[6] == "alive":
                        button_press(77)
                else:
                    label_87 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_87.grid(row = 8, column = 6)

            elif loc == 88:
                button_88.grid_remove()
                row_8_stat[loc_ind] = "dead"
                obj = row_8[loc_ind]
                turns += 1
                if obj == "💣":
                    label_88 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = "💣", background = "Red")
                    game_over = 1
                elif obj == 0:
                    label_88 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid")
                    if row_7_stat[6] == "alive":
                        button_press(77)
                    if row_8_stat[6] == "alive":
                        button_press(87)
                    if row_7_stat[7] == "alive":
                        button_press(78)
                else:
                    label_88 = tk.Label(width = 2, height = 1, borderwidth = 1, relief = "solid", text = obj)
                label_88.grid(row = 8, column = 7)
        
        if flag_on == 1:
            if loc == 11:
                if flag_11 == 0:
                    button_11.config(text = "🚩")
                    flag_11 = 1
                elif flag_11 == 1:
                    button_11.config(text = "")
                    flag_11 = 0
            elif loc == 12:
                if flag_12 == 0:
                    button_12.config(text = "🚩")
                    flag_12 = 1
                elif flag_12 == 1:
                    button_12.config(text = "")
                    flag_12 = 0
            elif loc == 13:
                if flag_13 == 0:
                    button_13.config(text = "🚩")
                    flag_13 = 1
                elif flag_13 == 1:
                    button_13.config(text = "")
                    flag_13 = 0
            elif loc == 14:
                if flag_14 == 0:
                    button_14.config(text = "🚩")
                    flag_14 = 1
                elif flag_14 == 1:
                    button_14.config(text = "")
                    flag_14 = 0
            elif loc == 15:
                if flag_15 == 0:
                    button_15.config(text = "🚩")
                    flag_15 = 1
                elif flag_15 == 1:
                    button_15.config(text = "")
                    flag_15 = 0
            elif loc == 16:
                if flag_16 == 0:
                    button_16.config(text = "🚩")
                    flag_16 = 1
                elif flag_16 == 1:
                    button_16.config(text = "")
                    flag_16 = 0
            elif loc == 17:
                if flag_17 == 0:
                    button_17.config(text = "🚩")
                    flag_17 = 1
                elif flag_17 == 1:
                    button_17.config(text = "")
                    flag_17 = 0
            elif loc == 18:
                if flag_18 == 0:
                    button_18.config(text = "🚩")
                    flag_18 = 1
                elif flag_18 == 1:
                    button_18.config(text = "")
                    flag_18 = 0
            elif loc == 21:
                if flag_21 == 0:
                    button_21.config(text = "🚩")
                    flag_21 = 1
                elif flag_21 == 1:
                    button_21.config(text = "")
                    flag_21 = 0
            elif loc == 22:
                if flag_22 == 0:
                    button_22.config(text = "🚩")
                    flag_22 = 1
                elif flag_22 == 1:
                    button_22.config(text = "")
                    flag_22 = 0
            elif loc == 23:
                if flag_23 == 0:
                    button_23.config(text = "🚩")
                    flag_23 = 1
                elif flag_23 == 1:
                    button_23.config(text = "")
                    flag_23 = 0
            elif loc == 24:
                if flag_24 == 0:
                    button_24.config(text = "🚩")
                    flag_24 = 1
                elif flag_24 == 1:
                    button_24.config(text = "")
                    flag_24 = 0
            elif loc == 25:
                if flag_25 == 0:
                    button_25.config(text = "🚩")
                    flag_25 = 1
                elif flag_25 == 1:
                    button_25.config(text = "")
                    flag_25 = 0
            elif loc == 26:
                if flag_26 == 0:
                    button_26.config(text = "🚩")
                    flag_26 = 1
                elif flag_26 == 1:
                    button_26.config(text = "")
                    flag_26 = 0
            elif loc == 27:
                if flag_27 == 0:
                    button_27.config(text = "🚩")
                    flag_27 = 1
                elif flag_27 == 1:
                    button_27.config(text = "")
                    flag_27 = 0
            elif loc == 28:
                if flag_28 == 0:
                    button_28.config(text = "🚩")
                    flag_28 = 1
                elif flag_28 == 1:
                    button_28.config(text = "")
                    flag_28 = 0
            elif loc == 31:
                if flag_31 == 0:
                    button_31.config(text = "🚩")
                    flag_31 = 1
                elif flag_31 == 1:
                    button_31.config(text = "")
                    flag_31 = 0
            elif loc == 32:
                if flag_32 == 0:
                    button_32.config(text = "🚩")
                    flag_32 = 1
                elif flag_32 == 1:
                    button_32.config(text = "")
                    flag_32 = 0
            elif loc == 33:
                if flag_33 == 0:
                    button_33.config(text = "🚩")
                    flag_33 = 1
                elif flag_33 == 1:
                    button_33.config(text = "")
                    flag_33 = 0
            elif loc == 34:
                if flag_34 == 0:
                    button_34.config(text = "🚩")
                    flag_34 = 1
                elif flag_34 == 1:
                    button_34.config(text = "")
                    flag_34 = 0
            elif loc == 35:
                if flag_35 == 0:
                    button_35.config(text = "🚩")
                    flag_35 = 1
                elif flag_35 == 1:
                    button_35.config(text = "")
                    flag_35 = 0
            elif loc == 36:
                if flag_36 == 0:
                    button_36.config(text = "🚩")
                    flag_36 = 1
                elif flag_36 == 1:
                    button_36.config(text = "")
                    flag_36 = 0
            elif loc == 37:
                if flag_37 == 0:
                    button_37.config(text = "🚩")
                    flag_37 = 1
                elif flag_37 == 1:
                    button_37.config(text = "")
                    flag_37 = 0
            elif loc == 38:
                if flag_38 == 0:
                    button_38.config(text = "🚩")
                    flag_38 = 1
                elif flag_38 == 1:
                    button_38.config(text = "")
                    flag_38 = 0
            elif loc == 41:
                if flag_41 == 0:
                    button_41.config(text = "🚩")
                    flag_41 = 1
                elif flag_41 == 1:
                    button_41.config(text = "")
                    flag_41 = 0
            elif loc == 42:
                if flag_42 == 0:
                    button_42.config(text = "🚩")
                    flag_42 = 1
                elif flag_42 == 1:
                    button_42.config(text = "")
                    flag_42 = 0
            elif loc == 43:
                if flag_43 == 0:
                    button_43.config(text = "🚩")
                    flag_43 = 1
                elif flag_43 == 1:
                    button_43.config(text = "")
                    flag_43 = 0
            elif loc == 44:
                if flag_44 == 0:
                    button_44.config(text = "🚩")
                    flag_44 = 1
                elif flag_44 == 1:
                    button_44.config(text = "")
                    flag_44 = 0
            elif loc == 45:
                if flag_45 == 0:
                    button_45.config(text = "🚩")
                    flag_45 = 1
                elif flag_45 == 1:
                    button_45.config(text = "")
                    flag_45 = 0
            elif loc == 46:
                if flag_46 == 0:
                    button_46.config(text = "🚩")
                    flag_46 = 1
                elif flag_46 == 1:
                    button_46.config(text = "")
                    flag_46 = 0
            elif loc == 47:
                if flag_47 == 0:
                    button_47.config(text = "🚩")
                    flag_47 = 1
                elif flag_47 == 1:
                    button_47.config(text = "")
                    flag_47 = 0
            elif loc == 48:
                if flag_48 == 0:
                    button_48.config(text = "🚩")
                    flag_48 = 1
                elif flag_48 == 1:
                    button_48.config(text = "")
                    flag_48 = 0
            elif loc == 51:
                if flag_51 == 0:
                    button_51.config(text = "🚩")
                    flag_51 = 1
                elif flag_51 == 1:
                    button_51.config(text = "")
                    flag_51 = 0
            elif loc == 52:
                if flag_52 == 0:
                    button_52.config(text = "🚩")
                    flag_52 = 1
                elif flag_52 == 1:
                    button_52.config(text = "")
                    flag_52 = 0
            elif loc == 53:
                if flag_53 == 0:
                    button_53.config(text = "🚩")
                    flag_53 = 1
                elif flag_53 == 1:
                    button_53.config(text = "")
                    flag_53 = 0
            elif loc == 54:
                if flag_54 == 0:
                    button_54.config(text = "🚩")
                    flag_54 = 1
                elif flag_54 == 1:
                    button_54.config(text = "")
                    flag_54 = 0
            elif loc == 55:
                if flag_55 == 0:
                    button_55.config(text = "🚩")
                    flag_55 = 1
                elif flag_55 == 1:
                    button_55.config(text = "")
                    flag_55 = 0
            elif loc == 56:
                if flag_56 == 0:
                    button_56.config(text = "🚩")
                    flag_56 = 1
                elif flag_56 == 1:
                    button_56.config(text = "")
                    flag_56 = 0
            elif loc == 57:
                if flag_57 == 0:
                    button_57.config(text = "🚩")
                    flag_57 = 1
                elif flag_57 == 1:
                    button_57.config(text = "")
                    flag_57 = 0
            elif loc == 58:
                if flag_58 == 0:
                    button_58.config(text = "🚩")
                    flag_58 = 1
                elif flag_58 == 1:
                    button_58.config(text = "")
                    flag_58 = 0
            elif loc == 61:
                if flag_61 == 0:
                    button_61.config(text = "🚩")
                    flag_61 = 1
                elif flag_61 == 1:
                    button_61.config(text = "")
                    flag_61 = 0
            elif loc == 62:
                if flag_62 == 0:
                    button_62.config(text = "🚩")
                    flag_62 = 1
                elif flag_62 == 1:
                    button_62.config(text = "")
                    flag_62 = 0
            elif loc == 63:
                if flag_63 == 0:
                    button_63.config(text = "🚩")
                    flag_63 = 1
                elif flag_63 == 1:
                    button_63.config(text = "")
                    flag_63 = 0
            elif loc == 64:
                if flag_64 == 0:
                    button_64.config(text = "🚩")
                    flag_64 = 1
                elif flag_64 == 1:
                    button_64.config(text = "")
                    flag_64 = 0
            elif loc == 65:
                if flag_65 == 0:
                    button_65.config(text = "🚩")
                    flag_65 = 1
                elif flag_65 == 1:
                    button_65.config(text = "")
                    flag_65 = 0
            elif loc == 66:
                if flag_66 == 0:
                    button_66.config(text = "🚩")
                    flag_66 = 1
                elif flag_66 == 1:
                    button_66.config(text = "")
                    flag_66 = 0
            elif loc == 67:
                if flag_67 == 0:
                    button_67.config(text = "🚩")
                    flag_67 = 1
                elif flag_67 == 1:
                    button_67.config(text = "")
                    flag_67 = 0
            elif loc == 68:
                if flag_68 == 0:
                    button_68.config(text = "🚩")
                    flag_68 = 1
                elif flag_68 == 1:
                    button_68.config(text = "")
                    flag_68 = 0
            elif loc == 71:
                if flag_71 == 0:
                    button_71.config(text = "🚩")
                    flag_71 = 1
                elif flag_71 == 1:
                    button_71.config(text = "")
                    flag_71 = 0
            elif loc == 72:
                if flag_72 == 0:
                    button_72.config(text = "🚩")
                    flag_72 = 1
                elif flag_72 == 1:
                    button_72.config(text = "")
                    flag_72 = 0
            elif loc == 73:
                if flag_73 == 0:
                    button_73.config(text = "🚩")
                    flag_73 = 1
                elif flag_73 == 1:
                    button_73.config(text = "")
                    flag_73 = 0
            elif loc == 74:
                if flag_74 == 0:
                    button_74.config(text = "🚩")
                    flag_74 = 1
                elif flag_74 == 1:
                    button_74.config(text = "")
                    flag_74 = 0
            elif loc == 75:
                if flag_75 == 0:
                    button_75.config(text = "🚩")
                    flag_75 = 1
                elif flag_75 == 1:
                    button_75.config(text = "")
                    flag_75 = 0
            elif loc == 76:
                if flag_76 == 0:
                    button_76.config(text = "🚩")
                    flag_76 = 1
                elif flag_76 == 1:
                    button_76.config(text = "")
                    flag_76 = 0
            elif loc == 77:
                if flag_77 == 0:
                    button_77.config(text = "🚩")
                    flag_77 = 1
                elif flag_77 == 1:
                    button_77.config(text = "")
                    flag_77 = 0
            elif loc == 78:
                if flag_78 == 0:
                    button_78.config(text = "🚩")
                    flag_78 = 1
                elif flag_78 == 1:
                    button_78.config(text = "")
                    flag_78 = 0
            elif loc == 81:
                if flag_81 == 0:
                    button_81.config(text = "🚩")
                    flag_81 = 1
                elif flag_81 == 1:
                    button_81.config(text = "")
                    flag_81 = 0
            elif loc == 82:
                if flag_82 == 0:
                    button_82.config(text = "🚩")
                    flag_82 = 1
                elif flag_82 == 1:
                    button_82.config(text = "")
                    flag_82 = 0
            elif loc == 83:
                if flag_83 == 0:
                    button_83.config(text = "🚩")
                    flag_83 = 1
                elif flag_83 == 1:
                    button_83.config(text = "")
                    flag_83 = 0
            elif loc == 84:
                if flag_84 == 0:
                    button_84.config(text = "🚩")
                    flag_84 = 1
                elif flag_84 == 1:
                    button_84.config(text = "")
                    flag_84 = 0
            elif loc == 85:
                if flag_85 == 0:
                    button_85.config(text = "🚩")
                    flag_85 = 1
                elif flag_85 == 1:
                    button_85.config(text = "")
                    flag_85 = 0
            elif loc == 86:
                if flag_86 == 0:
                    button_86.config(text = "🚩")
                    flag_86 = 1
                elif flag_86 == 1:
                    button_86.config(text = "")
                    flag_86 = 0
            elif loc == 87:
                if flag_87 == 0:
                    button_87.config(text = "🚩")
                    flag_87 = 1
                elif flag_87 == 1:
                    button_87.config(text = "")
                    flag_87 = 0
            elif loc == 88:
                if flag_88 == 0:
                    button_88.config(text = "🚩")
                    flag_88 = 1
                elif flag_88 == 1:
                    button_88.config(text = "")
                    flag_88 = 0

        if game_over == 1 or turns == 56:
            game_end()


    button_11 = tk.Button(width = 2, height = 1, command = lambda m = 11: button_press(m))
    button_12 = tk.Button(width = 2, height = 1, command = lambda m = 12: button_press(m))
    button_13 = tk.Button(width = 2, height = 1, command = lambda m = 13: button_press(m))
    button_14 = tk.Button(width = 2, height = 1, command = lambda m = 14: button_press(m))
    button_15 = tk.Button(width = 2, height = 1, command = lambda m = 15: button_press(m))
    button_16 = tk.Button(width = 2, height = 1, command = lambda m = 16: button_press(m))
    button_17 = tk.Button(width = 2, height = 1, command = lambda m = 17: button_press(m))
    button_18 = tk.Button(width = 2, height = 1, command = lambda m = 18: button_press(m))
    button_21 = tk.Button(width = 2, height = 1, command = lambda m = 21: button_press(m))
    button_22 = tk.Button(width = 2, height = 1, command = lambda m = 22: button_press(m))
    button_23 = tk.Button(width = 2, height = 1, command = lambda m = 23: button_press(m))
    button_24 = tk.Button(width = 2, height = 1, command = lambda m = 24: button_press(m))
    button_25 = tk.Button(width = 2, height = 1, command = lambda m = 25: button_press(m))
    button_26 = tk.Button(width = 2, height = 1, command = lambda m = 26: button_press(m))
    button_27 = tk.Button(width = 2, height = 1, command = lambda m = 27: button_press(m))
    button_28 = tk.Button(width = 2, height = 1, command = lambda m = 28: button_press(m))
    button_31 = tk.Button(width = 2, height = 1, command = lambda m = 31: button_press(m))
    button_32 = tk.Button(width = 2, height = 1, command = lambda m = 32: button_press(m))
    button_33 = tk.Button(width = 2, height = 1, command = lambda m = 33: button_press(m))
    button_34 = tk.Button(width = 2, height = 1, command = lambda m = 34: button_press(m))
    button_35 = tk.Button(width = 2, height = 1, command = lambda m = 35: button_press(m))
    button_36 = tk.Button(width = 2, height = 1, command = lambda m = 36: button_press(m))
    button_37 = tk.Button(width = 2, height = 1, command = lambda m = 37: button_press(m))
    button_38 = tk.Button(width = 2, height = 1, command = lambda m = 38: button_press(m))
    button_41 = tk.Button(width = 2, height = 1, command = lambda m = 41: button_press(m))
    button_42 = tk.Button(width = 2, height = 1, command = lambda m = 42: button_press(m))
    button_43 = tk.Button(width = 2, height = 1, command = lambda m = 43: button_press(m))
    button_44 = tk.Button(width = 2, height = 1, command = lambda m = 44: button_press(m))
    button_45 = tk.Button(width = 2, height = 1, command = lambda m = 45: button_press(m))
    button_46 = tk.Button(width = 2, height = 1, command = lambda m = 46: button_press(m))
    button_47 = tk.Button(width = 2, height = 1, command = lambda m = 47: button_press(m))
    button_48 = tk.Button(width = 2, height = 1, command = lambda m = 48: button_press(m))
    button_51 = tk.Button(width = 2, height = 1, command = lambda m = 51: button_press(m))
    button_52 = tk.Button(width = 2, height = 1, command = lambda m = 52: button_press(m))
    button_53 = tk.Button(width = 2, height = 1, command = lambda m = 53: button_press(m))
    button_54 = tk.Button(width = 2, height = 1, command = lambda m = 54: button_press(m))
    button_55 = tk.Button(width = 2, height = 1, command = lambda m = 55: button_press(m))
    button_56 = tk.Button(width = 2, height = 1, command = lambda m = 56: button_press(m))
    button_57 = tk.Button(width = 2, height = 1, command = lambda m = 57: button_press(m))
    button_58 = tk.Button(width = 2, height = 1, command = lambda m = 58: button_press(m))
    button_61 = tk.Button(width = 2, height = 1, command = lambda m = 61: button_press(m))
    button_62 = tk.Button(width = 2, height = 1, command = lambda m = 62: button_press(m))
    button_63 = tk.Button(width = 2, height = 1, command = lambda m = 63: button_press(m))
    button_64 = tk.Button(width = 2, height = 1, command = lambda m = 64: button_press(m))
    button_65 = tk.Button(width = 2, height = 1, command = lambda m = 65: button_press(m))
    button_66 = tk.Button(width = 2, height = 1, command = lambda m = 66: button_press(m))
    button_67 = tk.Button(width = 2, height = 1, command = lambda m = 67: button_press(m))
    button_68 = tk.Button(width = 2, height = 1, command = lambda m = 68: button_press(m))
    button_71 = tk.Button(width = 2, height = 1, command = lambda m = 71: button_press(m))
    button_72 = tk.Button(width = 2, height = 1, command = lambda m = 72: button_press(m))
    button_73 = tk.Button(width = 2, height = 1, command = lambda m = 73: button_press(m))
    button_74 = tk.Button(width = 2, height = 1, command = lambda m = 74: button_press(m))
    button_75 = tk.Button(width = 2, height = 1, command = lambda m = 75: button_press(m))
    button_76 = tk.Button(width = 2, height = 1, command = lambda m = 76: button_press(m))
    button_77 = tk.Button(width = 2, height = 1, command = lambda m = 77: button_press(m))
    button_78 = tk.Button(width = 2, height = 1, command = lambda m = 78: button_press(m))
    button_81 = tk.Button(width = 2, height = 1, command = lambda m = 81: button_press(m))
    button_82 = tk.Button(width = 2, height = 1, command = lambda m = 82: button_press(m))
    button_83 = tk.Button(width = 2, height = 1, command = lambda m = 83: button_press(m))
    button_84 = tk.Button(width = 2, height = 1, command = lambda m = 84: button_press(m))
    button_85 = tk.Button(width = 2, height = 1, command = lambda m = 85: button_press(m))
    button_86 = tk.Button(width = 2, height = 1, command = lambda m = 86: button_press(m))
    button_87 = tk.Button(width = 2, height = 1, command = lambda m = 87: button_press(m))
    button_88 = tk.Button(width = 2, height = 1, command = lambda m = 88: button_press(m))
    button_flag = tk.Button(width = 2, height = 1, text = "🚩", background = "Blue", command = flag_press)


    button_11.grid(row = 1, column = 0)
    button_12.grid(row = 1, column = 1)
    button_13.grid(row = 1, column = 2)
    button_14.grid(row = 1, column = 3)
    button_15.grid(row = 1, column = 4)
    button_16.grid(row = 1, column = 5)
    button_17.grid(row = 1, column = 6)
    button_18.grid(row = 1, column = 7)
    button_21.grid(row = 2, column = 0)
    button_22.grid(row = 2, column = 1)
    button_23.grid(row = 2, column = 2)
    button_24.grid(row = 2, column = 3)
    button_25.grid(row = 2, column = 4)
    button_26.grid(row = 2, column = 5)
    button_27.grid(row = 2, column = 6)
    button_28.grid(row = 2, column = 7)
    button_31.grid(row = 3, column = 0)
    button_32.grid(row = 3, column = 1)
    button_33.grid(row = 3, column = 2)
    button_34.grid(row = 3, column = 3)
    button_35.grid(row = 3, column = 4)
    button_36.grid(row = 3, column = 5)
    button_37.grid(row = 3, column = 6)
    button_38.grid(row = 3, column = 7)
    button_41.grid(row = 4, column = 0)
    button_42.grid(row = 4, column = 1)
    button_43.grid(row = 4, column = 2)
    button_44.grid(row = 4, column = 3)
    button_45.grid(row = 4, column = 4)
    button_46.grid(row = 4, column = 5)
    button_47.grid(row = 4, column = 6)
    button_48.grid(row = 4, column = 7)
    button_51.grid(row = 5, column = 0)
    button_52.grid(row = 5, column = 1)
    button_53.grid(row = 5, column = 2)
    button_54.grid(row = 5, column = 3)
    button_55.grid(row = 5, column = 4)
    button_56.grid(row = 5, column = 5)
    button_57.grid(row = 5, column = 6)
    button_58.grid(row = 5, column = 7)
    button_61.grid(row = 6, column = 0)
    button_62.grid(row = 6, column = 1)
    button_63.grid(row = 6, column = 2)
    button_64.grid(row = 6, column = 3)
    button_65.grid(row = 6, column = 4)
    button_66.grid(row = 6, column = 5)
    button_67.grid(row = 6, column = 6)
    button_68.grid(row = 6, column = 7)
    button_71.grid(row = 7, column = 0)
    button_72.grid(row = 7, column = 1)
    button_73.grid(row = 7, column = 2)
    button_74.grid(row = 7, column = 3)
    button_75.grid(row = 7, column = 4)
    button_76.grid(row = 7, column = 5)
    button_77.grid(row = 7, column = 6)
    button_78.grid(row = 7, column = 7)
    button_81.grid(row = 8, column = 0)
    button_82.grid(row = 8, column = 1)
    button_83.grid(row = 8, column = 2)
    button_84.grid(row = 8, column = 3)
    button_85.grid(row = 8, column = 4)
    button_86.grid(row = 8, column = 5)
    button_87.grid(row = 8, column = 6)
    button_88.grid(row = 8, column = 7)
    button_flag.grid(row = 0, column = 7)
    
    window.mainloop()
    window_end.mainloop()