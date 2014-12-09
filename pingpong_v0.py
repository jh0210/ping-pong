# Calculate ping-pong signature from Ravi server csv file
# 2014.03.24 wrote for python3
#
# 1. problem of taking 'abs', now take real overlap taking orientation.
#
# may have to include the next line for python2
#
#from __future__ import print_function
#

data=open('23_28_roo.csv')
start=[]
j1=[]
j3=[]
ori=[]
ping=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for each_line in data:
    s_data=each_line.split(",")
    if s_data[0]!='seq':
           start.append(int(s_data[19]))
           j1.append(int(s_data[16])) # het ov - 14, het tes - 15, thoc5 mut ov 16, thoc5 mut tes - 17
           ori.append(s_data[24])
         
#   j3.append(int(s_data[16]))
    

# print(start[1],j1[1],j3[1],ori[1])

start_len=len(start)

for x in range(0,start_len-1):
    position_1=start[x]
    read_no_1=j1[x]
    for y in range(0,start_len-1):
        if ori[x]=='+\n' and ori[y]=='-\n':
            position_2=start[y]
            read_no_2=j1[y]
            gap=position_2-position_1
            if gap>=0 and gap<=24:
                ping[gap]=ping[gap]+read_no_1*read_no_2                
        if ori[x]=='-\n' and ori[y]=='+\n':
            position_2=start[y]
            read_no_2=j1[y]
            gap=position_1-position_2
            if gap>=0 and gap<=24:
                ping[gap]=ping[gap]+read_no_1*read_no_2

out=open('pingpong.csv','w')
for item in ping:
    print(item,file=out)

out.close()

print('run finished')

