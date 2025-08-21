import pandas as pd

# 저장된 파일 불러오기
df = pd.read_csv('transfermarkt50.csv')
# print(df)

# print(df.shape) # (행, 열)
# print(df.info())
# print(df.head()) # 앞에서부터 (default=5)개 조회 = df[0:5]
# print(df.tail()) # 뒤에서부터 (default=5)개 조회
# print(df[['Number', 'Name']].head())

# print(df.iloc[0:2])
# print(df.loc[0, 'Name']) # 첫 번째 행의 이름이 Name인 값
# print(df.loc[0:5, ['Name', 'Team']]) # 행은 처음부터 5까지. 열은 Name, Team인 값

# print(df['Age'] <= 20) # True, False로 표기
# print(df[df['Age'] <= 20]) # 나이가 20 이하인 선수
# print(df[df['Team'] == 'Real Madrid']) # 소속팀이 레알 마드리드인 선수

# Q. loc 조건으로 나이가 30 이상인 선수의 Name, Value
# print(df.loc[df['Age'] >= 30, ['Name', 'Value']])