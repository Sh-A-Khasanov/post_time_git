from bs4 import BeautifulSoup
import re

# HTML faylni ochamiz va o'qib olamiz
with open("Facebook2.html", "r", encoding="utf-8") as file:
    html = file.read()

# BeautifulSoup orqali parse qilamiz
soup = BeautifulSoup(html, 'html.parser')

posts = soup.find_all(attrs={"aria-posinset": True})
aria_info = []

# posts1 = driver.find_elements(By.CSS_SELECTOR, "[aria-posinset]")
# print(posts)
for post in posts:

    # print(f"{post}\n\n")
    aria_labelledby = post.get("aria-labelledby")
    aria_posinset = post.get("aria-posinset")
    aria_describedby = post.get("aria-describedby", "")
    describedby_ids = aria_describedby.split()

    # Har bir IDni nomlaymiz (agar mavjud bo‘lsa)
    id_1 = describedby_ids[0] if len(describedby_ids) > 0 else None
    id_2 = describedby_ids[1] if len(describedby_ids) > 1 else None
    id_3 = describedby_ids[2] if len(describedby_ids) > 2 else None
    id_4 = describedby_ids[3] if len(describedby_ids) > 3 else None
    id_5 = describedby_ids[4] if len(describedby_ids) > 4 else None
    print(f"1 - {id_1}")
    print(f"2 - {id_2}")
    print(f"3 - {id_3}")
    print(f"4 - {id_4}")
    print(f"5 - {id_5}")
    # print(f"aria_labelledby : {aria_labelledby}")
        

    # ID bo'yicha divni topamiz (bu yerda h3)
    target_h3 = soup.find("h3", id=aria_labelledby)

    # h3 ichidagi span ichidagi matnni olamiz
    name_tag = target_h3.find("span", class_="html-span") if target_h3 else None
    name_text = name_tag.get_text() if name_tag else "Ism topilmadi"
    name_text = ' '.join(name_text.split())
    print(f"{aria_labelledby} id bilan bog'liq ism: {name_text}")



    # id bo'yicha time_text divni topamiz
    target_div = soup.find("div", id=id_1)
    # div ichidagi <span> ni topib, uning matnini olamiz
    time_tag = target_div.find("span") if target_div else None
    time_text = time_tag.get_text() if time_tag else "time_text topilmadi"
    print(f"{id_1} time_text : {time_text}")

    # id bo'yicha kerakli divni topamiz
    target_div = soup.find("div", id=id_1)
    # div ichidagi <a> ni topib, href atributini olamiz
    a_tag = target_div.find("a") if target_div else None
    link = a_tag['href'] if a_tag and a_tag.has_attr('href') else "Silka topilmadi"
    # id bo'yicha kerakli divni topamiz
    target_div = soup.find("div", id=id_1)
    print(f"{id_1} - Topilgan link:", link)

    # id bo'yicha post_text divni topamiz
    target_div = soup.find("div", id=id_2)
    if target_div:
        # div ichidagi <a> tegini topamiz (agar URL bo'lsa)
        link_tag = target_div.find("a")
        if link_tag and link_tag.get("href"):
            # To'liq URLni href atributidan olamiz
            full_url = link_tag["href"]
            post_text = full_url
        else:
            # Agar <a> tegi bo'lmasa, oddiy matnni olamiz
            post_tag = target_div.find("div")
            post_text = post_tag.get_text() if post_tag else "user posti topilmadi"
    else:
        post_text = "user posti topilmadi"

    # Bosh va oxirgi bo'shliqlarni olib tashlash va ortiqcha bo'shliqlarni bitta bo'shliq bilan almashtirish
    post_text = ' '.join(post_text.split())
    print(f"URLda link bo'lsa - {id_2} - text: {post_text}\n\n\n")





    # id bo'yicha post_text divni topamiz
    # # target_div = soup.find("div", id=id_2)
    # div ichidagi <span> ni topib, uning matnini olamiz
    # post_tag = target_div.find("div") if target_div else None
    # post_text = post_tag.get_text() if post_tag else "user posti topilmadi"
    # # Bosh va oxirgi bo'shliqlarni olib tashlash va ortiqcha bo'shliqlarni bitta bo'shliq bilan almashtirish
    # post_text = ' '.join(post_text.split())
    # print(f"{id_2} - text: {post_text}\n\n\n")



    # id bo'yicha kerakli divni topamiz
    target_div = soup.find("div", id=id_4)
    # div ichidagi <a> ni topib, href atributini olamiz
    a_tag = target_div.find("a") if target_div else None
    link = a_tag['href'] if a_tag and a_tag.has_attr('href') else "Post rasm Silka topilmadi"
    # id bo'yicha kerakli divni topamiz
    target_div = soup.find("div", id=id_4)
    print(f"{id_4} - Post rasm link:", link)










    print(f"aria-posinset ------------- {aria_posinset}")
# Stringni raqamga aylantirib, taqqoslash
    if aria_posinset is not None and int(aria_posinset) == 5:
        break


    
