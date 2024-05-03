import requests
from bs4 import BeautifulSoup

from lib.formulate import formulate_data


def crawl_music():
    html = requests.get('https://namu.wiki/w/%EC%A0%80%EC%9D%8C/%EB%85%B8%EB%9E%98%20%EB%AA%A9%EB%A1%9D').text
    soup = BeautifulSoup(html, 'html.parser')


    tables = soup.select(
        '#app > div > div._1XS3A-J6 > div.mZDlmqYb > div > div.LVWdlGyI > div > div:nth-child(2) > div > div > div:nth-child(9)')
    woman = soup.select(
        '#app > div > div._1XS3A-J6 > div.mZDlmqYb > div > div.LVWdlGyI > div > div:nth-child(2) > div > div > div:nth-child(11)')
    woman = woman[0].find_all('table', class_='wiki-table')

    data = []
    for table in tables:
        arrays = table.find_all('table', class_='wiki-table')
        arrays.append(woman[0])
        for arr in arrays:
            tmp = arr.find_all('div', class_='wiki-paragraph')
            if tmp[4].text == "최고음" or tmp[3].text == "최고음":
                i = 5 if tmp[4].text == "최고음" else 4
                gender = 0 if tmp[4].text == "최고음" else 1
                while True:
                    if i == len(tmp):
                        break
                    if tmp[i].text:
                        singer = tmp[i].text
                        song = tmp[i + 1].text
                        lowest_note = tmp[i + 2].text.split("(")[1].replace(")", "").strip()
                        highest_note = tmp[i + 3].text.split("(")[1].replace(")", "").strip()
                        youtube_url = f"https://www.youtube.com/results?search_query={singer}+{song}"
                        data.append(formulate_data(singer, song, highest_note, lowest_note, gender, youtube_url))
                    else:
                        i += 1
                        continue
                    i += 4
            else:
                highest_note = tmp[0].text.split("(")[1].replace(")", "").strip()
                for i in range(4, len(tmp), 3):
                    singer = tmp[i].text
                    song = tmp[i + 1].text
                    lowest_note = tmp[i + 2].text.split("(")[1].replace(")", "").strip()
                    youtube_url = f"https://www.youtube.com/results?search_query={singer}+{song}"
                    data.append(formulate_data(singer, song, highest_note, lowest_note, 0, youtube_url))

    return data