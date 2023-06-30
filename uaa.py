#utf8 coding
#author Hamayon
import random
application_version = '311.0.0.40.119'
application_version_code = '227842969'
density = '2.0113'
width = '720'
height = '1240'
inform = 'IN6'
ua_string = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/' + f"{{density={density},width={width},height={height}}}" + f';FBLC/en_US;FBRV/{application_version_code};FBCR/Telenor;FBMF/INFINIX MOBILE LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix_{inform};FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
print(ua_string)