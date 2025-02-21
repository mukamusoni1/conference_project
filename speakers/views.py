from django.shortcuts import render

# Create your views here.
  speakers = [
        {'name': 'Emerance', 'bio' : 'IT support', 'contact': '0783243222', 'id': 1},
        {'name': 'Gratia', 'bio' : 'IT support', 'contact': '0783243222', 'id': 2},
        {'name': 'Nadjima', 'bio' : 'IT support', 'contact': '0783243222', 'id': 3},
        {'name': 'Joana', 'bio' : 'IT support', 'contact': '0783243222', 'id': 4},
        {'name': 'James', 'bio' : 'IT support', 'contact': '0783243222', 'id': 5},
    ]
def speaker_list(request):
    return render(request, 'speakers/speaker_list.html', {'speakers': speakers})
def create_speaker(request):
    return render(request, 'speakers/create_speaker.html')
def speaker_details(request, speaker_id):
    return render(request, 'speakers/speaker_details.html', {'speakers': speakers})
def update_speaker(request, speaker_id):
    return render(request, 'speakers/update_speaker.html', {'speakers': speakers})
def delete_speaker(request, speaker_id):
    return render(request, 'speaker/delete_speaker.html', {'speakers': speakers})