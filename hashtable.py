#!/usr/bin/python3


class HashTable:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.values = [None]*capacity

    def __len__(self) -> int:
        return self.capacity

    def __setitem__(self, key: str, value: str):
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key: str) -> str:
        index = hash(key) % len(self)
        value = self.values[index]
        if not value:
            raise KeyError(key)
        return value

    def get(self, key, default: str = None) -> str:
        index = hash(key) % len(self)
        value = self.values[index]
        if not value:
            return default
        return value

if __name__ == "__main__":
    ht = HashTable(3)
