import cgi

data = cgi.FieldStorage()
obj = data["filename"]  # 获得上传的分装过的文件对象
filename = obj.filename  # 获得上传的文件的原名字
file = obj.file  # 获得的是文件对象本身

new_file = open("D:/python-server/"+filename, mode="wb")
new_file.write(file.read())  # 将上传的文件写入到一个目录去
new_file.flush()
new_file.close()


print("Content-type:text/plain")
print()

print("ok")


