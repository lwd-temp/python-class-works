# print("       静夜思"+"\n"+"     作者：李白"+"\n"+"床前明月光，疑似地上霜。"+"\n"+"举头望明月，低头思故乡。")
# 就一行

# center方法让字符串居中，可以指定居中的宽度和填充字符
print("静夜思".center(20, "　"))
print("作者：李白".center(20, "　"))
print("床前明月光，疑似地上霜。".center(20, "　"))
print("举头望明月，低头思故乡。".center(20, "　"))

print("静夜思".center(20, "　")+"\n"+"作者：李白".center(20, "　")+"\n" +
      "床前明月光，疑似地上霜。".center(20, "　")+"\n"+"举头望明月，低头思故乡。".center(20, "　"))

title = input("请输入诗的题目：")
author = input("请输入诗的作者：")
first = input("请输入前两句诗：")
second = input("请输入后两句诗：")
longest = max(len(title), len(author), len(first), len(second))
print(title.center(longest, "　"))
print(author.center(longest, "　"))
print(first.center(longest, "　"))
print(second.center(longest, "　"))
