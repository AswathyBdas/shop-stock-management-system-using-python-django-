from django.shortcuts import render
from sale import dbconnection
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
def index(request):
    return render(request,'index.html')
def admin(request):
    if request.method=="POST":
        e=request.POST.get("e")
        p=request.POST.get("p")
        sql="select * from admin where email='"+e+"' and password='"+p+"'"
        data=dbconnection.selectone(sql)
        if data:
           if data[4]=="admin":
              return HttpResponseRedirect("adminhome?id="+str(data[0]))
        else:
            msg="invalid username or password"
            return render(request,"admin.html",{"msg":msg})
    return render(request,'admin.html')
def adminhome(request):
    bid=request.GET['id']
    sql="select * from admin where id='"+bid+"'"
    d=dbconnection.selectone(sql)
    return render(request,"adminhome.html",{'d':d})
def staff(request):
    if request.method=="POST":
        n=request.POST.get("n")
        p=request.POST.get("p")
        sql="select * from addstaff where name='"+n+"' and password='"+p+"'"
        data=dbconnection.selectone(sql)
        if data:
           if data[9]=="staff":
        #    request.session['name']=n
            return HttpResponseRedirect("staffhome?id="+str(data[0]))
        else:
            msg="invalid username or password"
            return render(request,"staff.html",{"msg":msg})
    return render(request,'staff.html')
def client(request):
    if request.method=="POST":
        e=request.POST.get("e")
        p=request.POST.get("p")
        sql="select * from addclient where email='"+e+"' and password='"+p+"'"
        data=dbconnection.selectone(sql)
        if data:
           request.session['email']=e
           return HttpResponseRedirect("clienthome")
        else:
            msg="invalid username or password"
            return render(request,"client.html",{"msg":msg})
    return render(request,'client.html')
def customer(request):
    if request.method=="POST":
        e=request.POST.get("e")
        p=request.POST.get("p")
        sql="select * from addcustomer where email='"+e+"' and password='"+p+"'"
        data=dbconnection.selectone(sql)
        if data:
           request.session['email']=e
           return HttpResponseRedirect("customerhome")
        else:
            msg="invalid username or password"
            return render(request,"customer.html",{"msg":msg})
    return render(request,'customer.html')

def category(request):
    if request.method=="POST":
        ct=request.POST.get("ct")
        up=request.FILES["f"]
        fs=FileSystemStorage()
        fs.save("sale/static/upload/"+up.name,up)
        sql="select * from addcategory where category='"+ct+"' and image='"+up.name+"'"
        d=dbconnection.selectone(sql)
        if d:
            return render(request,'category.html',{'message':'Already exists'})
        sql1="insert into addcategory(category,image)values('"+ct+"','"+up.name+"')"
        dbconnection.insert(sql1)
        return HttpResponseRedirect('category')
    sql2="select * from addcategory"
    data=dbconnection.selectall(sql2)
    return render(request,'category.html',{"data":data})
        # return HttpResponseRedirect('category')
    
def subcategory(request):
    if request.method=="POST":
        ct=request.POST.get("ct")
        sc=request.POST.get("sc")
        sql="select * from addsubcategory where subcategory='"+sc+"'"
        d=dbconnection.selectone(sql)
        if d:
            return render(request,'subcategory.html',{'message':'Already exists'})
        sql1="insert into addsubcategory(category,subcategory)values('"+ct+"','"+sc+"')" 
        dbconnection.insert(sql1)
        return HttpResponseRedirect('subcategory')
    sql="select * from addsubcategory"
    data=dbconnection.selectall(sql)
    return render(request,'subcategory.html',{"data":data})
def addclient(request):
    if request.method=="POST":
        n=request.POST.get("n")
        e=request.POST.get("e")
        p=request.POST.get("p")
        s=request.POST.get("s")
        m=request.POST.get("m")
        up=request.FILES["f"]
        fs=FileSystemStorage()
        fs.save("sale/static/upload/"+up.name,up)
        sql1="insert into addclient(name,email,password,state,mobno,logo)values('"+n+"','"+e+"','"+p+"','"+s+"','"+m+"','"+up.name+"')"
        dbconnection.insert(sql1)
        return HttpResponseRedirect('addclient')
    sql="select * from addclient"
    data=dbconnection.selectall(sql)
    return render(request,'addclient.html',{'data':data})
