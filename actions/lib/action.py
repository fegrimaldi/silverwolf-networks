"""Provides a base action class for implementing actions related to network device management.

This module defines a base class `BaseAction` which inherits from `st2common.runners.base_action.Action`. 
It serves as the foundation for implementing various actions related to network device management. 
It initializes connection information for network devices using configuration parameters such as 
username and password.

Example:
    from st2common.runners.base_action import Action

    class MyAction(BaseAction):
        def __init__(self, config):
            super(MyAction, self).__init__(config)
            # Additional initialization logic

        def run(self, **parameters):
            # Implement the logic for the action
            pass

Attributes:
    None

Methods:
    __init__(config): Initializes the action with the provided configuration parameters.
    run(parameters): This method should be overridden in derived classes to implement the 
    specific action logic.

"""

from st2common.runners.base_action import Action

class BaseAction(Action):
    def __init__(self, config):
        """Initializes the action with configuration parameters.

        Args:
            config (dict): A dictionary containing configuration parameters.
        """
        super(BaseAction, self).__init__(config)
        self._username = self.config["username"]
        self._password = self.config["password"]

        self.conn_info = {
            "device_type": "cisco_nxos",
            "host": None,
            "username": self._username,
            "password": self._password,
        }
