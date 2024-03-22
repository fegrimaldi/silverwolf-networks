from lib import action
from lib.webmethod import WebMethod


class GetGluDeviceId(action.BaseAction):
    def run(self, **parameters):
        self.web_method = WebMethod(verify=False)
        response_raw = self.web_method.call(
            method="GET",
            url=f"{self.glu_base_url}/api/devices",
            params={
                "orgId": "b131860f-ed86-4a87-a896-3a140e2c4ea9",
                "name": parameters["device_name"],
            },
            headers=None,
            payload=None,
            auth=self.glu_auth,
        )
        if response_raw is not None:
            response = response_raw.json()
            return response[0]["id"]
        else:
            return {"status": "unhandled exception"}
