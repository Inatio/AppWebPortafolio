from multiprocessing import AuthenticationError
from django.shortcuts import HttpResponse, render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views import View


from index.report import ReservaPDF
from index.models_new_3 import Usuario, Departamento, Reserva, Contacto, Disponibilidad, Pago
from index.forms import UsuarioRegisterForm, ReservaForm, ContactoForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        form = UsuarioRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['nombre']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UsuarioRegisterForm()

    context = { 'form' : form}
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method=="POST":
        try:
            detalleUsuario=Usuario.objects.get(correo=request.POST['correo'], contraseña=request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['correo']=detalleUsuario.correo
            return render(request, 'index.html')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Datos incorrectos')
    return render(request, 'accounts/login.html')

def logout(request):
    try:
        del request.session['correo']
    except:
        return redirect(request, 'index.html')
    return render(request, 'index.html')

def reservas(request):
    arriendos = Departamento.objects.all()
    disponible = Disponibilidad.objects.get(descr_estado="disponible")
    usuario = request.session['correo']
    reserva = Reserva.objects.filter(usuario__correo=usuario)
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(arriendos, 5)
        arriendos = paginator.page(page)
    except:
        raise Http404


    data = {
        'arriendos': arriendos,
        'disponible': disponible,
        'reserva': reserva
    }

    return render(request, "reservation/list.html", data)

class ContactView(SuccessMessageMixin, CreateView):
    form_class = ContactoForm
    model = Contacto
    template_name = 'contact.html'
    success_url = reverse_lazy('index')
    success_message = _('Mensaje')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ContactView, self).get_form_kwargs(*args, **kwargs)
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

class CrearReserva(SuccessMessageMixin, CreateView):

    form_class = ReservaForm
    model = Reserva
    template_name = 'reservation/reservar.html'
    success_url = reverse_lazy('listado')
    success_message = _('Reserva Creada')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(CrearReserva, self).get_form_kwargs(*args, **kwargs)
        return kwargs
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        valor = (obj.dias*obj.departamento.tarifa_diaria)
        valor_a_cobrar = (valor*0.30)
        Pago.objects.get_or_create(pago_inicial=valor_a_cobrar)
        obj.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    

class ReservaPDFView(View):
    """
    Imprimir Reserva
    """
    def get(self, request, **kwargs):
        # Obtenemos empresa asociada
        usuario_on = request.session['correo']
        usuario = Usuario.objects.filter(correo=usuario_on)
        reserva = Reserva.objects.get()

        r = ReservaPDF(
            reserva=reserva
        )
        return r.pdf_response()

def payment(request):
    return render(request, 'reservation/payment.html')
