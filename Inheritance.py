# base class,parent class, common attribute + funtionality class
# derived class, child class, uncommon attribute + funtionality class
class Gadget:
    def __init__(self,brand,prize,color,origin) -> None:
        self.brand=brand
        self.prize=prize
        self.color=color
        self.origin=origin

    def run(self):
        return f'Running device :{self.brand}'
    

class laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory
        self.ssd=ssd

    def coding(self):
        return f'learning python and practising'
    
class Phone:
    def __init__(self,dual_sim) -> None:
        self.dual_sim=dual_sim

    def phone_call(self, number, text):
        return f'sending sms to: {number} with: {text},'
    
class camera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel

    def change_len(self):
        pass