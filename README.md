Status Badge: ![Python application](https://github.com/peeyushsinghal/Smart_Device/actions/workflows/python-app-1.yml/badge.svg)

# Smart Device Class

A Python class implementation for managing smart devices with dynamic status tracking and device information management.

## Features

- Device state management (online/offline)
- Dynamic status updates and tracking
- Callable instances for quick device information
- Device information function attribute
- Device counter for tracking total instances
- Type hints for better code clarity
- Continuous Integration with GitHub Actions

## Installation

Clone this repository:
```bash
git clone <repository-url>
```

## Usage

### Basic Usage

```python
from smart_device import SmartDevice    

# Create a new device
thermostat = SmartDevice("Thermostat", "T-1000")

# Update device status
thermostat.update_status("temperature", 72)
thermostat.update_status("humidity", 45)
# Get status
current_temp = thermostat.get_status("temperature") # Returns 72
# Toggle device online state
thermostat.toggle_online() # Device is now online
```
### Device Information
```python
Get device info using the callable attribute
device_info = thermostat.device_info()
Returns: {
"name": "Thermostat",
"model": "T-1000",
"online": True,
"status": {"temperature": 72, "humidity": 45}
}
# Get formatted device string using call
device_str = thermostat() # Returns: "Thermostat (Model: T-1000)"
```
### Reset Device
```python
thermostat.reset() # Resets device to initial state
```

## API Reference

### Class: SmartDevice

#### Constructor

- `SmartDevice(device_name: str, model_number: str, is_online: bool = False)`

#### Properties

- `device_name`: Name of the device
- `model_number`: Model number of the device
- `is_online`: Online status of the device
- `status`: Dictionary containing device status attributes
- `device_count`: Class variable tracking total number of devices

#### Methods

- `update_status(attribute: str, value: int) -> None`: Update device status
- `get_status(attribute: str) -> Union[int, str]`: Get status of specific attribute
- `toggle_online() -> None`: Toggle online status
- `reset() -> None`: Reset device to initial state
- `__call__() -> str`: Get formatted device string
- `device_info() -> dict`: Get complete device information

## Testing

Run the tests using pytest:
```bash
pytest test_smart_device.py
```

## Continuous Integration

This project uses GitHub Actions for continuous integration. The workflow automatically:
- Runs on Python 3.x
- Installs dependencies
- Runs all test cases
- Validates code formatting

You can view the test results in the Actions tab of the repository. The workflow configuration can be found in `.github/workflows/python-app-1.yml`.

