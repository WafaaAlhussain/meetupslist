from django.shortcuts import render

# Create your views here.


def index(request):
    meetups = [
        {'title': 'A First Meetup', 'location': 'Tokyo', 'slug': 'a-first-meeting'},
        {'title': 'A Second Meetup', 'location': 'England', 'slug': 'a-second-meeting'},
        {'title': 'A Third Meetup', 'location': 'Istanbul', 'slug': 'a-third-meeting'}
    ]
    return render(request, 'meetups/index.html', {'meetups': meetups})


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meeting',
    }
    return render(request, 'meetups/meetup_details.html', {'meetup': selected_meetup})
