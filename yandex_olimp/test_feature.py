import os
import time

path = '/media/urik/0c4b8c2e-70df-4fcb-8f32-e40c12632d2d/@home/yuriy/Docum/Books about programming'
path_normalized = os.path.normpath(path)
print(path_normalized)

count = 0
for dir_path, dir_names, file_names in os.walk(path_normalized):
    # print('*' * 27)
    # print(dir_path, dir_names, file_names)
    # print(os.path.dirname(dir_path))
    count += len(file_names)
    for file in file_names:
        full_file_path = os.path.join(dir_path, file)
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        if file_time[0] == 2019 and file_time[1] == 5:
            # выводим только файлы за 2013 год
            print(file)
print(count)


print(__file__, os.path.dirname(__file__))