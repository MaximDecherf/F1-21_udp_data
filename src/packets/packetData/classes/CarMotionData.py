import struct

class CarMotionData():
    #TODO : normaliszed data 

    BYTES_SPLITS = {'world_position_x' : [True, float ,4], 'world_position_y' : [True, float, 8], 'world_position_z' : [True, float, 12], 'world_velocity_x' : [True, float, 16] , 'world_velocity_y' : [True, float, 20], 'world_velocity_z' : [True, float, 24], 
    'world_forward_dir_x' : [True, int, 26], 'world_forward_dir_y' : [True, int, 28], 'world_forward_dir_z' : [True, int, 30], 'world_right_dir_x' : [True, int, 32] , 'world_right_dir_y' : [True, int, 34], 'world_right_dir_z' : [True, int, 36], 'g_force_lateral' : [True, float, 40], 'g_force_longitudinal' : [True, float, 44], 'g_force_vertical' : [True, float, 48], 'yaw' : [True, float, 52], 'pitch' : [True, float, 56], 'roll' : [True, float, 60]}

    SIZE = 60

    def __init__(self, data):
        if len(data) == self.SIZE:
            end_prev = 0
            for key, value in self.BYTES_SPLITS.items():
                if value[0]:
                    if value[1] == int:
                            setattr(self, key, int.from_bytes(data[end_prev:value[2]], byteorder='little'))
                            end_prev = value[2]
                    elif value[1] == float:
                            setattr(self, key, struct.unpack('<f', data[end_prev:value[2]]))
                            end_prev = value[2]

                self.data_lenhgt = len(data)

        else:
            raise ValueError('Data must be size of {0} bytes'.format(self.SIZE)) 

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)

