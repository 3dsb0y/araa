# ARAA (Adaptive Randomized Anti-AFK)

## Description

ARAA is a lightweight script that helps prevent getting kicked for being AFK (Away From Keyboard) by performing random actions like mouse movements, key presses, typing, and other in-game interactions. It simulates user activity to keep you active and avoid automatic logouts due to inactivity.

## Installation

### Prerequisites

Before running the script, you need to install some Python libraries. You can install them using `pip`:

1. Install the required dependencies:
    ```bash
    pip install pydirectinput colorama
    ```

   These libraries are used for simulating keyboard and mouse events, as well as handling colored terminal output.

2. Additionally, the following standard libraries are required (no installation needed for these):
   - `shutil` – for file and system operations.
   - `urllib` – for HTTP requests.
   - `ctypes` – for interacting with system-level functions (Windows-specific).

### Download the Script

1. Clone the repository:
    ```bash
    git clone https://github.com/nwsynx/araa.git
    cd araa
    ```

2. Make sure you have the `araa_config.json` configuration file. If it's missing, create it using the example below.

## Usage

1. Download the script from [GitHub](https://github.com/nwsynx/araa).
2. Run the script:
    ```bash
    python araa.py
    ```

The script will load the configuration file `araa_config.json`, check for updates, and begin executing random actions to simulate user activity.

## Configuration

The configuration is stored in the `araa_config.json` file, which should be in the same directory as the script. Here is an example configuration:

```json
{
  "options_mode": {
    "spin_camera": true,
    "jumps": true,
    "clicking": true,
    "move_around": true,
    "writing": true,
    "emotes": true,
    "chat_commands": true,
    "check_menu": true
  },
  "option_settings": {
    "spin_camera": {
      "minimum": 1,
      "maximum": 3
    },
    "jumps": {
      "minimum": 2,
      "maximum": 5,
      "interval": 1
    },
    "clicking": {
      "minimum": 3,
      "maximum": 10,
      "interval": 0.5,
      "duration": 0.1
    },
    "writing": {
      "interval": 0.2,
      "strings": ["Hello", "Hi", "Bye", "Thanks"]
    }
  },
  "sleep_minimum": 5,
  "sleep_maximum": 10
}
```

- **options_mode**: Enable/disable specific actions.
- **option_settings**: Customize parameters for each action.
- **sleep_minimum** and **sleep_maximum**: Set the range of time the script will "sleep" between actions.
