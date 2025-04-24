from abc import ABC, abstractmethod


class Meal(ABC):
    def prepare(self):
        self.required_operataion()
        self.prepare_ingredients()
        self.cook()
        self.serve()

    def prepare_ingredients(self):
        raise NotImplementedError()

    def cook(self):
        raise NotImplementedError()

    def serve(self):
        raise NotImplementedError()

    @abstractmethod
    def required_operataion(self) -> None:
        pass

    def hook1(self) -> None:
        pass


class BurgerMeal(Meal):
    def required_operataion(self):
        print(f"Starting to proccec of creating {type(self).__name__}")

    def prepare_ingredients(self):
        print("Preparing burger ingredients")

    def cook(self):
        print("Cooking burger")

    def serve(self):
        print("Serving burger")

    def hook1(self) -> None:
        print("overwriten the method")


class PizzaMeal(Meal):
    def required_operataion(self):
        print(f"Starting to proccec of creating {type(self).__name__}")

    def prepare_ingredients(self):
        print("Preparing pizza ingredients")

    def cook(self):
        print("Cooking pizza")

    def serve(self):
        print("Serving pizza")


burger_meal = BurgerMeal()
burger_meal.prepare()

pizza_meal = PizzaMeal()
pizza_meal.prepare()
