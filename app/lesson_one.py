# this is a practice from codility lesson one
def solution(N):
    N = _remove_zeros_in_the_end(N)
    max_length = 0
    length_counter = 0

    while N >= 1:
        if N % 2 == 0:
            length_counter += 1
        else:
            if max_length < length_counter: max_length = length_counter
            length_counter = 0
        N //= 2
    return max_length

def _remove_zeros_in_the_end(N):
    while N > 1 and N % 2 == 0: N //= 2
    return N