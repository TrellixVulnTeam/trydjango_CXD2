from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.
def home_view(request,*args,**kwargs):
  print(args,kwargs)
  print(request.user)	
  return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
   return render(request,"contact.html",{})

def about_view(request,*args,**kwargs):
   my_context={
   "my_text":"This is about us",
    "this_is_true":True,
    "my_number":123,
    "my_list":[1313,4231,312,"Abc"]

   }
   

   return render(request,"about.html",my_context)

def social_view(request,*args,**kwargs):
   return render(request,"social.html",{})
