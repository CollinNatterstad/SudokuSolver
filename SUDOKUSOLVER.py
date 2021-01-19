def main():
    #defines sudoku board that we are trying to solve.
    
    board = [
        [2,0,3,0,4,0,8,0,0],
        [0,0,0,0,0,3,0,9,6],
        [0,6,0,0,0,0,0,0,7],
        [0,0,0,0,3,6,0,0,0],
        [1,9,4,0,0,0,6,3,2],
        [0,0,0,4,9,0,0,0,0],
        [3,0,0,0,0,0,0,5,0],
        [9,8,0,3,0,0,0,0,0],
        [0,0,6,0,8,0,7,0,3]
    ]

    def solve(bor):
        
        #pass the next empty box into a function variable
        find = find_empty(bor)
        #if there isn't another empty box returns true. 
        if not find:
            return True
        #if there is an empty box, row/column variables are provided by find.   
        else: 
            row, col = find
        
        #function will use for loop to insert and test a number in each empty box.
        for i in range(1,10):

            if valid(bor, i, (row,col)):

                #if the solution is good, that solution replaces 0 on the board.
                bor[row][col] = i

                #If solution is correct, returns true and exits loop. 
                if solve(bor):
                    return True

                #resets last element to zero and repeats the process until a valid solution is present. 
                bor[row][col]=0

        # if none of these numbers are true, returns false and repeats loop. 
        return False


    def valid(bor, num, pos):
        
        
        #check row
        #checks through the row of 9 index positions denoting row 0 - 8.
        # checks rows to ensure that the number we just inserted is not anywhere else in the row excluding the current insertion element.       
        for i in range(len(bor[0])):
            if bor[pos[0]][i]== num and pos[1]!=i:
                return False

        #check column
        #checks through the row of 9 index position denoting column 0-8.
        #checks columns so that the number we just inserted does not match other numbers in the column. 
        for i in range(len(bor)):
            if bor[i][pos[1]] == num and pos [0] != i:
                return False
        
        #check 3x3 box
        #inte0ger division to figure out which box we are in. 
        box_x = pos[1]//3 
        box_y = pos[0]//3
        
        #looks for box multply by three to locate position pair within that box. 
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3,box_x*3 +3):
                #checks to ensure that the number we just inserted at position pair i,j does not match any other within that box. Excluding the inserted number itself. 
                if bor[i][j] == num and (i,j) !=pos:
                    return False
        
        return True

    #creates the spacing for the sudoku board. 
    def print_board(bor):

        #uses modulus to find the spacing between 3 total rows. Inserts dashed lines. 
        for i in range(len(bor)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - -")

        #uses modulus to find the vertical edge of 3x3 box. Placing a vertical line without changing the row.
            for j in range (len(bor[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end = "")

                #at index 8 prints position pair i,j
                if j == 8:
                    print(bor[i][j])
                
                #otherwise, prints value pair i,j with a space between values. 
                else:
                    print(str(bor[i][j])+ " ",end = "")
    
    def find_empty(bor):

        #enumerates over i,j position pairs until it finds a pair with a zero value. 
        for i, row in enumerate(bor):
            for j, val in enumerate(row):
                if val == 0:
                    #returns i,j position pair when value = 0. 
                    return (i,j)

        #returns none when there are no longer any empty spaces. 
        return None

   
    #print and solve functions. 
    print_board(board)
    solve(board)
    print("______________________")
    print_board(board)

if __name__ == "__main__":
    main()