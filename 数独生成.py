import random

# 创建一个空的数独对象

def create_sudoku():
    return [[0 for _ in range(9)] for _ in range(9)]  # 9x9 空数独

# 检验数独是否有效

def is_valid(sudoku, row, col, num):
    # 行列是否有重合数字
    for i in range(9):
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False

    # 九宫格内是否有重合数字
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if sudoku[i][j] == num:
                return False

    return True  # 符合条件

# 填充数独

def fill_sudoku(sudoku):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:  # 找到空格
                numbers = list(range(1, 10))
                random.shuffle(numbers)  # 随机打乱数字顺序
                for num in numbers:
                    if is_valid(sudoku, row, col, num):  # 如果数字合法
                        sudoku[row][col] = num  # 填入数独
                        if fill_sudoku(sudoku):  # 如果填入数字后可以继续填入
                            return True  # 填入成功
                        else:
                            sudoku[row][col] = 0  # 填入数字后不行，需要回溯
                return False  # 所有数字都试过，仍无法填入，返回失败
    return True  # 所有空格都填满，数独有效

# 生成一个完整的数独

def generate_sudoku():
    sudoku = create_sudoku()
    fill_sudoku(sudoku)
    return sudoku

# 检查数独是否有唯一解

def has_unique_solution(sudoku):
    solutions = []
    solve_sudoku(sudoku, solutions)
    return len(solutions) == 1

# 解数独并记录所有解

def solve_sudoku(sudoku, solutions):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:  # 找到空格
                for num in range(1, 10):
                    if is_valid(sudoku, row, col, num):  # 如果数字合法
                        sudoku[row][col] = num  # 填入数独
                        if solve_sudoku(sudoku, solutions):  # 如果填入数字后可以继续填入
                            if len(solutions) > 1:
                                return False  # 找到多个解，直接返回
                            solutions.append([row[:] for row in sudoku])
                        sudoku[row][col] = 0  # 填入数字后不行，需要回溯
                return False  # 所有数字都试过，仍无法填入，返回失败
    return True  # 所有空格都填满，数独有效

# 移除一些数字以创建一个未完成的数独

def remove_numbers(sudoku, num_holes):
    count = 0
    while count < num_holes <= 50: # 移除的数字最多50个
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if sudoku[row][col] != 0:
            num = sudoku[row][col]
            sudoku[row][col] = 0
            if has_unique_solution(sudoku):
                count += 1
            else:
                sudoku[row][col] = num  # 如果移除后没有唯一解，恢复原数字

# 打印数独

def print_sudoku(sudoku):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # 打印分隔线
        print(" ".join(str(x) if x != 0 else '.' for x in row[:3]) + " | " +
              " ".join(str(x) if x != 0 else '.' for x in row[3:6]) + " | " +
              " ".join(str(x) if x != 0 else '.' for x in row[6:]))

# 示例：生成并打印一个未完成的数独
sudoku = generate_sudoku()
remove_numbers(sudoku, 40)  # 移除 40 个数字 移除数字越多，可能没有唯一解，会恢复原数字
print_sudoku(sudoku)