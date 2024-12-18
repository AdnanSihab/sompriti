from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/register.html', context)

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return



# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from .forms import RegistrationForm

# # Register View
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])  # Hash the password
#             user.save()
#             messages.success(request, "Account created successfully. You can now log in.")
#             return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'accounts/register.html', {'form': form})

# # Login View
# def user_login(request):
#     if request.method == 'POST':
#         user = authenticate(
#             request, 
#             username=request.POST['username'], 
#             password=request.POST['password']
#         )
#         if user:
#             login(request, user)
#             return redirect('home')
#         messages.error(request, "Invalid credentials")
#     return render(request, 'accounts/login.html')

# # Logout View
# def user_logout(request):
#     logout(request)
#     return redirect('login')

