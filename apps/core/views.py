from django.shortcuts import render

# HJEMME
def hjemme(request):
    return render(request, 'core/home.html')
# SIDER

    # INFO
def info(request):
    return render(request, 'pages/info/info.html')
        # ÅPNINGSTIDER
def openhours(request):
    return render(request, 'pages/info/openhours.html')
        # RULES
def rules(request):
    return render(request, 'pages/info/rules.html')
        # ABOUT
def about(request):
    return render(request, 'pages/info/about.html')
        # SPONSORS
def sponsors(request):
    return render(request, 'pages/info/sponsors.html')
        # PARENT
def parent(request):
    return render(request, 'pages/info/parent.html')

    # TJENESTER
        # LAN&BD
def lan(request):
    return render(request, 'pages/tjenester/lan.html')
        # LEIE UTSTYR
def rent_items(request):
    return render(request, 'pages/tjenester/rent-items.html')
        # LEIE LOKALET
def rent_place(request):
    return render(request, 'pages/tjenester/rent-place.html')
        # SKOLEUNDERVISNING
def school(request):
    return render(request, 'pages/tjenester/school.html')

    # ESPORT
        # KURS
def esport_course(request):
    return render(request, 'pages/esport/course.html')
        # ARRANGAMENTER
def events(request):
    return render(request, 'pages/esport/events.html')
        # GALLERI
def esport_galleri(request):
    return render(request, 'pages/esport/gallery.html')
        # SPILL & KONSOLLER
def spill_konsoller(request):
    return render(request, 'pages/esport/games.html')
        # TURNERINGER
def turneringer(request):
    return render(request, 'pages/esport/tournaments.html')

    # KUNST
        # KURS
def art_course(request):
    return render(request, 'pages/kunst/course.html')
        # GALLERI
def art_galleri(request):
    return render(request, 'pages/kunst/gallery.html')
        # VÅR AVDELING
def our_art(request):
    return render(request, 'pages/kunst/our-art.html')

    # KONTAKT
def contact(request):

    # if request.method=='POST' and 'contact' in request.POST:
    #     navn = request.POST.get('navn')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')

    #     data = {
    #         'navn': navn,
    #         'email': email,
    #         'message': message,
    #     }
    #     message = dedent('''
    #     Fra: {}

    #     Navn: {}

    #     Beskjed: {}
    #     ''').format(data['email'], data['navn'], data['message'], )
    #     send_mail('Webiser Contact Form', message, '', ['sabertoothtri@gmail.com'])
    #     return redirect('/email-success')

    return render(request, 'pages/contact/contact.html')  

    # PRISER
def prices(request):
    return render(request, 'pages/prices/prices.html')