import cloudconvert
import os
from io import StringIO
from django.conf import settings
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

api = cloudconvert.Api(
    'n0yudcTgpfqp9umtYY-2EG3IvuB25JqLTFUE4M1rlKLpA8eA7P6Qv2p2s6UyinBBO8vDrcX72dKjef8Xr5Ze8Q')

dist_path = os.path.join(settings.MEDIA_ROOT, 'slide/pdf/')

# input_file: local file location
def convert_and_download(input_file):
    # 绝对路径
    file_path = os.path.join(settings.MEDIA_ROOT, input_file.name)
    whole_filename = os.path.split(file_path)[-1]
    filename, file_extension = os.path.splitext(whole_filename)

    store_path = os.path.join(dist_path, whole_filename + '.pdf')
    print(store_path)

    process = api.convert({
        'inputformat': file_extension[1:],
        'outputformat': 'pdf',
        'input': 'upload',
        'file': open(file_path, 'rb')
    })
    print('waiting')
    process.wait()
    print('downloading')
    if not os.path.exists(dist_path):
        os.makedirs(dist_path)
    process.download(store_path)
    # pdf = open(store_path)
    return 'slide/pdf/' + whole_filename + '.pdf'
