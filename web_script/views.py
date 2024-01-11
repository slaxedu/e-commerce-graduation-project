from django.template.defaultfilters import slugify
from django.shortcuts import render
from items.models import Product, Category, Brand, Review
from account.models import CustomUser
import re
import random
from django.http import HttpResponse

import requests 
from bs4 import BeautifulSoup
import csv
import string
details = """Display Size	6.1 inches
Display Resolution	828x1792
Touch Screen	Yes
Processor CPU	Hexa-core
INTERNAL STORAGE	128 GB
Memory RAM	4 GB
Operating System	IOS
Operating System Version	IOS 13
OPERATING SYSTEM	iOS
Main Camera	12 MP + 12 MP
Selfie Camera	12 MP
Video Recording Type	2160p@24/30/60fps
Network Type	2G, 3G, 4G
SIM Card	Single SIM
SIM Card	Single SIM
SIM Type	Nano SIM
Product Color	Black
WiFi	Yes
Bluetooth	Yes
Battery capacity	3110 mAh battery
Weight	150 g"""

# details = """Laptop Category	Gaming
# Processor	AMD
# Graphics Card	NVIDIA® GeForce RTX
# RAM	32GB
# Hard Disk Capacity	1TB
# Display Size	16 inches
# Operating System	Windows
# """



def web(request):

    # url = "https://dream2000.com/en/mobiles.html?product_list_limit=100"
    # response = requests.get(url)

    # if response.status_code == 200:
    #     soup = BeautifulSoup(response.content, 'html.parser')

    #     products = soup.find_all("div", {'class': 'product-item-info'})

    #     for index, product in enumerate(products, start=1):
    #         try:
    #             product_title = product.find('a', {'class': 'product-item-link'}).text.strip()
    #             product_price = product.find('span', {'class': 'special-price'}).find('span', {'class': 'price'}).text.strip()

    #             # Check if 'img' tag has 'src' attribute
    #             product_image_tag = product.find('img', {'class': 'product-image-photo'})
    #             product_image = product_image_tag['data-src'] if product_image_tag and 'src' in product_image_tag.attrs else 'Image not found'
    #             print(product_image_tag['data-src'])
    #             print(f"Product {index}:")
    #             print(f"Title: {product_title}")
    #             print(f"Price: {product_price}")
    #             print(f"Image: {product_image}")
    #             print("-" * 30)
    #         except Exception as e:
    #             print(f"Error processing product {index}: {e}")

    # else:
    #     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")



    # cat = Category.objects.get(category_name='Mobiles & Tablets')
    # # cat = Category.objects.all()
    # # br = Brand.objects.get(name='Apple')
    # br = Brand.objects.all()

    # print(br)
    # product = Product.objects.all().order_by('id')
    # j = 1
    # for i in product:
    #     Product.objects.filter(id=i.id).update(count=j)
    #     print(j)
    #     j+=1

    # page = requests.get("https://dream2000.com/en/mobiles.html?_=1704508154879&p=3&product_list_limit=100")
    # # page = requests.get("https://dream2000.com/en/mobiles.html?product_list_limit=100")
    # # page = requests.get("https://dream2000.com/en/mobiles.html?_=1704506553979&p=2&product_list_limit=100")
    # page = requests.get("https://dream2000.com/en/tablets.html?product_list_limit=100")
    
    # def main(page, k):
        
    #     print("main####################")
    #     scr = page.content
    #     soup = BeautifulSoup(scr, 'lxml')
    #     product_details = []
    #     products = soup.find_all("div", {'class': 'product-item-info'})
    #     # print(products)
    #     dict_list  = []
    #     # print(product)
        
    #     def get_product_info(product, k):
    #         product_title = product.find('a', {'class': 'product-item-link'}).text.strip()
    #         product_photo = product.find('img', {'class': 'product-image-photo'})['data-src']
    #         product_price = product.find('span', {'class': 'special-price'}).find('span', {'class': 'price'}).text.strip()
    #         print("################################################")
    #         print(product_title)
    #         print(product_photo)
    #         print(product_price)
    #         print("################################################")
    #         out = re.findall(r'\d+\.\d+', product_price)
    #         float_value = float(out[0])
    #         dict_list.append({'name':product_title, 'image':product_photo, 'price': product_price})

    #         print(f"TSSSSSSSSSSSSSS {product_photo}")
    #         img_data = requests.get(f"{product_photo}").content
    #         with open(f"B:\\BOOK\Graduation Project\\New folder (2)\media\image\product\\another\\phone{k}.jpg", 'wb') as handler:
    #             handler.write(img_data)
    #             k+=1
    #         prod = Product.objects.create(
    #             name= product_title,
    #             description= details,
    #             # image = 'https://dream2000.com/media/catalog/product/cache/f0c876fc5fd423dc009b2416a0e65966/s/a/samsung-a53-5g-_8_128_-awesome-black-1.jpg',
    #             image = f'image\product\\another\\phone{k}.jpg',
    #             category_id =  cat, 
    #             price = float_value,
    #             quantity_in_stock = 100,
    #             # brand_id = br,
    #             slug = slugify(product_title)
    #         )
    #     print("main####################")
    #     for i in products:
    #         k +=1
    #         print("******************&&&&&&&&&&&&&")
    #         print(k)
    #         print("******************&&&&&&&&&&&&&")
    #         try:
    #             get_product_info(i, k)
    #         except:
    #             continue
    # k = 400
    # main(page, k)
    # product = Product.objects.all()
    # for i in product:
    #     br = i.name.split(' ')[0]
    #     brand, created = Brand.objects.get_or_create(name=br)
    #     if not i.brand_id:
    #         test_product = Product.objects.get(slug=i.slug)
    #         if created:
    #             test_product.brand_id = brand.id
    #     if not i.brand_id:
    #         try:
    #             brad = Brand.objects.get(name=br)
    #             prod = Product.objects.get(name=i.name)
    #             prod.brand_id = brad
    #             prod.save()
    #             print("Successed")
    #         except:
    #             print("Not Found this instance")

                
    # cat = Category.objects.get(category_name='Mobiles & Tablets')
    # # cat = Category.objects.all()
    # # br = Brand.objects.get(name='Apple')
    # br = Brand.objects.all()

    # print(br)
    # product = Product.objects.all().order_by('id')
    # j = 1
    # for i in product:
    #     Product.objects.filter(id=i.id).update(count=j)
    #     print(j)
    #     j+=1

    # page = requests.get("https://dream2000.com/en/mobiles.html?product_list_limit=100")
    
    # def main(page):
    #     print("main####################")
    #     scr = page.content
    #     soup = BeautifulSoup(scr, 'lxml')
    #     product_details = []
    #     products = soup.find_all("div", {'class': 'product-item-info'})
    #     print(products)
    #     dict_list  = []
    #     # print(product)
    
    #     def get_product_info(product, k):
    #         product_title = product.find('a', {'class': 'product-item-link'}).text.strip()
    #         product_photo = product.find('img', {'class': 'product-image-photo'})['src']
    #         product_price = product.find('span', {'class': 'special-price'}).find('span', {'class': 'price'}).text.strip()
    #         print(product_title)
    #         print(product_photo)
    #         print(product_price)
    #         out = re.findall(r'\d+\.\d+', product_price)
    #         float_value = float(out[0])
    #         dict_list.append({'name':product_title, 'image':product_photo, 'price': product_price})

    #         print(f"TSSSSSSSSSSSSSS {product_photo}")
    #         img_data = requests.get(f"{product_photo}").content
    #         with open(f"B:\\BOOK\Graduation Project\\New folder (2)\media\image\product\\another\\phone{k}.jpg", 'wb') as handler:
    #             handler.write(img_data)
    #             k+=1
    #         prod = Product.objects.create(
    #             name= product_title,
    #             description= details,
    #             # image = 'https://dream2000.com/media/catalog/product/cache/f0c876fc5fd423dc009b2416a0e65966/s/a/samsung-a53-5g-_8_128_-awesome-black-1.jpg',
    #             image = f'image\product\\another\\phone{k}.jpg',
    #             category_id =  cat, 
    #             price = float_value,
    #             quantity_in_stock = 100,
    #             # brand_id = br,
    #             slug = slugify(product_title)
    #         )
    #     print("main####################")
    #     k = 1
    #     for i in products:
    #         print("test 1")
    #         print(i)
    #         try:
    #             get_product_info(i, k)
    #         except:
    #             continue
    #         k +=1
    # # main(page)
    # product = Product.objects.filter(category_id_id=162)
    # print(product)
    # for i in product:
        
    #     br = i.name.split(' ')[0]
    #     print(br)
    #     brand, created = Brand.objects.get_or_create(name=br)
    #     if not i.brand_id:
    #         test_product = Product.objects.get(slug=i.slug)
    #         if created:
    #             test_product.brand_id = brand.id
    #     if not i.brand_id:
    #         try:
    #             brad = Brand.objects.get(name=br)
    #             prod = Product.objects.get(name=i.name)
    #             prod.brand_id = brad
    #             prod.save()
    #             print("Successed")
    #         except:
    #             print("Not Found this instance")
