from django.http import HttpResponse


def novo_doce(request):
    return HttpResponse("novo doce de leite")

def leite_com_goiaba(request):
    return HttpResponse("doce de leite com goiaba")

def ainda_tem_doce(request):
    return HttpResponse("ainda tem doce de leite")