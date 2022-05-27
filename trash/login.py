# 模拟用户登录
users = ['root', 'westos']
passwords = ['123', '456']

# 登录函数
def login(users, passwords, selectedUser=""):
    if selectedUser == "":
        inuser = input("请输入用户名：")
        if inuser in users:
            index = users.index(inuser)
            correctPassword = passwords[index]
            inpassword = input("请输入密码：")
            if inpassword == correctPassword:
                print("登录成功，欢迎您！")
                return 0, "OK"
            else:
                print("密码错误，请重新输入！")
                return 1, str(inuser)
        else:
            print("该用户不存在")
            return 2, "User Error"
    else:
        if selectedUser in users:
            index = users.index(selectedUser)
            correctPassword = passwords[index]
            inpassword = input("请输入密码：")
            if inpassword == correctPassword:
                print("登录成功，欢迎您！")
                return 0, "OK"
            else:
                print("密码错误，请重新输入！")
                return 1, str(selectedUser)
        else:
            print("【内部错误，这个问题不该发生】")
            return 3, "Internal Error"

# 主函数，负责次数限制和调用登录
def main():
    count = 0
    username = ""
    while count < 3:
        result = login(users, passwords, username)
        if result[0] == 0:
            break
        elif result[0] == 1:
            count += 1
            username = result[1]
        elif result[0] == 2:
            count += 1
        elif result[0] == 3:
            print("【内部错误，这个问题不该发生】")
            break
    else:
        print("已经尝试3次，没有机会了。")

# 这个判断式仅在直接执行时为True，当作为模块导入时为False
if __name__ == "__main__":
    main()
