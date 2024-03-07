"""_summary_
"""

from netmiko import ConnectHandler
import re


class Device:

    def __init__(self, conn_info):
        self.device_type = conn_info["device_type"]
        self.host = conn_info["host"]
        self.username = conn_info["username"]
        self.password = conn_info["password"]
        self.session = ConnectHandler(
            device_type=self.device_type,
            host=self.host,
            username=self.username,
            password=self.password,
        )

    def get_ntp_state(self):

        results = self.session.send_command("show ntp peer-status")
        pattern = "([\*]192\.168\.10\.1[01])"

        x = re.search(pattern, results)

        status = {"device": self.host, "status": None}
        if x:
            status["status"] = "OK"
            status["ntp_peer"] = x.group(0)
        else:
            status["status"] = "NOT_OK"
        return status
