from command import TurnOnCommand, TurnOffCommand, Device

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

if __name__ == '__main__':
    # Device instances
    light = Device("Light")

    # Command instances
    turn_on_light = TurnOnCommand(light)
    turn_off_light = TurnOffCommand(light)

    # Remote control invoker
    remote = RemoteControl()

    # Menyalakan lampu
    remote.set_command(turn_on_light)
    remote.press_button()

    # Mematikan lampu
    remote.set_command(turn_off_light)
    remote.press_button()
