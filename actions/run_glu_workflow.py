from lib import action
from lib.webmethod import WebMethod

workflow_id = "af06b8d9-4110-4f45-8149-a53950764913"  #! NTP WF


class RunGluWorklflow(action.BaseAction):
    def run(self, **parameters):
        self.web_method = WebMethod(verify=False)
        response_raw = self.web_method.call(
            "POST",
            f"{self.glu_base_url}/api/workflows/{workflow_id}/run",
            json={
                "orgId": self.org_id,
                "deviceIds": [parameters["device_id"]],
                "inputParameters": {},
            },
            headers=None,
            auth=self.glu_auth,
        )
        if response_raw is not None:
            return response_raw.status_code
        else:
            return {"status": "unhandled exception"}
