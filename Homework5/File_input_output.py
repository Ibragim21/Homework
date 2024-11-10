# task1
# with open('Homework5/test.txt', mode='r') as file:
#     text=file.read()
#     print(text)
# task2
# x=int(input('enter a number: '))
# def read_lines():
#     with open('Homework5/test.txt', mode='r') as file:
#         line=file.readlines()
#         print(line[:x])
# read_lines()
# task3
# def append_text_to_file(file_name, text):
#     with open('Homework5/test.txt', 'a') as file:
#         file.write(text + '\n')
    
#     with open('Homework5/test.txt', 'r') as file:
#         content = file.read()
#         print(content)
# file_name = 'Homework5/test.txt'
# text = '\nThis is the appended text.'
# append_text_to_file(file_name, text)
# task4
# def read_last_n_lines(file_name, n):
#     with open('Homework5/test.txt', 'r') as file:
#         lines = file.readlines()
#         for line in lines[-n:]:
#             print(line, end='')

# file_name = 'Homework5/test.txt'
# n = 3
# read_last_n_lines(file_name, n)
# task5
# def read_file_into_list(file_name):
#     with open('Homework5/test.txt', 'r') as file:
#         lines = file.readlines()
#     return lines

# file_name = 'Homework5/test.txt'
# lines = read_file_into_list(file_name)
# print(lines)
# task6
# def read_file_into_variable(file_name):
#     with open('Homework5/test.txt', 'r') as file:
#         content = file.read()
#     return content

# file_name = 'Homework5/test.txt'
# content = read_file_into_variable(file_name)
# print(content)
# task7
# def read_file_into_array(file_name):
#     with open('Homework5/test.txt', 'r') as file:
#         lines = [line.strip() for line in file]
#     return lines

# file_name = 'Homework5/test.txt'
# lines_array = read_file_into_array(file_name)
# print(lines_array)
# task8
# def find_longest_words(file_name):
#     with open(file_name, 'r') as file:
#         words = file.read().split()
#     longest_words = sorted(words, key=len, reverse=True)
#     return longest_words[:5]  # Adjust the number of longest words to return

# file_name = 'Homework5/test.txt'
# longest_words = find_longest_words(file_name)
# print(longest_words)
# # task9
# def count_lines_in_file(file_name):
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#     return len(lines)

# file_name = 'Homework5/test.txt'
# num_lines = count_lines_in_file(file_name)
# print(f'Total number of lines: {num_lines}')
# # task10
# from collections import Counter

# def count_word_frequency(file_name):
#     with open(file_name, 'r') as file:
#         words = file.read().split()
#     word_counts = Counter(words)
#     return word_counts

# file_name = 'Homework5/test.txt'
# word_frequencies = count_word_frequency(file_name)
# print(word_frequencies)
# # task11
# import os

# def get_file_size(file_name):
#     file_size = os.path.getsize(file_name)
#     return file_size

# file_name = 'Homework5/test.txt'
# size = get_file_size(file_name)
# print(f'File size: {size} bytes')
# task12
# def write_list_to_file(file_name, data):
#     with open(file_name, 'w') as file:
#         for item in data:
#             file.write(f'{item}\n')

# file_name = 'Homework5/test.txt'
# data_list = ['apple', 'banana', 'cherry']
# write_list_to_file(file_name, data_list)
# task13
# def copy_file_contents(source_file, destination_file):
#     with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
#         dest.write(src.read())

# source_file = 'Homework5/test.txt'
# destination_file = 'copy.txt'
# copy_file_contents(source_file, destination_file)
# task14
# def combine_files(file1, file2, output_file):
#     with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
#         for line1, line2 in zip(f1, f2):
#             out.write(line1.strip() + ' ' + line2)

# file1 = 'Homework5/file1.txt'
# file2 = 'Homework5/file2.txt'
# output_file = 'Homework5/combined.txt'
# combine_files(file1, file2, output_file)
# task15
# import random

# def read_random_line(file_name):
#     with open(file_name, 'r') as file:
#         lines = file.readlines()
#     random_line = random.choice(lines)
#     return random_line.strip()

# file_name = 'Homework5/test.txt'
# random_line = read_random_line(file_name)
# print(f'Random line: {random_line}')
# task16
# def is_file_closed(file_name):
#     file = open(file_name, 'r')
#     is_closed = file.closed
#     file.close()
#     return is_closed

# file_name = 'Homework5/example.txt'
# closed_status = is_file_closed(file_name)
# print(f'Is the file closed? {closed_status}')
# task17
# def remove_newlines_from_file(file_name):
#     with open(file_name, 'r') as file:
#         content = file.read().replace('\n', '')
#     with open(file_name, 'w') as file:
#         file.write(content)

# file_name = 'Homework5/test.txt'
# remove_newlines_from_file(file_name)
# task18
def count_words_in_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().split()
    return len(words)

file_name = 'Homework5/test.txt'
num_words = count_words_in_file(file_name)
print(f'Number of words: {num_words}')

# task19
def extract_characters_from_files(file_list):
    characters = []
    for file_name in file_list:
        with open(file_name, 'r') as file:
            characters.extend(file.read())
    return characters

file_list = ['file1.txt', 'file2.txt']
characters = extract_characters_from_files(file_list)
print(characters)

# task20
import string

def generate_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as file:
            file.write(f'This is file {letter}.txt')

generate_alphabet_files()

# task21
import string

def create_alphabet_file(file_name, letters_per_line):
    alphabet = string.ascii_uppercase
    with open(file_name, 'w') as file:
        for i in range(0, len(alphabet), letters_per_line):
            file.write(alphabet[i:i + letters_per_line] + '\n')

file_name = 'Homework5/alphabet.txt'
letters_per_line = 5
create_alphabet_file(file_name, letters_per_line)