from abc import ABC, abstractmethod


class PlayerDecorator(ABC):
    @abstractmethod
    def handle_input(self, c):
        pass


class BasePlayer:
    def __init__(self):
        pass

    def handle_input(self, c):
        if c == "w":
            print("moving forward")
        elif c == "a":
            print("moving left")
        elif c == "s":
            print("moving back")
        elif c == "d":
            print("moving right")
        elif c == "e":
            print("attacking ")
        elif c == " ":
            print("jumping")
        else:
            print("undefined command")


class BlazingPlayer(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee

    def handle_input(self, c):
        if c == "e":
            print("using fire ", end="")

        self.wrapee.handle_input(c)


class BowmanPlayer(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee

    def handle_input(self, c):
        if c == "e":
            print("with arrows ", end="")

        self.wrapee.handle_input(c)


class BouncyPlayer(PlayerDecorator):
    def __init__(self, wrapee):
        self.wrapee = wrapee

    def handle_input(self, c):
        if c == " ":
            print("double jump")
        else:
            self.wrapee.handle_input(c)


player = BasePlayer()
player.handle_input("e")
player.handle_input(" ")


player = BlazingPlayer(player)
player.handle_input("e")
player.handle_input(" ")
