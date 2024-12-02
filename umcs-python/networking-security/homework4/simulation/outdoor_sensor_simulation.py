import time


class OutdoorSensorSimulation:
    def __init__(self, outdoor_sensor, mqtt_manager):
        self.outdoor_sensor = outdoor_sensor
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the outdoor sensor and publish its data."""
        while True:
            self.simulate_step()
            time.sleep(3)  # Simulate every 3 seconds

    def simulate_step(self):
        """Simulate one step for the outdoor sensor."""
        if self.outdoor_sensor.powered:
            data = self.outdoor_sensor.generate_data()
            for key, value in data.items():
                topic = f"home/{self.outdoor_sensor.group_id}/{self.outdoor_sensor.device_type}/{self.outdoor_sensor.device_id}/{key}/update"
                self.mqtt_manager.publish(topic, value)
                print(f"Published to {topic}: {value}")
        else:
            print(
                f"{self.outdoor_sensor.device_type} {self.outdoor_sensor.device_id} is powered OFF."
            )
