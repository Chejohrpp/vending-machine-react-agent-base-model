class VendingMachineModel:

    def __init__(self):
        self.status = {"without_coin","get_coin","served_c1","served_c2","served_c3"}
        self.perception = { 'moneda', 'c1', 'c2', 'c3', 'servido' }
        self.rules = {
            "without_coin":"ask_for_coin",
            "get_coin":"ask_for_code",
            "served_c1":"serve_c1_wait",
            "served_c2":"serve_c2_wait",
            "served_c3":"serve_c3_wait"
        }
        self.model = [
            ('without_coin', 'ask_for_coin', 'moneda', 'get_coin'),
            ('get_coin', 'ask_for_code', 'c1', 'served_c1'),
            ('get_coin', 'ask_for_code', 'c2', 'served_c2'),
            ('get_coin', 'ask_for_code', 'c3', 'served_c3'),
            ('served_c1', 'serve_c1_wait', 'servido', 'without_coin'),
            ('served_c2', 'serve_c2_wait', 'servido', 'without_coin'),
            ('served_c3', 'serve_c3_wait', 'servido', 'without_coin'),
            ('get_coin', 'ask_for_code', 'moneda', 'get_coin'),
            ('get_coin', 'ask_for_code', 'servido', 'get_coin'),
            ('served_c1', 'serve_c1_wait', 'moneda', 'get_coin'),
            ('served_c2', 'serve_c2_wait', 'moneda', 'get_coin'),
            ('served_c3', 'serve_c3_wait', 'moneda', 'get_coin'),
        ]
        self.actions = {"ask_for_coin": "Ingrese moneda",
        	"ask_for_code": "Ingrese codigo",
        	"serve_c1_wait": "Sirviendo refresco 1 y espera...",
        	"serve_c2_wait": "Sirviendo refresco 2 y espera...",
        	"serve_c3_wait": "Sirviendo refresco 3 y espera..."
        }
    
    def updateStatus(self, presentStatus, presentAction, perception):
        newStatus = self.existInModel(presentStatus, presentAction, perception)
        return 'without_coin' if newStatus is None else newStatus

        
    def existInModel(self, presentStatus, presentAction, perception):
        patern = (presentStatus, presentAction, perception)
        matching_transition = next((transition[3] for transition in self.model if transition[:3] == patern), None)
        return matching_transition

    
    def printValues(self,presentStatus, presentAction,textToPrint):
        print("\nCurrently Status: " + presentStatus)
        print("Currently Action: " + presentAction + "\n")
        print(textToPrint)
    