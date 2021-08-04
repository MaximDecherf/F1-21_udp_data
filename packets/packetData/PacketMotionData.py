from .classes.CarMotionData import CarMotionData
import struct

class PacketMotionData():
    BYTES_SPLITS_FLOAT_ARRAYS = {'suspension_position' : 1336, 'suspension_velocity' : 1352, 'suspension_acceleration' : 1368, 'wheel_speed' : 1384, 'wheel_slip': 1400}

    BYTES_SPLITS_FLOAT = {'local_velocity_x' : 1404, 'local_velocity_y' : 1408, 'local_velocity_z' : 1412, 'angular_velocity_x' : 1416, 'angular_velocity_y' : 1420, 'angular_velocity_z' : 1424, 'angular_acceleration_x' : 1428, 'angular_acceleration_y' : 1432, 'angular_acceleration_z' : 1436, 'front_wheels_angle' : 1440}

    #TODO refractor code

    def __init__(self, body_data):
        if body_data != None:
            self.body_data = body_data
            all_car_motion_data = []
            for i in range(22): #first 1320 bytes are for the carmotion of all (22)players, the carmotionData is 60 bytes long
                start_point = i*60 + 1
                car = CarMotionData(body_data[start_point:start_point+60])
                all_car_motion_data.append(car)

            self.all_car_motion_data = all_car_motion_data
            self.data_lenhgt = len(body_data)


            #extra player car only data
            wheel_data = []
            start_point = 1320
            for key, value in self.BYTES_SPLITS_FLOAT_ARRAYS.items(): 
                #makes an array for each wheel of the car in the order of RL, RR, FL, FR, each wheel is 4 bytes
                wheel_data = [struct.unpack('<f',body_data[i+start_point : i+start_point+4]) for i in range(0, 16, 4)]
                setattr(self, key, wheel_data)
                start_point = start_point + 16 
            
            end_prev = 1400 
            # non array values of car
            for key, value in self.BYTES_SPLITS_FLOAT.items():
                setattr(self, key, struct.unpack('<f', body_data[end_prev:value]))
                end_prev = value
                


    def __len__(self):
        return self.data_lenhgt

    def __str__(self):
        return  str({'all_car_motion_data' : self.all_car_motion_data, 'suspension_position' : self.suspension_position, 'suspension_velocity' : self.suspension_velocity, 'suspension_acceleration' : self.suspension_acceleration, 'wheel_speed' : self.wheel_speed, 'wheel_slip': self.wheel_slip, 'local_velocity_x' : self.local_velocity_x, 'local_velocity_y' : self.local_velocity_y, 'local_velocity_z' : self.local_velocity_z, 'angular_velocity_x' : self.angular_velocity_x, 'angular_velocity_y' : self.angular_velocity_y, 'angular_velocity_z' : self.angular_velocity_z, 'angular_acceleration_x' : self.angular_acceleration_x, 'angular_acceleration_y' : self.angular_acceleration_y, 'angular_acceleration_z' : self.angular_acceleration_z, 'front_wheels_angle' : self.front_wheels_angle})
    
    def __repr__(self):
        return  {'all_car_motion_data' : self.all_car_motion_data, 'suspension_position' : self.suspension_position, 'suspension_velocity' : self.suspension_velocity, 'suspension_acceleration' : self.suspension_acceleration, 'wheel_speed' : self.wheel_speed, 'wheel_slip': self.wheel_slip, 'local_velocity_x' : self.local_velocity_x, 'local_velocity_y' : self.local_velocity_y, 'local_velocity_z' : self.local_velocity_z, 'angular_velocity_x' : self.angular_velocity_x, 'angular_velocity_y' : self.angular_velocity_y, 'angular_velocity_z' : self.angular_velocity_z, 'angular_acceleration_x' : self.angular_acceleration_x, 'angular_acceleration_y' : self.angular_acceleration_y, 'angular_acceleration_z' : self.angular_acceleration_z, 'front_wheels_angle' : self.front_wheels_angle}