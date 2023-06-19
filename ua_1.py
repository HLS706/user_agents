#utf8 coding by Hamayon khan
import requests
import random
res = requests.get("https://ipinfo.io/")
data = res.json()
logo = ("""\033[1;92m
888    888 888      .d8888b.           Country: {} ({})
888    888 888     d88P  Y88b 
888    888 888     Y88b.      
8888888888 888      "Y888b.   
888    888 888         "Y88b. 
888    888 888           "888 
888    888 888     Y88b  d88P 
888    888 88888888 "Y8888P"              
\033[1;32m--------------------------------------------------
[+] AUTHOR   :     HAMAYON KHAN
[+] GITHUB   :     HLS706
[+] CODE     :     USER-AGENT
[+] VERSION  :     1.0.0 
\033[1;32m----------------------------------------------""".format(data['country'], data['ip']))

print(logo)


base_user_agent = "Dalvik/1.6.0 (Linux; U; Android {0}; {1} Build/{2}) " \
    "[FBAN/{3};FBAV/{4};FBBV/{5};FBDM/{{density=3.0,width={6},height={7}}};FBLC/it_IT;FBRV/\033[1;31m{8}\033[0m;FBCR/{9};FBMF/{10};FBBD/{10};FBPN/com.facebook.katana;FBDV/{11};FBSV/{0};FBOP/1;FBCA/x86:armeabi-v7a;]"


android_versions = ['5.0', '5.1.1', '6.0', '7.0', '7.1.1', '8.0', '8.1', '9.0', '10.0']
facebook_versions = ['106.0.0.26.68', '107.0.0.0.50', '108.0.0.17.68', '124.0.0.0.52', '125.0.0.23.80', '314.1.0.45.119']
dimensions_list = ['1440x2560', '1080x1920', '750x1334', '1242x2208', '720x1280', '480x854', '640x1136', '768x1280']
device_list = ['Samsung Galaxy S10', 'Samsung Galaxy S10 Plus', 'Samsung Galaxy S21 Ultra', 'Samsung Galaxy Note 20 Ultra', 
               'Sony Xperia 1 II', 'Sony Xperia 5 II', 'Infinix Note 8', 'Infinix Note 8i',
               'Google Pixel 5', 'OnePlus 8T', 'Xiaomi Mi 10T', 'Huawei P40 Pro']
fbcr_list = ['Afghan Wireless', 'Etisalat Afghanistan', 'MTN Afghanistan', 'Roshan', 'Salaam Telecom']



print("\033[1;33;40m" + "Enter 'S' to start the program, or 'E' to exit: " + "\033[0m")


while True:
    menu = input("\033[1;34;40m" + "Enter your choice: " + "\033[0m")
    if menu.lower() == 's':
        
        print("\nStarting the program...")
        
        android_version = random.choice(android_versions)
        dimensions = random.choice(dimensions_list)
        device = random.choice(device_list)
        facebook_version = random.choice(facebook_versions)
        fbcr = random.choice(fbcr_list)
        user_agent = base_user_agent.format(android_version, dimensions.split('x')[0], dimensions.split('x')[1], 'FB4A', facebook_version, facebook_version.split('.')[0], dimensions.split('x')[0], dimensions.split('x')[1], facebook_version, fbcr, device.replace(' ', '_'), device.replace(' ', '_') + '_' + android_version.replace('.', '_'))

        
        print("\033[1;35;40m" + user_agent + "\033[0m")

    elif menu.lower() == 'e':
        print("\nGoodbye!")
        break
    else:
        print("\nInvalid choice! Please enter 'S' or 'E'.")
#dont forget the credit!
#for any help inbox me into what's app {+93744040422}