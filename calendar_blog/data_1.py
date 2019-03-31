from django.shortcuts import render
import json

posts = [
    {
        'author': 'Doston Hamrakulov',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Bucky Rober',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Bucky Rober',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    },
    {
        'author': 'Doston H',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2016'
    },
    {
        'author': 'D Hamrakulov',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2013'
    },
    {
        'author': 'Bucky Rober',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

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

def contact(request):
    return render(request, 'calendar_blog/contact.html', {'title': 'Contact'})

def source_code(request):
    return render(request, 'calendar_blog/source_code.html', {'title': 'Contact'})



# this yerdan    
