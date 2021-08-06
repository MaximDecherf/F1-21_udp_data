from .classes.CarMotionData import CarMotionData
import struct

class PacketMotionData():
    #x_p_... extra player car only data

    BYTES_SPLITS = {'car_motion_data' : [False, 60, CarMotionData, 1320], 'x_p_suspension_position' : [False, 4, float, 1336], 'x_p_suspension_velocity' : [False, 4, float, 1352], 'x_p_suspension_acceleration' : [False, 4, float, 1368], 'x_p_wheel_speed' : [False, 4, float, 1384], 'x_p_wheel_slip': [False, 4, float, 1400], 'x_p_local_velocity_x' : [True, float, 1404], 'x_p_local_velocity_y' : [True, float, 1408], 'x_p_local_velocity_z' : [True, float, 1412], 'x_p_angular_velocity_x' : [True, float, 1416], 'x_p_angular_velocity_y' : [True, float, 1420], 'x_p_angular_velocity_z' : [True, float, 1424], 'x_p_angular_acceleration_x' : [True, float, 1428], 'x_p_angular_acceleration_y' : [True, float, 1432], 'x_p_angular_acceleration_z' : [True, float, 1436], 'x_p_front_wheels_angle' : [True, float, 1440]}

    def __init__(self, body_data):
        self.body_data = body_data
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                    setattr(self, key, int.from_bytes(body_data[end_prev:value[2]], byteorder='little'))
                    end_prev = value[2]
            else:
                data_list = []
                while value[3] > end_prev:
                    if value[2] == float:
                        data_list.append(struct.unpack('<f',body_data[end_prev:end_prev+value[1]]))
                    else:
                        data_list.append(value[2](body_data[end_prev:end_prev+value[1]]))
                    end_prev = end_prev+value[1]
                setattr(self, key, data_list)
                end_prev = value[3]
        self.data_lenhgt = len(body_data)


    def __len__(self):
        return self.data_lenhgt

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        del full_dict['body_data']
        return str(self.__class__) + " : " + str(full_dict)