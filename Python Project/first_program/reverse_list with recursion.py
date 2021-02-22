lists = [1, 2, 3, 4, 5]

def reverse_list_recursive(some_list):
    if len(some_list) == 0:
        return []
    return  [some_list[-1]]+reverse_list_recursive(some_list[:-1])

print(reverse_list_recursive(lists))
