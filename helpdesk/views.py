from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm


def index(request):
    Tickets = Ticket.objects.order_by('-id')
    return render(request, 'helpdesk/index.html', {'title': 'Главная ептыть нах', 'tasks': Tickets})


def about(request):
    return render(request, 'helpdesk/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TicketForm()
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'helpdesk/create.html', contex)
