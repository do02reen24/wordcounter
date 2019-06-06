from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def ex_count(request):
    return render(request, 'ex_count.html')

def result(request):
    text=request.GET['fulltext']
    words = text.split() # 공백 기준으로 나눠서 리스트로 만들어줌.
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary:
            # increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html',{'full': text, 'total': len(words), 'dictionary' : word_dictionary.items()})