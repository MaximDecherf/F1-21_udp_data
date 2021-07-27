from .packetBody import PacketBody
from .classes.CarMotionData import CarMotionData

class PacketMotionData(PacketBody):

    def __init__(self, body_data, packet_id):
        super().__init__(body_data, packet_id)
        all_car_motion_data = []
        for i in range(22): #first 1320 bytes are for the carmotion of all (22)players, the carmotionData is 60 bytes long
            start_point = i*60 + 1
            car = CarMotionData(body_data[start_point:start_point+59])
            all_car_motion_data.append(car)

        self.all_car_motion_data = all_car_motion_data