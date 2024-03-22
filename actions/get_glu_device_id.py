from lib import action
from lib.webmethod import WebMethod


class GetGluDeviceId(action.BaseAction):
    def run(self, **parameters):
        self.web_method = WebMethod()
        response_raw = self.web_method.call(
            "GET",
            f"{self.glu_base_url}/api/devices",
            {
                "orgId": "b131860f-ed86-4a87-a896-3a140e2c4ea9",
                "name": parameters["device_name"],
            },
            headers=None,
            auth=self.auth,
        )
        response = response_raw.json()
        return response[0]["id"]
