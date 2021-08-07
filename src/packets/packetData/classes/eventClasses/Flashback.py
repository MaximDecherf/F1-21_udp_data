import struct

class Flashback:

    def __init__(self, data):
        self.flashback_frame_identifer =  int.from_bytes(data[0:4], byteorder='little')
        self.flashback_session_time = struct.unpack('<f', data[4:8])

            
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)
    