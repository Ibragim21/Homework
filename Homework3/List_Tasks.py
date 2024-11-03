#1
# mylist = [1, 2, 3, 1, 5, 1]
# print(mylist.count(1))
#2
# mylist = [1,2,2,3,4]
# print(sum(mylist))
#3
# mylist = [1,2,2,3,4]
# print(max(mylist))
#5
# mylist = [1,2,2,3,4]
# print(1 in mylist)
#6
# mylist = [1,2,2,3,4]
# if len(mylist)>0:
#     print(mylist[0])
# else:
#     print('list is empty')
#7
# mylist = [1,2,2,3,4]
# if len(mylist)>0:
#     print(mylist[len(mylist)-1])
# else:
#     print('list is empty')
#8
# mylist = [1,2,2,3,4]
# new_list=mylist[0:3]
# print(new_list)
#9
# mylist = [1,2,2,3,4]
# print(mylist[::-1])
#10
# mylist = [1,9,5,2,2,3,4]
# print(sorted(mylist))
#11
# mylist = [1,9,5,2,2,3,4,1,3]
# print(list(set(mylist)))
#12
# mylist = ['nas','k.dot','2pac','drizzy']
# mylist.insert(1,'outkast')
# print(mylist)
#13
# mylist = ['nas', 'outkast', 'k.dot', '2pac', 'drizzy']
# print(mylist.index('2pac'))
#14
# mylist = ['nas', 'outkast', 'k.dot', '2pac', 'drizzy']
# if len(mylist)>0:
#     print(False)
# else:
#     print(True)
#15
# mylist = [1,9,5,2,2,3,4,1,3]
# a=0
# for i in  mylist:
#     if i % 2 ==0:
#         a+=1
# print(a)
#16
# mylist = [1,9,5,2,2,3,4,1,3]
# a=0
# for i in  mylist:
#     if i % 2 !=0:
#         a+=1
# print(a)
#17
# mylist = [1,9,5,2,2,3,4,1,3]
# MYLIST= ['hi','bye']
# print(mylist+MYLIST)
#18
# mylist = [1,9,5,2,2,3,4,1,3]
# sublist = [1,7,6]
# for i in sublist:
#     if i in mylist:
#         print(True)
#     else:
#         print(False)
#19
# mylist = [1,9,5,2,2,3,4,1,3]
# mylist[4]='new value'
# print(mylist)
#20
# mylist = [1,9,5,2,2,3,4,1,3]
# mylist.remove(max(mylist))
# print(max(mylist))
#21
# def find_second_smallest(numbers):
#     unique_numbers = list(set(numbers))
#     unique_numbers.sort()
#     return unique_numbers[1] if len(unique_numbers) > 1 else None

# numbers = [5, 2, 9, 1, 5, 6]
# second_smallest = find_second_smallest(numbers)
# print(second_smallest)
# 22
# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter_even_numbers(numbers)
# print(even_numbers)
# 23
# def filter_odd_numbers(numbers):
#     return [num for num in numbers if num % 2 != 0]

# numbers = [1, 2, 3, 4, 5, 6]
# odd_numbers = filter_odd_numbers(numbers)
# print(odd_numbers)
# 24
# def list_length(numbers):
#     return len(numbers)

# numbers = [1, 2, 3, 4, 5, 6]
# length = list_length(numbers)
# print(length)
# 25
# def create_copy(original_list):
#     return original_list.copy()

# original_list = [1, 2, 3, 4, 5]
# copied_list = create_copy(original_list)
# print(copied_list)
# 26
# def get_middle_element(numbers):
#     n = len(numbers)
#     mid = n // 2
#     if n % 2 == 0:
#         return numbers[mid - 1: mid + 1]
#     else:
#         return numbers[mid]
# numbers = [1, 2, 3, 4, 5, 6]
# middle_elements = get_middle_element(numbers)
# print(middle_elements)
# 27
# def find_max_of_sublist(numbers, start, end):
#     return max(numbers[start:end])
# numbers = [1, 2, 3, 4, 5, 6]
# max_value = find_max_of_sublist(numbers, 1, 4)
# print(max_value)
# 28
# def find_min_of_sublist(numbers, start, end):
#     return min(numbers[start:end])
# numbers = [1, 2, 3, 4, 5, 6]
# min_value = find_min_of_sublist(numbers, 1, 4)
# print(min_value)
# 29
# def remove_element_by_index(numbers, index):
#     if 0 <= index < len(numbers):
#         return numbers[:index] + numbers[index+1:]
#     return numbers
# numbers = [1, 2, 3, 4, 5]
# new_list = remove_element_by_index(numbers, 2)
# print(new_list)
# 30
# def is_sorted(numbers):
#     return numbers == sorted(numbers)
# numbers = [1, 2, 3, 4, 5]
# sorted_check = is_sorted(numbers)
# print(sorted_check)
# 31
# def repeat_elements(numbers, times):
#     return [num for num in numbers for _ in range(times)]

# numbers = [1, 2, 3]
# repeated_list = repeat_elements(numbers, 2)
# print(repeated_list)
# 32
# def merge_and_sort(list1, list2):
#     return sorted(list1 + list2)

# list1 = [3, 1, 4]
# list2 = [2, 5]
# merged_sorted_list = merge_and_sort(list1, list2)
# print(merged_sorted_list)
# 33
# def find_all_indices(numbers, element):
#     return [i for i, x in enumerate(numbers) if x == element]

# numbers = [1, 2, 3, 2, 1, 2]
# indices = find_all_indices(numbers, 2)
# print(indices)
# 34
# def rotate_list(numbers, k):
#     k %= len(numbers)
#     return numbers[-k:] + numbers[:-k]

# numbers = [1, 2, 3, 4, 5]
# rotated_list = rotate_list(numbers, 2)
# print(rotated_list)
# 35
# def create_range_list(start, end):
#     return list(range(start, end + 1))

# range_list = create_range_list(1, 10)
# print(range_list)
# 36
# def sum_positive_numbers(numbers):
#     return sum(num for num in numbers if num > 0)

# numbers = [-1, 2, -3, 4, 5]
# positive_sum = sum_positive_numbers(numbers)
# print(positive_sum)
# 37
# def sum_negative_numbers(numbers):
#     return sum(num for num in numbers if num < 0)
# numbers = [-1, 2, -3, 4, 5]
# negative_sum = sum_negative_numbers(numbers)
# print(negative_sum)
# 38
# def check_palindrome(numbers):
#     return numbers == numbers[::-1]

# numbers = [1, 2, 3, 2, 1]
# is_palindrome = check_palindrome(numbers)
# print(is_palindrome)
# 39
# def create_nested_list(numbers, sublist_size):
#     return [numbers[i:i + sublist_size] for i in range(0, len(numbers), sublist_size)]

# numbers = [1, 2, 3, 4, 5, 6]
# nested_list = create_nested_list(numbers, 2)
# print(nested_list)
# 40
# def unique_elements_in_order(numbers):
#     seen = set()
#     unique_numbers = []
#     for num in numbers:
#         if num not in seen:
#             unique_numbers.append(num)
#             seen.add(num)
#     return unique_numbers

# numbers = [1, 2, 3, 2, 1, 4]
# unique_ordered_list = unique_elements_in_order(numbers)
# print(unique_ordered_list)