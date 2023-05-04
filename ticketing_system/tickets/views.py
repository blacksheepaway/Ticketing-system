from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Ticket

def ticket_overview(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_overview.html', {'tickets': tickets})


@login_required
def profile(request):
    return render(request, 'tickets/profile.html')

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

@login_required
def ticket_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        ticket = Ticket(title=title, description=description, user=request.user)
        ticket.save()
        return redirect('ticket_detail', pk=ticket.pk)
    return render(request, 'tickets/ticket_create.html')

@login_required
def ticket_update(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket.title = request.POST['title']
        ticket.description = request.POST['description']
        ticket.save()
        return redirect('ticket_detail', pk=ticket.pk)
    return render(request, 'tickets/ticket_update.html', {'ticket': ticket})
