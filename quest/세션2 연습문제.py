try :
    f=open("diamonds_data.csv",'r')
    lines=f.readlines()
    temp = lines
"D:\\그로스해커스\\파이썬세션데이터\\{0}.csv"
except :
     print("파일 경로가 틀렸습니다")

else:
    a = open("new_file2.csv", 'w')
    for line in temp:
        line=line.rstrip("\n").split(",")
        line.reverse()
        line.append("\n")
        _str = ",".join(line)
        a.write(_str)

print("생성완료")
f.close()
a.close()