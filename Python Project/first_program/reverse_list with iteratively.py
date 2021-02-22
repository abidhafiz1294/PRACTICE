lists = [1,2,3,4,5]

def reverse_list(A):
    new_list = []

    for i in range(0,len(A)):
       new_list.append(0)

    for i in range(len(A)-1, -1, -1):
        new_list[len(A)-1-i] = A[i]

    return new_list

print(reverse_list(lists))
