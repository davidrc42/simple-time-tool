import config
from playsound import playsound


class Time:
    def __init__(
        self,
        # in minutes
        breakTime,
        sessionTime,
        sessionCount,
    ):
        self.currentSeconds = 0
        self.currentMinutes = sessionTime
        self.currentHours = 0
        self.breakTime = breakTime
        self.sessionTime = sessionTime
        self.sessionCount = sessionCount
        # either session(counting down), break(counting down), downtime(waiting for click between sesion and break),active
        self.sessionOrBreak = "session"
        self.status = "active"
        # when a session or break ends the first alarm must be instant this variable is responsible for  that
        self.firstAlarmOff = False

    def returnTimeFormatted(self):
        formattedTime = ""
        if self.currentHours > 0:
            formattedTime += f"{self.currentHours}:"

        if self.currentMinutes < 10:
            formattedTime += f"0{self.currentMinutes}:"
        elif self.currentMinutes > 0:
            formattedTime += f"{self.currentMinutes}:"

        if self.currentSeconds < 10:
            formattedTime += f"0{self.currentSeconds}"
        elif self.currentSeconds > 0:
            formattedTime += f"{self.currentSeconds}"
        elif self.currentSeconds <= 0:
            formattedTime += f"00"
        return formattedTime

    def passSecond(self):
        self.currentSeconds -= 1
        if self.currentSeconds == 0:
            self.checkForReset()
        if self.currentSeconds < 0:
            self.passMinute()
            self.currentSeconds = 59

    def passMinute(self):
        if self.currentMinutes < 0:
            if self.currentHours > 0:
                self.currentMinutes = 59
                self.currentHours -= 1
        self.currentMinutes -= 1

    def setSessionOrBreak(self, state):
        self.sessionOrBreak = state

    def setStatus(self, status):
        self.status = status

    def setSessionCount(self, sessionCount):
        if sessionCount == -1:
            self.sessionCount -= 1
        else:
            self.sessionCount = sessionCount

    def setCurrentMinutes(self, minutes):
        self.currentMinutes = minutes

    def setCurrentSeconds(self, seconds):
        self.currentSeconds = seconds

    def playAlarm(self):
        playsound("/home/david/code/simple-time-tool/src/birdSound.wav")

    def checkForReset(self):
        if (
            self.currentSeconds == 0
            and self.currentMinutes == 0
            and self.currentHours == 0
        ):
            self.firstAlarmOff = True
            if self.sessionOrBreak == "session" and self.sessionCount > 1:
                self.setSessionCount(-1)
                self.setCurrentMinutes(self.breakTime)
                self.setCurrentSeconds(0)
                self.setStatus("downtime")
                self.setSessionOrBreak("break")
            elif self.sessionOrBreak == "break":
                self.setStatus("downtime")
                self.setCurrentMinutes(self.sessionTime)
                self.setCurrentSeconds(0)
                self.setSessionOrBreak("session")
            else:
                self.setStatus("finished")
                print("congrats you finished everything")


myTime = Time(config.breakTime, config.sessionTime, config.sessionCount)
