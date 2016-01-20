# これでCreateViewでユーザーを作れる
# http://stackoverflow.com/questions/26510242/django-how-to-login-user-directly-after-registration-using-generic-createview

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class IndexView(TemplateView):
    template_name = 'myapp/index.html'
    


class AccountCreateView(CreateView):
    # デフォルトのテンプレート名を使用する場合、modelを指定しないと以下のエラー
    # TemplateResponseMixin requires either a definition of 'template_name' or an implementation of 'get_template_names()'
    model = User
    
    form_class = UserCreationForm
    
    def get_success_url(self):
        return reverse('my:user_creation')
        
        
class AccountUpdateView(UpdateView):
    # modelを指定しないと、以下のエラー
    # AccountUpdateView is missing a QuerySet. Define AccountUpdateView.model, AccountUpdateView.queryset, or override AccountUpdateView.get_queryset().
    model = User
    form_class = UserChangeForm
    
    def get_success_url(self):
        return reverse('my:user_change', args=(self.object.id, ))