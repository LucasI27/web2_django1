
from django.contrib import admin
from django.urls import path
from polls.views import novo_doce, leite_com_goiaba, ainda_tem_doce

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ainda_tem_doce/', ainda_tem_doce),
    path('leite_com_goiaba/', leite_com_goiaba),
    path('novo_doce/', novo_doce),
] 
