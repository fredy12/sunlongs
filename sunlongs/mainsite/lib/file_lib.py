'''
Created on 2015-9-16

@author: tongkai.ytk(ziyu) <tongkai.ytk@alibaba-inc.com>
'''
from mainsite.models import FileInfoForm, FileInfo
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        if 'media_type' not in request.POST:
            request.POST['media_type'] = 'image'
        form = FileInfoForm(request.POST, request.FILES)
        if form.is_valid():
            return form.save()


@csrf_exempt
def delete_file(request):
    file_id = request.POST['file_id']
    f = FileInfo.objects.get(id=file_id)
    f.delete()


@csrf_exempt
def edit_file(request):
    file_id = request.POST['file_id']
    f = FileInfo.objects.get(id=file_id)
    form = FileInfoForm(request.POST, instance=f)
    if form.is_valid():
        form.save()

