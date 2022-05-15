import getpass
import hashlib


def getPass(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()


def inputPass():
    passw = getpass.getpass('请输入密码：')
    return passw


def getuser():
    user = input('请输入用户名：')
    return user


def checkPass(user, password):
    if user == 'python' and getPass(password) == 'e10adc3949ba59abbe56e057f20f883e':
        print("欢迎进入python学习课程！")
        return True
    else:
        print("用户名或密码错误，请重新输入")
        return False


checkPass(getuser(), inputPass())
