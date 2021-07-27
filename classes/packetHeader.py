class PacketHeader():
    BYTES_SPLITS = {'packet_format' : 2, 'game_major_version' : 3, 'game_minor_version' : 4, 'packet_version' : 5 , 'packet_id' : 6, 'session_uuid' : 14, 'session_time' : 18, 'frame_identifier' : 22, 'player_car_index' : 23, 'secondary_player_car_index' : 24}
    HEADER_SIZE = 24

    def __init__(self, header_data):
        end_prev = 0
        if len(header_data) == self.HEADER_SIZE:
            for key, value in self.BYTES_SPLITS.items():
                setattr(self, key, int.from_bytes(header_data[end_prev:value], byteorder='little'))
                end_prev = value

            self.header_length = len(header_data)

        else:
            raise ValueError('Header must be size of {0} bytes'.format(self.HEADER_SIZE)) 



    def get_game_version(self):
        return (str(self.game_major_version) + "." + str(self.game_minor_version))

    def __len__(self):
        return self.header_length

    def __repr__(self):
            return {'packet_format':self.packet_format, 'game_major_version':self.game_major_version, 'game_minor_version':self.game_minor_version, 'packet_version':self.packet_version, 'packet_id':self.packet_id, 'session_uuid':self.session_uuid, 'session_time':self.session_time, 'frame_identifier':self.frame_identifier, 'player_car_index':self.player_car_index, 'secondary_player_car_index':self.secondary_player_car_index}


    def __str__(self):
        return str({'packet_format':self.packet_format, 'game_major_version':self.game_major_version, 'game_minor_version':self.game_minor_version, 'packet_version':self.packet_version, 'packet_id':self.packet_id, 'session_uuid':self.session_uuid, 'session_time':self.session_time, 'frame_identifier':self.frame_identifier, 'player_car_index':self.player_car_index, 'secondary_player_car_index':self.secondary_player_car_index})