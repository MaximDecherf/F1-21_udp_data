import struct

class CarSetupData:

    BYTES_SPLITS = {'front_wing' : [True, int, 1], 'rear_wing' : [True, int, 2], 'on_throttle' : [True, int, 3], 'off_throttle' : [True, int, 4], 'front_camber' : [True, float, 8], 'rear_camber' : [True, float, 12], 'front_toe' : [True, float, 16], 'rear_toe' : [True, float, 20], 'front_suspension' : [True, int, 21], 'rear_suspension' : [True, int, 22], 'front_anti_roll_bar' : [True, int, 23], 'rear_anti_roll_bar' : [True, int, 24], 'front_suspension_height' : [True, int, 25],  'rear_suspension_height' : [True, int, 26],  'break_pressure' : [True, int, 27],  'brake_bias' : [True, int, 28], 'rear_left_tyre_pressure' : [True, float, 32], 'rear_right_tyre_pressure' : [True, float, 36], 'front_left_tyre_pressure' : [True, float, 40], 'front_right_tyre_pressure' : [True, float, 44], 'ballast' : [True, int, 45], 'fuelload' : [True, float, 49]}

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
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        del full_dict['body_data']
        return str(self.__class__) + " : " + str(full_dict)