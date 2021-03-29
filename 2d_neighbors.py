import sys
import heapq
import time

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'{self.x}, {self.y}'
    def __repr__(self):
        return f'({self.x}, {self.y})'
    def __eq__(self,o):
        return (
            self.__class__ == o.__class__ and
            self.x == o.x and 
            self.y == o.y
            )
    def __hash__(self):
        return hash((self.x,self.y))

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.index = 0
    
    def is_empty(self):
        return len(self.queue) == 0

    def push(self,elem,metric):
        heapq.heappush(self.queue, (metric, self.index, elem))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    def __repr__(self):
        return repr(self.queue)
    
    def size(self):
        return len(self.queue)
    
    def __len__(self):
        return len(self.queue)

def main():
    start = time.time()
    args = sys.argv[1:]
    pq_x = PriorityQueue()
    pq_y = PriorityQueue()
    neighboors = set()

    file = args[0]
    dist = int(args[1])
    f = open(file,"r")
    for l in f:
        x , y = l.split(" ", maxsplit=1)
        pq_x.push(Point(int(x),int(y)),int(x))
        pq_y.push(Point(int(x),int(y)),int(y))
    
    n_points = len(pq_x)

    bands_x = []
    p0 = pq_x.pop()
    pq_temp = PriorityQueue()
    while(not pq_x.is_empty()):
        p1 = pq_x.pop()
        if p1.x - p0.x <= dist:
            if pq_temp.is_empty():
                pq_temp.push(p0,p0.y)
            pq_temp.push(p1,p1.y)
        else:
            if len(pq_temp) >= 2:
                bands_x.append(pq_temp)
                pq_temp = PriorityQueue()
        p0 = p1

    if len(pq_temp) >= 2:
        bands_x.append(pq_temp)

    for b in bands_x:
        p0 = b.pop()
        while(not b.is_empty()):
            p1 = b.pop()
            if abs(p1.y - p0.y) + abs(p1.x - p0.x) <= dist:
                neighboors.add(p0)
                neighboors.add(p1)
            p0 = p1

    bands_y = []
    p0 = pq_y.pop()
    pq_temp = PriorityQueue()
    while(not pq_y.is_empty()):
        p1 = pq_y.pop()
        if p1.y - p0.y <= dist:
            if pq_temp.is_empty():
                pq_temp.push(p0,p0.x)
            pq_temp.push(p1,p1.x)
        else:
            if len(pq_temp) >= 2:
                bands_y.append(pq_temp)
                pq_temp = PriorityQueue()
        p0 = p1

    if len(pq_temp) >= 2:
        bands_y.append(pq_temp)

    for b in bands_y:
        p0 = b.pop()
        while(not b.is_empty()):
            p1 = b.pop()
            if abs(p1.y - p0.y) + abs(p1.x - p0.x) <= dist:
                neighboors.add(p0)
                neighboors.add(p1)
            p0 = p1

    n_neighboors = len(neighboors)
    end = time.time()
    elapsed = end - start

    print(neighboors)

    report = f'{n_points} processed in {elapsed} sec. {n_neighboors} points have neighboors at d<={dist}'

    print(report)

    file_result = file.split(".txt")[0] + "_d" + str(dist) + "_result.txt"
    f = open(file_result,'w')
    for n in neighboors:
        f.write(f'{n.x} {n.y}\n')
    f.write(report)
    f.close()

if __name__ == "__main__":
    main()