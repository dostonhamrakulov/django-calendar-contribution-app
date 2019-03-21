from django.shortcuts import render
import json

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
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
months = ["Yanvar", "Fevral", "Mart"]

with open('calendar_blog/deutsch.json') as f:
    deutsch_json_parsed = json.load(f)


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'calendar_blog/home.html', context)


def about(request):
    return render(request, 'calendar_blog/about.html', {'title': 'About'})

def calendarr(request):
    context = {
    'deutsch_json':deutsch_json_parsed["deutsch"],
    'month':'Yanvar'
    }
    return render(request, 'calendar_blog/calendar.html', context)
