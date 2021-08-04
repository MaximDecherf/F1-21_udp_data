import struct

class SpeedTrap:

    def __init__(self, data):
        self.vehicle_index = int.from_bytes(data[0:1], byteorder='little')
        self.speed = struct.unpack('<f', data[1:5])
        self.overall_fastest_in_session = int.from_bytes(data[5:6], byteorder='little')
        self.driver_fastest_in_session = int.from_bytes(data[6:7], byteorder='little')

        
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)