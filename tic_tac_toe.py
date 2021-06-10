import random
l = 0
user_symbol = ""
user_score = 0
computer_score = 0
title = "Tic-Tac-Toe!"
print(title)
for x in title:
    l+=1
print("-"*l)
print('''
Rules:
1. Like normal tic-tac-toe but with a small twist.
2. First, you have to choose your symbol, X or O.
3. Since you cannot put the symbol in a place directly, we will use the coordinate system.
4. First you will enter the row you want the symbol to be placed in and then the column.
5. Get three of your symbols in a row to win!
''')

def valid_symbol(a):
    while a!="X" and a!="O" and a!="STOP":
        print("Invalid symbol.")
        a = input("Enter your symbol (X or O) or 'stop' to stop the program: ")
        a = a.capitalize()
    return a

def valid_row(b):
    while True:
        try:
            b = int(b)
            break
        except ValueError:
            print("Your input is not an integer.")
            b = input("Choose which row you want your symbol to be placed in: ")
    while b<1 or b>3:
        print("Your input should only be 1, 2 or 3.")
        b = input("Choose which row you want your symbol to be placed in: ")
        while True:
            try:
                b = int(b)
                break
            except ValueError:
                print("Your input is not an integer.")
                b = input("Choose which row you want your symbol to be placed in: ")
    return b

def valid_column(c):
    while True:
        try:
            c = int(c)
            break
        except ValueError:
            print("Your input is not an integer.")
            c = input("Choose which column you want your symbol to be placed in: ")
    while c<1 or c>3:
        print("Your input should only be 1, 2 or 3.")
        c = input("Choose which column you want your symbol to be placed in: ")
        while True:
            try:
                c = int(c)
                break
            except ValueError:
                print("Your input is not an integer.")
                c = input("Choose which column you want your symbol to be placed in: ")
    return c

def symbol_place(d, e, f):
    e-=1
    if d==1:
        row_1[e] = f
    elif d==2:
        row_2[e] = f
    else:
        row_3[e] = f
    print(row_1[0], " |", row_1[1], "|", row_1[2])
    print("-"*9)
    print(row_2[0], " |", row_2[1], "|", row_2[2])
    print("-"*9)
    print(row_3[0], " |", row_3[1], "|", row_3[2])
    print("="*9)

def computer_location_pull(g, h, i, r, s, t, z, m):
    g = str(g)
    h = str(h)
    user_location = g+", "+h
    i.remove(user_location)
    u = [row_1[0], row_2[0], row_3[0]]
    v = [row_1[1], row_2[1], row_3[1]]
    w = [row_1[2], row_2[2], row_3[2]]
    x = [row_1[0], row_2[1], row_3[2]]
    y = [row_1[2], row_2[1], row_3[0]]
    if r==["", m, m] or u==["", m, m] or x==["", m, m]:
        computer_location = "1, 1"
    elif r==[m, "", m] or v==["", m, m]:
        computer_location = "1, 2"
    elif r==[m, m, ""] or w==["", m, m] or y==["", m, m]:
        computer_location = "1, 3"
    elif s==["", m, m] or u==[m, "", m]:
        computer_location = "2, 1"
    elif s==[m, "", m] or v==[m, "", m] or x==[m, "", m] or y==[m, "", m]:
        computer_location = "2, 2"
    elif s==[m, m, ""] or w==[m, "", m]:
        computer_location = "2, 3"
    elif t==["", m, m] or u==[m, m, ""] or y==[m, m, ""]:
        computer_location = "3, 1"
    elif t==[m, "", m] or v==[m, m, ""]:
        computer_location = "3, 2"
    elif t==[m, m, ""] or w==[m, m, ""] or x==[m, m, ""]:
        computer_location = "3, 3"
    elif r==["", z, z] or u==["", z, z] or x==["", z, z]:
        computer_location = "1, 1"
    elif r==[z, "", z] or v==["", z, z]:
        computer_location = "1, 2"
    elif r==[z, z, ""] or w==["", z, z] or y==["", z, z]:
        computer_location = "1, 3"
    elif s==["", z, z] or u==[z, "", z]:
        computer_location = "2, 1"
    elif s==[z, "", z] or v==[z, "", z] or x==[z, "", z] or y==[z, "", z]:
        computer_location = "2, 2"
    elif s==[z, z, ""] or w==[z, "", z]:
        computer_location = "2, 3"
    elif t==["", z, z] or u==[z, z, ""] or y==[z, z, ""]:
        computer_location = "3, 1"
    elif t==[z, "", z] or v==[z, z, ""]:
        computer_location = "3, 2"
    elif t==[z, z, ""] or w==[z, z, ""] or x==[z, z, ""]:
        computer_location = "3, 3"
    else:
        computer_location = random.choice(i)
    i.remove(computer_location)
    computer_row = int(computer_location[0])
    computer_column = int(computer_location[3])
    return computer_row, computer_column

