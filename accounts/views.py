from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages

def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # user = form.save(commit=False)
            # password = form.cleaned_data['password']
            # user.set_password(password)  # This hashes the password
            # user.role = User.CUSTOMER
            # user.save()
            # messages.success(request, 'User registered successfully.')

            #create the user using create_user method
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password = form.cleaned_data['password']
            user=User.objects.create_user(first_name=first_name, last_name=last_name,username=username,email=email,password=password)  
            user.role = User.CUSTOMER    
            user.save()       
            messages.success(request, 'User registered successfully.')
            return redirect('registerUser')  # Redirect to the same page or another page
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)