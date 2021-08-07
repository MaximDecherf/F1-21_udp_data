
class LapHistoryData:

    def __init__(self, data):
        self.lap_time_in_ms = int.from_bytes(data[0:4], byteorder='little')
        self.sector1_time_in_ms = int.from_bytes(data[4:6], byteorder='little')
        self.sector2_time_in_ms = int.from_bytes(data[6:8], byteorder='little')
        self.sector3_time_in_ms = int.from_bytes(data[8:10], byteorder='little')
        self.lap_valid_bit_flags = int.from_bytes(data[10:11], byteorder='little')
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)