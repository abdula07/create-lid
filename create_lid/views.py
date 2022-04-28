from django.shortcuts import render

from djangoProject import settings
from .forms import LidForm
from bitrix24 import *
from dadata import Dadata


# Create your views here.

def create_lid(request):
    bx24 = Bitrix24(settings.bitrix_url_web_hook)
    error = False
    if request.method == 'POST':
        # Форма была отправлена на сохранение.
        form = LidForm(request.POST)
        if form.is_valid():
            # Все поля формы прошли валидацию
            cd = form.cleaned_data
            token = settings.badata_token
            secret = settings.badata_secret
            dadata = Dadata(token, secret)
            result = dadata.clean("address", cd['address'])
            fio = cd['fio']
            result_fio = dadata.clean("name", fio)
            fio_list = fio.split()
            if len(fio_list) <= 2:
                error = True
            else:
                bx24.callMethod('crm.lead.add', fields={
                    "TITLE": "FatJoint LLC",
                    "NAME": result_fio['name'],
                    "SECOND_NAME": result_fio['surname'],
                    "LAST_NAME": result_fio['patronymic'],
                    "STATUS_ID": "NEW",
                    "OPENED": "Y",
                    "ASSIGNED_BY_ID": 1,
                    "CURRENCY_ID": "USD",
                    "OPPORTUNITY": 12500,
                    "ADDRESS_CITY": result['city'],
                    "ADDRESS_COUNTRY": result['country'],
                    "PHONE": [{"VALUE": cd['phone'], "VALUE_TYPE": "WORK"}]
                })

    else:
        form = LidForm()

    return render(request, 'main.html', {'form': form, 'error': error})
