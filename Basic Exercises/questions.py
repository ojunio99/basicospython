def questions():
    name = input('What is your name? ')
    print(f'Hi {name}, nice to meet you.')
    age = input('How old are you? ')
    print(f'So, your name is {name} and you are {age} years old?')

def yesorno():
    resposta = input("Please, answer with 'yes' or 'no': ").lower()
    if resposta == 'yes' or resposta == 'sim':
        print("Thank you for your time.")
    elif resposta == 'no' or resposta == 'nao':
        print("You answered no!")
        questions()
    else:
        print("Please, answer with 'yes' or 'no'.")
        yesorno()

questions()
# Chamar a função para fazer a pergunta
yesorno()
