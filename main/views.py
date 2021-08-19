import os
from django.shortcuts import render
import pandas as pd
import pickle
from django.contrib import messages
from django.conf import settings
# Create your views here.
def home(request):
    context={}
    if request.method=='POST':
        manufacturer=request.POST["manufacturer"]
        category=request.POST["category"]
        screensize=request.POST["screen_size"]
        screen=request.POST["screen_res"]
        cpu_model=request.POST["cpu"]
        ram=request.POST["ram"]
        storage=request.POST["storage"]
        gpu=request.POST["gpu"]
        weight=request.POST["weight"]
        operating_sys=request.POST["os_val"]
        price=request.POST["price"]
        price_path=os.path.join(settings.MEDIA_ROOT,'main/LRModel_price.pkl')
        sales_path=os.path.join(settings.MEDIA_ROOT,'main/LRModel_sales.pkl')

        with open(price_path,'rb') as f:
            mp = pickle.load(f)

            prediction = mp.predict(pd.DataFrame([[manufacturer,category,screensize,screen, cpu_model,ram,storage,gpu,operating_sys,weight]],columns=['Manufacturer','Category','Screen Size','Screen','CPU','RAM','Storage','GPU','Operating System','Weight']))
            messages.success(request,"Laptop can be Priced around: Rs."+str(int(prediction[0])))
        with open(sales_path,'rb') as f:
            sales_mp=pickle.load(f)
            prediction = sales_mp.predict(pd.DataFrame([[manufacturer,category,screensize,screen, cpu_model,ram,storage,gpu,operating_sys,weight,price]],columns=['Manufacturer','Category','Screen Size','Screen','CPU','RAM','Storage','GPU','Operating System','Weight','Price']))
            messages.success(request,"Predicted Laptop sales are (in units sold): "+str(int(prediction[0])))
    path=os.path.join(settings.MEDIA_ROOT,'main/price_dataset.csv')
    laptop=pd.read_csv(path)
    manufacturer = sorted(laptop['Manufacturer'].unique())
    category = sorted(laptop['Category'].unique())
    screen_size=sorted(laptop['Screen Size'].unique())
    screen = sorted(laptop['Screen'].unique())
    cpu=sorted(laptop['CPU'].unique())
    ram = sorted(laptop['RAM'].unique())
    storage = sorted(laptop['Storage'].unique())
    gpu = sorted(laptop['GPU'].unique())
    os_name = sorted(laptop['Operating System'].unique())
    weight = sorted(laptop['Weight'].unique())
    context={'manufacturers':manufacturer,'categories':category,'screen_sizes':screen_size,'screen_res':screen,'cpus':cpu,'ram':ram,'storage':storage,'gpu':gpu,'os_name':os_name,'weight':weight}
    
    
    return render(request,'main/home.html',context=context)