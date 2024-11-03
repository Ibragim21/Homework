# 1
# element = 5
# t = (1, 5, 3, 5, 5, 2)
# occurrences = t.count(element)
# 2
# t = (1, 5, 3, 5, 2)
# max_element = max(t) if t else None
# 3
# t = (1, 5, 3, 5, 2)
# min_element = min(t) if t else None
# 4
# element = 3
# t = (1, 5, 3, 5, 2)
# is_present = element in t
# 5
# t = (1, 5, 3, 5, 2)
# first_element = t[0] if t else None
# 6
# t = (1, 5, 3, 5, 2)
# last_element = t[-1] if t else None
# 7
# t = (1, 5, 3, 5, 2)
# length = len(t)
# 8
# t = (1, 5, 3, 5, 2)
# sliced_tuple = t[:3]
# 9
# t1 = (1, 2, 3)
# t2 = (4, 5, 6)
# concatenated = t1 + t2
# 10
# t = ()
# is_empty = len(t) == 0
# 11
# element = 5
# t = (1, 5, 3, 5, 5, 2)
# indices = [i for i, x in enumerate(t) if x == element]
# 12
# t = (1, 5, 3, 5, 2)
# unique_sorted = sorted(set(t), reverse=True)
# second_largest = unique_sorted[1] if len(unique_sorted) > 1 else None
# 13
# t = (1, 5, 3, 5, 2)
# unique_sorted = sorted(set(t))
# second_smallest = unique_sorted[1] if len(unique_sorted) > 1 else None
# 14
# element = 7
# single_element_tuple = (element,)
# 15
# lst = [1, 2, 3, 4]
# converted = tuple(lst)
# 16
# t = (1, 2, 3, 4)
# is_sorted = all(t[i] <= t[i + 1] for i in range(len(t) - 1))
# 17
# start, end = 1, 3
# t = (1, 5, 3, 5, 2)
# max_subtuple = max(t[start:end + 1]) if start <= end < len(t) else None
# 18
# start, end = 1, 3
# t = (1, 5, 3, 5, 2)
# min_subtuple = min(t[start:end + 1]) if start <= end < len(t) else None
# 19
# element = 5
# t = (1, 5, 3, 5, 2)
# lst = list(t)
# if element in lst:
#     lst.remove(element)
# removed = tuple(lst)
# 20
# indices = [(0, 2), (1, 3)]
# t = (1, 5, 3, 5, 2)
# nested = tuple(tuple(t[i] for i in idx) for idx in indices)
# 21
# times = 3
# t = (1, 2, 3)
# repeated = tuple(x for x in t for _ in range(times))
# 22
# start, end = 1, 10
# range_tuple = tuple(range(start, end + 1))
# 23
# t = (1, 2, 3, 4)
# reversed_tuple = t[::-1]
# 24
# t = (1, 2, 3, 2, 1)
# is_palindrome = t == t[::-1]
# 25
# t = (1, 2, 3, 2, 1)
# seen = set()
# unique = tuple(x for x in t if not (x in seen or seen.add(x)))
