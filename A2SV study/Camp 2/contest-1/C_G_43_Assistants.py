import heapq

t = int(input())
for _ in range(t):
    n = int(input())
    intervals = [tuple(map(int, input().split())) for _ in range(n)]

    intervals.sort()
    
    assistants = [] 
    
    for interval in intervals:
        start, end = interval
        
        if not assistants or assistants[0] > start:
            heapq.heappush(assistants, end)
        else:
           
            heapq.heappop(assistants)
            heapq.heappush(assistants, end)
  
    print(len(assistants))
