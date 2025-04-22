from abc import abstractmethod, ABC


class Subsystem(ABC):
    @abstractmethod
    def operation1(self) -> str:
        pass

    @abstractmethod
    def operation_n(self) -> str:
        pass


class Facade:
    def __init__(self, subsystem1: Subsystem, subsystem2: Subsystem):
        self._subsystem1 = subsystem1 or subsystem1()
        self._subsystem2 = subsystem2 or subsystem2()

    def operation(self):
        results = []
        results.append("Facade initializes subsystems:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade orders subsystems to perform the action:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!"

    def operation_n(self) -> str:
        return "Subsystem1: Go!"


class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Ready!"

    def operation_z(self) -> str:
        return "Subsystem2: Go!"


subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
res = facade.operation()
print(res)
