from django.shortcuts import render, get_object_or_404
from .models import Educational


def all_educational(request):
    Insights = Educational.objects.order_by('-date')
    return render(request, 'Educational/all_educational.html', {'Insights':Insights})


def detail(request, Insight_id):
    Insight = get_object_or_404(Educational, pk= Insight_id)
    return render(request, 'Educational/detail.html',{'Insight':Insight})
