
import time
import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")  # Faqat muhim xatolar chiqadi
options.add_argument("--disable-notifications")  # 🚫 Bildirishnomalarni bloklaydi

options.add_argument("--log-level=3")  # Faqat muhim xatolar chiqadi

driver = webdriver.Chrome(options=options)



driver.get("https://www.facebook.com")  # misol uchun

email = driver.find_element("id", "email")
email.send_keys("sherxaan4@gmail.com")

paswd = driver.find_element("id", "pass")
paswd.send_keys("Sher39395050--++@@")
submit_btn = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
submit_btn.click()
time.sleep(30)
print("1- kirish")



time.sleep(5)
driver.get("https://www.facebook.com/")  #guruh silkasi

print("Page loaded, starting scraping")

guruh_idlar = [626031773676623, 526988876848279, 2456888334665692,1303473427410101]
# guruh_idlar = [2456888334665692]
admin_guruhlar = [526988876848279,2456888334665692]


# 2d ni vaqt ko'rinishiga ko'chiradi
def parse_created_time(created_time_str):
    time_regex = re.compile(r'^(\d+)([hmdwy])$')
    match = time_regex.match(created_time_str)
    
    if not match:
        return None  # format mos kelmasa, None qaytaramiz

    value, unit = match.groups()
    value = int(value)
    now = datetime.now()

    if unit == 'm':
        dt = now - timedelta(minutes=value)
    elif unit == 'h':
        dt = now - timedelta(hours=value)
    elif unit == 'd':
        dt = now - timedelta(days=value)
    elif unit == 'w':
        dt = now - timedelta(weeks=value)
    elif unit == 'y':
        dt = now - timedelta(days=value * 365)
    else:
        return None

    return dt.strftime("%Y-%m-%d %H:%M:%S")




# Pageni pastga yuritadi

def scroll_page(driver, scroll_pause_time=3, max_scrolls=5):

    last_height = driver.execute_script("return document.body.scrollHeight")
        
    for _ in range(max_scrolls):
        # Sahifani pastga skroll qilamiz
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        # Sahifa to'liq yuklanishini kutish
        time.sleep(scroll_pause_time)
        
        # Yangi scroll qilingan balandlikni olish
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        # Agar sahifa balandligi o'zgarmasa, skroll qilishni to'xtatamiz
        if new_height == last_height:
            break
        
        last_height = new_height

for guruh_id in guruh_idlar:
    driver.get(f"https://www.facebook.com/groups/{guruh_id}/posts/")  # Bu yerga sahifa URL'sini qo'yish mumkin
    print(f"guruh_id : {guruh_id}")
    time.sleep(5)

    scroll_page(driver, scroll_pause_time=3, max_scrolls=10)
    # Sahifani BeautifulSoup bilan tahlil qilish
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    # aria-posinset atributiga ega barcha postlarni olish
    posts = soup.find_all(attrs={"aria-posinset": True})

    aria_info = []

    # Har bir postni ko'rib chiqish va kerakli ma'lumotlarni olish
    for post in posts:
        time.sleep(1)
        aria_labelledby = post.get("aria-labelledby")
        aria_posinset = post.get("aria-posinset")
        aria_describedby = post.get("aria-describedby", "")
        
        # describedby_id-larni ajratish
        describedby_ids = aria_describedby.split()

        # Har bir post haqida ma'lumotlarni ekranga chiqarish
        aria_info.append({
            "aria_posinset": aria_posinset,
            "aria_labelledby": aria_labelledby,
            "aria_describedby": aria_describedby,
            "describedby_ids": describedby_ids
        })

        # print(f"aria-posinset: {aria_posinset}")
        # print(f"aria-labelledby: {aria_labelledby}")
        # print(f"aria-describedby: {aria_describedby}")
        # print(f"describedby_ids: {describedby_ids}")

    # Bajarilgan ma'lumotlarni ko'rsatish
    print(f"Topilgan postlar soni: {len(posts)}")


    # Target classlar
    target_class = "x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz x1heor9g xkrqix3 x1sur9pj x1s688f"
    css_selector = '[tabindex="0"].' + ".".join(target_class.split())

    # Barcha post elementlarni Selenium orqali olish
    post_elements = driver.find_elements(By.XPATH, '//*[@aria-posinset]')

    print(f"Jami postlar soni: {len(post_elements)}")

    for idx, post in enumerate(post_elements, start=1):
        print(f"\n📌 Post {idx}")
        try:
            # Ichki elementlardan faqat 1-chi (agar mavjud bo‘lsa)
            inner_elements = post.find_elements(By.CSS_SELECTOR, css_selector)
            if inner_elements:
                print(f"  🔹 {inner_elements[0].text.strip()}")
            else:
                print("  ⚠️ Hech qanday mos element topilmadi.")
        except Exception as e:
            print(f"  ❌ Xatolik: {e}")

