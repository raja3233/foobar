def answer(meetings):
    sortedList=sorted(meetings,key = lambda x: x[0])
    print sortedList
    meetings.sort(key = lambda x : x[1])
    print meetings
    meetingsAttending = [meetings[0]]
    while True:
        currentMeeting = meetingsAttending[-1]
        print meetingsAttending
        nextMeeting = findNextMeeting(currentMeeting,meetings,meetings.index(currentMeeting),len(meetings)-1)
        if not nextMeeting:
            break
        meetingsAttending.append(nextMeeting)
    return len(meetingsAttending)


def findNextMeeting(currentMeeting,meetings,left,right):
    ''' Find optimal next meeting'''
    ''' Find next non overlapping meeting that
        finishes first using Binary search Mechanism'''
    mid = (left + right)/2
    targetMeeting = meetings[mid]
    if left == right and currentMeeting[1] > targetMeeting[0]:
        return
    elif (left == right and currentMeeting[1] <= targetMeeting[0]):
        return targetMeeting
    elif currentMeeting[1] <= targetMeeting[0]:
        return findNextMeeting(currentMeeting,meetings,left,mid)
    else:
        return findNextMeeting(currentMeeting,meetings,mid+1,right)






import randomTimeIntervals
print answer([[1, 6], [1, 20], [2, 12], [4, 16], [5, 18], [8, 16], [9, 16], [17, 19], [18, 19], [19, 20]])
print answer(randomTimeIntervals.generateIntervals(frequency=10))
