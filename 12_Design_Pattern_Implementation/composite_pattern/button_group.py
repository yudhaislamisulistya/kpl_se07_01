from button import SingleButton, Button

class ButtonGroup(Button):
    def __init__(self):
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def press(self):
        for button in self.buttons:
            button.press()

if __name__ == '__main__':
    # Create individual buttons
    button1 = SingleButton("Start")
    button2 = SingleButton("Stop")
    button3 = SingleButton("Reset")

    # Create a ButtonGroup and add buttons
    button_group = ButtonGroup()
    button_group.add_button(button1)
    button_group.add_button(button2)
    button_group.add_button(button3)

    print("\nPressing button group:")
    button_group.press()