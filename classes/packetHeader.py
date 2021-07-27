class PacketHeader():
    BYTES_SPLITS = {'packet_format' : 2, 'game_major_version' : 3, 'game_minor_version' : 4, 'packet_version' : 5 , 'packet_id' : 6, 'session_uuid' : 14, 'session_time' : 18, 'frame_identifier' : 22, 'player_car_index' : 23, 'secondary_player_car_index' : 24}
    HEADER_SIZE = 24


    # def __init__(self, packet_format, game_major_version, game_minor_version, packet_version, packet_id, session_uuid, session_time, frame_identifier, player_car_index, secondary_player_car_index):
    #     self.packet_format = int.from_bytes(packet_format, byteorder='little')
    #     self.game_major_version = int.from_bytes(game_major_version, byteorder='little')
    #     self.game_minor_version = int.from_bytes(game_minor_version, byteorder='little')
    #     self.packet_version = int.from_bytes(packet_version, byteorder='little')
    #     self.packet_id = int.from_bytes(packet_id, byteorder='little' )
    #     self.session_uuid = int.from_bytes(session_uuid, byteorder='little')
    #     self.session_time = int.from_bytes(session_time, byteorder='little')
    #     self.frame_identifier = int.from_bytes(frame_identifier, byteorder='little') 
    #     self.player_car_index = int.from_bytes(player_car_index, byteorder='little')
    #     self.secondary_player_car_index = int.from_bytes(secondary_player_car_index, byteorder='little')


    def __init__(self, header_data):
        end_prev = 0
        if len(header_data) == HEADER_SIZE:
            for key, value in BYTES_SPLITS.items():
                self.key = int.from_bytes(header_data[end_prev:value], byteorder='little')
                end_prev = value
        else:
            raise ValueError('Header must be size of {0} bytes'.format(HEADER_SIZE)) 
	       


    def get_game_version(self):
        return (self.game_major_version + "." + self.game_minor_version)

    def __repr__(self):
            return {'packet_format':self.packet_format, 'game_major_version':self.game_major_version, 'game_minor_version':self.game_minor_version, 'packet_version':self.packet_version, 'packet_id':self.packet_id, 'session_uuid':self.session_uuid, 'session_time':self.session_time, 'frame_identifier':self.frame_identifier, 'player_car_index':self.player_car_index, 'secondary_player_car_index':self.secondary_player_car_index}

    def __str__(self):
        return str({'packet_format':self.packet_format, 'game_major_version':self.game_major_version, 'game_minor_version':self.game_minor_version, 'packet_version':self.packet_version, 'packet_id':self.packet_id, 'session_uuid':self.session_uuid, 'session_time':self.session_time, 'frame_identifier':self.frame_identifier, 'player_car_index':self.player_car_index, 'secondary_player_car_index':self.secondary_player_car_index})