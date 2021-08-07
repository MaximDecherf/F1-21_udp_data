
class StopGoPenaltyServed:

    def __init__(self, data):
        self.vehicle_index = int.from_bytes(data[0:1], byteorder='little')
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)