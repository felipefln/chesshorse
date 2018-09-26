from django.shortcuts import render
from chesshorse.core.board import Board

# Create your views here.
def index(request):
    context = {}
    if request.method == 'POST':
        position = request.POST.get('position')
        list_positions = Board.get_result(position)
        context['result'] = list_positions

    return render(request, 'index.html', context=context)
