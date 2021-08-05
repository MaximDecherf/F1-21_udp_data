import struct

class CarDamageData:

    BYTES_SPLITS = {'tyres_wear' : [False, 4, float, 16], 'tyres_damage' : [False, 1, int, 20], 'brakes_damage' : [False, 1, int, 24], 'front_left_wing_damage' : [True, int, 25], 'front_right_wing_damage' : [True, int, 26], 'rear_wing_damage' : [True, int, 27], 'floor_damage' : [True, int, 28], 'diffuser_damage' : [True, int, 29], 'sidepod_damage' : [True, int, 30], 'drs_fault' : [True, int, 31], 'gearbox_damage' : [True, int, 32], 'engine_damage' : [True, int, 33], 'engine_MGUH_wear' : [True, int, 34],  'engine_ES_wear' : [True, int, 35], 'engine_CE_wear' : [True, int, 36], 'engine_ICE_wear' : [True, int, 37], 'engine_MGUK_wear' : [True, int , 38], 'engine_TC_wear' : [True, int, 39]} 

    def __init__(self, data):
        end_prev = 0
        for key, value in self.BYTES_SPLITS.items():
            if value[0]:
                if value[1] == int:
                    setattr(self, key, int.from_bytes(data[end_prev:value[2]], byteorder='little'))
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