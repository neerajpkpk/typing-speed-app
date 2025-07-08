from django.shortcuts import render

import random
from django.shortcuts import render,redirect
from .story_data import story_dict

def home_view(request):
    # If user has provided custom text
    if request.session.get('from_custom'):
        paragraph = request.session.get('custom_text')
        difficulty = "custom"
        request.session['from_custom'] = False  # only once use
    else:
        from .story_data import story_dict
        import random
        keys = list(story_dict.keys())
        last_key = request.session.get('last_story_key')
        available_keys = [k for k in keys if k != last_key]
        selected_key = random.choice(available_keys if available_keys else keys)
        selected_story = story_dict[selected_key]
        request.session['last_story_key'] = selected_key
        paragraph = selected_story['text']
        difficulty = selected_story['difficulty']

    return render(request, 'testapp/home.html', {
        'paragraph': paragraph,
        'difficulty': difficulty,
    })


def custom_text_view(request):
    if request.method == 'POST':
        user_text = request.POST.get('user_text')
        if user_text:
            request.session['custom_text'] = user_text
            request.session['from_custom'] = True
            return redirect('home')
    return render(request, 'testapp/custom_input.html')

# testapp/views.py



def default_text_view(request):
    return redirect('home')  # ya render custom paragraph if needed



from django.core.management import call_command
from django.contrib.auth.models import User

def setup_view(request):
    # Run migrations
    call_command('migrate')

    # Create superuser if not exists
    if not User.objects.filter(username='neerajguptaji').exists():
        User.objects.create_superuser('neerajguptaji', 'neerajyes05@gmail.com', 'Asdf#123456')

    return HttpResponse("✔️ Migration done and superuser created.")