def addstaff(request):
    if request.method=="POST":
        n=request.POST.get("n")
        e=request.POST.get("e")
        p=request.POST.get("p")
        g=request.POST.get("g")
        a=request.POST.get("a")
        mo=request.POST.get("mo")
        pl=request.POST.get("pl")
        up=request.FILES["f"]
        fs=FileSystemStorage()
        fs.save("sale/static/upload/"+up.name,up)
        sql1="insert into addstaff(name,email,password,gender,age,mobno,place,photo)values('"+n+"','"+e+"','"+p+"','"+g+"','"+a+"','"+mo+"','"+pl+"','"+up.name+"')"
        dbconnection.insert(sql1)
        return HttpResponseRedirect('addstaff')
    sql="select * from addstaff"
    d=dbconnection.selectall(sql)
    return render(request,'addstaff.html',{'d':d})
def staffhome(request):
    bid=request.GET['id']
    sql="select * from addstaff where id='"+bid+"'"
    d=dbconnection.selectone(sql)
    return render(request,'staffhome.html',{'d':d})
def customerhome(request):
    return render(request,'customerhome.html')
def addcustomer(request):
    if request.method=="POST":
        n=request.POST.get("n")
        e=request.POST.get("e")
        p=request.POST.get("p")
        m=request.POST.get("m")
        g=request.POST.get("g")
        sql1="insert into addcustomer(name,email,password,mobno,gender)values('"+n+"','"+e+"','"+p+"','"+m+"','"+g+"')"
        dbconnection.insert(sql1)
        return HttpResponseRedirect('addcustomer')
    return render(request,'addcustomer.html')
def stock(request):
    return render(request,'stock.html')
def addstock(request):
    # sql1="select * from addcategory"
    # data=dbconnection.selectall(sql1)
    # sql2="select * from addsubcategory"
    # d=dbconnection.selectall(sql2)
    # sql3="select * from addclient"
    # da=dbconnection.selectall(sql3)
    # if request.method=="POST":
    #     ct=request.POST.get("ct")
    #     sc=request.POST.get("sc")
    #     cl=request.POST.get("cl")
    #     qu=request.POST.get("qu")
    #     sql1="insert into addstock(category,subcategory,client,quantity)values('"+ct+"','"+sc+"','"+cl+"','"+qu+"')"
    #     dbconnection.insert(sql1)                    
    # return render(request,'addstock.html',{"data":data,"d":d,"da":da})
    return render(request,'addstock.html')
def currentstock(request):
    sql="select * from current"
    data=dbconnection.selectall(sql)
    return render(request,'currentstock.html',{'data':data})
def updatestock(request):
    if request.method=="POST":
        import datetime
        ct=request.POST.get("ct")
        sc=request.POST.get("sc")
        cl=request.POST.get("cl")
        qu=request.POST.get("qu")
        sg=request.POST.get("sg")
        tm=request.POST.get("tm")
        pm=request.POST.get("pm")
        date=str(datetime.date.today())
        b=int(tm)-int(pm)
        sql3="insert into updatestock(category,subcategory,client,quantity,single,tamount,pamount,balance,date)values('"+ct+"','"+sc+"','"+cl+"','"+qu+"','"+sg+"','"+str(tm)+"','"+str(pm)+"','"+str(b)+"','"+str(date)+"')"
        dbconnection.insert(sql3)
        sql11="select * from updatestock"
        d1=dbconnection.selectone(sql11)
        q=d1[4]
        nwq=int(q)+int(qu)
        sql4="select * from current where subcategory='"+sc+"'"
        d3=dbconnection.selectone(sql4)
        if d3:
            sql6="update current set quantity='"+str(nwq)+"'where subcategory='"+sc+"'"
            dbconnection.update(sql6)
        else:
            sql7="insert into current(category,subcategory,client,quantity)values('"+ct+"','"+sc+"','"+cl+"','"+qu+"')"
            dbconnection.insert(sql7)
            return HttpResponseRedirect("updatestock")
    sql="select * from addcategory"
    data=dbconnection.selectall(sql)
    sql1="select * from addsubcategory"
    d=dbconnection.selectall(sql1)
    sql2="select * from addclient"
    da=dbconnection.selectall(sql2)
    return render(request,'updatestock.html',{"data":data,"d":d,"da":da})
def emptystock(request):
    sql="select * from updatestock where quantity<5"
    d=dbconnection.selectall(sql)
    return render(request,'emptystock.html',{'d':d})
