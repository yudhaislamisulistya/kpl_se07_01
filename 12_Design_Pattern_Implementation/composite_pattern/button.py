from abc import ABC, abstractmethod

# Composite Pattern
class Button(ABC):
    @abstractmethod
    def press(self):
        pass

class SingleButton(Button):
    def __init__(self, label):
        self.label = label

    def press(self):
        print(f"Button '{self.label}' pressed.")
