import numpy as np

def input_matrix_from_user():
    # Take matrix size as input
    while True:
        try:
            row_number = int(input("enter number of rows: "))
            column_number = int(input("enter number of columns: "))
            break
        except ValueError:
            print("That was no valid number. Try to input integer again ")
        
    # initialise matrix with zeroes
    matrix = np.zeros((row_number, column_number))

    # input each element row at a time
    for row_iterator in range(row_number):
        for column_iterator in range(column_number):
            while True:
                try:
                    matrix[row_iterator][column_iterator] = input(f'enter value for row number: {row_iterator + 1} and column number: {column_iterator +1 } ')
                    break
                except ValueError:
                    print("That was no valid number. Try to input number again ")   
    return matrix
    
matrix = input_matrix_from_user()
