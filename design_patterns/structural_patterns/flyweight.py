import json
from typing import Dict


class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state: str):
        s = json.dumps(self.shared_state)
        u = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory:
    fylweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict):
        for item in initial_flyweights:
            self.fylweights[self.get_key(item)] = Flyweight(item)

    def get_key(self, state: Dict):
        return "_".join(sorted(state))

    def get_flyweight(self, shared_state: Dict):
        key = self.get_key(shared_state)
        if not self.fylweights.get(key):
            print("FlyweightFactory: Can't find a flyweight, creating new one.")
            self.fylweights[key] = Flyweight(shared_state)
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self.fylweights[key]

    def list_flyweights(self):
        count = len(self.fylweights)
        print(f"FlyweightFactory: I have {count} flyweights:")
        print("\n".join(map(str, self.fylweights.keys())), end="")


def add_car_to_police_database(
    factory: FlyweightFactory,
    plates: str,
    owner: str,
    brand: str,
    model: str,
    color: str,
):
    print("\n\nClient: Adding a car to database.")
    flyweight = factory.get_flyweight([brand, model, color])
    # The client code either stores or calculates extrinsic state and passes it
    # to the flyweight's methods.
    flyweight.operation([plates, owner])


flyweights = [
    ["Chevrolet", "Camaro2018", "pink"],
    ["Mercedes Benz", "C300", "black"],
    ["Mercedes Benz", "C500", "red"],
    ["BMW", "M5", "red"],
    ["BMW", "X6", "white"],
]
factory = FlyweightFactory(flyweights)
factory.list_flyweights()


add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")

add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")
