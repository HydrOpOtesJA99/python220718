import re 

f=open('c:\\work\\PV3.txt','rt')
g=open('c:\\work\\PV3_copy.txt','wt',encoding='utf-8') # output 파일

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리하는 식으로 바꿔줘야함 
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("\d{4}", line)): # 연속된 4개의 수가 있는 line을 찾아라
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()







