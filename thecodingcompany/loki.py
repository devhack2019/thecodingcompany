import time
l1 = 0
l2 = 0
round = 0
students=[]
loki = 0
rate = 0.5
start = time.time()
count = 0
while loki < 40:
    print('Round ' + str(round))
    f = open("in.txt","r")
    in_item = f.read()
    in_item = in_item.strip()
    in_item = in_item.split("\n")
    for i in range(l1,len(in_item),1):
        in_item[i] = in_item[i].split(" ")
        exist = 0
        for j in students:
            if j['name'] == in_item[i][0]:
                j['in'] = float(in_item[i][1])
                j['status'] = 'IN'
                exist = 1
        if exist == 0:
            dict1 = {'name' : in_item[i][0],'in' : float(in_item[i][1]),'out' : float(0),'tin' : float(0),'tout' : float(0),'status' : 'IN'}
            students.append(dict1)
    l1 = len(in_item)
    f.close()
    f = open("out.txt","r")
    out_item = f.read()
    out_item = out_item.strip()
    out_item = out_item.split("\n")
    for i in range(l2,len(out_item),1):
        out_item[i] = out_item[i].split(" ")
        exist = 0
        for j in students:
            if j['name'] == out_item[i][0]:
                j['out'] = float(out_item[i][1])
                j['status'] = 'OUT'
                exist = 1
        if exist == 0:
            dict1 = {'name' : out_item[i][0],'in' : float(0),'out' : float(out_item[i][1]),'tin' : float(0),'tout' : float(0),'status' : 'OUT'}
            students.append(dict1)
    l2 = len(out_item)
    f.close()
    f = open("real_time_count.txt",'w')
    count=0
    for a in students:
        if a['status'] == 'IN':
            a['tin'] = a['tin'] + rate
        else:
            a['tout'] = a['tout'] + rate 
        if(a['in'] > a['out']):
            print(a['name'], " is INSIDE\ttotal in time : ",a['tin'],"\ttotal out time : ",a['tout'])
            count = count + 1
            f.write(a['name'] + "\n")
        else:
            print(a['name'], " is OUTSIDE\ttotal in time : ",a['tin'],"\ttotal out time : ",a['tout'])
    print("\n")
    round = round + 1
    loki = loki + 1
    f.close()
    time.sleep(rate)
