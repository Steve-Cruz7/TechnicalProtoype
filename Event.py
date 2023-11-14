#In this prototype, an event will consist of a time stamp, log info, and team association

class Event:
    def __init__(self, timeStamp, logInfo, teamAssociation):
        self.timeStamp = timeStamp
        self.logInfo = logInfo
        self.teamAssociation = teamAssociation

    def __str__(self):
        return "Time Occured: {self.timeStamp} \n Info: {self.logInfo} \n Team: {self.teamAssociation}"
