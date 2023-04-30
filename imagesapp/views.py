from django.shortcuts import render
from . forms import ImageForm
from . models import Image
# Create your views here.

'''working files are setting.py,url.py,images.html,forms.py,models.py and views.py and media also which is external folder where django looked for images'''
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)#request.FILES is mandatory while working with image uploader
        if form.is_valid():
            form.save()

    form = ImageForm()
    imgs = Image.objects.all()
    return render(request,'imagesapp/images.html',{'form':form,'imgs':imgs})