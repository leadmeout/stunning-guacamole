from django.shortcuts import render
from .forms import TariffCalcForm
from utils.calculator import result_generator


def index(request):

    form = TariffCalcForm
    context = {'form': form}
    return render(request, 'clickapp/index.html', context)


def result(request):

    form = TariffCalcForm(request.POST)
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            return render(request, 'clickapp/result.html', context)
    else:
        return render(request, 'clickapp/index.html', context)
