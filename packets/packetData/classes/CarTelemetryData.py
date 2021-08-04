import struct

class CarTelemetryData:

    BYTES_SPLITS = {'speed' : [True, int, 2], 'throttle' : [True, float, 6], 'steer' : [True, float, 10], 'brake' : [True, float, 14], 'clutch' : [True, int, 15], 'gear' : [True, int, 16], 'engine_RPM': [True, int, 18], 'drs' : [True, int, 19], 'rev_lights_percent' : [True, int, 20], 'rev_lights_bit_value' : [True, int, 22], 'brakes_temperature' : [False, 2, int, 30], 'tyres_surface_temperature' : [False, 1, int, 34], 'tyres_inner_temperature' : [False, 1, int, 38], 'engine_temperature' : [True, int, 40], 'tyres_pressure': [False, 4, float, 56], 'surface_type' : [False, 1 , int, 60]}

    def __init__(self, data):
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                    setattr(self, key, int.from_bytes(data[end_prev:value[2]], byteorder='little'))
                    end_prev = value[2]
                elif value[1] == float:
                    setattr(self, key, struct.unpack('<f', data[end_prev:value[2]]))
                    end_prev = value[2]
            else:
                data_list = []
                while value[3] > end_prev:
                    if value[2] == int:
                        data_list.append(int.from_bytes(data[end_prev:end_prev+value[1]], byteorder='little'))
                    elif value[2] == float:
                        data_list.append(struct.unpack('<f',data[end_prev:end_prev+value[1]]))
                    end_prev = end_prev+value[1]
                setattr(self, key, data_list)
                end_prev = value[3]
        
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)