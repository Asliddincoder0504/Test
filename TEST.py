import json

def savolni_yuklash():
    with open('tests.json', 'r') as file:
        return json.load(file)


def save_user(user):
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        users = []

    user_exists = False
    for existing_user in users:
        if existing_user['name'] == user['name'] and existing_user['surname'] == user['surname']:
            existing_user['score'] = user['score']
            user_exists = True
            break

    if not user_exists:
        user.append(user)

    users = sorted(users, key=lambda x: x.get('score', 0), reverse=True)

    with open('users.json', 'r') as file:
        json.dump(users, file)


def display_rating():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Reyting hali mavjud emas")
        return

    print("\n Ishtirokchilar reytingi:")
    print(f"{'O`rin':<6}{'Ism':<15}{'Familya':<15}{'Ball':<6}")
    for idx, user in enumerate(users[:10], start=1):
        print(f"{idx:<1}|{user['name']:<15}{user['surname']:<15}|{user['score']:<6}")


def start_quiz():
    if 'name' not in globals() or 'surname' not in globals():
        global name, surname
        print("Testga xush kelibsz!")
        name = input("Ismingizni kiriting: ")
        surname = input("Familyangizni  kiriting: ")
    questions = savolni_yuklash()
    score = 0

    for i, question in enumerate(questions):
        print(f"\nSavol {i + 1}:{question['question']}")
        for idx, answer in enumerate(question['answers']):
            print(f"{idx + 1}. {answer['key']}")
        while True:
            user_input = input("Javob raqamini kiriting (yoki) 'h' yordam uchun: ")

            if user_input.lower() == 'h':
                print("Yordam! Ikki no'to'g'ri javob olib tashlanadi: ")
                incorrect = [idx for idx, answer in enumerate(question['answer']) if not answer['istrue']]
                incorrect = incorrect[:2]
                for idx in incorrect:
                    print(f"{idx + 1}.{question['answers']['key']}")
            elif user_input.isdigit() and 1 <= int(user_input) <= len(question['answers']):
                selected_answer = question['answers'][int(user_input) - 1]
                if selected_answer['isTrue']:
                    print("To'g'ri! Keyingi savolga o'tilmoqda")
                    score += 1
                    break
            else:
                print("Noto'g'ri! Testdan chiqilmoqda")

    save_user({"name": name, "surname": surname, "score": score})


def main():
    while True:
        print("\nAsosiy menyu:")
        print("1. Testni boshlash")
        print("2. Reyting")
        print("0. Chiqish")

        choice = input("Tanlovingizni kiriting: ")

        if choice == '1':
            start_quiz()
        elif choice == '2':
            display_rating()
        elif choice == '0':
            print("Dasturdan chiqilmoqda.")
            break
        else:
            print("To`g`ri tanlovni kiriting.")

if __name__ == "__main__":
    main()


