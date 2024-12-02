import time


class LightSwitchSimulation:
    def __init__(self, light_switch, mqtt_manager):
        self.light_switch = light_switch
        self.mqtt_manager = mqtt_manager

    def simulate(self):
        """Simulate the light switch and publish its state."""
        while True:
            self.simulate_step()
            time.sleep(4)  # Simulate every 4 seconds

    def simulate_step(self):
        """Simulate one step for the light switch."""
        if self.light_switch.powered:
            state = self.light_switch.toggle_state()
            topic = f"home/{self.light_switch.group_id}/{self.light_switch.device_type}/{self.light_switch.device_id}/state/update"
            self.mqtt_manager.publish(topic, state)
            print(f"Published to {topic}: {state}")
        else:
            print(
                f"{self.light_switch.device_type} {self.light_switch.device_id} is powered OFF."
            )
