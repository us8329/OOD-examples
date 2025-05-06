'''
purpose : ensure a class has only one instance and provide a global point of access
key points: 
    1. private constructor 
    2. static instance holder 
    3. thread safety consideration 
'''


class ApplicationState:
    instance = None 
    
    def __init__(self):
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance
    
appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn)
print(appState2.isLoggedIn)
 