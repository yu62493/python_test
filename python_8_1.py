# _*_ coding:utf-8 _*_
fp = open("readme.txt","r")
readmes = fp.readlines()
fp.close()
i=1
print("The line of Python")
for line in readmes:
	print("Line {}: {}".format(i,line),end="")
	i += 1
