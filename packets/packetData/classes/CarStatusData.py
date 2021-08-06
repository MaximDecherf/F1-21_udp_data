import struct

class CarStatusData:

    BYTES_SPLITS = {'traction_control' : [True, int, 1], 'anti_lock_brakes' : [True, int, 2], 'fuel_mix' : [True, int, 3], 'front_brake_bias' : [True, int, 4], 'pit_limitier_status' : [True, int, 5], 'fuel_in_tank' : [True, float, 9], 'fuel_capacity' : [True, float, 13], 'fuel_remaining_laps' : [True, float, 17], 'max_RPM' : [True, int, 19], 'idle_RPM' : [True, int, 21], 'max_gears' : [True, int, 22], 'drs_allowed' : [True, int, 23], 'drs_activation_distance' : [True, int, 25], 'actual_tyre_compound' : [True, int, 26], 'visual_tyre_compound' : [True, int, 27], 'tyres_age_laps': [True, int, 28], 'vehicle_fia_flags': [True, int, 29], 'ers_store_energy' : [True, float, 33], 'ers_deploy_mode' : [True, int, 34], 'ers_harvested_this_lap_MGUK' : [True, float, 38], 'ers_harvested_this_lap_MGUH' : [True, float, 42], 'ers_deployed_this_lap' : [True, float, 46], 'network_paused' : [True, int, 47]}

    NUMBER_DECODER = {'anti_lock_brakes' : ['off', 'on'], 'fuel_mix' : ['lean', 'standard', 'rich', 'max'], 'pit_limitier_status' : ['off', 'on'], 'drs_allowed' : ['not allowed', 'allowed'], 'drs_activation_distance' : ['DRS not available'], 'actual_tyre_compound' : {16 : 'F1 Modern C5', 17 : 'F1 Modern C4', 18 : 'F1 Modern C3', 19 : 'F1 Modern C2', 20 : 'F1 Modern C1', 7 : 'F1 Modern inter', 8 : 'F1 Modern wet', 9 : 'F1 classic dry', 10 : 'F1 classic wet', 11 : 'F2 super soft', 12 : 'F2 soft', 13 : 'F2 medium', 14 : 'F2 hard', 15 : 'F2 wet' }, 'visual_tyre_compound' : {16 : 'F1 Visual soft', 17 : 'F1 Visual medium', 18 : 'F1 Visual hard', 7 : 'F1 Visual inter', 8 : 'F1 Visual wet', 9 : 'F1 classic dry', 10 : 'F1 classic wet', 15 : 'F2 19 wet', 19 : 'F2 19 super soft', 20 : 'F2 19 soft', 21 : 'F2 19 medium', 22 : 'F2 19 hard'}, 'vehicle_fia_flags' : ['none', 'green', 'blue', 'yellow', 'red'], 'ers_deploy_mode' : ['none', 'medium', 'hotlap', 'overtake']} 

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
            elif key == 'drs_activation_distance' and int_value != 0:
                setattr(self, key, f'DRS in {int_value} meters')
            else:
                setattr(self, key, decoder[int_value])
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)