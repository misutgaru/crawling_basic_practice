import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Whale/4.33.325.17 Safari/537.36'
}

# 7개 정보를 담을 빈 리스트 만들기
number = []
name = []
position = []
age = []
nation = []
team = []
value = []

player_list = []

for i in range(1, 3):

    url = f"https://www.transfermarkt.com/marktwerte/wertvollstespieler/marktwertetop?page={i}"

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser') # r.content 대신 r.text도 가능

    # 선수들의 정보가 담긴 태그와 클래스 찾기
    player_info = soup.find_all('tr', class_=['odd', 'even'])

    # 첫번째 요소 확인하기
    # print(player_info[0])

    # 전체 개수 확인하기
    # print(len(player_info))

    # player_info 에서 td 태그만 모두 찾기
    for info in player_info:
        player = info.find_all('td')
        # print(player)
        # print(player[0])

        # 해당 정보를 찾아서 각 리스트에 .append로 추가하기
        # number.append(player[0].text)
        # name.append(player[3].text)
        # position.append(player[4].text)
        # age.append(player[5].text)
        # nation.append(player[6].img['alt'])
        # team.append(player[7].img['alt'])
        # value.append(player[8].text.strip())

        player_list.append([player[0].text, player[3].text, player[4].text, player[5].text, player[6].img['alt'], player[7].img['alt'], player[8].text.strip()])

    time.sleep(1)

df2 = pd.DataFrame(player_list, columns=['Number', 'Name', 'Position', 'Age', 'Nation', 'Team', 'Value'])
print(df2)
df2.to_csv('transfermarkt50.csv', index=False)

# df = pd.DataFrame(
#     {
#         'number': number,
#         'name': name,
#         'position': position,
#         'age': age,
#         'nation': nation,
#         'team': team,
#         'value': value
#     }
# )
# print(df)

# df.to_csv('transfermakt25.csv', index=False)