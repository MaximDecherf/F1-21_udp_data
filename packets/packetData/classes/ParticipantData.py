import re

class ParticipantData:

    NUMBER_DECODER = {'ai_controlled' : ['Human', 'Ai'], 'my_team' : ['otherwise'], 'your_telemetry' : ['restricted', 'public']}
    
    #TODO add appendix

    def __init__(self, data, decode_numbers=True):
        self.ai_controlled = int.from_bytes(data[0:1], byteorder='little') 
        self.driver_id = int.from_bytes(data[1:2], byteorder='little')
        self.network_id = int.from_bytes(data[2:3], byteorder='little')
        self.team_id = int.from_bytes(data[3:4], byteorder='little')
        self.my_team = int.from_bytes(data[4:5], byteorder='little')
        self.race_number = int.from_bytes(data[5:6], byteorder='little')
        self.nationality = int.from_bytes(data[6:7], byteorder='little')
        self.name = re.sub(r'\x00', '', data[7:55].decode("utf-8"))
        self.your_telemetry = int.from_bytes(data[55:56], byteorder='little')

        if decode_numbers:
            self.decode_numbers() 
    
    
    def decode_numbers(self):
        for key, decoder in self.NUMBER_DECODER.items():
            int_value = getattr(self, key)
            if int_value < 0:
                setattr(self, key, 'my team') # for my team flag
            else:
                setattr(self, key, decoder[int_value])
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        return str(self.__class__) + " : " + str(full_dict)
