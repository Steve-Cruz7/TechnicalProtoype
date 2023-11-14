#Assuming that each node will have some color (determined by team), list of connections, timestamp, log information

class Node:
    def __init__(self, color, connections, timeStamp, logInfo):
        self.color = color
        self.connections = connections
        self.timeStamp = timeStamp
        self.logInfo = logInfo