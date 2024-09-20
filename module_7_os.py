#coding: utf8
import os
import time

root_directory = os.getcwd()
directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(os.getcwd(), root, file)
        if r'\.\.' in filepath:
            filepath = filepath.replace('\.\.', '\.')
        else:
            filepath = filepath.replace('\.', '')
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.abspath(os.path.join(filepath, os.pardir))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
