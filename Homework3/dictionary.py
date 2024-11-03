1
d = {'a': 1, 'b': 2}
key = 'a'
value = d.get(key, 'Key not found')
2
d = {'a': 1, 'b': 2}
key = 'a'
exists = key in d
3
d = {'a': 1, 'b': 2}
key_count = len(d)
4
d = {'a': 1, 'b': 2}
keys_list = list(d.keys())
5
d = {'a': 1, 'b': 2}
values_list = list(d.values())
6
d1 = {'a': 1}
d2 = {'b': 2}
merged_dict = {**d1, **d2}
7
d = {'a': 1, 'b': 2}
key = 'a'
removed_value = d.pop(key, 'Key not found')
8
d = {'a': 1, 'b': 2}
d.clear()
9
d = {}
is_empty = len(d) == 0
10
d = {'a': 1, 'b': 2}
key = 'a'
key_value_pair = (key, d[key]) if key in d else 'Key not found'
11
d = {'a': 1, 'b': 2}
key = 'a'
d[key] = 3
12
d = {'a': 1, 'b': 2, 'c': 1}
value_count = list(d.values()).count(1)
13
d = {'a': 1, 'b': 2}
inverted_dict = {v: k for k, v in d.items()}
14
d = {'a': 1, 'b': 2, 'c': 1}
value = 1
keys_with_value = [k for k, v in d.items() if v == value]
15
keys = ['a', 'b']
values = [1, 2]
d = dict(zip(keys, values))
16
d = {'a': 1, 'b': {'c': 2}}
has_nested_dict = any(isinstance(v, dict) for v in d.values())
17
d = {'a': 1, 'b': {'c': 2}}
nested_value = d['b'].get('c')
18
from collections import defaultdict
default_dict = defaultdict(lambda: 'default value')
19
d = {'a': 1, 'b': 2, 'c': 1}
unique_values_count = len(set(d.values()))
20
d = {'b': 2, 'a': 1}
sorted_by_key = dict(sorted(d.items()))
21
d = {'b': 2, 'a': 1}
sorted_by_value = dict(sorted(d.items(), key=lambda item: item[1]))
22
d = {'a': 1, 'b': 2, 'c': 3}
filtered_dict = {k: v for k, v in d.items() if v > 1}
23
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
common_keys = d1.keys() & d2.keys()
24
t = (('a', 1), ('b', 2))
d = dict(t)
25
d = {'a': 1, 'b': 2}
first_pair = next(iter(d.items()), 'Dictionary is empty')