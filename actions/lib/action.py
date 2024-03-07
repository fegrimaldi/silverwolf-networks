from st2common.runners.base_action import Action


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self._username = self.config["username"]
        self._password = self.config["password"]

        self.conn_info = {
            "device_type": "cisco_nxos",
            "host": None,
            "username": self._username,
            "password": self._password,
        }
