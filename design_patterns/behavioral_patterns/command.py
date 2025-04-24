from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Concrete command classes
class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()


# Receiver class
class Light:
    def on(self):
        print("Light is on")

    def off(self):
        print("Light is off")


# Invoker class
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, slot, command):
        self.commands[slot] = command

    def press_button(self, slot):
        if slot in self.commands:
            self.commands[slot].execute()


# Usage
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(0, light_on)
remote.set_command(1, light_off)

remote.press_button(0)  # Output: Light is on
remote.press_button(1)  # Output: Light is off
