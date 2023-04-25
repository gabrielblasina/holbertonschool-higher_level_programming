#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    max_value = max(a_dictionary.values())
    best_key = [k for k, v in a_dictionary.items() if v == max_value][0]
    return best_key
