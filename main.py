# Changable variables
string_to_hash = "Hello world!"
# Changable variables end here

convert_matrix = [[]]
convert_matrix_level = 0


def convert_string_to_matrix(matrix, matrix_level):
    for v in string_to_hash:
        if len(matrix[matrix_level]) == 5:
            matrix_level = matrix_level + 1
            matrix.append([v])
        else:
            matrix[matrix_level].append(v)

    return matrix, matrix_level


convert_matrix, convert_matrix_level = convert_string_to_matrix(
    convert_matrix, convert_matrix_level)

last_row = convert_matrix[convert_matrix_level]


def fill_matrix_gaps(row):
    len_last_row = len(row)
    if len_last_row < 5:
        needed_number = 5 - len_last_row
        for i in range(needed_number):
            row.append(" ")


fill_matrix_gaps(last_row)


def create_hash_from_matrix(matrix):
    final_hash = ""
    col_level = 0
    row_level = 0

    for dip in range(5):
        for local_row in range(len(matrix)):
            row_level = (len(matrix)-1) - local_row

            col_level = dip
            final_hash += str(matrix[row_level][col_level])

    return final_hash


def decodeCode():
    pass


hashed_code = create_hash_from_matrix(convert_matrix)
print(f"'{hashed_code}'")
