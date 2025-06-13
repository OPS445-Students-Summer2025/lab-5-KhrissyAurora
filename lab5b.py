#!/usr/bin/env python3
# Author ID: 114163223

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        return [f"Error reading file: {e}"]

def append_file_string(file_name, string_of_lines):  # <-- this must exist
    try:
        with open(file_name, 'a') as f:
            f.write(string_of_lines)
    except Exception as e:
        print(f"Error appending to file: {e}")

def write_file_list(file_name, list_of_lines):
    try:
        with open(file_name, 'w') as f:
            for line in list_of_lines:
                f.write(line + '\n')
    except Exception as e:
        print(f"Error writing list to file: {e}")

def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        with open(file_name_read, 'r') as f_read, open(file_name_write, 'w') as f_write:
            for i, line in enumerate(f_read.readlines(), 1):
                f_write.write(f"{i}:{line.strip()}\n")
    except Exception as e:
        print(f"Error copying with line numbers: {e}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))