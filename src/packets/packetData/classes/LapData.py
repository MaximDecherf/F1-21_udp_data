import struct

class LapData:

    BYTES_SPLITS = {'last_lap_time_in_MS' : [True, int, 4], 'current_lap_time_in_MS' : [True, int, 8], 'sector1_time_in-MS': [True, int, 12], 'lap_distance' : [True, float, 16], 'total_distance': [True, float, 20], 'safety_car_delta': [True, float, 24], 'car_position' : [True, int, 25], 'current_lap_num': [True, int, 26], 'pit_status': [True, int, 27], 'num_pit_stops' : [True, int, 28], 'sector' : [True, int, 29], 'current_lap_invalid' : [True, int, 30], 'penalties' : [True, int, 31], 'warnings' : [True, int, 32], 'num_unserved_drive_through_pens' : [True, int, 33], 'num_unserved_stop_go_pens' : [True, int, 34], 'grid_position': [True, int, 35], 'driver_status': [True, int, 36], 'result_status': [True, int, 37], 'pit_lane_timer_active' : [True, int, 38], 'pit_lane_time_in_MS' : [True, int , 40], 'pit_stop_timer_in_MS' : [True, int, 42], 'pit_stop_should_serve_pen' : [True, int, 43]}

    NUMBER_DECODER = {'pit_status' : ['none', 'pitting', 'in pit area'], 'sector' : ['sector1', 'sector2', 'sector3'], 'current_lap_invalid' : ['valid', 'invalid'], 'driver_status' : ['in garage', 'flying lap', 'in lap', 'out lap', 'on track'], 'result_status' : ['invalid', 'inactive', 'active', 'finished', 'dnf', 'disqualified', 'not classified', 'retired'], 'pit_lane_timer_active' : ['inactive', 'active']}


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
        return str(self.__class__) + " : " + str(self.__dict__)