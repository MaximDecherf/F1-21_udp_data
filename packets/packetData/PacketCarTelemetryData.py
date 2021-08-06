import struct
from .classes.CarTelemetryData import CarTelemetryData

class PacketCarTelemetryData:

    BYTES_SPLITS = {'car_telemetry_data' : [False, 60, CarTelemetryData ,1320], 'mfd_panel_index' : [True, int, 1321], 'mfd_panel_index_secondary_player' : [True, int, 1322], 'suggested_gear' : [True, int, 1323]}

    NUMBER_DECODER = {'mfd_panel_index' : ['car setup', 'pits', 'damage', 'engine', 'temperatures']}

    def __init__(self, body_data, decode_numbers=True):
        self.body_data = body_data
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                    setattr(self, key, int.from_bytes(body_data[end_prev:value[2]], byteorder='little'))
                    end_prev = value[2]
                elif value[1] == float:
                    setattr(self, key, struct.unpack('<f', body_data[end_prev:value[2]]))
                    end_prev = value[2]
            else:
                data_list = []
                while value[3] > end_prev:
                    data_list.append(value[2](body_data[end_prev:end_prev+value[1]]))
                    end_prev = end_prev+value[1]
                setattr(self, key, data_list)
                end_prev = value[3]
        self.data_lenhgt = len(body_data)
        if decode_numbers:
            self.decode_numbers() 
    
    
    def decode_numbers(self):
        for key, decoder in self.NUMBER_DECODER.items():
            int_value = getattr(self, key)
            if int_value < 0:
                setattr(self, key, 'invalid')
            else:
                setattr(self, key, decoder[int_value])
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        del full_dict['body_data']
        return str(self.__class__) + " : " + str(full_dict)