from django.urls import path
from webapp import views

urlpatterns = [
     path('home/',views.home,name="home"),
     path('products_page/',views.products_page,name="products_page"),
     path('about/',views.about,name="about"),
     path('services/',views.services,name="services"),
     path('blog/',views.blog,name="blog"),
     path('contact/',views.contact,name="contact"),
     path('save_contact/',views.save_contact,name="save_contact"),
     path('product_filter/<cat_name>/',views.product_filter,name="product_filter"),
     path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
     path('sign_up/',views.sign_up,name="sign_up"),
     path('',views.log_in,name="log_in"),
     path('save_signup/',views.save_signup,name="save_signup"),
     path('user_login/',views.user_login,name="user_login"),
     path('user_logout/',views.user_logout,name="user_logout"),
     path('save_cart/',views.save_cart,name="save_cart"),
     path('cart_page/',views.cart_page,name="cart_page"),
     path('checkout_page/',views.checkout_page,name="checkout_page"),
     path('remove_product/<int:prod_id>/',views.remove_product,name="remove_product"),
     path('save_order/', views.save_order, name="save_order"),
     path('payment_page/', views.payment_page, name="payment_page"),

]
