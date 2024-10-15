# Luka Jioshvili
# Compiler/IDE - Pycharm
# Python 3.9
import psutil
import time
import numpy


class MonitorNetwork:
    def __init__(self):
        self.packets_receive: int = 0
        self.average_packets_receive: list = []

    def get_packets_receive(self, average_of_tries: int) -> int:
        if average_of_tries <= 0:
            return 0

        i: int = 0
        try:
            while i < average_of_tries:
                item = psutil.net_io_counters()
                print(f"Packet {i + 1}: {item}")
                self.average_packets_receive.append(item.packets_recv)
                time.sleep(1)
                i += 1
        except (TypeError, NameError) as error:
            print("<< WARNING >>  ", error)
        else:
            assert not len(self.average_packets_receive) == 0, "<< WARNING >> Not enough packets to continue."
            packet = sum(self.average_packets_receive) / len(self.average_packets_receive)
            print("Received packets acquired successfully.")
            self.set_packets_receive(packet)
        finally:
            return self.packets_receive

    def set_packets_receive(self, packet_number: int):
        try:
            self.packets_receive = int(packet_number)
        except (TypeError, NameError) as error:
            print("<< WARNING >>  ", error)
        else:
            print("Received packets saved successfully.")


class RandomNumber:
    def __init__(self):
        self.number: int = 0

    @staticmethod
    def integer_16_bits(number: int) -> int:
        return numpy.int16(number)


class InteractUser:
    def __init__(self):
        self.welcome_phrase: str = "<| Generate 16-bit integer with the network statistics |>"
        self.network_packets: str = "Insert the number of packets to acquire random number from:"
        self.type_error: str = "<< WARNING >> TypeError, please insert integer."
        self.value_error: str = "<< WARNING >> ValueError, please insert valid number"
        self.restart_phrase: str = "<< INFO >> Try again ? Insert 'y' else any key"

    def interact(self) -> int:
        print(self.welcome_phrase)
        while True:
            try:
                packet_number = input(f"{self.network_packets} ")
                packet_number = int(packet_number)
                assert not packet_number < 0, "<< WARNING >> Please insert number greater than zero ( 0 )."
            except TypeError as error:
                print(f"{self.type_error}: ", error)
            except ValueError as error:
                print(f"{self.value_error}: ", error)
            else:
                return packet_number

    def restart(self) -> bool:
        key_pressed: str = str(input(f"{self.restart_phrase} : "))
        if key_pressed.lower() == "y":
            return True

        return False


if __name__ == "__main__":
    while True:
        try:
            input_number: int = InteractUser().interact()
        except TypeError as error:
            print(error)
            break
        else:
            network = MonitorNetwork().get_packets_receive(input_number)
            random = RandomNumber().integer_16_bits(network)
            print(random)
        finally:
            restart = InteractUser().restart()
            if not restart:
                break

    print("Ding Dong !!!")
