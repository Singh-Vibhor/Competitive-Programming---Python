import collections
import string


def distance(a, b):
    return abs(ord(a) - ord(b))


def cheapest_good_form(s):
    state_to_min_cost = {(None, False): 0}
    for original_letter in s:
        options = collections.defaultdict(list)
        for state, min_cost in state_to_min_cost.items():
            previous_letter, needs_adjacent_copy = state
            for letter in string.ascii_lowercase:
                cost = min_cost + distance(original_letter, letter)
                if letter == previous_letter:
                    options[(letter, False)].append(cost)
                elif not needs_adjacent_copy:
                    options[(letter, True)].append(cost)
        state_to_min_cost = {state: min(costs) for (state, costs) in options.items()}
    return min((cost for ((_, needs_adjacent_copy),cost,) in state_to_min_cost.items()if not needs_adjacent_copy),default=0,)


print(cheapest_good_form(""))
print(cheapest_good_form("a"))
print(cheapest_good_form("azcb"))
print(cheapest_good_form("abcdef"))

