## 죽음의 행맨 게임
"😁죽음의 행맨 게임에 오신 여러분 환영 합니다🎰."

word_categories = {
    "food": ["pizza", "salad", "cheese", "apple", "bread"],
    "animals": ["sheep", "horse", "snake", "tiger", "panda"],
    "objects": ["chair", "phone", "clock", "table", "brush"],
    "feelings": ["happy", "angry", "tired", "scared", "sad"],
    "colors": ["green", "black", "white", "brown", "pink"],
    "jobs": ["nurse", "chef", "pilot", "baker", "actor"] }


while True:
    print("😁🤞")
    print("👉 선택 가능한 주제 종류:")
    for subject in word_categories :
        print(f"{subject}")

    print ( "원하시는 게임의 주제를 선택하시오.")
    user_choice = input()

    if user_choice in word_categories :
        