import socket
import json

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
grid = json.loads(client_socket.recv(1024).decode())
print(grid)

backtracking_grid = grid

# function to check if the grid is full
def is_full():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True

### SOLVING WITH BACKTRACKING

#function to check if the value is valid for the row
def is_valid_row(row, value):
    global grid
    for i in range(9):
        if grid[row][i] == value:
            return False
    return True

#function to check if the value is valid for the column
def is_valid_col(col, value):
    global grid
    for i in range(9):
        if grid[i][col] == value:
            return False
    return True

#function to check if the value is valid for the box
def is_valid_box(row, col, value):
    global grid
    box_row = row // 3
    box_col = col // 3
    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if grid[i][j] == value:
                return False
    return True

# function implementing the backtracking algorithm
def backtracking():
    print('backtracking')
    global backtracking_grid
    for row in range(9):
        for col in range(9):
            if backtracking_grid[row][col] == 0:
                for value in range(1, 10):
                    if is_valid_row(row, value) and is_valid_col(col, value) and is_valid_box(row, col, value):
                        backtracking_grid[row][col] = value
                        print_backtracking_grid()
                        if backtracking():
                            return True
                        backtracking_grid[row][col] = 0
                return False
    print_backtracking_grid()
    if is_full():
        print('is_full')
        return True
    

# function to print the grid
def print_backtracking_grid():
    print('backtracking_grid')
    global backtracking_grid
    for i in range(9):
        if i % 3 == 0:
            print('-------------------------')
        for j in range(9):
            if j % 3 == 0:
                print('|', end=' ')
            print(backtracking_grid[i][j], end=' ')
        print('|')
    print('-------------------------')


if __name__ == '__main__':
    # first call to the backtracking function
    # when the function returns True, the grid is solved and start sending the values to the server until the grid is full
    backtracking()

    # function to send the values to the server
    def send_values():
        global backtracking_grid
        for i in range(9):
            for j in range(9):
                if backtracking_grid[i][j] != 0:
                    data = json.dumps({'row': i, 'col': j, 'value': backtracking_grid[i][j]})
                    client_socket.send(data.encode())
                    grid = json.loads(client_socket.recv(1024).decode())
                    print(grid)

    send_values()