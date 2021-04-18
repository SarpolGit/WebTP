from django.shortcuts import render

questions = [
    {
        'id': idx,
        'title': f'# {idx}',
        'text': f'Рыба #{idx}'
    } for idx in range(10)
]

def index(request):
    return render(request,'index.html',{})

def ask(request):
    return render(request,'ask.html',{})

def question(request):
    return render(request,'question.html',{})

def hot(request):
    return render(request,'hot.html',{'questions': questions})

