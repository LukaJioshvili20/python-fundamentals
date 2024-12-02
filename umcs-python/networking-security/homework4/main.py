from broker.mqtt_manager import MQTTManager
from menu import DeviceSelector
from simulation.simulation_controller import SimulationController


def main():
    """
    Main function to initialize the MQTT manager, handle user input, and control simulations.
    """
    print("=== MQTT Broker Connection ===")

    # Step 1: Initialize the MQTT Manager (prompts user for broker details)
    mqtt_manager = MQTTManager()
    mqtt_manager.connect()
    mqtt_manager.start()

    # Step 2: Display device selection menu
    selector = DeviceSelector()
    selected_device = selector.get_selection()
    print(f"You selected: {selected_device}")

    # Step 3: Initialize the Simulation Controller
    controller = SimulationController(mqtt_manager)

    # Step 4: Subscribe to appropriate topics
    if selected_device == "All devices":
        # Subscribe to the root topic to listen to all messages
        mqtt_manager.subscribe(
            "home/#", lambda client, userdata, message: print_message(message)
        )
    else:
        # Subscribe to topics for the selected device
        base_topic = f"home/{selected_device.replace(' ', '_').lower()}/#"
        mqtt_manager.subscribe(
            base_topic, lambda client, userdata, message: print_message(message)
        )

    # Step 5: Start the simulation
    if selected_device == "All devices":
        controller.simulate_all_devices()
    else:
        controller.simulate_device(selected_device)

    # Stop the MQTT manager gracefully on exit
    mqtt_manager.stop()


def print_message(message):
    """
    Helper function to print received MQTT messages.

    Args:
        message: The MQTT message object containing topic and payload.
    """
    print(f"Message received on topic '{message.topic}': {message.payload.decode()}")


if __name__ == "__main__":
    main()
