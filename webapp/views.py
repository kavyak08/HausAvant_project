from django.shortcuts import render,redirect
from adminapp.models import ProductDb,CategoryDb
from webapp.models import ContactDb,SignupDb,CartDb,OrderDb
from django.contrib import messages
import razorpay

# Create your views here.
def home(request):
    categories = CategoryDb.objects.all()

    cart = CartDb.objects.filter(Username=request.session['Name']).count()
    return render(request,"home.html",{'categories':categories,'cart':cart})

def products_page(request):
    products = ProductDb.objects.all()
    return render(request,"products_page.html",{'products':products})

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")


def blog(request):
    return render(request,"blog.html")


def contact(request):
    return render(request,"contact.html")

def save_contact(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        mb = request.POST.get('mob')
        em = request.POST.get('email')
        ms = request.POST.get('mes')

    obj = ContactDb(Name=nm,Mobile=mb,Email=em,Message=ms)
    obj.save()

    return redirect(contact)

def product_filter(request,cat_name):
    data = ProductDb.objects.filter(category=cat_name)
    return render(request,"products_filter.html",{'data':data})

def single_product(request,pro_id):
    data = ProductDb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data})

def sign_up(request):

    return render(request,"signup.html")

def log_in(request):

    return render(request,"login.html")


def save_signup(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        mb = request.POST.get('mobile')
        em = request.POST.get('email')
        ps = request.POST.get('pass')
        rps = request.POST.get('re_pass')

    obj = SignupDb(Name=nam,Mobile=mb,Email=em,Password=ps,Rpassword=rps)


    if SignupDb.objects.filter(Name=nam).exists():
        messages.warning(request, "User Already Exists..")
        return redirect(sign_up)
    elif SignupDb.objects.filter(Email=em).exists():
        messages.warning(request,"Email address Already exists...!")
        return redirect(sign_up)

    obj.save()

    return redirect(log_in)

def user_login(request):
    if request.method == "POST":
        un = request.POST.get('name')
        pswd = request.POST.get('pass')
        if SignupDb.objects.filter(Name=un,Password=pswd).exists():
            request.session['Name'] = un
            request.session['Password'] = pswd
            messages.success(request,"welcome")

            return redirect(home)
        else:
            messages.warning(request, "Invalid Username!")

            return redirect(log_in)
    else:
        messages.error(request, "Please check your password!")

        return redirect(log_in)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    messages.success(request, "Successfully logged out")

    return redirect(home)

def save_cart(request):
    if request.method == "POST":
        nam = request.POST.get('name')
        qn = request.POST.get('qty')
        prc = request.POST.get('mrp')
        tprc = request.POST.get('tmrp')
        prod = request.POST.get('pro')

    obj = CartDb(Username=nam,Quantity=qn,Price=prc,Total_price=tprc,Product_name=prod)
    obj.save()



    return redirect(home)


def cart_page(request):
    data = CartDb.objects.filter(Username=request.session['Name'])

    subtotal = 0
    shipping_amount = 0
    total_amount = 0

    for i in data:
        subtotal=subtotal + i.Total_price

        if subtotal>50000:
            shipping_amount = 1000
        else:
            shipping_amount = 2000

        total_amount = shipping_amount + subtotal

    return render(request,"cart_page.html",{'data':data, 'subtotal':subtotal, 'shipping_amount':shipping_amount,
                                            'total_amount':total_amount})





def remove_product(request,prod_id):
    dlt = CartDb.objects.filter(id=prod_id)
    dlt.delete()

    return redirect(cart_page)

def checkout_page(request):
    cart = CartDb.objects.filter(Username=request.session['Name'])

    subtotal = 0
    shipping_amount = 0
    total_amount = 0

    for i in cart:
        subtotal = subtotal+i.Total_price

        if subtotal > 50000:
            shipping_amount = 1000
        else:
            shipping_amount = 2000

        total_amount = shipping_amount + subtotal

    return render(request, "checkout.html", {'cart': cart, 'subtotal': subtotal, 'shipping_amount': shipping_amount,
                                              'total_amount': total_amount})





def save_order(request):
    if request.method == "POST":
        nam = request.POST.get('c_fname')
        em = request.POST.get('email')
        phn = request.POST.get('phone')
        adrs = request.POST.get('c_address')
        plc = request.POST.get('place')
        pin = request.POST.get('pincode')
        tp = request.POST.get('total')
        msg = request.POST.get('c_order_notes')
        obj = OrderDb(Name=nam, Email=em, Mobile=phn, Total_price=tp, Address=adrs, Place=plc,Postal=pin, Message=msg)
        obj.save()


    return redirect(checkout_page)



def payment_page(request):
    #Retrieve the data from OrderDb with specified ID
    customer = OrderDb.objects.order_by('-id').first()

    #Get payment amount of the specufied customer
    payy = customer.Total_price


    #Convert the amount into paisa
    amount = int(payy*100)

    payy_str = str(amount)


    for i in payy_str:
        print(i)

        if request.method == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_RNRcEXvnVcvUjY','zelmaSU2MH4xbjOF1aVX0m4m'))
            payment = client.order.create({'amount':amount,'currency':order_currency})

    return render(request,"payment.html",{'customer':customer,'payy_str':payy_str})