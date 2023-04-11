from django.shortcuts import render, redirect
from .forms import HistoryForm
from .models import History
import qrcode

# Create your views here.
def new(request):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        form_is_valid = form.is_valid()
        if form_is_valid:
            data = form.save()
            print (data.id)
        return redirect("history/"+str(data.id))
    else:
        form = HistoryForm()
    return render(request=request, template_name='new_history.html', context={"form":form})

def history(request, id):
    history = History.objects.filter(pk=id)
    url =  request.get_host() + "/history/"+str(id)
    image = qrcode.make(url)
    nombre_imagen = "./clinic_history/static/images/qr.png"
    with open(nombre_imagen, "wb") as archivo_imagen:
        image.save(archivo_imagen)
    return render(request=request, template_name='history.html', context={"history":history, "qr": nombre_imagen})