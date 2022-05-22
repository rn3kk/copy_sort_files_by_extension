import datetime
import glob
import os
import shutil
import traceback
import uuid

path_sort = 'd:\видео_сортированные'
path = 'd:\фотографии'
if __name__ == '__main__':

    extensions = []
    for file in glob.iglob(path + '/**/*.3gp', recursive=True):
        file_extension = os.path.splitext(file)[1]
        extensions.append(file_extension)
        t = os.path.getmtime(file)
        dt = datetime.datetime.fromtimestamp(t)
        y = str(dt)[:4]
        m = str(dt)[5:7]

        p = path_sort + '\\' + y + '\\' + m + '\\' + str(uuid.uuid1()) + file_extension
        try:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            shutil.copy(file, p)
            print(file, 'DONE')
        except Exception as e:
            print('Exception copy', file, 'to', p)
            traceback.print_stack()
    print(list(set(extensions)))



