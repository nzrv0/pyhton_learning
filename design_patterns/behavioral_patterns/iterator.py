from collections.abc import Iterable, Iterator
from typing import Any


class WordsCollection(Iterable):
    pass


class AlphabeticalOrderIterator(Iterator):
    position: int = None
    reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self.collection = collection
        self.reverse = reverse
        self.position = -1 if reverse else 0

    def __next__(self) -> Any:
        try:
            value = self.collection[self.position]
            self.position += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class WordsCollection(Iterable):
    def __init__(self, collection: list[Any] | None = None) -> None:
        self.collection = collection or []

    def __getitem__(self, idx):
        return self.collection[idx]

    def __iter__(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> AlphabeticalOrderIterator:
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self.collection.append(item)


collection = WordsCollection()
collection.add_item("First")
collection.add_item("Second")
collection.add_item("Third")

print("Straight traversal:")
print("\n".join(collection))
print("")


print("Reverse traversal:")
print("\n".join(collection.get_reverse_iterator()), end="")