def checkout(request):
    return render(request,'checkout.html')
def saleassign(request):
    bid=request.GET['id']
    sql="select * from addstaff where id='"+bid+"'"
    d=dbconnection.selectone(sql)
    sn=d[1]
    if request.method=="POST":
        a=request.POST.get("a")
        t=request.POST.get("t")
        sql="insert into target(name,target,balance)values('"+sn+"','"+t+"','0')"
        dbconnection.insert(sql)
    sql="select * from addsubcategory"
    d=dbconnection.selectall(sql)
    return render(request,'saleassign.html',{"d":d,"sn":sn})
def target(request):
    bid=request.GET['id']
    sql="select * from addstaff where id='"+bid+"'"
    d=dbconnection.selectone(sql)
    u=d[1]
    p=d[3]
    sql1="select* from target where name='"+u+"' and password='"+p+"'"
    d1=dbconnection.selectall(sql1)
    sql2="select * from addstaff  where name='"+u+"' and password='"+p+"'"
    d2=dbconnection.selectall(sql2)
    return render(request,'target.html',{"d":d,'d1':d1,'d2':d2})
def billing1(request):
    bid=request.GET['id']
    sql="select * from admin where id='"+bid+"'"
    d=dbconnection.selectone(sql)
    if bid=='1':
        u="admin"
        pa=d[2]
    else:
        u=d[1]
        pa=d[2]
    import datetime,random
    date=datetime.date.today()
    if request.method=="POST":
        c=request.POST.get('c')
        p=request.POST.get('p')
        bn=random.randrange(1000,2000)
        newbn="BL"+str(bn)
        sql="insert into billgenerate(billno,customername,phonenumber,date,amount,staffdealed,password)values('"+str(newbn)+"','"+c+"','"+p+"','"+str(date)+"','0','"+u+"','"+pa+"')"
        dbconnection.insert(sql)
        sql1="select * from billgenerate order by billid DESC"
        d=dbconnection.selectone(sql1)
        return HttpResponseRedirect("bill1?id="+str(d[0]))
    sql2="select * from addcustomer"
    ds=dbconnection.selectall(sql2)
    return render(request,'billing1.html',{'ds':ds})
def billing2(request):
    bid=request.GET['id']
    sql="select * from addstaff where id='"+bid+"'"
    d=dbconnection.selectone(sql)
    if bid=='1':
        u="staff"
        pa=d[2]
    else:
        u=d[1]
        pa=d[2]
    import datetime,random
    date=datetime.date.today()
    if request.method=="POST":
        c=request.POST.get('c')
        p=request.POST.get('p')
        bn=random.randrange(1000,2000)
        newbn="BL"+str(bn)
        sql="insert into billgenerate(billno,customername,phonenumber,date,amount,staffdealed,password)values('"+str(newbn)+"','"+c+"','"+p+"','"+str(date)+"','0','"+u+"','"+pa+"')"
        dbconnection.insert(sql)
        sql1="select * from billgenerate order by billid DESC"
        d=dbconnection.selectone(sql1)
        return HttpResponseRedirect("bill2?id="+str(d[0]))
    sql2="select * from addcustomer"
    ds=dbconnection.selectall(sql2)
    return render(request,'billing2.html',{'ds':ds})
def bill1(request):
    bid=request.GET["id"]
    sql="select * from billgenerate where billid='"+bid+"'"
    d=dbconnection.selectone(sql)
    b=d[1]
    sql9="select * from billgenerate where billid='"+bid+"'"
    d=dbconnection.selectone(sql9)
    d=d[1]
    import datetime,random
    date=datetime.date.today()
    if request.method=="POST":
        p=request.POST.get('p')
        q=request.POST.get('q')
        pr=request.POST.get('pr')
        t=int(q)*int(pr)
        sql1="insert into bill1(billid,date,billno,product,quantity,price,totalprice)values('"+bid+"','"+str(date)+"','"+b+"','"+p+"','"+q+"','"+pr+"','"+str(t)+"')"
        dbconnection.insert(sql1)
        sql="select * from billgenerate where billid='"+bid+"'"
        data=dbconnection.selectone(sql)
        cr=data[5]
        n=int(t)
        ta=int(cr)+int(n)
        ta1=str(ta)
        sql3="update billgenerate set amount='"+str(ta1)+"' where billid='"+bid+"'"
        dbconnection.update(sql3)
        sql2="select * from bill1 where billid='"+bid+"'"
        d1=dbconnection.selectall(sql2)
        sql7="select * from billgenerate where billid='"+bid+"'"
        d2=dbconnection.selectall(sql7)
        sql4="select * from billgenerate where billid='"+bid+"'"
        d3=dbconnection.selectone(sql4)
        sql5="select * from current where subcategory='"+p+"'"
        data4=dbconnection.selectone(sql5)
        se=data4[4]
        r=int(se)-int(q)
        sql8="update current set quantity='"+str(r)+"' where subcategory='"+p+"'"
        de=dbconnection.update(sql8)
        return render(request,'bill1.html',{'d1':d1,'d2':d2,'d3':d3,'de':de,'data4':data4})
    sql6="select * from current"
    d8=dbconnection.selectall(sql6)
    return render(request,'bill1.html',{'d8':d8})
    
