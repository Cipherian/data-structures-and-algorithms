from data_structures.queue import Queue, Node


class AnimalShelter:
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        if animal.value == "cat":
            self.cat.enqueue(animal)
        if animal.value == "dog":
            self.dog.enqueue(animal)
        else:
            return None

    def dequeue(self, animal):
        if animal == "cat":
            return self.cat.dequeue()
        if animal == "dog":
            return self.dog.dequeue()
        else:
            return None


class Dog(Node):
    def __init__(self, value="dog"):
        super().__init__(value)


class Cat(Node):
    def __init__(self, value="cat"):
        super().__init__(value)
