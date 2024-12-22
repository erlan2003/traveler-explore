
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from home.forms import RegisterForm
from django.shortcuts import render
from .models import Attraction
from .forms import AttractionForm
from django.http import JsonResponse

def attraction_detail(request, pk):
    attraction = get_object_or_404(Attraction, pk=pk)
    return render(request, 'attraction-detail.html', {'attraction': attraction})

def home(request):
    return render(request, 'home.html')


def tours(request):
    return render(request, 'tours.html')

# def attractions(request):
#      if request.method == 'POST':
#         form = AttractionForm(request.POST, request.FILES)
#         if form.is_valid():
#             attraction = form.save(commit=False)
            
#             # Обработка загружаемого файла
#             image = request.FILES.get('image_path')
#             if image:
#                 image_base64 = base64.b64encode(image.read()).decode('utf-8')
#                 attraction.image_path = image_base64
            
#             attraction.save()
#             return redirect('attractions')
#         else:
#             form = AttractionForm()
#         attractions = Attraction.objects.all()
#         return render(request, 'attractions.html',{'attractions': attractions, 'form': form})


def attractions(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST, request.FILES)
        if form.is_valid():
            attraction = form.save(commit=False)
            
            # Обработка загружаемого файла
            image = request.FILES.get('image_path')
            if image:
                image_base64 = base64.b64encode(image.read()).decode('utf-8')
                attraction.image_path = image_base64

            attraction.save()
            return JsonResponse({'message': 'Достопримечательность успешно добавлена'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
       
    else:
        form = AttractionForm()

    attractions = Attraction.objects.all()
    return render(request, 'attractions.html', {'attractions': attractions, 'form': form})


def about(request):
    return render(request, 'about.html')

def profile_view(request):
    return render(request, 'profile.html')

def contact(request):
    return render(request, 'contact.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


import base64

def add_attraction(request):
    if request.method == 'POST':
        form = AttractionForm(request.POST, request.FILES)
        if form.is_valid():
            attraction = form.save(commit=False)
            
            # Обработка загружаемого файла
            image = request.FILES.get('image_path')
            if image:
                image_base64 = base64.b64encode(image.read()).decode('utf-8')
                attraction.image_path = image_base64

            attraction.save()
            return redirect('attractions')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    elif request.method == 'GET':  # Добавлен блок для GET-запроса
        form = AttractionForm()
        return render(request, 'add_attraction.html', {'form': form})

    return JsonResponse({'message': 'Метод запроса не поддерживается'}, status=405)



def search_attractions(request):
    query = request.GET.get('query', '')  # Получаем параметр 'query' из GET-запроса
    attractions = Attraction.objects.all()

    if query:
        # Фильтруем достопримечательности по имени
        attractions = attractions.filter(name__icontains=query)

    # Преобразуем объекты изображений в их URL
    for attraction in attractions:
        if attraction.image_path:
            attraction.image_path = attraction.image_path  # Получаем URL изображения

    return render(request, 'attractions.html', {'attractions': attractions, 'query': query})

