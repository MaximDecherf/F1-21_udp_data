class CarMotionData():
    BYTES_SPLITS_INT = {'world_forward_dir_x' : 26, 'world_forward_dir_y' : 28, 'world_forward_dir_z' : 30, 'world_right_dir_x' : 32 , 'world_right_dir_y' : 34, 'world_right_dir_z' : 36}
    #normaliszed

    BYTES_SPLITS_FLOAT = {'world_position_x' : 4, 'world_position_y' : 8, 'world_position_z' : 12, 'world_velocity_x' : 16 , 'world_velocity_y' : 20, 'world_velocity_z' : 24, 'g_force_lateral' : 40, 'g_force_longitudinal' : 44, 'g_force_vertical' : 48, 'yaw' : 52, 'pitch' : 56, 'roll' : 60}

    SIZE = 60

    def __init__(self, data):
        end_prev = 24 # int values start from byte 24 until byte 36
        if len(data) == self.SIZE:
            for key, value in self.BYTES_SPLITS_INT.items():
                setattr(self, key, int.from_bytes(data[end_prev:value], byteorder='little'))
                end_prev = value

        
            end_prev = 0 # float values start from byte 0 until byte 24 and from byte 36 until byte 60
            for key, value in self.BYTES_SPLITS_FLOAT.items():
                setattr(self, key, float.from_bytes(data[end_prev:value], byteorder='little'))
                end_prev = value

            self.data_lenhgt = len(data)

        else:
            raise ValueError('Data must be size of {0} bytes'.format(self.SIZE)) 
