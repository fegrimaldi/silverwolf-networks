"""Provides a class to interact with network devices and retrieve their NTP, BGP, and OSPF states.

This module includes a class `Device` with methods to connect to network devices and retrieve their 
NTP synchronization state, BGP neighbor states, and OSPF neighbor count and IDs.

Example:
    conn_info = {
        "device_type": "cisco_nxos",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "password",
    }
    device = Device(conn_info)
    ntp_status = device.ntp_state()
    bgp_status = device.bgp_state()
    ospf_status = device.ospf_state()

Attributes:
    conn_info (dict): A dictionary containing connection information for the network device, 
    including keys 'device_type', 'host', 'username', and 'password'.

Methods:
    ntp_state(): Retrieves the NTP synchronization state of the device.
    bgp_state(): Retrieves the BGP neighbor states of the device.
    ospf_state(): Retrieves the OSPF neighbor count and IDs of the device.

"""

from netmiko import ConnectHandler
import re

class Device:

    def __init__(self, conn_info):
        """Initializes a Device object with connection information."""
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
        """Retrieves the NTP synchronization state of the device."""
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
        """Retrieves the BGP neighbor states of the device."""
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
        """Retrieves the OSPF neighbor count and IDs of the device."""
        results = self.session.send_command("show ip ospf neighbors")
        pattern = r"Total number of neighbors: (?P<neighbor_count>\d)"
        status = {"device": self.host, "ok": None}
        match = re.search(pattern, results)
        if match:
            neighbor_count = int(match.group("neighbor_count"))
            if neighbor_count == 2:
                status["ok"] = True
            else:
                status["ok"] = False
            status["neighbor_count"] = neighbor_count

        pattern_neighbor = r"^\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        neighbor_ids = []
        for line in results.splitlines():
            match = re.search(pattern_neighbor, line)
            if match:
                neighbor_ids.append(match.group(1))

        status["neighbors"] = neighbor_ids
        return status
