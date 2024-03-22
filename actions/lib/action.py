from st2common.runners.base_action import Action


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self._username = self.config["username"]
        self._password = self.config["password"]
        self.glu_auth = (self.config["glu_username"], self.config["glu_password"])
        self.glu_base_url = self.config["glu_base_url"]
        self.org_id = self.config["glu_org_id"]

        self.conn_info = {
            "device_type": "cisco_nxos",
            "host": None,
            "username": self._username,
            "password": self._password,
        }
