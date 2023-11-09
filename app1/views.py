from django.shortcuts import render
from .models import UserImage
from .forms import UserImageForm
# Create your views here.
def home(request):
    img = UserImage.objects.all()
    if request.method=='POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = UserImageForm()
    return render(request, 'home.html', {'img':img, 'form':form})