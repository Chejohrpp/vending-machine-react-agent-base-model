class VendingMachine:

    def __init__(self):
        self.rules = {
            "coin":"ask-code",
            "c1":"serve-soda-1",
            "c2":"serve-soda-2",
            "c3":"serve-soda-3"
        }

    def makeAction(self,code):
        for key in self.rules:
            if key == code:
                print(self.rules[key])


vending_machine = VendingMachine()
print(vending_machine.rules)

while(True):
    print("Ingrese el codigo")
    code = input()
    vending_machine.makeAction(code)
