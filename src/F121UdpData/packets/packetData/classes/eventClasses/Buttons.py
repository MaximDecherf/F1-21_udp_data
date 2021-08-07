
class Buttons:

    def __init__(self, data):
        self.button_status =  int.from_bytes(data[0:4], byteorder='little')

    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        return str(self.__class__) + " : " + str(self.__dict__)