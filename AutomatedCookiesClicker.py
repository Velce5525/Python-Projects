import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(5)

z = driver.find_element(By.ID, "langSelect-EN")
z.click()
time.sleep(5)

for i in range(30000):
    try:
        pole_pari = driver.find_element(By.ID, "cookies")
        text_od_kol = pole_pari.text
        pari_koj_gi_imame = int(text_od_kol.split()[0])


        try:
            pole_banka = driver.find_element(By.ID, "productPrice3")
            pari_banka = int(pole_banka.text)
            if pari_koj_gi_imame >= pari_banka:
                mine = driver.find_element(By.ID, "product3")
                mine.click()
        except:
            pass

        try:
            pole_mine = driver.find_element(By.ID, "productPrice3")
            pari_mine = int(pole_mine.text)
            if pari_koj_gi_imame >= pari_mine:
                mine = driver.find_element(By.ID, "product3")
                mine.click()
        except:
            pass


        try:
            pole_farma = driver.find_element(By.ID, "productPrice2")
            pari_farma = int(pole_farma.text)
            if pari_koj_gi_imame >= pari_farma:
                farma = driver.find_element(By.ID, "product2")
                farma.click()
        except:
            pass


        try:
            pole_baba = driver.find_element(By.ID, "productPrice1")
            pari_baba = int(pole_baba.text)
            if pari_koj_gi_imame >= pari_baba:
                baba = driver.find_element(By.ID, "product1")
                baba.click()
        except:
            pass
        try:
            pole_cursor = driver.find_element(By.ID, "productPrice0")
            pari_cursor = int(pole_cursor.text)
            if pari_koj_gi_imame >= pari_cursor:
                cursor = driver.find_element(By.ID, "product0")
                cursor.click()
        except:
            pass

        try:
            for j in range(100):
                golemo_kopce = driver.find_element(By.ID, "bigCookie")
                golemo_kopce.click()
        except:
            pass

    except:
        pass

time.sleep(30000)
