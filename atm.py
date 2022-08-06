import random as rdm

class atm:
    def __init__(self):
        self.id = rdm.randint(0, 10000)
        self.saldo = 0
        self.pin = ""
    
    def getId(self):
        return self.id
    
    def verifyPin(self, pin):
        if (self.pin == pin):
            return True
        else:
            return False

    def setPin(self, pin):
        self.pin = pin
    
    def changePin(self, pin, newPin):
        verifyPin = self.verifyPin(pin)
        if (self.pin == pin):
            self.pin = newPin
        return verifyPin * "Pin Changed" + (not verifyPin) * "Wrong Pin"
    
    def deposit(self, pin, saldo):
        verifyPin = self.verifyPin(pin)
        if (verifyPin):
            self.saldo += saldo
        return verifyPin * f"Rp {saldo} has been deposited" + (not verifyPin) * "Wrong Pin"
    
    def checkBal(self, pin):
        verifyPin = self.verifyPin(pin)
        return verifyPin * f"Current Balance: {self.saldo}" + (not verifyPin) * "Wrong Pin"

    def withdraw(self, pin, sum):
        verifyPin = self.verifyPin(pin)
        if (verifyPin):
            self.saldo -= sum
        return verifyPin * f"Current Balance: {self.saldo}" + (not verifyPin) * "Wrong Pin"

test = atm()
test.setPin("12345")
print(test.changePin("12345", "1235"))
print(test.deposit("1235", 10000))
print(test.checkBal("1235"))