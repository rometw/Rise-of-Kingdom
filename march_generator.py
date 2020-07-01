

class March:
    def __init__(self,troop,primary,*secondary):
        self.primary = primary
        if secondary:
            self.secondary = secondary
        else:
            print('Primary only')
            self.secondary = []
        self.troop = troop
       
        

    def __delete__(self,march):
        del march
        

    
    
    

