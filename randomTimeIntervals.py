import random
def generateIntervals(start=0,end=20,frequency=10):
    time_overlapping_intervals = []
    for i in range(frequency):
        x = random.randint(start, end - 1)
        y = random.randint(x + 1, end)
        time_overlapping_intervals.append([x, y])

    return time_overlapping_intervals

