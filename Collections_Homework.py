### Homework Description ###

# 1. create a list of random number of dicts (from 2 to 10)
#
# dict's random numbers of keys should be letter,
# dict's values should be a number (0-100),
# example: [{'a': 5, 'b': 7, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}]
# 2. get previously generated list of dicts and create one common dict:
#
# if dicts have same key, we will take max value, and rename key with dict number with max value
# if key is only in one dict - take it as is,
# example: {'a_1': 5, 'b': 7, 'c': 35, 'g_2': 42}


import random
import string


def generate_random_dict():
    num_keys = random.randint(2, 5)  # Random number of keys in a dict
    keys = random.sample(string.ascii_lowercase, num_keys)
    return {key: random.randint(0, 100) for key in keys}


def generate_list_of_dicts():
    num_dicts = random.randint(2, 10)  # Random number of dicts
    return [generate_random_dict() for _ in range(num_dicts)]


def merge_dicts(dict_list):
    merged = {}
    key_source = {}

    for idx, d in enumerate(dict_list, start=1):
        for key, value in d.items():
            if key not in merged or value > merged[key]:
                merged[key] = value
                key_source[key] = idx

    return {f"{k}_{key_source[k]}" if list(key_source.values()).count(v) > 1 else k: v for k, v in merged.items()}


if __name__ == "__main__":
    random_dicts = generate_list_of_dicts()
    print("Generated list of dicts:", random_dicts)
    merged_result = merge_dicts(random_dicts)
    print("Merged dict:", merged_result)
