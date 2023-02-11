# 끝말잇기 단어 리스트 주어질 때, 몇 번째 사람이 탈라하는지 확인하라

words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

num =int(len(words)) #7

for i in range(1,num):
    if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
        print(f'탈락한 사람: {i+1}번째 사람')


 # 중복 단어  words[i] in words[:i]