def draw_square(size:int, filled=False, char="*")-> str:
    """
    This function draws a square of given size.

    Args:
        size (int): size of the square (side length).
        filled (bool, optional): If True, the square is filled. Defaults to False.
        char (str, optional): Character used to draw the square. Defaults to "*".

    Returns:
        str: A string representation of the square.
    """
    if size == 1:
        return char

    rows = []

    if filled:
        for _ in range(size):
            rows.append(char * size)

    else:
        rows.append(char * size)

        for _ in range(size - 2):
            rows.append(char + " " * (size - 2) + char)
        rows.append(char * size)

    return "\n".join(rows)

def draw_number_triangle(height:int)->str:
    """
    This function draws a triangle of numbers with the given height.
    i.e height = 4
    returns: 
        1 
        2 3 
        4 5 6 
        7 8 9 10
        
    Args:
        height (int): height of the triangle.

    Returns:
        string : A string representation of the number triangle.
    """
    current_number = 1
    rows = []

    for row in range(1, height + 1):
        current_row = []

        for _ in range(row):
            current_row.append(str(current_number))
            current_number += 1

            rows.append(" ".join(current_row))

    return "\n".join(rows)


def factorial(n:int):
    """
    Calculate factorial of n (n!)
    A factorial is the product of all positive integers less than or equal to n.
    i.e factorial(5) or 5! = 5 * 4 * 3 * 2 * 1 = 120

    n: non-negative integer
    return: n!
    """
    if n == 0 or n == 1:
        return 1
    
    result = 1

    for i in range(2, n + 1):
        result = result * i

    return result
    
def bar_graph()->str:
    """
    This function draws a graph of averages per class:
    
    read data from grades.txt, there is data for 8 class and marks for 15 students per class
    each row represents a class and each column represents a student marks
    
    Task is to draw a bar graph of averages per class:
    each '*' represents 10 % 
    i.e
    
    Class averages:
    1: *****
    2: ********
    3: **
    4: *****
    ... etc.

    returns:
        str: string of the graph
    """
    data = []

    with open("grades.txt", "r") as file:
        for line in file:
            marks = line.split()

            clean_marks = []
            for mark in marks:
                mark = mark.strip()
                mark = mark.replace(",", "")
                mark = int(mark)
                clean_marks.append(mark)

            data.append(clean_marks)

    graph_rows = []

    for i in range(len(data)):
        class_marks = data[i]
        average = sum(class_marks) / len(class_marks)
        number_of_stars = round(average / 10)
        row_string = "Class " + str(i + 1) + ": " + "*" * number_of_stars
        graph_rows.append(row_string)

    return "\n".join(graph_rows)


def pascals_triangle(rows:int)->list[int]:
    """ p(n, k) = n! / (k! * (n-k)!)
    
    
    n: number of rows starting from 0
    k: column number starting from 0
    i.e 
    rows 
    0:              1
    1:            1   1
    2:          1   2   1
    3:        1   3   3   1
    4:      1   4   6   4   1
    5:    1  5  10  10   5   1
    6:  1  6  15  20  15   6   1
    7:1  7 21  35  35  21   7   1
    
    example:
        pascals_triangle(5)
        returns [1, 5, 10, 10, 5, 1]
        using 'p(n, k) = n! / (k! * (n-k)!)'
    """
    pass


    
    
def main():
    chars = ['#', '*', '+', '@', '%']
    for i in range(3,8):
        print(draw_square(i,False,char=chars[i-3]))


    
            
    print()
    print(draw_number_triangle(6))
    print(factorial(5))
    print()
    print(pascals_triangle(5))
    print(bar_graph())
    print()
 
    
if __name__ == "__main__":
    main()
