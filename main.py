#! usr/bin/env python3
def make_user(user_name, user_age):
    user = {
        'name': user_name,
        'age': user_age
    }

    return user


def format_user(user):
    formated_user = f"{user['name']}, {user['age']}"
    return formated_user


ivan = make_user('ivan', 18)
print(ivan)
print(format_user(ivan))
