from lib import action
from lib.device import Device
import sys


class GetNtpState(action.BaseAction):
    def run(self):
        self._host = sys.argv[1]
        self.conn_info["host"] = self._host

        self.device = Device(conn_info=self.conn_info)

        output = str(self.device.get_ntp_state())

        self.device.session.disconnect()

        return output
