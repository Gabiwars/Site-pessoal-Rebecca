from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})



def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # Pegando o que o usuario digitou e colocando em uma lista
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send an email

        contato = "Name: " + message_name + " Email: " + message_email + " Menssagen: " + message

        send_mail(
            'Contato pelo site',
            contato,  # subject (nome da pessoa que esta enviando o email)   message (mensagem que a pessoa escrever)
            message_email,  # from email (do email da pessoa)
            ['rebeccasiteteste@gmail.com'],  # to email (para esse email)
            )

        return render(request, 'contact.html', {'message_name': message_name})  # Depois vai retornar uma mensagem que vai ser o nome
                # da pessoa. Retornando a pagina contact.html e o key do dicionario que eh message_name que vai ser o nome

    else:
        return render(request, 'contact.html', {})  # Caso a pessoa nao digite nada vai aparecer apena a pagina contact.html


def about(request):
    return render(request, 'about.html', {})


def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_message = request.POST['your-message']

        # send an email
        appointment = "Name: " + your_name + " Phone: " + your_phone + " Email: " + your_email + " Address: " + your_address + " Message: " + your_message

        send_mail(
            'Appointment Request',  # subject (nome da pessoa que esta enviando o email)
            appointment,  # message (mensagem que a pessoa escrever)
            your_email,  # from email (do email da pessoa)
            ['rebeccasiteteste@gmail.com'],  # to email (para esse email)
            )

        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_message': your_message})

    else:
        return render(request, 'home.html', {})  # Caso a pessoa nao digite nada vai aparecer apena a pagina contact.html

