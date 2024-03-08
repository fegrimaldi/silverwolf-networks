"""_summary_
"""

from netmiko import ConnectHandler
import re
import json


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
        status = {"device": self.host, "OK": None}
        if x:
            status["OK"] = True
            status["ntp_peer"] = x.group(0)
        else:
            status["OK"] = False
        return json.dumps(status)

    def get_bgp_state(self):

        results = self.session.send_command("show ip bgp neighbors | in BGP")
        pattern = "BGP neighbor is\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*BGP state\s*=\s*(\w+)"
        paragraphs = results.split("BGP neighbor")[1:]
        paragraphs = ["BGP neighbor " + p.strip() for p in paragraphs]
        bgp_state = []
        status = True
        for i in paragraphs:
            y = re.findall(pattern, i, flags=re.DOTALL)
            if y[0][1] != "Established":
                status = False
            bgp_state.append({"neighbor": y[0][0], "state": y[0][1]})
        status = {"device": "192.168.10.101", "OK": status, "state": bgp_state}
        return json.dumps(status)
