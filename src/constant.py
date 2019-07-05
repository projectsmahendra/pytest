api_url_user_prefix = '/api/v1/user'
api_url_user_list = "/list"
api_url_user = "/<int:user_id>"
api_url_user_register = "/register"


def test(**kwargs):
    for key, value in kwargs.items():
        print("key={}--value={}".format(key, value))


data = {
    "one": "1",
    "two": "2",
    "three": "3"
}

import os

# print(__dict__)
# print(os.path.abspath(__file__))
# print(data.items())
# for key, value in data.items():
    # print(key+"---"+value)
# test(**data)


def hi(*asdf,**sdf):
    print(type(asdf))
    print(type(sdf))

hi(1,2,3,a=1,b=2)