#     user_cookie = request.COOKIES.get('csrftoken','')
#     user_session_id = request.COOKIES.get('sessionid','')
#     user_os = request.META['OS']
#     user_name = request.META['USERNAME']
#     user_computer_name = request.META['COMPUTERNAME']
#     user_core = request.META['NUMBER_OF_PROCESSORS']
#     user_name = request.META['USERNAME']

#     user_agent = request.META.get('HTTP_USER_AGENT', '')
#     ip_address = request.META.get('REMOTE_ADDR', '')
#     referrer = request.META.get('HTTP_REFERER', '')
#     accepted_languages = request.META.get('HTTP_ACCEPT_LANGUAGE', '')

#     print(f"1- {user_agent}")
#     print(f"2- {ip_address}")
#     print(f"3- {referrer}")
#     print(f"4- {accepted_languages}")

# # Analyze or log the collected information


#     print(user_cookie)
#     print(user_session_id)
#     print(user_os)
#     print(user_name)
#     print(user_computer_name)
    # print(user_name)
    # print(user_core)
    # print(request.META)
    # main(page)
    # return render(request, 'temp.html')
    # product = Product.objects.all()

    return HttpResponse('nothing')


from django.contrib.auth.hashers import make_password


def slug_autocomplet(request):
    # product_query = Product.objects.all()

    # for obj in product_query:
    #     obj.slug = slugify(obj.name)
    #     obj.save()

    # names = [
    #     "Ahmed Abdel-Rahman", "Mona Ibrahim", "Hassan Mahmoud", "Nourhan Samir", "Ali Said",
    #     "Fatima Hassan", "Omar Farouk", "Aya Kamal", "Mahmoud Salah", "Salma Ahmed",
    #     "Karim Hossam", "Dina Kamal", "Tamer Adel", "Hoda Abdel-Aziz", "Amr Ali", "Rania Magdy",
    #     "Khaled Adel", "Yasmin Youssef", "Ahmed Samir", "Yasmine Tarek", "Mohamed Gamal",
    #     "Leila Mohamed", "Sherif Ahmed", "Alia Hassan", "Yasser Mohamed", "Rehab Adel",
    #     "Hossam Abdel-Hamid", "Asmaa Hany", "Sameh Ahmed", "Mariam Reda", "Ahmed Abdel-Fattah",
    #     "Nadia Hossam", "Mahmoud Essam", "Rasha Samy", "Kareem Tarek", "Nada Mohamed",
    #     "Tarek Hany", "Heba Mohamed", "Mohamed Yassin", "Rania Ali", "Ahmed Mohsen",
    #     "Dalia Tamer", "Sherif Mahmoud", "Nour Essam", "Mohamed Salah", "Hana Ahmed",
    #     "Amr Abdel-Moneim", "Salwa Hassan", "Omar Abdel-Aziz", "Lamia Hossam", "Hisham Ahmed",
    #     "Hend Ali", "Ahmed Abdel-Latif", "May Mahmoud", "Sherif Mohamed", "Nourhan Youssef",
    #     "Tamer Salah", "Dina Ahmed", "Mahmoud Yassin", "Fatma Hossam", "Hany Abdel-Hamid",
    #     "Nada Ali", "Essam Youssef", "Aisha Hassan", "Samir Ahmed", "Mona Hossam",
    #     "Ahmed Kamal", "Rana Hany", "Mohamed Hossam", "Nourhan Ahmed", "Karim Tarek",
    #     "Marwa Ahmed", "Mahmoud Samy", "Yasmine Ahmed", "Hossam Essam", "Nour Mohamed",
    #     "Tamer Youssef", "Yasmin Hossam", "Ahmed Adel", "Lamia Mohamed", "Hassan Hany",
    #     "Dina Adel", "Mohamed Hany", "Nada Tarek", "Sherif Salah", "Rasha Ahmed",
    #     "Tarek Mohamed", "Salma Adel", "Karim Salah", "Heba Mohamed", "Ali Abdel-Hamid",
    #     "Mona Kamal", "Mohamed Youssef", "Rania Hassan", "Ahmed Hossam", "Mariam Samir",
    #     "Hossam Kamal", "Aya Salah", "Khaled Mohamed", "Nourhan Tarek", "Tamer Ali",
    #     "Hana Hossam", "Essam Salah", "Yasmin Adel", "Amr Hany", "Nada Salah",
    #     "Mahmoud Abdel-Latif", "Yasmine Hassan", "Hossam Hany", "May Mohamed", "Ahmed Youssef",
    #     "Salwa Hossam", "Ali Hany", "Rania Samir", "Mohamed Abdel-Fattah", "Fatma Kamal",
    #     "Kareem Mohamed", "Dalia Salah", "Mahmoud Tarek", "Nour Ali", "Samir Hany",
    #     "Mona Adel", "Ahmed Abdel-Gawad", "Heba Salah", "Hossam Salah", "Rasha Hossam",
    #     "Tarek Salah", "Yasmin Tamer", "Mohamed Adel", "Aya Hossam", "Sami Abdel-Latif",
    #     "Nourhan Hany", "Karim Hossam", "Rania Ali", "Ahmed Abdel-Moneim", "Salwa Ali",
    #     "Ali Hossam", "Nada Hany", "Mohamed Yassin", "Rasha Hany", "Tarek Ahmed",
    #     "May Hassan", "Hisham Salah", "Mona Salah", "Ahmed Abdel-Razek", "Dina Hany",
    #     "Samir Hossam", "Yasmin Mohamed", "Hossam Mohamed", "Nourhan Salah", "Ali Salah",
    #     "Mariam Ahmed", "Tamer Mohamed", "Rania Youssef", "Mohamed Abdel-Aziz", "Nada Mohamed",
    #     "Karim Adel", "Hana Mohamed", "Mahmoud Hany", "Salma Salah", "Amr Mohamed",
    #     "Lamia Adel", "Yasmin Salah", "Hassan Hossam", "Mona Hany", "Tamer Hossam",
    #     "Rasha Salah", "Ahmed Hany", "Dalia Ali", "Karim Salah", "Marwa Hossam",
    #     "Sami Ali", "Yasmin Hany", "Mohamed Salah", "Nada Ahmed", "Hossam Adel",
    #     "Rania Salah", "Mahmoud Hossam", "Ali Ali", "Dina Youssef", "Tamer Hany",
    #     "Mariam Salah", "Hassan Salah", "May Hossam", "Ahmed Ali", "Salwa Mohamed",
    #     "Kareem Hany", "Heba Hossam", "Hana Salah", "Nourhan Ali", "Mohamed Hany",
    #     "Yasmin Hossam", "Sami Salah", "Lamia Salah", "Omar Adel", "Rania Hossam",
    #     "Mahmoud Ali", "Aya Mohamed", "Hisham Hossam", "Nour Ali"
    # ]
    # email_address = ['ahmed_abdel00-rahman@gmail.com', 'mona_ibrahim@gmail.com', 'hassan_mahmoud@gmail.com', 'nourhan_samir@gmail.com', 'ali_said@gmail.com', 'fatima_hassan@gmail.com', 'omar_farouk@gmail.com', 'aya_kamal@gmail.com', 'mahmoud_salah@gmail.com', 'salma_ahmed@gmail.com', 'karim_hossam@gmail.com', 'dina_kamal@gmail.com', 'tamer_adel@gmail.com', 'hoda_abdel-aziz@gmail.com', 'amr_ali@gmail.com', 'rania_magdy@gmail.com', 'khaled_adel@gmail.com', 'yasmin_youssef@gmail.com', 'ahmed_samir@gmail.com', 'yasmine_tarek@gmail.com', 'mohamed_gamal@gmail.com', 'leila_mohamed@gmail.com', 'sherif_ahmed@gmail.com', 'alia_hassan@gmail.com', 'yasser_mohamed@gmail.com', 'rehab_adel@gmail.com', 'hossam_abdel-hamid@gmail.com', 'asmaa_hany@gmail.com', 'sameh_ahmed@gmail.com', 'mariam_reda@gmail.com', 'ahmed_abdel-fattah@gmail.com', 'nadia_hossam@gmail.com', 'mahmoud_essam@gmail.com', 'rasha_samy@gmail.com', 'kareem_tarek@gmail.com', 'nada_mohamed@gmail.com', 'tarek_hany@gmail.com', 'heba_mohamed@gmail.com', 'mohamed_yassin@gmail.com', 'rania_ali@gmail.com', 'ahmed_mohsen@gmail.com', 'dalia_tamer@gmail.com', 'sherif_mahmoud@gmail.com', 'nour_essam@gmail.com', 'mohamed_salah@gmail.com', 'hana_ahmed@gmail.com', 'amr_abdel-moneim@gmail.com', 'salwa_hassan@gmail.com', 'omar_abdel-aziz@gmail.com', 'lamia_hossam@gmail.com', 'hisham_ahmed@gmail.com', 'hend_ali@gmail.com', 'ahmed_abdel-latif@gmail.com', 'may_mahmoud@gmail.com', 'sherif_mohamed@gmail.com', 'nourhan_youssef@gmail.com', 'tamer_salah@gmail.com', 'dina_ahmed@gmail.com', 'mahmoud_yassin@gmail.com', 'fatma_hossam@gmail.com', 'hany_abdel-hamid@gmail.com', 'nada_ali@gmail.com', 'essam_youssef@gmail.com', 'aisha_hassan@gmail.com', 'samir_ahmed@gmail.com', 'mona_hossam@gmail.com', 'ahmed_kamal@gmail.com', 'rana_hany@gmail.com', 'mohamed_hossam@gmail.com', 'nourhan_ahmed@gmail.com', 'karim_tarek@gmail.com', 'marwa_ahmed@gmail.com', 'mahmoud_samy@gmail.com', 'yasmine_ahmed@gmail.com', 'hossam_essam@gmail.com', 'nour_mohamed@gmail.com', 'tamer_youssef@gmail.com', 'yasmin_hossam@gmail.com', 'ahmed_adel@gmail.com', 'lamia_mohamed@gmail.com', 'hassan_hany@gmail.com', 'dina_adel@gmail.com', 'mohamed_hany@gmail.com', 'nada_tarek@gmail.com', 'sherif_salah@gmail.com', 'rasha_ahmed@gmail.com', 'tarek_mohamed@gmail.com', 'salma_adel@gmail.com', 'karim_salah@gmail.com', 'heba_mohamed@gmail.com', 'ali_abdel-hamid@gmail.com', 'mona_kamal@gmail.com', 'mohamed_youssef@gmail.com', 'rania_hassan@gmail.com', 'ahmed_hossam@gmail.com', 'mariam_samir@gmail.com', 'hossam_kamal@gmail.com', 'aya_salah@gmail.com', 'khaled_mohamed@gmail.com', 'nourhan_tarek@gmail.com', 'tamer_ali@gmail.com', 'hana_hossam@gmail.com', 'essam_salah@gmail.com', 'yasmin_adel@gmail.com', 'amr_hany@gmail.com', 'nada_salah@gmail.com', 'mahmoud_abdel-latif@gmail.com', 'yasmine_hassan@gmail.com', 'hossam_hany@gmail.com', 'may_mohamed@gmail.com', 'ahmed_youssef@gmail.com', 'salwa_hossam@gmail.com', 'ali_hany@gmail.com', 'rania_samir@gmail.com', 'mohamed_abdel-fattah@gmail.com', 'fatma_kamal@gmail.com', 'kareem_mohamed@gmail.com', 'dalia_salah@gmail.com', 'mahmoud_tarek@gmail.com', 'nour_ali@gmail.com', 'samir_hany@gmail.com', 'mona_adel@gmail.com', 'ahmed_abdel-gawad@gmail.com', 'heba_salah@gmail.com', 'hossam_salah@gmail.com', 'rasha_hossam@gmail.com', 'tarek_salah@gmail.com', 'yasmin_tamer@gmail.com', 'mohamed_adel@gmail.com', 'aya_hossam@gmail.com', 'sami_abdel-latif@gmail.com', 'nourhan_hany@gmail.com', 'karim_hossam@gmail.com', 'rania_ali@gmail.com', 'ahmed_abdel-moneim@gmail.com', 'salwa_ali@gmail.com', 'ali_hossam@gmail.com', 'nada_hany@gmail.com', 'mohamed_yassin@gmail.com', 'rasha_hany@gmail.com', 'tarek_ahmed@gmail.com', 'may_hassan@gmail.com', 'hisham_salah@gmail.com', 'mona_salah@gmail.com', 'ahmed_abdel-razek@gmail.com', 'dina_hany@gmail.com', 'samir_hossam@gmail.com', 'yasmin_mohamed@gmail.com', 'hossam_mohamed@gmail.com', 'nourhan_salah@gmail.com', 'ali_salah@gmail.com', 'mariam_ahmed@gmail.com', 'tamer_mohamed@gmail.com', 'rania_youssef@gmail.com', 'mohamed_abdel-aziz@gmail.com', 'nada_mohamed@gmail.com', 'karim_adel@gmail.com', 'hana_mohamed@gmail.com', 'mahmoud_hany@gmail.com', 'salma_salah@gmail.com', 'amr_mohamed@gmail.com', 'lamia_adel@gmail.com', 'yasmin_salah@gmail.com', 'hassan_hossam@gmail.com', 'mona_hany@gmail.com', 'tamer_hossam@gmail.com', 'rasha_salah@gmail.com', 'ahmed_hany@gmail.com', 'dalia_ali@gmail.com', 'karim_salah@gmail.com', 'marwa_hossam@gmail.com', 'sami_ali@gmail.com', 'yasmin_hany@gmail.com', 'mohamed_salah@gmail.com', 'nada_ahmed@gmail.com', 'hossam_adel@gmail.com', 'rania_salah@gmail.com', 'mahmoud_hossam@gmail.com', 'ali_ali@gmail.com', 'dina_youssef@gmail.com', 'tamer_hany@gmail.com', 'mariam_salah@gmail.com', 'hassan_salah@gmail.com', 'may_hossam@gmail.com', 'ahmed_ali@gmail.com', 'salwa_mohamed@gmail.com', 'kareem_hany@gmail.com', 'heba_hossam@gmail.com', 'hana_salah@gmail.com', 'nourhan_ali@gmail.com', 'mohamed_hany@gmail.com', 'yasmin_hossam@gmail.com', 'sami_salah@gmail.com', 'lamia_salah@gmail.com', 'omar_adel@gmail.com', 'rania_hossam@gmail.com', 'mahmoud_ali@gmail.com', 'aya_mohamed@gmail.com', 'hisham_hossam@gmail.com', 'nour_ali@gmail.com']
    # phone_numbers = [
    #     "+2011" + "".join(str(random.randint(0, 9)) for _ in range(8)) for _ in range(200)
    # ]

    # rows = []
    # passlist = []
    # emaillist = []
    # phonelist = []
    # usernamelist = []
    # g = 0
    # # for i in range(1000):
    # for k in names:
    #     characters = string.ascii_letters + string.digits + string.punctuation
    #     passworder = ''.join(random.choice(characters) for _ in range(8))
    #     # print(characters)
    #     passworder+='test1'
    #     print(f"this is name {k}")
    #     print('\n')
    #     print(f"this is email {email_address[g]}")
    #     print('\n')
    #     print(f"this is PhoneNumber: {phone_numbers[g]}")
    #     print('\n')
    #     print(f"this is password {passworder}")
    #     print('\n')
    #     try:
    #         user = CustomUser.objects.create(
    #             password = make_password(passworder),
    #             email = email_address[g],
    #             phone_number = phone_numbers[g],
    #             username = k, 
    #         )
    #         passlist.append(passworder)
    #         emaillist.append(email_address[g])
    #         phonelist.append(phone_numbers[g])
    #         usernamelist.append(k)
    #     except:
    #         print('nothing')
    #     g+=1
        
    # rows.append(passlist)
    # rows.append(emaillist)
    # rows.append(phonelist)
    # rows.append(usernamelist)
    # with open('C:\\Users\\omar\\Desktop\\csvfile.csv', 'w') as csvfile:
    #     csvwriter = csv.writer(csvfile)
    #     csvwriter.writerow(['password', 'email', 'phone', 'username'])
    #     csvwriter.writerows(rows)

    # for i in range(700):
    #     try:
    #         product = Product.objects.get(id=random.randint(38, 834))
    #         user = CustomUser.objects.get(id=3)
    #         reve = Review.objects.create(
    #             rate = random.randint(0, 5),
    #             comment = 'This is Comment',
    #             product_id = product,
    #             user_id = user,
    #         )
    #         print(i)
    #     except:
            
    #         continue

    return HttpResponse("Succedfully")


