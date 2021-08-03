import struct

class MarshalZone:



    def __init__(self, data):
     
        self.zone_flag = int.from_bytes(data[4], byteorder='little')
        self.zone_start = struct.unpack('<f', data[0:4])
        
        
        #zone_flag : -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        # source :  https://forums.codemasters.com/topic/80231-f1-2021-udp-specification/

    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)