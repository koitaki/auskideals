from django.shortcuts import render
from email_collector.models import ProspectiveUser

def handle_form(request):
    if request.method == 'GET':
        return render(request, 'email_collector/index.html')
    if request.method == 'POST':
        user = ProspectiveUser(email_address=request.POST['email_address'])
        user.save()
        return render(request, 'email_collector/index.html', {'data': user })