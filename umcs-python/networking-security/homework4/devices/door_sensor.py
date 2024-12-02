from .device import Device  # Import the base Device class


class DoorSensor(Device):
    def __init__(self, group_id, device_id):
        super().__init__(group_id, "door_sensor", device_id)
        self.state = "CLOSED"

    def open_door(self):
        if self.powered:
            self.state = "OPEN"
            print(f"Door Sensor {self.device_id}: Door is OPEN.")
        else:
            print(f"Door Sensor {self.device_id} cannot operate. Power is OFF.")

    def close_door(self):
        if self.powered:
            self.state = "CLOSED"
            print(f"Door Sensor {self.device_id}: Door is CLOSED.")
        else:
            print(f"Door Sensor {self.device_id} cannot operate. Power is OFF.")
