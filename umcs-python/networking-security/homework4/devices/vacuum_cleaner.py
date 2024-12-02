from .device import Device  # Import the base Device class


class VacuumCleaner(Device):
    def __init__(self, group_id, device_id):
        super().__init__(group_id, "vacuum", device_id)
        self.state = "IDLE"

    def start_cleaning(self):
        if self.powered:
            self.state = "CLEANING"
            print(f"Vacuum {self.device_id} is now cleaning.")
        else:
            print(f"Vacuum {self.device_id} cannot clean. Power is OFF.")

    def stop_cleaning(self):
        if self.powered and self.state == "CLEANING":
            self.state = "IDLE"
            print(f"Vacuum {self.device_id} has stopped cleaning.")
        else:
            print(f"Vacuum {self.device_id} is already idle or not powered.")
