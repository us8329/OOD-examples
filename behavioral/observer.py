'''
pubsub pattern - used in distributed systems 

Purpose : Define a one-to-many dependency so that when one object changes state, all its dependents are notified and updated automatically.
Key Points:
    1. Loose coupling via a subject interface
    2. Useful for event handling, MVC, and reactive systems

Publisher - source of events 
Observers - notified when events happen in real time.
'''

class YoutubeChannel():
    def __init__(self, name):
        self.name = name
        self.subscribers = []
    
    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self,event):
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self,name):
        self.name = name
    
    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")


channel = YoutubeChannel("sinha")

channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))
channel.subscribe(YoutubeUser("sub3"))

channel.notify("A new video is released")