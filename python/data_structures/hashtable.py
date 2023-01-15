class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size:int = 1024):
        self.size = size
        self.prime = 31 # Change this to change the number that the hash function is primed with
        self._buckets = size * [None]


    def hash_function(self, key: str):
        return sum(ord(c) * self.prime**i for i, c in enumerate(key[::-1])) % self.size


    def set(self, key: str, value: any):
        index = self.hash_function(key)
        self._buckets[index] = [key, value]


    def get(self, key:str) -> any:
        index = self.hash_function(key)
        if self._buckets[index]:
            return self._buckets[index][1]
        else:
            return None


    def delete(self, key:str) -> None:
        index = self.hash_function(key)
        if self._buckets[index]:
            self._buckets[index] = None
        else:
            return None


    def has(self, key: str) -> bool:
        index = self.hash_function(key)
        if self._buckets[index] is not None:
            return True
        else:
            return False

    def keys(self):
        keys = []
        for i in range(self.size):
            if self._buckets[i] is not None:
                keys.append(i)
        return keys

