import pandas as pd

df = pd.read_csv('transfermarkt50.csv')

# 인덱스로 정렬하기
# df.head()
# print(df.sort_index().head())

# 내람차순으로 정리하기
# print(df.sort_index(ascending=False).head())

# sort_values로 정렬하기
# 나이많은 선수 10명 보여주기
# print(df.sort_values('Age'))

# 인덱스를 칼럼 이름으로 바꾸기
# print(df.set_index('Number'))

# 칼럼 이름 바꾸고 저장하기
# Team을 Club으로 바꾸기
# df.rename(columns={'Team':'Club'}, inplace=True) # inplace = False 는 변경된 값을 저장 X
# print(df.head())

# 데이터 전처리
df['Value'] = df['Value'].str.replace('€', '')
df['Value'] = df['Value'].str.replace('m', '').astype('float')
# print(df['Value'].head())

# 새로운 컬럼 만들기
df['시장 가치(억)'] = df['Value']*13

# 칼럼 삭제
df.drop(columns=['Value'], inplace=True)
# print(df.head())

# 통계분석
# print(df.describe()) # 숫자형 데이터에 관한 통계치

# 평균
# print(df['Age'].mean())

# 몸값 합계
# print(df['시장 가치(억)'].sum())

# 선수들이 속한 가장 많은 나라? 최다 빈도 값
# print(df['Nation'].mode())

# 국적이 브라질인 선수?
# print(df[df['Nation'] == 'Brazil'])

# 데이터를 그룹으로 묶어 분석
# g = df.groupby('Nation')
# print(g.size())
# print(g.sum())
# print(g['시장 가치(억)'].sum())

# 시장 가치가 큰 Team 순으로 정렬
c = df.groupby('Team')
print(c['시장 가치(억)'].sum().sort_values(ascending=False))