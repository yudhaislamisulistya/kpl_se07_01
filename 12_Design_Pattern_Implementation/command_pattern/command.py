from abc import ABC, abstractmethod

# Command Pattern
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()

# Receiver Class
class Device:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f'{self.name} is now ON.')

    def turn_off(self):
        print(f'{self.name} is now OFF.')
