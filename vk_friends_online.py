import vk
import getpass
import os


def get_application_id():
    return os.environ.get('ONLINE_WATCHER_VK_ID')


def get_online_friends(login, password):
    app_id = get_application_id()
    session = vk.AuthSession(
        app_id=app_id,
        user_login=login,
        user_password=password,
        scope='friends'
    )
    api = vk.API(session)
    friend_ids = api.friends.getOnline(
        fields=['first_name', 'last_name']
    )
    friends = api.users.get(
        user_ids=friend_ids
    )
    return friends


def output_friends_online(friends_data):
    for friend in friends_data:
        print(
            '{} {}'.format(
                friend['first_name'],
                friend['last_name']
            )
        )


if __name__ == '__main__':
    login = input('Login: ')
    password = getpass.getpass(prompt='Password: ')
    try:
        friends_online = get_online_friends(login, password)
        if not friends_online:
            print('There are no any friend currently online')
        else:
            print('These friends are currently online:')
            output_friends_online(friends_online)
    except vk.AuthSession:
        exit('Authentication error')
