import requests
from bs4 import BeautifulSoup

url = 'https://boards.greenhouse.io/sidewalklabs#.WAfElZMrIXp'
board = requests.get(url)

soup = BeautifulSoup(board.content, 'html.parser')

eng_jobs = soup.find_all(department_id="24990")


for eng_job in eng_jobs:
    title = eng_job.find('a', href_="")
    location = eng_job.find('span', class_="location")
    link = eng_job.find('a')['href']

    print(title.text)
    print(location.text)
    print("https://boards.greenhouse.io{}".format(link))
    print()
