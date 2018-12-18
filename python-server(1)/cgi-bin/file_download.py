file = open("d:/python-server/1.txt", mode="rt")

# 设置文件下载的响应头
print("Content-Disposition: attachment; filename=d:/python-server/1.txt")
print()

print(file.read())


