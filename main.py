from src.utils import user_choice_hh


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    print('Здравствуйте! \n'
          'Эта программа поможет Вам в поиске вакансий на сайте HeadHunter.  \n'
          'Введите "start" для начала работы или "stop" для завершения\n')

    while True:
        user_choice_platform = input()
        if user_choice_platform == 'start':
            user_choice_hh()
            break
        elif user_choice_platform == 'stop':
            print('До свидания')
            break
        else:
            print('Неверный запрос')
            break


if __name__ == '__main__':
    user_interaction()
