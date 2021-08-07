
class TyreStintHistoryData:

    def __init__(self, data):
        self.end_lap = int.from_bytes(data[0:1], byteorder='little')
        self.tyre_actual_compound = int.from_bytes(data[1:2], byteorder='little')
        self.tyre_visual_compound = int.from_bytes(data[2:3], byteorder='little')

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)