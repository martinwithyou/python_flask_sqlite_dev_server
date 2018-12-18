import cgi
import codecs, sys

# 解决编码问题
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)

data = cgi.FieldStorage()  # 获得客户端提交的数据对象
username = data.getvalue("username")  # 根据客户端提交的参数的名字 获取对应的值
password = data.getvalue("password")
sex = data.getvalue("sex")
hobby = data.getvalue("hobby")
self = data.getvalue("self")

#  处理处理 - 将数据进行保存
file = open("user.txt", "at")
user = {"username": username, "password": password, "sex": sex, "hobby": hobby, "self": self}
file.write(str(user))
file.write("\n")


# 开始响应程序 处理程序写在响应程序之前
print("Content-type:text/html;charset=utf8")  # 设置响应头时 指定浏览器打开的编码
print()

print("ok")
print("<p>")
print("恭喜您注册成功<br/>")
print(str(user))
print("</p>")

