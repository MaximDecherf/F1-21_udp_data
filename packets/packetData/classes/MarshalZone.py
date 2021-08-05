import struct

class MarshalZone:

    NUMBER_DECODER = {'zone_flag' : ['none', 'green', 'blue', 'yellow', 'red']}

    def __init__(self, data, decode_numbers=True):
     
        self.zone_flag = int.from_bytes(data[4:5], byteorder='little')
        self.zone_start = struct.unpack('<f', data[0:4])

        if decode_numbers:
            self.decode_numbers()            

    def decode_numbers(self):
        for key, decoder in self.NUMBER_DECODER.items():
            int_value = getattr(self, key)
            if int_value < 0:
                setattr(self, key, 'invalid')
            else:
                setattr(self, key, decoder[int_value])
        
        
        #zone_flag : -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        # source :  https://forums.codemasters.com/topic/80231-f1-2021-udp-specification/

    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)