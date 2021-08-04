from .classes.MarshalZone import MarshalZone
from .classes.WeatherForecastSample import WeatherForecastSample
import struct

class PacketSessionData:
    BYTES_SPLITS = {'weather' : [True, int, 1], 'track_temperature' : [True, int, 2], 'air_temperature' : [True, int, 3], 'total_laps' : [True, int, 4], 'track_length' : [True, int, 6], 'session_type' : [True, int, 7], 'track_id' : [True, int, 8], 'formula_type' : [True, int, 9], 'session_time_left' : [True, int, 11], 'session_duration' : [True, int, 13], 'pit_speed_limit' : [True, int, 14], 'game_paused' : [True, int, 15], 'is_spectating' : [True, int, 16], 'spectator_car_index' : [True, int, 17], 'sli_pro_native_support' : [True, int, 18], 'num_marshal_zones' : [True, int, 19], 'marshal_zones' : [False, 5, MarshalZone, 124], 'network_game' : [True, int, 125], 'num_weather_forecast_samples' : [True, int, 127], 'weather_forecast_samples' : [False, 8, WeatherForecastSample, 575], 'forecast_accuracy' : [True, int, 576], 'ai_difficulty' : [True, int, 577], 'season_link_identifier' : [True, int, 581], 'weekend_link_identifier' : [True, int, 585], 'session_link_identifier' : [True, int, 589], 'pit_stop_window_ideal__lap' : [True, int, 590], 'pit_stop_window_latest_lap' : [True, int, 591], 'pit_stop_rejoin_position' : [True, int, 592], 'steering_assist' : [True, int, 593], 'braking_assist' : [True, int, 594], 'gearbox_assist' : [True, int, 595], 'pit_assist' : [True, int, 596], 'pit_realese_assist' : [True, int, 597], 'ERS_assist' : [True, int, 598], 'DRS_assist' : [True, int, 599], 'dynamic_racing_line' : [True, int, 600], 'dynamic_racing_line_type' : [True, int, 601]}

    # 2 list types 
    # starting with true are single values
    # starting with false is a list of items with each size of item and type of item

    def __init__(self, body_data):
            self.body_data = body_data
            end_prev = 0
            for key, value in self.BYTES_SPLITS.items():
                if value[0]:
                    if value[1] == int:
                        setattr(self, key,  struct.unpack('<i', body_data[end_prev:value[2]]))
                        end_prev = value[2]
                    elif value[1] == float:
                        setattr(self, key, struct.unpack('<f', body_data[end_prev:value[2]]))
                        end_prev = value[2]
                else:
                    data_list = []
                    while value[3] > end_prev:
                        data_list.append(value[2](body_data[end_prev:end_prev+value[1]]))
                        end_prev = end_prev+value[1]
                    setattr(self, key, data_list)
                    end_prev = value[3]
            self.data_lenhgt = len(body_data)

        
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)