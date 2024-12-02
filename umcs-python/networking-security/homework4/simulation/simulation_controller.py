# Device simulators
from .door_sensor_simulation import DoorSensorSimulation
from .indoor_sensor_simulation import IndoorSensorSimulation
from .light_switch_simulation import LightSwitchSimulation
from .outdoor_sensor_simulation import OutdoorSensorSimulation
from .vacuum_cleaner_simulation import VacuumCleanerSimulation

# Devices
from ..devices.device_type import DeviceType
from ..devices.door_sensor import DoorSensor
from ..devices.indoor_sensor import IndoorSensor
from ..devices.light_switch import LightSwitch
from ..devices.outdoor_sensor import OutdoorSensor
from ..devices.vacuum_cleaner import VacuumCleaner


class SimulationController:
    """
    Controls the simulation of devices based on user selection.
    """

    def __init__(self, mqtt_manager):
        """
        Initializes the controller with an MQTT manager and simulation classes.
        """
        self.mqtt_manager = mqtt_manager
        self.device_classes = {
            DeviceType.DOOR_SENSOR.value: DoorSensor,
            DeviceType.INDOOR_SENSOR.value: IndoorSensor,
            DeviceType.OUTDOOR_SENSOR.value: OutdoorSensor,
            DeviceType.LIGHT_SWITCH.value: LightSwitch,
            DeviceType.VACUUM_CLEANER.value: VacuumCleaner,
        }
        self.simulation_classes = {
            DeviceType.DOOR_SENSOR.value: DoorSensorSimulation,
            DeviceType.INDOOR_SENSOR.value: IndoorSensorSimulation,
            DeviceType.OUTDOOR_SENSOR.value: OutdoorSensorSimulation,
            DeviceType.LIGHT_SWITCH.value: LightSwitchSimulation,
            DeviceType.VACUUM_CLEANER.value: VacuumCleanerSimulation,
        }

    def simulate_device(self, device_name):
        """
        Simulates a single device.

        Args:
            device_name (str): The name of the device to simulate.
        """
        device_class = self.device_classes[device_name]
        simulation_class = self.simulation_classes[device_name]
        device = device_class(
            "home", device_name.replace(" ", "_").lower(), self.mqtt_manager
        )
        simulation = simulation_class(device, self.mqtt_manager)

        print(f"Simulating {device_name}... Press Ctrl+C to stop.")
        try:
            simulation.simulate()  # Run simulation
        except KeyboardInterrupt:
            print(f"\nStopped simulation for {device_name}.")

    def simulate_all_devices(self):
        """
        Simulates all devices concurrently.
        """
        simulations = []
        for name, cls in self.device_classes.items():
            device = cls("home", name.replace(" ", "_").lower(), self.mqtt_manager)
            simulation_cls = self.simulation_classes[name]
            simulations.append(simulation_cls(device, self.mqtt_manager))

        print("Simulating all devices... Press Ctrl+C to stop.")
        try:
            while True:
                for simulation in simulations:
                    simulation.simulate_step()  # Perform one step per device
        except KeyboardInterrupt:
            print("\nStopped simulation for all devices.")
