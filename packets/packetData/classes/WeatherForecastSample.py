
class WeatherForecastSample:

    def __init__(self, data):
        self.session_type =  int.from_bytes(data[0:1], byteorder='little')
        self.time_offset = int.from_bytes(data[1:2], byteorder='little')
        self.weather = int.from_bytes(data[2:3], byteorder='little')
        self.track_temperature = int.from_bytes(data[3:4], byteorder='little')
        self.track_temperature_change = int.from_bytes(data[4:5], byteorder='little')
        self.air_temperature = int.from_bytes(data[5:6], byteorder='little')
        self.air_temperature_change = int.from_bytes(data[6:7], byteorder='little')
        self.rain_percentage = int.from_bytes(data[7:8], byteorder='little')
        

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)