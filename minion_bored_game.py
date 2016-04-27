def answer(t, n):
    '''minion bored game'''
    '''Return posible paths for a given n and t'''
    current_state = [0] * n
    current_state[0] = 1
    for chance in range(t):
        new_state = [0] * n
        remaining_chances = t - chance
        #min position for minion to reach last square for t chances
        min_position = max(0, (n - 1) - remaining_chances)

        for i in range(min_position, n):
            if i == n-1:
                #only stay case for last square
                 new_state[i] += current_state[i]
            elif i == 0:
                #forward and backward for first square
                new_state[i] += current_state[i]
                new_state[i+1] += current_state[i]
            else:
                #forward backward and stay case
                new_state[i-1] += current_state[i]
                new_state[i] += current_state[i]
                new_state[i+1] += current_state[i]

        current_state = new_state
    return current_state[n-1] % 123454321




