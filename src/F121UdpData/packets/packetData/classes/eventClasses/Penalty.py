
class Penalty:

    def __init__(self, data):
        self.penalty_type = int.from_bytes(data[0:1], byteorder='little')
        self.infringement_type = int.from_bytes(data[1:2], byteorder='little')
        self.vehicle_index = int.from_bytes(data[2:3], byteorder='little')
        self.other_vehicle_index = int.from_bytes(data[3:4], byteorder='little')
        self.time = int.from_bytes(data[4:5], byteorder='little')
        self.lap_num = int.from_bytes(data[5:6], byteorder='little')
        self.places_gained = int.from_bytes(data[6:7], byteorder='little')

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)