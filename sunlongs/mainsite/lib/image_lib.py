'''
Created on 2015-9-16

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''
from mainsite.models import ImageInfoForm, ImageInfo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        form = ImageInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()


@csrf_exempt
def delete_image(request):
    image_id = request.POST['image_id']
    image = ImageInfo.objects.get(id=image_id)
    image.delete()


@csrf_exempt
def edit_image(request):
    image_id = request.POST['image_id']
    image = ImageInfo.objects.get(id=image_id)
    form = ImageInfoForm(request.POST, instance=image)
    if form.is_valid():
        form.save()

