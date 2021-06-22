# Changable variables
string_to_hash = "Hello world!"
column_length = 10
# Changable variables end here


def convert_string_to_hash(column_no, string):
    to_hash_string = string
    convert_matrix = [[]]
    convert_matrix_level = 0

    convert_matrix, convert_matrix_level = convert_string_to_matrix(
        to_hash_string, column_no, convert_matrix, convert_matrix_level)

    last_row = convert_matrix[convert_matrix_level]

    fill_matrix_gaps(column_no, last_row)

    return create_hash_from_matrix(column_no, convert_matrix)


def convert_string_to_matrix(string, column_no, matrix, matrix_level):
    for v in string:
        if len(matrix[matrix_level]) == column_no:
            matrix_level = matrix_level + 1
            matrix.append([v])
        else:
            matrix[matrix_level].append(v)

    return matrix, matrix_level


def fill_matrix_gaps(column_no, row):
    len_last_row = len(row)
    if len_last_row < column_no:
        needed_number = column_no - len_last_row
        for i in range(needed_number):
            row.append(" ")


def create_hash_from_matrix(column_no, matrix):
    final_hash = ""
    col_level = 0
    row_level = 0

    for dip in range(column_no):
        for local_row in range(len(matrix)):
            row_level = (len(matrix)-1) - local_row

            col_level = dip
            final_hash += str(matrix[row_level][col_level])

    return final_hash


def decodeCode():
    pass


print(convert_string_to_hash(column_length, string_to_hash))
