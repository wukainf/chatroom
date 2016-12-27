import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class ChartRoom():
    def __init__(self,ID,name):
        self.mumber = []
        self.ID = ID
        self.name = name

    def addNewMember(self,user):
        self.mumber.append(user.username)

    def remMember(self,user):
        self.mumber.remove(user.username)

    def getAllMember(self):
        return self.mumber
