import time


class DoorSensorSimulation:
    def __init__(self, door_sensor, mqtt_manager):
        self.door_sensor = door_sensor
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the door sensor and publish its state."""
        while True:
            self.simulate_step()
            time.sleep(2)  # Simulate every 2 seconds

    def simulate_step(self):
        """Simulate one step for the door sensor."""
        if self.door_sensor.powered:
            state = self.door_sensor.generate_state()
            topic = f"home/{self.door_sensor.group_id}/{self.door_sensor.device_type}/{self.door_sensor.device_id}/state/update"
            self.mqtt_manager.publish(topic, state)
            print(f"Published to {topic}: {state}")
        else:
            print(
                f"{self.door_sensor.device_type} {self.door_sensor.device_id} is powered OFF."
            )
