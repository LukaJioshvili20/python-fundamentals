import time


class VacuumCleanerSimulation:
    def __init__(self, vacuum_cleaner, mqtt_manager):
        self.vacuum_cleaner = vacuum_cleaner
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the vacuum cleaner and publish its commands."""
        while True:
            self.simulate_step()
            time.sleep(5)  # Simulate every 5 seconds

    def simulate_step(self):
        """Simulate one step for the vacuum cleaner."""
        if self.vacuum_cleaner.powered:
            command = self.vacuum_cleaner.generate_command()
            topic = f"home/{self.vacuum_cleaner.group_id}/{self.vacuum_cleaner.device_type}/{self.vacuum_cleaner.device_id}/command/update"
            self.mqtt_manager.publish(topic, command)
            print(f"Published to {topic}: {command}")
        else:
            print(
                f"{self.vacuum_cleaner.device_type} {self.vacuum_cleaner.device_id} is powered OFF."
            )
