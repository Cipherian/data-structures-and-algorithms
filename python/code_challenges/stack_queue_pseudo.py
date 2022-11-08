from data_structures.stack import Stack


class PseudoQueue(Stack):

    def enqueue(self, value):
        temp = PseudoQueue()
        while self.is_empty() is False:
            temp.push(self.pop())
        self.push(value)
        while temp.is_empty() is False:
            self.push(temp.pop())

    def dequeue(self):
        if self.is_empty() is False:
            return self.pop()


