#Encapsulation
class accountInfoProtected:
    def __init__(self):
        self.__AccountNumber = "AMBER-USA" # this is the private attribute - to change its value,
        #we must do it within the class
        self._Password = "Z01Mm%tfQ" # this is the protected attribute

    def getAccount(self):
        print(self.__AccountNumber)

    def setAccount(self, Account):
        self.__AccountNumber = Account

SensitiveInfo = accountInfoProtected() # instantiating object and calling it SensitiveInfo
SensitiveInfo.getAccount() # this returns the initial value set by init

SensitiveInfo.setAccount("AMBER-NORTH-AMERICA")#changing value of the attribute 
SensitiveInfo.getAccount() # this returns the new account number given in previous function

SensitiveInfo._Password = "PasswordProtected" # we can change the value outside of the class
print(SensitiveInfo._Password)
