import random

print("Enter the number of frames: ",end="")
capacity = int(input())
s=[]
printall=0

print("Enter the number of products: ",end="")
products = int(input())
print("Enter the number of customers: ",end="")
customers = int(input())
'''r=[8]
if customers in [r]:
    for i in range (customers):
        p=random.randint(0,10000)
        for j in range(len(ranges[customers])-1):
            if p<ranges[customers][j]:
                s.append(j)
                break
else:'''
for i in range(customers):
    s.append(random.randint(0,products-1))
#print(s)
#s = list(map(int,input().strip().split()))


#FIFO Algorithm


f,fault,top= [],0,0

print("-"*50,"FIFO","-"*50)
if printall:
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
print("\nFault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
        else:
            f[top] = i
            top = (top+1)%capacity
        fault += 1
        pf = 'Miss'
    else:
        pf = 'Hit'
    if printall:
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
file=open('output.txt','w')
file.write("FIFO Page Replacemet Algorithm\n")
file.write("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))



#Second Chance Algorithm

f,fault,front,pf = [],0,0,'Hit'
bit=[]
print("-"*47,"Second Chance","-"*47)
if printall:
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
print("\nFault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            bit.append(0)
        else:
            while(bit[front]==1):
                bit[front]=0
                front = (front+1)%capacity
            f[front] = i
            front = (front+1)%capacity
        fault += 1
        pf = 'Miss'
    else:
        bit[f.index(i)]=1
        pf= 'Hit'
    if printall:
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
#file=open('output.txt','w')
file.write("FIFO Page Replacemet Algorithm\n")
file.write("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))



#LRU Algorithm

f,st,fault,pf = [],[],0,'No'
print("\n","-"*50,"LRU","-"*50)
if printall:
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
print("\nFault\n   ↓\n")
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            st.append(len(f)-1)
        else:
            ind = st.pop(0)
            f[ind] = i
            st.append(ind)
        pf = 'Miss'
        fault += 1
    else:
        st.append(st.pop(st.index(f.index(i))))
        pf = 'Hit'
    if printall:
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
#file=open('output.txt','w')
file.write("\n\n\nLeast Recently Used Page Replacemet Algorithm\n")
file.write("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))

# Marking Algorithm

print("-"*50,"Marking","-"*50)
if printall:
    print("\nString|Frame →\t",end='')
    for i in range(capacity):
        print(i,end=' ')
print("\nFault\n   ↓\n")
f,fault,front,pf,mark= [],0,0,'Hit',[]
for i in s:
    if i not in f:
        if len(f)<capacity:
            f.append(i)
            mark.append(0)
        else:
            unmarked =[]
            for j in range(capacity):
                if mark[j]==0:
                    unmarked.append(j)
            if len(unmarked)>0:
                random.shuffle(unmarked)
                f[unmarked[0]]=i
            else:
                for j in range(capacity):
                    mark[j]=0
                for j in range(capacity):
                    if mark[j]==0:
                        unmarked.append(j)
                random.shuffle(unmarked)
                f[unmarked[0]]=i
            pf = 'Miss'
            fault+=1
    else:
        mark[f.index(i)]=1
        pf= 'Hit'
    if printall:
        print("   %d\t\t"%i,end='')
        for x in f:
            print(x,end=' ')
        for x in range(capacity-len(f)):
            print(' ',end=' ')
        print(" %s"%pf)
print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))
#file=open('output.txt','w')
file.write("\n\n\nMarking Page Replacemet Algorithm\n")
file.write("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(s),fault,(fault/len(s))*100))




file.close()