def valid_user_location(j, k, l):
    j = str(j)
    k = str(k)
    user_location = j+", "+k
    while not(user_location in l):
        print("The spot is already occupied. Choose a different vacant spot.")
        j = input("Choose which row you want your symbol to be placed in: ")
        j = valid_row(j)
        k = input("Choose which column you want your symbol to be placed in: ")
        k = valid_column(k)
        j = str(j)
        k = str(k)
        user_location = j+", "+k
    j = int(j)
    k = int(k)
    return j, k

while user_symbol!="STOP":
    row_1 = ["", "", ""]
    row_2 = ["", "", ""]
    row_3 = ["", "", ""]
    count = 0
    location_list = ["1, 1", "1, 2", "1, 3", "2, 1", "2, 2", "2, 3", "3, 1", "3, 2", "3, 3"]
    print(row_1[0], " |", row_1[1], "|", row_1[2])
    print("-"*9)
    print(row_2[0], " |", row_2[1], "|", row_2[2])
    print("-"*9)
    print(row_3[0], " |", row_3[1], "|", row_3[2])
    user_symbol = input("Enter your symbol (X or O) or 'stop' to stop the program: ")
    user_symbol = user_symbol.upper()
    user_symbol = valid_symbol(user_symbol)
    if user_symbol!="STOP":
        if user_symbol=="X":
            computer_symbol = "O"
        else:
            computer_symbol = "X"

        while count<9:
            count+=2
            user_row = input("Choose which row you want your symbol to be placed in: ")
            user_row = valid_row(user_row)
            user_column = input("Choose which column you want your symbol to be placed in: ")
            user_column = valid_column(user_column)
            user_location = valid_user_location(user_row, user_column, location_list)
            user_row = user_location[0]
            user_column = user_location[1]
            symbol_place(user_row, user_column, user_symbol)
            if count<9:
                computer_location = computer_location_pull(user_row, user_column, location_list, row_1, row_2, row_3, user_symbol, computer_symbol)
                computer_row = computer_location[0]
                computer_column = computer_location[1]
                symbol_place(computer_row, computer_column, computer_symbol)
            if count>5:
                column_1 = [row_1[0], row_2[0], row_3[0]]
                column_2 = [row_1[1], row_2[1], row_3[1]]
                column_3 = [row_1[2], row_2[2], row_3[2]]
                diagonal_1 = [row_1[0], row_2[1], row_3[2]]
                diagonal_2 = [row_1[2], row_2[1], row_3[0]]
                if row_1==[user_symbol, user_symbol, user_symbol] or row_2==[user_symbol, user_symbol, user_symbol] or row_3==[user_symbol, user_symbol, user_symbol] or column_1==[user_symbol, user_symbol, user_symbol] or column_2==[user_symbol, user_symbol, user_symbol] or column_3==[user_symbol, user_symbol, user_symbol] or diagonal_1==[user_symbol, user_symbol, user_symbol] or diagonal_2==[user_symbol, user_symbol, user_symbol]:
                    print('''
Congratulations!
You won!
                        ''')
                    user_score+=1
                    break
                elif row_1==[computer_symbol, computer_symbol, computer_symbol] or row_2==[computer_symbol, computer_symbol, computer_symbol] or row_3==[computer_symbol, computer_symbol, computer_symbol] or column_1==[computer_symbol, computer_symbol, computer_symbol] or column_2==[computer_symbol, computer_symbol, computer_symbol] or column_3==[computer_symbol, computer_symbol, computer_symbol] or diagonal_1==[computer_symbol, computer_symbol, computer_symbol] or diagonal_2==[computer_symbol, computer_symbol, computer_symbol]:
                    print('''
Oh no!
You lost
                        ''')
                    computer_score+=1
                    break
                elif count==10:
                    print("It's a tie!")
                    print("")
                    break
print("Your score: ", user_score)
print("Computer's score: ", computer_score)