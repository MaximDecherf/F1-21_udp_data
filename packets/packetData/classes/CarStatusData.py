import struct

class CarStatusData:

    BYTES_SPLITS = {'traction_control' : [True, int, 1], 'anti_lock_brakes' : [True, int, 2], 'fuel_mix' : [True, int, 3], 'front_brake_bias' : [True, int, 4], 'pit_limitier_status' : [True, int, 5], 'fuel_in_tank' : [True, float, 9], 'fuel_capacity' : [True, float, 13], 'fuel_remaining_laps' : [True, float, 17], 'max_RPM' : [True, int, 19], 'idle_RPM' : [True, int, 21], 'max_gears' : [True, int, 22], 'drs_allowed' : [True, int, 23], 'drs_activation_distance' : [True, int, 25], 'actual_tyre_compound' : [True, int, 26], 'visual_tyre_compound' : [True, int, 27], 'tyres_age_laps': [True, int, 28], 'vehicle_fia_flags': [True, int, 29], 'ers_store_energy' : [True, float, 33], 'ers_deploy_mode' : [True, int, 34], 'ers_harvested_this_lap_MGUK' : [True, float, 38], 'ers_harvested_this_lap_MGUH' : [True, float, 42], 'ers_deployed_this_lap' : [True, float, 46], 'network_paused' : [True, int, 47]}

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
        return str(self.__class__) + " : " + str(full_dict)