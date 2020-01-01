# min heap priority queue helper functions: bubble_up and bubble_down
def bubble_up(queue, index):
    if index == 0: return 
    else:
        parent = (index + 1) // 2 - 1
        if queue[index].distance < queue[parent].distance:
            queue[index], queue[parent] = queue[parent], queue[index]
            bubble_up(queue, parent)
    return

def bubble_down(queue, index):
    size = len(queue)
    left = index * 2 + 1
    right = index * 2 + 2
    if left >= size: return
    elif right >= size:
        if queue[index].distance > queue[left].distance:
            queue[index], queue[left] = queue[left], queue[index]
    else:
        if queue[left].distance < queue[right].distance:
            smaller = left
        else: smaller = right
        if queue[index].distance > queue[smaller].distance:
            queue[index], queue[smaller] = queue[smaller], queue[index]
            bubble_down(queue, smaller)

# min heap used for priority queue of available parking spots
class PriorityQueue:
    def __init__(self, spot_index):
        self.q = []
        for spot in spot_index:
            self.q.append(spot)

    def insert(self, spot):
        self.q.append(spot)
        bubble_up(self.q, len(self.q) - 1)

    def pop_min(self):
        last = len(self.q) - 1
        self.q[0], self.q[last] = self.q[last], self.q[0]
        spot = self.q.pop()
        bubble_down(self.q, 0)
        return spot