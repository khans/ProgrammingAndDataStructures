#Schedule minimum meeting rooms based on the intervals list (start time and end time)
import heapq
class Interval:
  def __init__(self,start,end):
    self.start = start
    self.end = end

    
def minMeetingRooms(intervals):
    intervals.sort(key=lambda x:x.start)
    heap = []  # stores the end time of intervals
    for i in intervals:
        print (i.start,i.end)
        print (heap)
        if heap and i.start >= heap[0]: 
            print('Replacing')
            # means two intervals can use the same room
            heapq.heapreplace(heap, i.end)
            print(heap)
        else:
            # a new room is allocated
            print('My turn')
            heapq.heappush(heap, i.end)
            print(heap)
    return len(heap)

intervals = [(Interval(1,3)),(Interval(4,7)),(Interval(6,7)),(Interval(1,5))]
print(minMeetingRooms(intervals))