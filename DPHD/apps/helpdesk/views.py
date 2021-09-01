from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm


@login_required
def index(request):
    Tickets = Ticket.objects.order_by('-id')
    return render(request, 'helpdesk/index.html')


def adm(request):
    return render(request, 'helpdesk/adm/panel.html')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return render(request, 'registration/logged_out.html')


@login_required
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
