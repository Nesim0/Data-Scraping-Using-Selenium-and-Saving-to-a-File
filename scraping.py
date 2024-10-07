from selenium import webdriver  
import time
import random
driver = webdriver.Chrome()
pagecount = 1
all_text=[]
adet = 0
sayac=1
url = "https://eksisozluk.com/isik-hizini-4111180236-350km-halatla-asabilmek--7886330?a=popular&p="
while pagecount <=2:
    sayi = random.randint(1,10)
    tam_url= url + str(sayi) 
    driver.get(tam_url)
    cek = driver.find_elements("css selector", ".content")
    time.sleep(3)
    for i in cek:
        all_text.append(i.text)
    pagecount+=1
    # anlikadet= len(cek)
    # adet+=anlikadet
with open("output.txt", "w", encoding="utf-8") as file:
    for metin in all_text:
        file.write(str(sayac) + ". " + metin + "\n\n")
        sayac+=1
# print(all_text)
# print(adet)

driver.quit()
