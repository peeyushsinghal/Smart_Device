from typing import Union

class SmartDevice:
    """
    A class representing a smart device.
    """
    device_count = 0

    def __init__(self, device_name :str, 
                 model_number :str, 
                 is_online :bool=False) -> None:
        """
        Initialize a new SmartDevice instance.

        Args:
            device_name (str): The name of the device.
            model_number (str): The model number of the device.
            is_online (bool, optional): Whether the device is online. Defaults to False.
        Returns:
            None
        """
        self.device_name = device_name
        self.model_number = model_number
        self.is_online = is_online
        self.status = {}
        SmartDevice.device_count += 1
        self.device_info = lambda: {
            "name": self.device_name,
            "model": self.model_number,
            "online": self.is_online,
            "status": self.status
        }

    def update_status(self, attribute :str, value :int) -> None:
        """
        Update the status of the device.

        Args:
            attribute (str): The attribute to update.
            value (int): The value to update the attribute to.
        Returns:
            None
        """
        self.status[attribute] = value

    def get_status(self, attribute :str) -> Union[int, str]:
        """
        Get the status of the device.

        Args:
            attribute (str): The attribute to get the status of.

        Returns:
            Union[int, str]: The status of the attribute.
        """
        return self.status.get(attribute, 'Attribute not found')

    def toggle_online(self) -> None:
        """
        Toggle the online status of the device.

        Returns:
            None
        """
        self.is_online = not self.is_online

    def reset(self) -> None:
        """
        Reset the device to its initial state.

        Returns:
            None
        """
        self.is_online = False
        self.status = {}

    def __call__(self) -> str:
        """
        Return a string representation of the device.

        Returns:
            str: A string representation of the device.
        """
        return f"{self.device_name} (Model: {self.model_number})"
