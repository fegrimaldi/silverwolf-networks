

# Silverwolf Networks

Welcome to the Silverwolf Networks repository! This repository contains code for managing network devices, focusing on tasks such as retrieving 
BGP, NTP, and OSPF states. Below is an overview of the structure and functionality of the codebase.


SilverWolf Networks StackStorm/Gluware intergration proof-of-concept.

## Repository Structure

The repository consists of the following components:

- **`actions/`**: This directory contains specific actions implemented using the base action classes defined in `lib/action.py`.
  - `ntp_state`: 
  - `ospf_state`: 
  - `bgp_state`: 

- **`actions/lib/`**: This directory contains the main logic for interacting with network devices. It includes the following files:
  - `device.py`: Defines a `Device` class responsible for establishing connections to network devices and retrieving their states.
  - `action.py`: Defines base action classes that serve as foundations for implementing specific actions related to network device management.

- **`actions/workflows`**: Workflows
  - `get_device_state`: lorem ipsum
    - `ntp_state`
    - `ospf_state`
    - `bgp_state`

- **`rules`**: Rules (triggers)
  - `nagios_trigger`: lorem ipsum
  
- **`README.md`**: This file provides an overview of the repository and its contents.

## Components

### `lib/device.py`

This file contains a Python class `Device` responsible for interacting with network devices. It provides methods to retrieve the following states:

- NTP synchronization state (`ntp_state()`)
- BGP neighbor states (`bgp_state()`)
- OSPF neighbor count and IDs (`ospf_state()`)

### `lib/action.py`

This file defines a base action class `BaseAction`, which serves as the foundation for implementing various actions related to network device management. It includes methods for initializing actions with configuration parameters and running the action logic.

### `actions/`

This directory contains specific actions implemented using the `BaseAction` class. Each action corresponds to a specific task, such as retrieving BGP state (`GetBgpState`), NTP state (`GetNtpState`), or OSPF state (`GetOspfState`).

## Getting Started

To use the code in this repository, follow these steps:

1. Clone the repository to your local machine:

    `git clone <repository-url>`

2. Install the required dependencies:

    `st2 pack install file:///path/to/repo/silverwolf-networks`


3. Use the provided actions or extend them to suit your specific use case.

## Contributing

Contributions to Silverwolf Networks are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the Apache License - see the [LICENSE](LICENSE) file for details.

---

Silverwolf Networks - Developed by Fabricio Grimaldi.


