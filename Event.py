#In this prototype, an event will consist of a time stamp, log info, and team 

class Event:
    def __init__(self, timeStamp, logInfo, teamAssociation):
        self.timeStamp = timeStamp
        self.logInfo = logInfo
        self.teamAssociation = teamAssociation

    def __str__(self):
        return "Time Occured: {self.timeStamp} \n Info: {self.logInfo} \n Team: {self.teamAssociation}"

    # Setters
    def setTimeStamp(self, new):
        self.timeStamp = new

    def setlogInfo(self, new):
        self.logInfo = new

    def setTeamAssociation(self, new):
        self.teamAssociation = new

    # getters

    def getTimeStamp(self):
        return self.timeStamp
    
    def getlogInfo(self):
        return self.logInfo
    
    def getTeamAssociation(self):
        return self.teamAssociation
    