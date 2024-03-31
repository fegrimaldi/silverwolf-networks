"""Provides an action to retrieve the NTP synchronization state of a network device.

This module includes a class `GetNtpState` which inherits from `action.BaseAction`. 
It utilizes the `Device` class from the `lib.device` module to establish a connection 
to the specified network device and retrieve its NTP synchronization state.

Example:
    from lib import action
    from lib.device import Device

    class GetNtpState(action.BaseAction):
        def run(self, **parameters):
            self.conn_info["host"] = parameters["host"]
            self.device = Device(conn_info=self.conn_info)
            output = self.device.ntp_state()
            self.device.session.disconnect()
            return output

Attributes:
    None

Methods:
    run(parameters): Retrieves the NTP synchronization state of the specified network device.

"""

from lib import action
from lib.device import Device

class GetNtpState(action.BaseAction):
    def run(self, **parameters):
        """Retrieves the NTP synchronization state of the specified network device.

        Args:
            parameters (dict): A dictionary containing parameters required to run the action.
                - host (str): The hostname or IP address of the network device.

        Returns:
            dict: A dictionary containing the NTP synchronization state of the device.
        """
        self.conn_info["host"] = parameters["host"]
        self.device = Device(conn_info=self.conn_info)
        output = self.device.ntp_state()
        self.device.session.disconnect()
        return output
