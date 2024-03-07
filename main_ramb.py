from entities.vending_machine_model import VendingMachineModel


vending_machine = VendingMachineModel()

#default values to initialize
presentStatus = 'without_coin'
presentAction = vending_machine.rules[presentStatus]
vending_machine.printValues(presentStatus,presentAction,vending_machine.actions[presentAction])

while(True):
    print("Ingrese la percepcion. e.g:" + str(vending_machine.perception))
    perception = input()
    presentStatus = vending_machine.updateStatus(presentStatus,presentAction,perception)
    presentAction = vending_machine.rules[presentStatus]
    textToPrint = vending_machine.actions[presentAction]
    vending_machine.printValues(presentStatus,presentAction,textToPrint)
