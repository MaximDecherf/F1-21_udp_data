import struct

class MarshalZone:



    def __init__(self, data):
        self.zone_start = struct.unpack('<f', data[0:4])
        self.zone_flag = int.from_bytes(data[5], byteorder='little')
        
        #zone_flag : -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        # source :  https://forums.codemasters.com/topic/80231-f1-2021-udp-specification/

    def __str__(self):
        return str({"zone_start" : self.zone_start, "zone_flag" : self.zone_flag})

    def __repr__(self):
        return {"zone_start" : self.zone_start, "zone_flag" : self.zone_flag}