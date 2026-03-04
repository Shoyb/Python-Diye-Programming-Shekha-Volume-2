import os
import re
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

def create_directory(name):
    print('Creating directory')
    try:
        os.mkdir(name)
    except FileExistsError:
        print(name, "already exists")
        
def donwload_image(img_url, file_name):
    print("Donwloading image")
    try:
        response = requests.get(img_url)
    except:
        print('Image downloading error.')

    with open(file_name, 'wb') as f:
        f.write(response.content)
        

def get_directory_name(regex, url):
    result = re.findall(regex, url)
    if not result:
        return None
    dir_name = '-'.join(result[0])
    return dir_name

def process():
    main_dir = "dimik_pub"
    create_directory(main_dir)
    url = "https://web.archive.org/web/20230331200714/http://dimik.pub/"
    response = requests.get(url)
    if response.ok is False:
        sys.exit("Error")
    page_content = response.text
    
    regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><a.*?>(.*?)<', re.S)
    result = re.findall(regexp, page_content)
    
    regex = re.compile(r'/book/(\d+)/(\w+)-(\w+)-')
    
    for i in result:
        name = i[2]
        url = i[0]
        img_url = i[1]
        if get_directory_name(regex, url) is None:
            continue
        dir_name = main_dir + '/' + get_directory_name(regex, url)
        create_directory(dir_name)
        file_name = dir_name + '/' + 'info.txt'
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(name + '\n' + url)
        
        img_file_name = dir_name + '/' + '.png'
        donwload_image(img_url, img_file_name)
        
    
if __name__ == "__main__":
    process()
    print('Done')