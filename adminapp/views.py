from django.shortcuts import render,redirect
from adminapp.models import CategoryDb,ProductDb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

import datetime

from webapp.models import ContactDb

# Create your views here.

def index(request):
    date = datetime.datetime.now()
    product = ProductDb.objects.count()
    cate = CategoryDb.objects.count()
    return render(request,"index.html",{'date':date,'product':product,'cate':cate})

def add_category(request):
    return render(request,"add_category.html")

def save_category(request):
    if request.method == "POST":
        cn = request.POST.get('cname')
        des = request.POST.get('desc')
        im = request.FILES['img']
    obj = CategoryDb(Category=cn,Description=des,Image=im)
    obj.save()
    messages.success(request,"Category saved!")

    return redirect(add_category)

def display_category(request):

        cat = CategoryDb.objects.all()

        return render(request, "display_category.html", {'cat': cat})

def edit_category(request,cat_id):
    cat = CategoryDb.objects.get(id=cat_id)

    return render(request,"edit_category.html",{'cat':cat})

def update_category(request,cat_id):
    if request.method == "POST":
        cn = request.POST.get('cname')
        des = request.POST.get('desc')

        try:
            im = request.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)

        except MultiValueDictKeyError:

            file = CategoryDb.objects.get(id=cat_id).Image

        CategoryDb.objects.filter(id=cat_id).update(Category=cn,Description=des,Image=file)
        messages.success(request, "Category saved!")

        return redirect(display_category)

def delete_category(request,cat_id):

        dlt = CategoryDb.objects.filter(id=cat_id)
        dlt.delete()
        messages.error(request,"Category deleted")
        return redirect(display_category)





def add_product(request):
    cat = CategoryDb.objects.all()
    messages.success(request, "Product saved!")

    return render(request,"add_products.html",{'cat':cat})

def save_product(request):
        if request.method == "POST":
            cat = request.POST.get('category')
            pro = request.POST.get('pname')
            qn = request.POST.get('qty')
            mrp = request.POST.get('amt')
            cn = request.POST.get('cntry')
            mn = request.POST.get('manu')
            ds = request.POST.get('desc')
            im1 = request.FILES['img1']
            im2 = request.FILES['img2']
            im3 = request.FILES['img3']

            obj = ProductDb(category=cat, Product=pro, Quantity=qn, Price=mrp, Country=cn, Manufacture=mn, Description=ds, Image1=im1,Image2=im2,Image3=im3)
            obj.save()
            messages.success(request, "Product saved!")

            return redirect(add_product)


def display_product(request):
    prod = ProductDb.objects.all()

    return render(request,"display_product.html",{'prod':prod})


def edit_product(request,prod_id):
    cat = CategoryDb.objects.all()
    prod = ProductDb.objects.get(id=prod_id)

    return render(request,"edit_product.html",{'prod':prod,'cat':cat})

def update_product(request,prod_id):
    if request.method == "POST":
        cat = request.POST.get('category')
        pro = request.POST.get('pname')
        qn = request.POST.get('qty')
        mrp = request.POST.get('amt')
        cn = request.POST.get('cntry')
        mn = request.POST.get('manu')
        ds = request.POST.get('desc')

        try:
            im1 = request.FILES['img1']
            fs = FileSystemStorage()
            file1 = fs.save(im1.name,im1)

        except MultiValueDictKeyError:

            file1 = ProductDb.objects.get(id=prod_id).Image1

        try:
            im2 = request.FILES['img2']
            fs = FileSystemStorage()
            file2 = fs.save(im2.name, im2)

        except MultiValueDictKeyError:

            file2 = ProductDb.objects.get(id=prod_id).Image2

        try:
            im3 = request.FILES['img3']
            fs = FileSystemStorage()
            file3 = fs.save(im3.name, im3)

        except MultiValueDictKeyError:

            file3 = ProductDb.objects.get(id=prod_id).Image3

        ProductDb.objects.filter(id=prod_id).update(category=cat, Product=pro, Quantity=qn, Price=mrp, Country=cn, Manufacture=mn, Description=ds,
                        Image1=file1, Image2=file2, Image3=file3)


        return redirect(display_product)




def delete_product(request,prod_id):
    dlt = ProductDb.objects.filter(id=prod_id)
    dlt.delete()
    return redirect(display_product)

def admin_login(request):
    return render(request,"admin_login.html")

def login_admin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pswd = request.POST.get('pass')

        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pswd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pswd
                messages.success(request,"welcome!")

                return redirect(index)
            else:
                messages.warning(request,"Invalid Username!")

                return redirect(admin_login)
        else:
            messages.error(request, "Please check your password!")

            return redirect(admin_login)

def admin_logout(request):

    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def contact_data(request):
    data = ContactDb.objects.all()
    return render(request,"contact_data.html",{'data':data})

def delete_contact(request,c_id):
    dlt = ContactDb.objects.filter(id=c_id)
    dlt.delete()
    return redirect(contact_data)

