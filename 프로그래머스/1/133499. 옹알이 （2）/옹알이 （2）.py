def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for sound in sounds:
            if sound * 2 in word:
                break
            word = word.replace(sound, " ")
        # print(word)
        if word.strip() == "":
            answer += 1
                
    return answer