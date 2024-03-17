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

    def ntp_state(self):

        results = self.session.send_command("show ntp peer-status")
        pattern = "([\*]192\.168\.10\.1[01])"
        x = re.search(pattern, results)
        status = {"device": self.host, "ok": None}
        if x:
            status["ok"] = True
            status["ntp_peer"] = x.group(0)
        else:
            status["ok"] = False
        return status

    def bgp_state(self):

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
        status = {"device": self.host, "ok": status, "state": bgp_state}
        return status

    def ospf_state(self):
        results = self.session.send_command("show ip ospf neighbors")
        pattern = r"Total number of neighbors: (?P<neighbor_count>\d)"
        status = {"device": self.host, "ok": None}
        # Search for the pattern in the input string
        match = re.search(pattern, results)

        # Check if a match is found
        if match:
            # Extract the neighbor count from the match
            neighbor_count = int(match.group("neighbor_count"))
            if neighbor_count == 2:
                status["ok"] = True
            else:
                status["ok"] = False
            status["neighbor_count"] = neighbor_count

        # Regular expression pattern to capture neighbor IDs
        pattern_neighbor = r"^\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

        # Find all occurrences of neighbor IDs in the input string

        neighbor_ids = []
        for line in results.splitlines():
            match = re.search(pattern_neighbor, line)
            if match:
                neighbor_ids.append(match.group(1))

        status["neighbors"] = neighbor_ids
        return status
