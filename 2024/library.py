class Library:

    def split_input(input_stream, delimiter = None):
        left_column, right_column = [], []
        for line in input_stream:
            left, right = line.split(delimiter) if delimiter else line.split()
            left_column.append(left)
            right_column.append(right)
        return left_column, right_column
        
    def split_input_sorted(input_stream, delimiter = None):
        left_column, right_column = Library.split_input(input_stream, delimiter)
        return sorted(left_column), sorted(right_column)

    def read_file(filename = 'input.txt', mode = 'r'):
        input = open(filename, mode)
        return input