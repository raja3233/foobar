from math import factorial
def answer(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1
    root = seq[0]
    left_size = 0
    right_size = 0
    left_seq =[]
    right_seq =[]
    for value in seq[1:]:
        if value > root :
            left_size += 1
            left_seq.append(value)
        else:
            right_size += 1
            right_seq.append(value)
    permutations = (factorial(right_size + left_size) /
                    (factorial(right_size) * factorial(left_size)))
    return permutations * answer(right_seq) * answer(left_seq)