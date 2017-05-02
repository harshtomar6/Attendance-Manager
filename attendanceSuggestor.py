import time
from ast import literal_eval

timeTable = {
    "Monday": ["se", "dc", "m&m", "daa", "se", "ooc", "maths"],
    "Tuesday": ["maths", "dc", "m&m", "ooc", "daa lab"],
    "Wednesday": ["m&m", "se", "daa", "dc"],
    "Thursday": ["m&m", "daa", "ooc", "maths", "se", "dc", "m&m"],
    "Friday": ["m&m lab"],
    "Saturday": ["ooc", "maths", "daa", "dc"],
    "Sunday": []
}

class attendanceSuggestor:
    def __init__(self):
        fp = open("data1", "rb")
        data1 = fp.read().decode("utf-8")
        data1 = literal_eval(data1)
        self.attendance = data1

        fp2 = open("data2", "rb")
        data2 = fp2.read().decode("utf-8")
        data2 = literal_eval(data2)
        self.totalClasses = data2

        fp3 = open("data3", "rb")
        data3 = fp3.read().decode("utf-8")
        data3 = literal_eval(data3)
        self.currentStreak = data3

    def getPercentage(self, subjectName):
        return self.attendance[subjectName]/self.totalClasses[subjectName]*100

    def getCurrentStreak(self, subjectName):
        return self.currentStreak[subjectName]

    def getTodayBunkClasses(self):
        today = time.strftime("%A")

        for c in timeTable[today]:
            self.getNextBunkClass(c)

    def getNextBunkClass(self, subjectName):
        streak = self.getCurrentStreak(subjectName)
        percentage = self.getPercentage(subjectName)

        if streak >= 4 and percentage >= 80:
            print("HURRAY!! You can bunk "+str(subjectName).upper()+" class TODAY")
        elif streak < 4 and percentage >= 80:
            print("Come On!! "+str(4-int(streak))+" more classes to bunk " +str(subjectName).upper()+" class")
        elif percentage < 80:
            print("NO Bunking today!!. You need to maintain your attendance. "+str(self.getClassesToMaintain(subjectName))+" more to go")
        else:
            print("Sorry!! But I cannot suggest you right now")

    def getNextBunkDay(self):
        today = time.strftime("%A")
        for c in timeTable[today]:
            if currentStreak[c] >= 4:
                flag = 1
            else:
                return False

        return True

    def getClassesToMaintain(self, subjectName):
        difference = self.attendance[subjectName] - self.totalClasses[subjectName]
        attTemp = self.attendance[subjectName]
        classesTemp = self.totalClasses[subjectName]
        percent = attTemp/classesTemp*100
        count = 0

        while percent < 80.0:
            attTemp += 1
            classesTemp += 1
            count += 1
            percent = attTemp/classesTemp*100

        return count
