from lib import action
from lib.device import Device
import json


class GetBgpState(action.BaseAction):
    def run(self, **parameters):
        self.conn_info["host"] = parameters["host"]
        self.device = Device(conn_info=self.conn_info)
        output = self.device.get_bgp_state()
        self.device.session.disconnect()
        return output
