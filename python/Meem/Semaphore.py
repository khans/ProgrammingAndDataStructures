#Sempahoreis a lock that can hold multiple resources at a time, like 5 cpus, so available would be 5

from collections import deque
class Semaphore():
    def __init__(self,id,available):
        
        self.id = id
        self.available = available
        self.max = available
        self.queue = deque()
        
    def enter(self, t1):
        if self.available > 0:
            self.available -= 1
            return
        elif self.available == 0:
            self.queue.append(t1)
    
    def exit(self,t1):
        self.available += 1
        self.queue.popleft()
        return
    