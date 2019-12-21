from django.shortcuts import render
from django.utils import timezone
from .forms import EmpForm
from django.shortcuts import redirect
from django.contrib import messages

#def index(request):
 ##  return render(request, "index.html", {'form': Student})


def post_new(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            messages.success(request,'Message send successfully thank you for contacting us');
            return redirect('/')
    else:
        form = EmpForm()
    return render(request, 'contact.html', {'form': form})


