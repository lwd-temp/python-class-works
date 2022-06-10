# 长度大于等于5任意字符串
# 图形两个对角线是*，每行其他字符与字符串对应的字符相同

def getInput():
    # 获取用户输入
    while True:
        try:
            s = input('请输入字符串：')
            if len(s) >= 5:
                # len()函数返回字符串的长度
                return s
            elif not s.isalnum():
                # isalnum()判断是否为字母或数字
                print("请输入字母或数字")
            else:
                print('字符串长度不足5')
        except:
            print('输入错误')


def printPattern(s):
    # 打印图形
    # 图形两个对角线是*，每行其他字符与字符串对应的字符相同
    # 获取字符串总长度 = 图形横宽 = 图形行数
    maxlen = len(s)
    # 构造图形每一行
    for i in range(0, maxlen):
        # 未添加*的行
        line = s[i]*maxlen
        # 替换两个*
        # 别问我这两个表达式是怎么写的，我写的上一行，GitHub Copilot帮我写的下一行
        line = line[:i] + '*' + line[i+1:]
        line = line[:maxlen-i-1] + '*' + line[maxlen-i:]
        # 打印行
        print(line)


if __name__ == '__main__':
    # 这个判断仅在直接运行时为True，当作为模块被导入时为False
    s = getInput()
    printPattern(s)
