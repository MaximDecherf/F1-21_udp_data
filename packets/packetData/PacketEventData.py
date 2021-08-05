from .classes.eventClasses.Buttons import Buttons
from .classes.eventClasses.DriveThroughPenaltyServed import DriveThroughPenaltyServed
from .classes.eventClasses.FastestLap import FastestLap
from .classes.eventClasses.Flashback import Flashback
from .classes.eventClasses.Penalty import Penalty
from .classes.eventClasses.RaceWinner import RaceWinner
from .classes.eventClasses.Retirement import Retirement
from .classes.eventClasses.SpeedTrap import SpeedTrap
from .classes.eventClasses.StartLights import StartLights
from .classes.eventClasses.StopGoPenaltyServed import StopGoPenaltyServed
from .classes.eventClasses.TeamMateInPits import TeamMateInPits



class PacketEventData:

    EVENT_CODES = {'SSTA' : 'Sent when the session starts', 'SEND' : 'Sent when the session ends', 'FTLP' : FastestLap, 'RTMT' : Retirement, 'DRSE' : 'Race control have enabled DRS', 'DRSD' : "Race control have disabled DRS", 'TMPT' : TeamMateInPits, 'CHQF' : 'The chequered flag has been waved', 'RCWN' : RaceWinner, 'PENA' : Penalty, 'SPTP' : SpeedTrap, 'STLG' : StartLights, 'LGOT' : 'And it is Lights out and away we go, ki ki ki RAA, ki ki EYY', 'DTSV' : DriveThroughPenaltyServed, 'SGSV' : StopGoPenaltyServed, 'FLBK' : Flashback, 'BUTN' : Buttons }

    def __init__(self, body_data):
        self.body_data = body_data
        event_code = body_data[0:4].decode("utf-8")
        event = self.EVENT_CODES[event_code]
        if type(event) != str:
            event = event(body_data[4:])
        self.event = event
    
    def __repr__(self):
        return str(self.__dict__)
    
    def __str__(self):
        full_dict = self.__dict__
        del full_dict['body_data']
        return str(self.__class__) + " : " + str(full_dict)