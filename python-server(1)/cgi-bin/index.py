import codecs, sys
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


print("Content-type:text/html")  # 设置响应头
print()  # 打印一个空行
# 开始响应正文
print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("<meta charset='utf-8'/>")  # 告诉浏览器以什么样子的编码打开
print("</head>")
print("<body>")
print("这里是使用cgi程序响应的内容")
print("</body>")
print("</html>")
