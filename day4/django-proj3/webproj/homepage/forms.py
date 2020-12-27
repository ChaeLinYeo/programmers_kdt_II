from django import forms

from .models import Coffee # Model 호출

class CoffeeForm(forms.ModelForm): # ModelForm을 상속받는 CoffeeForm
    class Meta : # form을 만들기 위해 어떤 모델이 있어야하는지 여기에서 지정해준다
        model = Coffee
        fields = ('name', 'price', 'is_ice', 'menu_description') # 어떤 필드를 CoffeeForm에서 받을 것인지 적어주는 곳