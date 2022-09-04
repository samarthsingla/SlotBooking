
from django.contrib import admin
from django.urls import path, include
from account import views as account_views
from sports import urls as sports_urls
from sports import views as sports_views
import booking
urlpatterns = [
    path('admin/', admin.site.urls),
    path("account/", include("account.urls")),
    # path("", account_views.account_login, name="account-login"),
    path("sport/",include("sports.urls")),
    path("booking/", include("booking.urls")),
    path("", sports_views.home, name="home"),
    
]