def bill2(request):
    bid=request.GET["id"]
    sql="select * from billgenerate where billid='"+bid+"'"
    d=dbconnection.selectone(sql)
    b=d[1]
    sql1="select * from billgenerate where billid='"+bid+"'"
    d=dbconnection.selectone(sql1)
    d=d[1]
    import datetime,random
    date=datetime.date.today()
    if request.method=="POST":
        p=request.POST.get('p')
        q=request.POST.get('q')
        pr=request.POST.get('pr')
        t=int(q)*int(pr)
        sql1="insert into bill1(billid,date,billno,product,quantity,price,totalprice)values('"+bid+"','"+str(date)+"','"+b+"','"+p+"','"+q+"','"+pr+"','"+str(t)+"')"
        dbconnection.insert(sql1)
        sql="select * from billgenerate where billid='"+bid+"'"
        data=dbconnection.selectone(sql)
        cr=data[5]
        n=int(t)
        ta=int(cr)+int(n)
        ta1=str(ta)
        sql3="update billgenerate set amount='"+str(ta1)+"' where billid='"+bid+"'"
        dbconnection.update(sql3)
        sql2="select * from bill1 where billid='"+bid+"'"
        d1=dbconnection.selectall(sql2)
        sql7="select * from billgenerate where billid='"+bid+"'"
        d2=dbconnection.selectall(sql7)
        sql4="select * from billgenerate where billid='"+bid+"'"
        d3=dbconnection.selectone(sql4)
        sql5="select * from current where subcategory='"+p+"'"
        data4=dbconnection.selectone(sql5)
        se=data4[4]
        r=int(se)-int(q)
        sql8="update current set quantity='"+str(r)+"' where subcategory='"+p+"'"
        de=dbconnection.update(sql8) 
        return render(request,'bill2.html',{'d1':d1,'d2':d2,'d3':d3,'de':de,'data4':data4})
    sql6="select * from current"
    d55=dbconnection.selectall(sql6)
    return render(request,'bill2.html',{'d55':d55})
def sale(request):
    sql="select * from bill1"
    d=dbconnection.selectall(sql)
    return render(request,'sale.html',{'d':d})                        
def details(request):
    bid=request.GET['id']
    sql1="select * from bill1 where billid='"+bid+"'"
    d=dbconnection.selectall(sql1)
    sql2="select * from billgenerate where billid='"+bid+"'"
    d1=dbconnection.selectall(sql2)
    sql3="select * from billgenerate where billid='"+bid+"'"
    d3=dbconnection.selectone(sql3)
    if d3[6]=="admin":
        u="admin"
    else:
        u="staff"
    return render(request,'details.html',{'d':d,'d1':d1,'d3':d3,'u':u})
def topcustomer(request):
    sql="select * from billgenerate"
    d=dbconnection.selectall(sql)
    sql2="select * from billgenerate"
    d2=dbconnection.selectone(sql2)
    b=d2[0]
    sql1="select * from bill1 where billid='"+str(b)+"'"
    d1=dbconnection.selectone(sql1)
    sql2="select * from billgenerate order by price ASC"
    d2=dbconnection.selectone(sql2)
    return render(request,'topcustomer.html',{'d':d,'d1':d1,'d2':d2})
def clientpayment(request):
    sql="select * from updatestock"
    d=dbconnection.selectall(sql)
    return render(request,'clientpayment.html',{'d':d}) 
def mypurchase(request):
    return render(request,'mypurchase.html')
    




