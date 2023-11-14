import Event   #event class
import Node    #node class
import re      #regular expressions

#Assume that Logs have just been uploaded and parsed and there is a list of events
eventList = []
eventOne = Event.Event("10:10:10", "Something terrible happened", "Red")
eventTwo = Event.Event("10:12:00", "We fixed something terrible", "Blue")
eventThree = Event.Event("10:20:00", "Something even more terrible happened", "Red")
eventList.append(eventOne)
eventList.append(eventTwo)
eventList.append(eventThree)

nodeList = []
for event in eventList:
    #Creating list of nodes from events
    nodeList.append(Node.Node(event.teamAssociation, [], event.timeStamp, event.logInfo))

compareNodeList = nodeList

#compare nodes by converting time to a 6 digit number and measure absolute value of difference
for node in nodeList:
    nodeTime = re.split(":", node.timeStamp)
    nodeTimeRep = int(nodeTime[0])*10000
    nodeTimeRep = nodeTimeRep + int(nodeTime[1])*100
    nodeTimeRep = nodeTimeRep + int(nodeTime[2])
    for compareNode in compareNodeList:
        cNodeTime = re.split(compareNode.timeStamp, ":")
        cNodeTimeRep = int(nodeTime[0])*10000
        cNodeTimeRep = nodeTimeRep + int(nodeTime[1])*100
        cNodeTimeRep = nodeTimeRep + int(nodeTime[2])
        if(node != compareNode):
            if(abs(nodeTimeRep - cNodeTimeRep) < 5000):
                node.connections.append(compareNode)

print(nodeList[0].timeStamp)         
print(nodeList[0].connections[0].timeStamp)  

#Essentially, this implementation checks for how close the events were in happening by their time stamp
#This would be the default setup for the graph nodes but can be changed if they are inaccurate
#I contemplated adding a method to the node class to take care of the time conversion for me, but it was
#a last minute thought.
