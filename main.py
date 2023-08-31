import random
from time import sleep
import socket
import json
import requests

# This program should implement the sudoku game on a terminal

# create the 9x9 grid
grid = [[0 for x in range(9)] for y in range(9)]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))

# function to generate a random grid with an api
def generate_random_grid():
    URL = 'https://sudoku-api.vercel.app/api/dosuku'
    r = requests.get(url = URL)
    data = r.json()
    print(data)
    # print data keys
    print(data['newboard'].keys())
    if data['newboard']['message'] != 'All Ok':
        print('Error generating the grid')
        return None
    return data['newboard']['grids'][0]['value']

# function to start the grid with some values
def start_grid():
    global grid
    grid = generate_random_grid()

    # grid = [
    #     [5, 3, 0, 0, 7, 0, 0, 0, 0],
    #     [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #     [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #     [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #     [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #     [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #     [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #     [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #     [0, 0, 0, 0, 8, 0, 0, 7, 9],
    # ]

    # # medium
    # grid = [
    #     [0, 0, 0, 2, 6, 0, 7, 0, 1],
    #     [6, 8, 0, 0, 7, 0, 0, 9, 0],
    #     [1, 9, 0, 0, 0, 4, 5, 0, 0],
    #     [8, 2, 0, 1, 0, 0, 0, 4, 0],
    #     [0, 0, 4, 6, 0, 2, 9, 0, 0],
    #     [0, 5, 0, 0, 0, 3, 0, 2, 8],
    #     [0, 0, 9, 3, 0, 0, 0, 7, 4],
    #     [0, 4, 0, 0, 5, 0, 0, 3, 6],
    #     [7, 0, 3, 0, 1, 8, 0, 0, 0],
    # ]

    # # hard
    # grid = [
    #     [0, 2, 0, 6, 0, 8, 0, 0, 0],
    #     [0, 0, 0, 0, 7, 0, 0, 1, 2],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 3],
    #     [0, 0, 0, 0, 0, 3, 2, 0, 0],
    #     [0, 9, 3, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 4, 0, 0, 0, 0],
    #     [2, 0, 0, 0, 0, 0, 0, 0, 6],
    #     [3, 0, 0, 0, 0, 0, 4, 0, 0],
    #     [4, 0, 0, 0, 0, 0, 0, 5, 0],
    # ]

    # grid = [
    #     [0, 4, 9, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 6, 0, 0, 0],
    #     [0, 0, 5, 2, 8, 0, 0, 9, 0],
    #     [0, 9, 6, 0, 0, 5, 3, 0, 8],
    #     [0, 1, 0, 0, 6, 3, 4, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 3, 0, 0, 0, 9, 8, 0],
    #     [7, 0, 0, 0, 0, 0, 0, 1, 0],
    #     [0, 6, 0, 0, 3, 0, 0, 0, 0],
    # ]
    # grid = [
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]

# function to print the grid
def print_grid():
    global grid
    for i in range(9):
        if i % 3 == 0:
            print('-------------------------')
        for j in range(9):
            if j % 3 == 0:
                print('|', end=' ')
            print(grid[i][j], end=' ')
        print('|')
    print('-------------------------')

# function to check if the grid is full
def is_full():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True

# function to check if the grid is valid
def is_valid():
    global grid
    # check rows
    for i in range(9):
        row = []
        for j in range(9):
            if grid[i][j] != 0:
                row.append(grid[i][j])
        if len(row) != len(set(row)):
            return False
    # check columns
    for i in range(9):
        col = []
        for j in range(9):
            if grid[j][i] != 0:
                col.append(grid[j][i])
        if len(col) != len(set(col)):
            return False
    # check squares
    for i in range(3):
        for j in range(3):
            square = []
            for k in range(3):
                for l in range(3):
                    if grid[3*i+k][3*j+l] != 0:
                        square.append(grid[3*i+k][3*j+l])
            if len(square) != len(set(square)):
                return False
    return True

# function to check if the grid is solved
def is_solved():
    global grid
    if is_full() and is_valid():
        return True
    return False

# function to input value on the grid (row, col, value) if is valid
def input_value(row, col, value):
    global grid
    if grid[row][col] == 0:
        grid[row][col] = value
        if not is_valid():
            remove_value(row, col)
            print('Invalid input')
    else:
        print('Invalid input')

# function to remove value from the grid (row, col)
def remove_value(row, col):
    global grid
    if grid[row][col] != 0:
        grid[row][col] = 0
    else:
        print('Invalid input')

# function to user input a value on the grid
def user_input():
    global grid
    print('Enter the row, column and value (separated by spaces):')
    row, col, value = map(int, input().split())
    input_value(row-1, col-1, value)

# function to get user input from the client {'row': row, 'col': col, 'value': value}
def get_user_input():
    global grid
    data = conn.recv(1024)
    data = data.decode()
    print(data)
    data = json.loads(data)
    print(data)
    row = data['row']
    col = data['col']
    value = data['value']
    input_value(row, col, value)

# the game should initialize the connection with the client by a socket and wait for the client to connect
# after the connection is established, the game should start the grid and print it and send it to the client
# the game should receive the user input from the client and update the grid and send it to the client
if __name__ == '__main__':
    start_grid()
    print_grid()
    
    s.listen()
    conn, addr = s.accept()
    print('Connected by', addr)
    
    conn.send(json.dumps(grid).encode())
    while not is_solved():
        get_user_input()
        # user_input()
        print_grid()
        conn.send(json.dumps(grid).encode())
    print('Congratulations! You solved the sudoku!')
    conn.close()
    s.close()
    # generate_random_grid()


    