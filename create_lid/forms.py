from django import forms


class LidForm(forms.Form):
    fio = forms.CharField(label='Имя фамилия отчество', max_length=100)
    phone = forms.CharField(label='Номер Телефона', max_length=100)
    address = forms.CharField(label='Адрес проживания', max_length=100)
