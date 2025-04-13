from django.shortcuts import render
from django.core.cache import cache
from . import terms_work
from . import video_ref_work

def index(request):
    """Метод отображающий главную страницу"""  
    return render(request, "index.html")

def terms_list(request):
    """Метод отображающий страницу терминов""" 
    terms = terms_work.get_terms_for_table()
    return render(request, "term_list.html", context={"terms": terms})

def video_ref_list(request):
    """Метод отображающий старинцу ссыллок""" 
    terms = video_ref_work.get_video_ref_list()
    return render(request, "video-reference-list.html", context={"terms": terms})


def add_term(request):
    """Метод отображающий страницу добавление термина""" 
    return render(request, "term_add.html")

def add_video_ref(request):
    """Метод отображающий страницу добалвения ссылки""" 
    return render(request, "video-reference-add.html")

def send_term(request):
    """Метод отправки POST запроса для термина""" 
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_term = request.POST.get("new_term", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Термин должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            terms_work.write_term(new_term, new_definition)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        add_term(request)


def send_video_ref(request):
    """Метод отправки POST запроса для ссылки""" 
    if request.method == "POST":
        cache.clear()
        new_term = request.POST.get("new_term", "")
        new_ref = request.POST.get("new_ref", "").replace(";", ",")
        new_ref_definition = request.POST.get("new_ref_definition", "").replace(";", ",")
        context = {}
        if len(new_term) == 0:
            context["success"] = False
            context["comment"] = "Предмет должен быть не пустым"
        elif len(new_ref) == 0:
            context["success"] = False
            context["comment"] = "Ссылка должна быть не пустая"
        elif len(new_ref_definition) == 0:
            context["success"] = False
            context["comment"] = "Описание ссылки должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваш термин принят"
            video_ref_work.write_video_ref(new_term, new_ref, new_ref_definition)
        if context["success"]:
            context["success-title"] = ""
    return add_video_ref(request)


def show_stats(request):
    """Метод отображающий страницу статистики""" 
    stats = terms_work.get_terms_stats()
    return render(request, "stats.html", stats)
