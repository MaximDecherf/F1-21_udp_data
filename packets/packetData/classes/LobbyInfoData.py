import re

class LobbyInfoData:

    def __init__(self, data):
        self.ai_controlled = int.from_bytes(data[0:1], byteorder='little')
        self.team_id = int.from_bytes(data[1:2], byteorder='little')
        self.nationality = int.from_bytes(data[2:3], byteorder='little')
        self.name = re.sub(r'\x00', '', data[3:52].decode("utf-8")) #cleans up name 
        self.ready_status = int.from_bytes(data[52:53], byteorder='little')
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)