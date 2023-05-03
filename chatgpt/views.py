from django.shortcuts import render 
from django.shortcuts import redirect 


from chatgpt.OpenAI import main

# Create your views here.

def main_page(request):
    return render(request, 'chatgpt/main_page.html')

def chatting_page(request):
    if request.user.is_authenticated:
        question = request.GET.get('message')
        print(question)
        if question==None:
            question ="хелло"
        answer = main(question)
        context = {'answer': answer,'question':question}
        return render(request, 'chatgpt/chatting_page.html', context) 
    else:
        return redirect('login')
