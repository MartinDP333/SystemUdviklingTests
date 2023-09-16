class Television: # Television class with all methods (implemented to solve tests)
    def __init__(self):
        self.on = False
        self.channel = 5
        self.volume = 6
        self.mute = False
    def tvOnOff(self):
        self.on = not self.on
    def getCh(self):
        return self.channel
    def chUp(self):
        self.channel += 1
    def chDown(self):
        if self.channel > 0:
            self.channel -= 1
        else:
            self.channel = 0
    def getVol(self):
        return self.volume
    def volUp(self):
        self.volume += 2
    def volDown(self):
        if self.volume < 2:
            self.volume = 0
        else:
            self.volume -= 2
    def getMuted(self):
        return self.mute
    def muteOnOff(self):
        self.mute = not self.mute