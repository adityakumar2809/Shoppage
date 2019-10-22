from django.shortcuts import render, redirect
import random
import json
from . import forms


def home(request):

    if request.method == 'POST':

        form = forms.InventoryForm(request.POST)
        if form.is_valid():
            capacity = form.cleaned_data['frames']
            products = form.cleaned_data['products']
            customers = form.cleaned_data['customers']
        else:
            return redirect('home')

        s = []
        for i in range(customers):
            s.append(random.randint(0,products-1))


        # FIFO

        f,fault,top= [],0,0

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

        PageFault_1 = fault
        FaultRate_1 = round((fault/len(s))*100,2)



        # Second Chance

        f,fault,front,pf = [],0,0,'Hit'
        bit = []


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

        PageFault_2 = fault
        FaultRate_2 = round((fault/len(s))*100,2)


        # LRU

        f,st,fault,pf = [],[],0,'No'
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

        PageFault_3 = fault
        FaultRate_3 = round((fault/len(s))*100,2)

        # Marking

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

        PageFault_4 = fault
        FaultRate_4 = round((fault/len(s))*100,2)

        data = {
                "label": ['FIFO','Second Chance', 'LRU', 'Marking'],
                "value": [FaultRate_1,FaultRate_2,FaultRate_3,FaultRate_4]

            }
        
        jsondata = json.dumps(data)

        form = forms.InventoryForm(initial={'frames':capacity,'products':products,'customers':customers})
        return render(request, 'home.html', {'form':form,
                                             'jsondata':jsondata,
                                             'PageFault_1':PageFault_1,
                                             'FaultRate_1':FaultRate_1,
                                             'PageFault_2':PageFault_2,
                                             'FaultRate_2':FaultRate_2,
                                             'PageFault_3':PageFault_3,
                                             'FaultRate_3':FaultRate_3,
                                             'PageFault_4':PageFault_4,
                                             'FaultRate_4':FaultRate_4,   
        })

    else:
        form = forms.InventoryForm()
        return render(request, 'home.html', {'form':form,
                                             'jsondata':{},
                                             'PageFault_1':0,
                                             'FaultRate_1':0,
                                             'PageFault_2':0,
                                             'FaultRate_2':0,
                                             'PageFault_3':0,
                                             'FaultRate_3':0,
                                             'PageFault_4':0,
                                             'FaultRate_4':0,   
        })