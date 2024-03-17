from lib import action
from lib.device import Device



class GetOspfState(action.BaseAction):
    def run(self, **parameters):
        self.conn_info["host"] = parameters["host"]
        self.device = Device(conn_info=self.conn_info)
        output = self.device.ospf_state()
        self.device.session.disconnect()
        return output
