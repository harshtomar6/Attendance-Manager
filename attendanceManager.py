#Lets program an attendance Manager.

from ast import literal_eval
from attendanceSuggestor import attendanceSuggestor
from exception import exceptionManager
import time

timeTable = {
    "Monday": ["se", "dc", "m&m", "daa", "se", "ooc", "maths"],
    "Tuesday": ["maths", "dc", "m&m", "ooc", "daa lab"],
    "Wednesday": ["m&m", "se", "daa", "dc"],
    "Thursday": ["m&m", "daa", "ooc", "maths", "se", "dc", "m&m"],
    "Friday": ["m&m lab"],
    "Saturday": ["ooc", "maths", "daa", "dc"],
    "Sunday": []
}

class attendanceRegister:
    #Constructor
    def __init__(self):
        fp1 = open("data1","rb")
        self.data1 = fp1.read().decode("utf-8")
        self.data1 = literal_eval(self.data1)
        fp1.close()
        self.attendance = self.data1

        fp2 = open("data2", "rb")
        self.data2 = fp2.read().decode("utf-8")
        self.data2 = literal_eval(self.data2)
        fp2.close()
        self.classesOver = self.data2

        fp3 = open("data3", "rb")
        self.data3 = fp3.read().decode("utf-8")
        self.data3 = literal_eval(self.data3)
        self.currentStreak = self.data3

        fp4 = open("data4", "rb")
        self.data4 = fp4.read().decode("utf-8")
        self.data4 = literal_eval(self.data4)
        self.maxStreak = self.data4

    def addAttendance(self):
        todayClasses = timeTable[getWeekDay()]
        print("(Press 1 to mark present, 0 to absent and 2 to raise an exception)")
        for c in todayClasses:
            ch = input(c+": ")
            if ch == '1':
                self.attendance[c] += 1
                self.classesOver[c] += 1
                self.currentStreak[c] += 1
                self.updateMaxStreak(c)
            elif ch == '0':
                self.classesOver[c] += 1
                self.currentStreak[c] = 0
            elif ch == '2':
                print("1. Today is Holiday")
                print("2. Class didn't happened")
                print("3. Another Class happened")
                ch = int(input("Enter your choice: "))

                if ch == 1:
                    exceptionManager.holidayException(self)
                    return
                elif ch == 2:
                    subjects = exceptionManager.classNotHappenedException(self)
                elif ch == 3:
                    anotherClass = input("Which class happened: ")
                    self.attendance[anotherClass] += 1
                    self.classesOver[anotherClass] += 1
                    self.currentStreak[anotherClass] += 1
                    self.updateMaxStreak(anotherClass)
            else:
                print("Invalid Input")

        confirm = input("Press 1 to confirm, 0 to reset: ")
        if confirm == '1':
            self.writeData(self.attendance, "data1")
            self.writeData(self.classesOver, "data2")
            self.writeData(self.currentStreak, "data3")
            self.writeData(self.maxStreak, "data4")
            print("Attendance added successfully")
        if confirm == '0':
            for a in self.attendance:
                self.attendance[a] = self.data1[a]
            for c in self.classesOver:
                self.classesOver[c] = self.data2[c]
            print("Attendance reset successfully")

    def getSubjectAttendance(self, subjectName):
        arr = []
        arr.append(self.attendance[subjectName])
        arr.append(self.classesOver[subjectName])
        arr.append(self.attendance[subjectName]/self.classesOver[subjectName]*100)
        arr.append(self.currentStreak[subjectName])
        arr.append(self.maxStreak[subjectName])
        return arr

    def getAttendance(self):
        return self.attendance

    def getTotalClasses(self):
        return self.classesOver

    def getAttendancePercentage(self):
        arr = []
        for a in self.attendance:
            arr.append(self.attendance[a]/self.classesOver[a]*100)

        return arr

    def updateMaxStreak(self, subject):
        if self.currentStreak[subject] > self.maxStreak[subject]:
            self.maxStreak[subject] = self.currentStreak[subject]

    def getCurrentStreak(self):
        arr = []
        for a in self.currentStreak:
            arr.append(self.currentStreak[a])

        return arr

    def getMaxStreak(self):
        arr = []
        for a in self.maxStreak:
            arr.append(self.maxStreak[a])

        return arr

    def writeData(self, data, fileName):
        fp = open(fileName, "wb")
        fp.write(str(data).encode("utf-8"))
        fp.close()

def getWeekDay():
    return time.strftime("%A")

def getDate():
    return time.strftime("%d/%m/%Y")

def main():
    register = attendanceRegister()
    print(timeTable[getWeekDay()])
    print(getDate())
    while True:
        print("==============ATTENDANCE REGISTER================\n")
        print("1. ADD ATTENDANCE\n2. View subject ATTENDANCE\n3. View all Attendance\n4. Suggestion\n5. Show Time Table\n6. Exit\n")
        ch = int(input())
        if ch == 1:
            register.addAttendance()
        elif ch == 2:
            subjectName = input("Enter subject name to view attendance:  ")
            arr = register.getSubjectAttendance(subjectName)
            print("Subject\t  Attendance\tPercentage\tCrnt. Streak\tMAX Streak\n")
            print(subjectName +"\t\t"+str(arr[0])+"/"+str(arr[1])+"\t"+str(round(arr[2], 2))+"% \t\t   "+str(arr[3])+"\t\t   "+str(arr[4]))
        elif ch == 3:
            i=0
            attendance = register.getAttendance()
            classes = register.getTotalClasses()
            arr = register.getAttendancePercentage()
            arr2 = register.getCurrentStreak()
            arr3 = register.getMaxStreak()
            print("Subject\t  Attendance\tPercentage\tCrnt. Streak\tMAX Streak\n")
            for a in attendance:
                print(a + "\t\t"+str(attendance[a])+"/"+str(classes[a])+"\t"+str(round(arr[i], 2))+"% \t\t   "+str(arr2[i])+"\t\t   "+str(arr3[i]))
                i=i+1
            print("\n")

        elif ch == 4:
            suggest = attendanceSuggestor()
            print("1. Get TODAY Bunking classes")
            print("2. Get Next Bunking Class Status")
            print("3. Get Next FULL Bunk Day")
            status = int(input())
            if status == 1:
                suggest.getTodayBunkClasses()
            elif status == 2:
                subject = input("Enter subject name: ")
                suggest.getNextBunkClass(subject)
            elif status == 3:
                suggest.getNextBunkDay()

        elif ch == 5:
            for t in timeTable:
                print(t +": "+str(timeTable[t]))

        elif ch == 6:
            return

        else:
            print("INVALID INPUT")

main()
