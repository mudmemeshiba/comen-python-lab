class Switch:
    def __init__(self, name, status=False):
        self.name = name
        self.status = status

    def turn(self):
        if self.status == True:
            self.status = False
        else:
            self.status = True

    def clone(self):
        self.cloned = self.name + '.copy'
        self.clonedStatus = self.status
        return Switch(self.cloned, self.clonedStatus)

    def __str__(self):
        if self.status:
            return f"switch({self.name}) is on"
        else:
            return f"switch({self.name}) is off"
        
class Light(Switch):
    def __init__(self, name, switch):
        self.name = name
        self.switch = switch #Switch()

    def turn(self):
        self.switch.turn()

    def get_status(self):
        return self.switch.status
    
    def set_switch(self, new_switch):
        self.switch = new_switch 

    def clone(self):
        self.cloned = self.name + '.copy'
        self.clonedStatus = self.switch.clone()
        return Light(self.cloned, self.clonedStatus)

    def __str__(self):
        if self.name:
            return f"light({self.name}) with {self.switch}"
        else:
            return f"light({self.name}) with {self.switch}"
        
s1 = Switch("addy", True)
l1 = Light("abby", s1)
print(l1)