import requests
url = "https://onlineislemler.egm.gov.tr/sayfalar/ihbar.aspx"
title = input("İhbar Başlığı: ").strip()
description = input("İhbar Açıklaması: ").strip()
city = input("Şehir: ").strip()
district = input("İlçe: ").strip()
phone = input("Telefon Numarası: ").strip()
proxies = {
    "http": "PROXY",  
    "https": "PROXY",  
}
data = {
    "ctl00$ContentPlaceHolder1$txtIcerik": description,
    "ctl00$ContentPlaceHolder1$txtSehir": city,
    "ctl00$ContentPlaceHolder1$txtIlce": district,
    "ctl00$ContentPlaceHolder1$txtGsm": phone,
    "ctl00$ContentPlaceHolder1$txtAdres": "",
    "ctl00$ContentPlaceHolder1$txtTarih": "",
    "ctl00$ContentPlaceHolder1$txtMail": "",
    "ctl00$ContentPlaceHolder1$btnIhbar": "Gönder",
}
try:
    response = requests.post(url, data=data, proxies=proxies, timeout=10)
    if response.status_code == 200:
        print("İhbar başarıyla gönderildi!")
    else:
        print(f"Hata : {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"İnterneti ve proxy yi kontrol et : {e}")