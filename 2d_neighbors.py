import sys

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.dist2origin = x + y
    def __str__(self):
        return f'{self.x}, {self.y}'
    def __repr__(self):
        return f'({self.x}, {self.y})'

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def push(self,elem,metric):
        for i in range(len(self.queue)):
            if metric(elem) <= metric(self.queue[i]):
                self.queue.insert(i,elem)
                return None
        self.queue.append(elem)
        return None

    def pop(self):
        return self.queue.pop(0)
    
    def flush(self):
        self.queue = []

    def __repr__(self):
        return self.queue.__repr__()
    
    def size(self):
        return len(self.queue)
    
    def __len__(self):
        return len(self.queue)

def main():
    args = sys.argv[1:]
    pq = PriorityQueue()
    file = args[0]
    dist = int(args[1])
    f = open(file,"r")
    for l in f:
        x , y = l.split(" ", maxsplit=1)
        pq.push(Point(int(x),int(y)),lambda p: p.x)
    
    print('Total number of points: {}'.format(len(pq)))

    bands = []
    p0 = pq.pop()
    pq_temp = PriorityQueue()
    while(not pq.is_empty()):
        p1 = pq.pop()
        if p1.x - p0.x <= dist:
            if pq_temp.is_empty():
                pq_temp.push(p0,lambda p: p.y)
            pq_temp.push(p1,lambda p: p.y)
        else:
            if len(pq_temp) >= 2:
                bands.append(pq_temp)
                pq_temp = PriorityQueue()
        p0 = p1

    if len(pq_temp) >= 2:
        bands.append(pq_temp)

    neighboors = []

    for b in bands:
        p0 = b.pop()
        is_p0_in = False
        while(not b.is_empty()):
            p1 = b.pop()
            if (p1.y - p0.y <= dist) and (abs(p1.x - p0.x) <= dist):
                if not is_p0_in:
                    neighboors.append(p0)
                    is_p0_in = True
                neighboors.append(p1)
            p0 = p1

    print('Total number of neighbors: {}'.format(len(neighboors)))

    file_result = file.split(".txt")[0] + "_d" + str(dist) + "_result.txt"
    f = open(file_result,'w')
    for n in neighboors:
        f.write(f'{n.x} {n.y}\n')

if __name__ == "__main__":
    main()