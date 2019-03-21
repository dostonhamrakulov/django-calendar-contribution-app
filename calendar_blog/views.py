from django.shortcuts import render
import json

months = [
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
    {
        'month': 'CoreyMS'
    },
]


# calendar_post = {
#     {
#         'month': 'January',
#         '1':'green',
#         '2':'green',
#         '3':'green',
#         '4':'green',
#         '5':'green',
#         '6':'green',
#         '7':'green',
#         '8':'green',
#         '9':'green',
#         '10':'green',
#         '12':'green',
#         '13':'green',
#         '14':'green',
#         '15':'green',
#         '16':'green',
#         '17':'green',
#         '18':'green',
#         '19':'green',
#         '20':'green',
#         '21':'green',
#         '22':'green',
#         '23':'green',
#         '24':'green',
#         '25':'green',
#         '26':'green',
#         '27':'green',
#         '28':'green',
#         '29':'green',
#         '30':'green',
#         '31':'green'
#     }
# }

# jauary1 = [
#     {
#         'month':'January',
#         'day':'1',
#         'done':'white',
#         'hours':'3',
#     },
#     {
#         'month':'January',
#         'day':'2',
#         'done':'red',
#         'hours':'3',
#         'title':'Deutsch Learnen'
#     }
# ]
# months = ["Yanvar", "Fevral", "Mart"]

with open('calendar_blog/deutsch_oy_1.json') as f:
    json_01_ = json.load(f)

with open('calendar_blog/deutsch_oy_2.json') as f:
    json_02_ = json.load(f)

with open('calendar_blog/deutsch_oy_3.json') as f:
    json_03_ = json.load(f)

with open('calendar_blog/deutsch_oy_4.json') as f:
    json_04_ = json.load(f)

with open('calendar_blog/deutsch_oy_5.json') as f:
    json_05_ = json.load(f)

with open('calendar_blog/deutsch_oy_6.json') as f:
    json_06_ = json.load(f)

with open('calendar_blog/deutsch_oy_7.json') as f:
    json_07_ = json.load(f)

with open('calendar_blog/deutsch_oy_8.json') as f:
    json_08_ = json.load(f)

with open('calendar_blog/deutsch_oy_9.json') as f:
    json_09_ = json.load(f)

with open('calendar_blog/deutsch_oy_10.json') as f:
    json_10_ = json.load(f)

with open('calendar_blog/deutsch_oy_11.json') as f:
    json_11_ = json.load(f)

with open('calendar_blog/deutsch_oy_12.json') as f:
    json_12_ = json.load(f)



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'calendar_blog/home.html', context)


def about(request):
    return render(request, 'calendar_blog/about.html', {'title': 'About'})

def calendarr(request):
    context = {
    'january_19':json_01_["deutsch"],
    'fevral_19':json_02_["deutsch"],
    'mart19':json_03_["deutsch"],
    'april19':json_04_["deutsch"],
    'may19':json_05_["deutsch"],
    'iyun19':json_06_["deutsch"],
    'iyul19':json_07_["deutsch"],
    'avgust19':json_08_["deutsch"],
    'sentabr19':json_09_["deutsch"],
    'oktabr19':json_10_["deutsch"],
    'noyabr19':json_11_["deutsch"],
    'dekabr19':json_12_["deutsch"]
    }
    return render(request, 'calendar_blog/calendar.html', context)
