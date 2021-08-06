import struct

class FinalClassificationData:

    BYTES_SPLITS = {'position' : [True, int, 1], 'num_laps' : [True, int, 2], 'grid_position' : [True, int, 3], 'points' : [True, int, 4], 'num_pit_stops' : [True, int, 5], 'result_status' : [True, int, 6], 'best_lap_time_in_MS' : [True, int, 10], 'total_race_time' : [True, 'double', 18], 'penalties_time' : [True, int, 19], 'num_penalties' : [True, int, 20],  'num_tyre_stints' : [True, int, 21], 'tyre_stints_actual' : [False, 1, int, 29], 'tyre_stints_visual' : [False, 1, int, 37]}

    NUMBER_DECODER = {'result_status' : ['invalid', 'inactive', 'active', 'finished', 'dnf', 'disqualified', 'not classified', 'retired']}

    def __init__(self, data, decode_numbers=True):
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                    setattr(self, key, int.from_bytes(data[end_prev:value[2]], byteorder='little'))
                    end_prev = value[2]
                elif value[1] == float:
                    setattr(self, key, struct.unpack('<f', data[end_prev:value[2]]))
                    end_prev = value[2]
                elif value[1] == 'double':
                    setattr(self, key, struct.unpack('<d', data[end_prev:value[2]]))
                    end_prev = value[2]
            else:
                data_list = []
                while value[3] > end_prev:
                    if value[2] == int:
                        data_list.append(int.from_bytes(data[end_prev:end_prev+value[1]], byteorder='little'))
                    end_prev = end_prev+value[1]
                setattr(self, key, data_list)
                end_prev = value[3]
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
        return str(self.__class__) + " : " + str(full_dict)