from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy, reverse

from . import views

urlpatterns = [
    
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # Djangoで用意されたものを使いたい場合は、以下のincludeで良い
    # https://docs.djangoproject.com/en/1.9/topics/auth/default/#using-the-views
    # url('^', include('django.contrib.auth.urls'))
    

    # ログイン
    url(r'^login/$', auth_views.login, name='login'),
    
    
    # ログアウト後にテンプレートを表示
    # テンプレート名を`registration/logged_out.html`以外で明示的に指定しないと、
    # django adminのテンプレートが使われてしまう
    url(r'^logout-with-template/$', 
        auth_views.logout,
        {
            'template_name': 'myapp/logged_out.html',
        },
        name='logout_with_template'
    ),
    
    # ログアウト後に名前付きURLパターンのページヘリダイレクト
    # next_pageで
    # ・ハードコーディングする場合、
    # 　'next_page': 'mysite/',とすると、http://localhost:8002/mysite/logout/mysite/ に飛ばされる
    # ・reverseする
    #   django.core.exceptions.ImproperlyConfigured: The included URLconf 'myproject.url
    #   s' does not appear to have any patterns in it. If you see valid patterns in the
    #   file then the issue is probably caused by a circular import.
    # ・reverse_lazy
    #   正しくリダイレクトされる(テンプレート`myapp/logged_out.html`は表示されない)
    url(r'^logout-with-redirect/$', 
        auth_views.logout,
        {
            # 'next_page': 'mysite/',
            # 'next_page': reverse('my:index'),
            'next_page': reverse_lazy('my:index'),
            'template_name': 'myapp/logged_out.html',
        },
        name='logout_with_redirect'
    ),
    
    # ログアウト後にログインページヘリダイレクト
    # settings.pyで、LOGIN_URLを明示的に指定するか、ここでlogin_urlを指定する
    url(r'^logout-then-login/$', 
        auth_views.logout_then_login,
        {
            # 今回はsettings.pyで`LOGIN_URL`を指定したので、ここはコメントアウト
            # 'login_url': reverse_lazy('my:login'),
        },
        name='logout_then_login'
    ),
    
    
    # パスワード変更開始
    # `post_change_redirect`を指定しないと、ハードコーディングされた
    # reverse('password_change_done')
    # で名前解決しようとするので、それを避けるためにパラメータを必ず渡す
    # 他に、「Django Unleashed」のp503にある通り、adminアプリと名前空間が重複してるっぽいので、
    # ここでもテンプレート名を渡さないと、自作のテンプレートが使われない
    url(r'^password-change/$', 
        auth_views.password_change, 
        {
            'post_change_redirect': reverse_lazy('my:pwd_change_done'),
            'template_name': 'myapp/password_change_form.html',
        },
        name='pwd_change'
    ),
   
    # パスワード変更完了
    url(r'^password-change-done/$', 
        auth_views.password_change_done, 
        {
            'template_name': 'myapp/password_change_done.html',
        },
        name='pwd_change_done'
    ),
    
    
    # パスワードリセット
    # パスワード変更同様、adminアプリと名前空間が重複している模様
    # リセット用の情報入力
    url(r'^password-reset/$',
        auth_views.password_reset,
        {
            'post_reset_redirect': reverse_lazy('my:pwd_reset_done'),
            'template_name': 'myapp/password_reset_form.html',
            'email_template_name': 'myapp/password_reset_email.html',
            'subject_template_name': 'myapp/password_reset_subject.txt',
        },
        name='pwd_reset'
    ),
    
    # リセット用の情報入力完了
    url(r'^password-reset-done/$',
        auth_views.password_reset_done,
        {
            'template_name': 'myapp/password_reset_done.html',
        },
        name='pwd_reset_done'
    ),
    
    # 新規パスワードの入力
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {
            'template_name': 'myapp/password_reset_confirm.html',
            'post_reset_redirect': reverse_lazy('my:pwd_reset_complete'),
        },
        name='pwd_reset_confirm'
    ),
    
    # パスワードリセット完了
    url(r'^password-reset-complete/$',
        auth_views.password_reset_complete,
        {
            'template_name': 'myapp/password_reset_complete.html',
        },
        name='pwd_reset_complete'
    ),
    
    
    # ユーザー作成
    url(r'^user-creation/$', views.AccountCreateView.as_view(), name='user_creation'),
    
    # ユーザー情報変更
    url(r'^(?P<pk>[0-9]+)/update/$', views.AccountUpdateView.as_view(), name='user_change'),    
]