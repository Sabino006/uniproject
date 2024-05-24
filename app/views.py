from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import CustomUser
from app.models import GerarPedido
from app.models import Servicos
from django.contrib.auth import authenticate,login,logout
from app.forms import PedidoForms



def home(request):
    return render(request, 'login.html')

#Formulario de cadastro de clientes
def create_client(request):
    return render(request, 'dashboard/pages/create_cliente.html')

#Formulario de cadastro de admin
def create_admin(request):
    return render(request, 'dashboard/pages/create_admin.html')

#Formulario de cadastro de pedido
def create_pedido(request):
    return render(request, 'dashboard/pages/create_pedido.html')

#Formulario de login
def logar(request):
    return render(request, 'login.html')

#Pagina inicial do dashboard
def dashboard(request):
    cliente = CustomUser.objects.all()
    usuario = {
        'users': cliente
    }
    return render(request, 'dashboard/home_cliente.html', usuario)

def dashboard_admin(request):
    equipe = CustomUser.objects.all()
    usuario = {
        'users': equipe
    }
    return render(request, 'dashboard/home_admin.html', usuario)

def newpass(request):
    return render(request, 'dashboard/pages/newpass.html')

#Formulario de cadastro de serviço
def view_pedidos(request):
    pedidos = GerarPedido.objects.all()
    pedidos_view = {
        'view_pedidos': pedidos
    }
    return render(request, 'dashboard/pages/view_pedido.html', pedidos_view)

#Formulario de cadastro de serviço
def view_usuarios(request):
    usuarios_cadastrados = CustomUser.objects.all()
    verifica_usuarios = {
        'verifica_users': usuarios_cadastrados
    }
    return render(request, 'dashboard/pages/view_usuarios.html', verifica_usuarios)

#Inserção dos dados do admin
def criar_admin(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas são diferentes!'
        data['class'] = 'alert-danger'
    elif CustomUser.objects.filter(username=request.POST['user']):
        data['msg'] = 'Usuario já cadastrado'
        data['class'] = 'alert-danger'
    elif CustomUser.objects.filter(email=request.POST['email']):
        data['msg'] = 'e-mail já cadastrado'
        data['class'] = 'alert-danger'
    elif CustomUser.objects.filter(cpf_usuario=request.POST['cpf_usuario']):
        data['msg'] = 'CPF já cadastrado'
        data['class'] = 'alert-danger'
    else:
        user = CustomUser.objects.create_user(request.POST['user'],request.POST['email'], request.POST['password'])
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.cpf_usuario = request.POST['cpf_usuario']
        user.save()
        user.user_permissions.add(33,34)
        data['msg'] = 'Admin cadastrado com sucesso'
        data['class'] = 'alert-sucess'
    return render(request, 'dashboard/pages/create_admin.html',data)

#Inserção dos dados do cliente
def criar_cliente(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'As senhas são diferentes!'
        data['class'] = 'alert-danger'
    elif CustomUser.objects.filter(username=request.POST['user']):
        data['msg'] = 'Usuario já cadastrado'
        data['class'] = 'alert-danger'
    elif CustomUser.objects.filter(email=request.POST['email']):
        data['msg'] = 'e-mail já cadastrado'
        data['class'] = 'alert-danger'
    elif CustomUser.objects.filter(cpf_usuario=request.POST['cpf_usuario']):
        data['msg'] = 'CPF já cadastrado'
        data['class'] = 'alert-danger'
    else:
        user = CustomUser.objects.create_user(request.POST['user'],request.POST['email'], request.POST['password'])
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.cpf_usuario = request.POST['cpf_usuario']
        user.save()
        user.user_permissions.add(34)
        data['msg'] = 'Cadastro realizado com sucesso'
        data['class'] = 'alert-sucess'
    return render(request, 'dashboard/pages/create_cliente.html',data)

#Inserção dos dados do pedido
def criar_pedido(request):
    form = PedidoForms(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('/dashboard/')
    

    context = {
        'form': form
    }
    return render(request, 'dashboard/pages/create_pedido.html', context )

#Processar o login
def logando(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou senha incorreto'
        data['class'] = 'alert-danger'
        return render(request, 'login.html', data)       




#Deslogar
def logouts(request):
    logout(request)
    return redirect('/login/')

#Alterar senha
def changePassword(request):
    user = CustomUser.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/login/')