import random
import faker
from items.models import Comment, Review
def review_insert(request):



    fake = faker.Faker()

    def generate_electronic_product_dataset(num_samples):
        dataset = []
        for _ in range(num_samples):
            product_name = fake.word() + ' ' + fake.word() + ' ' + fake.word() + ' ' + fake.word()
            comment = fake.text()
            rating = random.randint(1, 5)
            dataset.append({
                'Product Name': product_name,
                'Comment': comment,
                'Rating': rating
            })
        return dataset

    # Set the number of samples you want in your dataset
    num_samples = 10000

    # Generate the dataset
    electronic_product_dataset = generate_electronic_product_dataset(num_samples)

    # Print the first few entries in the dataset
    # for i in range(100):
    #     print(electronic_product_dataset[i])
    for i in electronic_product_dataset:
        try:
            print(i['Comment'])
            print('\n')
            print(i['Rating'])
            com = Comment.objects.create(
                comment = i['Comment']
            )
            review = Review.objects.create(
                        user_id = random.randint(203735, 203933),
                        product_id = random.randint(388,1626),
                        rate  = i['Rating'],
                        comment = com,
                    )
        except:
            print('not found')

    return HttpResponse("Review is Inserted")











# {
#     'ALLUSERSPROFILE': 'C:\\ProgramData', 
#     'APPDATA': 'C:\\Users\\omar\\AppData\\Roaming', 
#     'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_13992_UZEOQEJDSZVDUWLN', 
#     'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
#     'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 
#     'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
#     'COMPUTERNAME': 'OMAR-LAPTOP', 
#     'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 
#     'DATAGRIP': 'C:\\Program Files\\JetBrains\\DataGrip 2023.2.1\\bin;',
#     'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 
#     'EFC_12192': '1', 'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
#     'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 'HOMEDRIVE': 'C:', 
#     'HOMEPATH': '\\Users\\omar', 'LOCALAPPDATA': 'C:\\Users\\omar\\AppData\\Local', 
#     'LOGONSERVER': '\\\\OMAR-LAPTOP', 
#     'MSMPI_BENCHMARKS': 'C:\\Program Files\\Microsoft MPI\\Benchmarks\\', 
#     'MSMPI_BIN': 'C:\\Program Files\\Microsoft MPI\\Bin\\', 
#     'NUMBER_OF_PROCESSORS': '12', 
#     'ONEDRIVE': 'C:\\Users\\omar\\OneDrive - Faculty Of Science (Zagazig University)', 
#     'ONEDRIVECOMMERCIAL': 'C:\\Users\\omar\\OneDrive - Faculty Of Science (Zagazig University)', 
#     'ONEDRIVECONSUMER': 'C:\\Users\\omar\\OneDrive', 
#     'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 
#     'OS': 'Windows_NT', 
#     'PATH': 'B:\\BOOK\\Graduation Project\\New folder (2)\\venv\\Scripts;C:\\Program Files\\Microsoft MPI\\Bin\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program Files\\MongoDB\\Server\\6.0\\bin;C:\\Program Files\\dotnet\\;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\10\\Windows Performance Toolkit\\;C:\\Users\\omar\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\omar\\AppData\\Roaming\\npm;C:\\MinGW\\bin;C:\\msys64\\mingw64\\bin;C:\\msys64\\mingw64\\bin;C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files (x86)\\Nmap;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\bin;;C:\\Program Files\\JetBrains\\DataGrip 2023.2.1\\bin;;C:\\Users\\omar\\AppData\\Local\\GitHubDesktop\\bin', 
#     'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL', 
#     'PROCESSOR_ARCHITECTURE': 'AMD64', 
#     'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD', 
#     'PROCESSOR_LEVEL': '23', 
#     'PROCESSOR_REVISION': '6001', 
#     'PROGRAMDATA': 'C:\\ProgramData', 
#     'PROGRAMFILES': 'C:\\Program Files', 
#     'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
#     'PROGRAMW6432': 'C:\\Program Files', 
#     'PSMODULEPATH': 'D:\\OOO\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\Tools\\PowerShell\\Modules\\', 
#     'PUBLIC': 'C:\\Users\\Public', 
#     'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\bin;', 
#     'SESSIONNAME': 'Console', 
#     'SYSTEMDRIVE': 'C:', 
#     'SYSTEMROOT': 'C:\\WINDOWS', 
#     'TEMP': 'C:\\Users\\omar\\AppData\\Local\\Temp', 
#     'TMP': 'C:\\Users\\omar\\AppData\\Local\\Temp', 
#     'USERDOMAIN': 'OMAR-LAPTOP', 
#     'USERDOMAIN_ROAMINGPROFILE': 'OMAR-LAPTOP', 
#     'USERNAME': 'omar', 
#     'USERPROFILE': 'C:\\Users\\omar', 
#     'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 
#     'VIRTUAL_ENV': 'B:\\BOOK\\Graduation Project\\New folder (2)\\venv', 
#     'VIRTUAL_ENV_PROMPT': 'venv', 
#     'WINDIR': 'C:\\WINDOWS', 
#     'TERM_PROGRAM': 'vscode', 
#     'TERM_PROGRAM_VERSION': '1.85.1', 
#     'LANG': 'en_US.UTF-8', 
#     'COLORTERM': 'truecolor', 
#     'GIT_ASKPASS': 'c:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 
#     'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 
#     'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 
#     'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-cafd9f28b0-sock', 
#     'VSCODE_INJECTION': '1', 
#     '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Microsoft MPI\\Bin\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program Files\\MongoDB\\Server\\6.0\\bin;C:\\Program Files\\dotnet\\;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\10\\Windows Performance Toolkit\\;C:\\Users\\omar\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\omar\\AppData\\Roaming\\npm;C:\\MinGW\\bin;C:\\msys64\\mingw64\\bin;C:\\msys64\\mingw64\\bin;C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files (x86)\\Nmap;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\bin;;C:\\Program Files\\JetBrains\\DataGrip 2023.2.1\\bin;;C:\\Users\\omar\\AppData\\Local\\GitHubDesktop\\bin', 'PYTHONUSERBASE': 'C:\\Users\\omar\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages', 
#     'DJANGO_SETTINGS_MODULE': 'project.settings', 
#     'RUN_MAIN': 'true', 
#     'SERVER_NAME': 'omar-laptop', 
#     'GATEWAY_INTERFACE': 'CGI/1.1', 
#     'SERVER_PORT': '8000', 
#     'REMOTE_HOST': '', 
#     'CONTENT_LENGTH': '', 
#     'SCRIPT_NAME': '', 
#     'SERVER_PROTOCOL': 'HTTP/1.1', 
#     'SERVER_SOFTWARE': 'WSGIServer/0.2', 
#     'REQUEST_METHOD': 'GET', 
#     'PATH_INFO': '/web/', 
#     'QUERY_STRING': '', 
#     'REMOTE_ADDR': '127.0.0.1', 
#     'CONTENT_TYPE': 'text/plain', 
#     'HTTP_HOST': '127.0.0.1:8000', 
#     'HTTP_CONNECTION': 'keep-alive', 
#     'HTTP_CACHE_CONTROL': 'max-age=0', 
#     'HTTP_SEC_CH_UA': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"', 
#     'HTTP_SEC_CH_UA_MOBILE': '?0', 
#     'HTTP_SEC_CH_UA_PLATFORM': '"Windows"', 
#     'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
#     'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 
#     'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 
#     'HTTP_SEC_FETCH_SITE': 'none', 
#     'HTTP_SEC_FETCH_MODE': 'navigate', 
#     'HTTP_SEC_FETCH_USER': '?1', 
#     'HTTP_SEC_FETCH_DEST': 'document', 
#     'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
#     'HTTP_ACCEPT_LANGUAGE': 'en-EG,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,en-US;q=0.6,en-GB;q=0.5,nl;q=0.4', 
#     'HTTP_COOKIE': 'csrftoken=Lzku7N6eQhIDJqm4EzVdirOSND15T5Hj; sessionid=r1syr7ktj374wun337i1gy9vd7r66mkj; mp_10bab2a6cec3a2ef62083257f3f09083_mixpanel=%7B%22distinct_id%22%3A%20%2218b9cb6af4e579-0d8f9b335f3a07-26031051-144000-18b9cb6af4fb33%22%2C%22%24device_id%22%3A%20%2218b9cb6af4e579-0d8f9b335f3a07-26031051-144000-18b9cb6af4fb33%22%2C%22%24initial_referrer%22%3A%20%22http%3A%2F%2F127.0.0.1%3A8000%2Fdjango-admin%2Flogin%2F%3Fnext%3D%2Fdjango-admin%2F%22%2C%22%24initial_referring_domain%22%3A%20%22127.0.0.1%3A8000%22%7D', 
#     'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x0000020D08CA1540>, 
#     'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 
#     'wsgi.version': (1, 0), 'wsgi.run_once': False, 
#     'wsgi.url_scheme': 'http', 
#     'wsgi.multithread': True, 
#     'wsgi.multiprocess': False, 
#     'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 
#     'CSRF_COOKIE': 'Lzku7N6eQhIDJqm4EzVdirOSND15T5Hj'
#     }





