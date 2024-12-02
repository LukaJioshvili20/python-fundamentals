from .device import Device  # Import the base Device class


class LightSwitch(Device):
    def __init__(self, group_id, device_id):
        super().__init__(group_id, "light_switch", device_id)
        self.state = "OFF"

    def toggle(self):
        if self.powered:
            self.state = "ON" if self.state == "OFF" else "OFF"
            print(f"Light Switch {self.device_id} toggled to {self.state}.")
        else:
            print(f"Light Switch {self.device_id} cannot toggle. Power is OFF.")

    def set_state(self, state):
        if self.powered:
            if state.upper() in ["ON", "OFF"]:
                self.state = state.upper()
                print(f"Light Switch {self.device_id} set to {self.state}.")
            else:
                print("Invalid state. Use 'ON' or 'OFF'.")
        else:
            print(f"Light Switch {self.device_id} cannot change state. Power is OFF.")
