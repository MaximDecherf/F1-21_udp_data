
class WeatherForecastSample:

    NUMBER_DECODER = {'weather' : ['clear', 'light cloud', 'overcast', 'light rain', 'heavy rain', 'storm'], 'session_type' : ['unknown', 'P1', 'P2', 'P3', 'short P5', 'Q1', 'Q2', 'Q3', 'short Q', 'OSQ', 'R', 'R2', 'R3', 'Time trial'], 'track_temperature_change' : ['up', 'down', 'no change'], 'air_temperature_change' : ['up', 'down', 'no change']}

    def __init__(self, data, decode_numbers=True):
        self.session_type =  int.from_bytes(data[0:1], byteorder='little')
        self.time_offset = int.from_bytes(data[1:2], byteorder='little')
        self.weather = int.from_bytes(data[2:3], byteorder='little')
        self.track_temperature = int.from_bytes(data[3:4], byteorder='little')
        self.track_temperature_change = int.from_bytes(data[4:5], byteorder='little')
        self.air_temperature = int.from_bytes(data[5:6], byteorder='little')
        self.air_temperature_change = int.from_bytes(data[6:7], byteorder='little')
        self.rain_percentage = int.from_bytes(data[7:8], byteorder='little')
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