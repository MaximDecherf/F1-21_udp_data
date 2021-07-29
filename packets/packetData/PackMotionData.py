from .classes.CarMotionData import CarMotionData

class PacketMotionData():

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
    
    
    def __call__(self, body_data):
        return PacketMotionData(body_data)

    def __len__(self):
        return self.data_lenhgt

    def __str__(self):
        return  str({'all_car_motion_data' : self.all_car_motion_data})
    
    def __repr__(self):
        return  {'all_car_motion_data' : self.all_car_motion_data}