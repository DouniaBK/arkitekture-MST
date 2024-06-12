from django.shortcuts import render


def home_view(request):
    return render(request, 'home/home.html')


def about_view(request):
    return render(request, 'home/about.html')


def services_view(request):
    return render(request, 'home/services.html')


def contact_view(request):
    return render(request, 'home/contact.html')


def portfolio_view(request):
    return render(request, 'home/portfolio.html')


def footer_view(request):
    return render(request, 'home/footer.html')


def terms_view(request):
    return render(request, 'home/terms.html')


def privacy_view(request):
    return render(request, 'home/privacy.html')


def disclaimer_view(request):
    return render(request, 'home/disclaimer.html')


def impressum_view(request):
    return render(request, 'home/impressum.html')


def projectone_view(request):
    return render(request, 'home/projectone.html')


def projecttwo_view(request):
    return render(request, 'home/projecttwo.html')