# {
#     'ALLUSERSPROFILE': 
#     'C:\\ProgramData', 'APPDATA': 
#     'C:\\Users\\omar\\AppData\\Roaming', 
#     'CHROME_CRASHPAD_PIPE_NAME': '\\\\.\\pipe\\crashpad_13992_UZEOQEJDSZVDUWLN', 
#     'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
#     'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 
#     'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
#     'COMPUTERNAME': 'OMAR-LAPTOP', 
#     'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 
#     'DATAGRIP': 'C:\\Program Files\\JetBrains\\DataGrip 2023.2.1\\bin;', 
#     'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 
#     'EFC_12192': '1', 
#     'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
#     'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 
#     'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\omar', 
#     'LOCALAPPDATA': 'C:\\Users\\omar\\AppData\\Local', 
#     'LOGONSERVER': '\\\\OMAR-LAPTOP', 
#     'MSMPI_BENCHMARKS': 'C:\\Program Files\\Microsoft MPI\\Benchmarks\\', 
#     'MSMPI_BIN': 'C:\\Program Files\\Microsoft MPI\\Bin\\', 
#     'NUMBER_OF_PROCESSORS': '12', 
#     'ONEDRIVE': 'C:\\Users\\omar\\OneDrive - Faculty Of Science (Zagazig University)', 
#     'ONEDRIVECOMMERCIAL': 'C:\\Users\\omar\\OneDrive - Faculty Of Science (Zagazig University)', 
#     'ONEDRIVECONSUMER': 'C:\\Users\\omar\\OneDrive', 
#     'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 
#     'OS': 'Windows_NT', 
#     'PATH': 'B:\\BOOK\\Graduation Project\\New folder (2)\\venv\\Scripts;C:\\Program Files\\Microsoft MPI\\Bin\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program Files\\MongoDB\\Server\\6.0\\bin;C:\\Program Files\\dotnet\\;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\10\\Windows Performance Toolkit\\;C:\\Users\\omar\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\omar\\AppData\\Roaming\\npm;C:\\MinGW\\bin;C:\\msys64\\mingw64\\bin;C:\\msys64\\mingw64\\bin;C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files (x86)\\Nmap;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\bin;;C:\\Program Files\\JetBrains\\DataGrip 2023.2.1\\bin;;C:\\Users\\omar\\AppData\\Local\\GitHubDesktop\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL', 
#     'PROCESSOR_ARCHITECTURE': 'AMD64', 
#     'PROCESSOR_IDENTIFIER': 'AMD64 Family 23 Model 96 Stepping 1, AuthenticAMD', 
#     'PROCESSOR_LEVEL': '23', 
#     'PROCESSOR_REVISION': '6001', 
#     'PROGRAMDATA': 'C:\\ProgramData', 
#     'PROGRAMFILES': 'C:\\Program Files', 
#     'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
#     'PROGRAMW6432': 'C:\\Program Files', 
#     'PSMODULEPATH': 'D:\\OOO\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\Tools\\PowerShell\\Modules\\', 
#     'PUBLIC': 'C:\\Users\\Public', 
#     'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\bin;', 
#     'SESSIONNAME': 'Console', 
#     'SYSTEMDRIVE': 'C:', 
#     'SYSTEMROOT': 'C:\\WINDOWS', 
#     'TEMP': 'C:\\Users\\omar\\AppData\\Local\\Temp', 
#     'TMP': 'C:\\Users\\omar\\AppData\\Local\\Temp', 
#     'USERDOMAIN': 'OMAR-LAPTOP', 
#     'USERDOMAIN_ROAMINGPROFILE': 'OMAR-LAPTOP', 
#     'USERNAME': 'omar', 
#     'USERPROFILE': 'C:\\Users\\omar', 
#     'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 
#     'VIRTUAL_ENV': 'B:\\BOOK\\Graduation Project\\New folder (2)\\venv', 
#     'VIRTUAL_ENV_PROMPT': 'venv', 
#     'WINDIR': 'C:\\WINDOWS', 
#     'TERM_PROGRAM': 'vscode', 
#     'TERM_PROGRAM_VERSION': '1.85.1', 
#     'LANG': 'en_US.UTF-8', 
#     'COLORTERM': 'truecolor', 
#     'GIT_ASKPASS': 'c:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass.sh', 
#     'VSCODE_GIT_ASKPASS_NODE': 'C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe', 
#     'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 
#     'VSCODE_GIT_ASKPASS_MAIN': 'c:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\resources\\app\\extensions\\git\\dist\\askpass-main.js', 
#     'VSCODE_GIT_IPC_HANDLE': '\\\\.\\pipe\\vscode-git-cafd9f28b0-sock', 
#     'VSCODE_INJECTION': '1', 
#     '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Microsoft MPI\\Bin\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\Program Files\\nodejs\\;C:\\Program Files\\MongoDB\\Server\\6.0\\bin;C:\\Program Files\\dotnet\\;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files (x86)\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\Client SDK\\ODBC\\170\\Tools\\Binn\\;C:\\Program Files\\Microsoft SQL Server\\160\\DTS\\Binn\\;C:\\Program Files (x86)\\Windows Kits\\10\\Windows Performance Toolkit\\;C:\\Users\\omar\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\omar\\AppData\\Roaming\\npm;C:\\MinGW\\bin;C:\\msys64\\mingw64\\bin;C:\\msys64\\mingw64\\bin;C:\\Users\\omar\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files (x86)\\Nmap;C:\\Program Files\\Azure Data Studio\\bin;C:\\Program Files\\JetBrains\\PyCharm 2023.2.1\\bin;;C:\\Program Files\\JetBrains\\DataGrip 2023.2.1\\bin;;C:\\Users\\omar\\AppData\\Local\\GitHubDesktop\\bin', 'PYTHONUSERBASE': 'C:\\Users\\omar\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\LocalCache\\local-packages', 
#     'DJANGO_SETTINGS_MODULE': 'project.settings', 
#     'RUN_MAIN': 'true', 
#     'SERVER_NAME': 'omar-laptop', 
#     'GATEWAY_INTERFACE': 'CGI/1.1', 
#     'SERVER_PORT': '8000', 
#     'REMOTE_HOST': '', 
#     'CONTENT_LENGTH': '', 
#     'SCRIPT_NAME': '', 
#     'SERVER_PROTOCOL': 'HTTP/1.1', 
#     'SERVER_SOFTWARE': 'WSGIServer/0.2', 
#     'REQUEST_METHOD': 'GET', 'PATH_INFO': '/web/', 
#     'QUERY_STRING': '', 'REMOTE_ADDR': '127.0.0.1', 
#     'CONTENT_TYPE': 'text/plain', 
#     'HTTP_HOST': '127.0.0.1:8000', 
#     'HTTP_CONNECTION': 'keep-alive', 
#     'HTTP_CACHE_CONTROL': 'max-age=0', 
#     'HTTP_SEC_CH_UA': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"', 
#     'HTTP_SEC_CH_UA_MOBILE': '?0', 
#     'HTTP_SEC_CH_UA_PLATFORM': '"Windows"', 
#     'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 
#     'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76', 
#     'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'HTTP_SEC_FETCH_SITE': 'cross-site', 
#     'HTTP_SEC_FETCH_MODE': 'navigate', 
#     'HTTP_SEC_FETCH_USER': '?1', 
#     'HTTP_SEC_FETCH_DEST': 'document', 
#     'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 
#     'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9,ar;q=0.8', 
#     'HTTP_COOKIE': 'csrftoken=aBSRdix9vH7wyZFOlDUwCApR92zDByeX; sessionid=on9jfcr3ik7r8pu7nvuotp00im5zwiza', 
#     'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x000002359C84CF40>, 
#     'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>, 
#     'wsgi.version': (1, 0), 
#     'wsgi.run_once': False, 
#     'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 
#     'wsgi.multiprocess': False, 
#     'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 
#     'CSRF_COOKIE': 'aBSRdix9vH7wyZFOlDUwCApR92zDByeX'}




