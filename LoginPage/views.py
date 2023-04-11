from django.shortcuts import render
from .forms import MyLoginForm

def Login(request):
    def Post_Info():
        if request.method == 'POST':
            form = MyLoginForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                pass
    is_mobile = False
    user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
    if 'mobile' in user_agent or 'android' in user_agent or 'iphone' in user_agent:
        is_mobile = True
    if is_mobile == True:
        Post_Info()
        return render(request, 'LoginPageMobile.html')
    else:
        Post_Info()
        return render(request, 'LoginPageMobile.html')