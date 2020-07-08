from django.conf.urls                   import url, include
from django.contrib.auth.decorators     import login_required
from django.shortcuts                   import redirect

from django.conf.urls.i18n 				import i18n_patterns
from django.views.i18n 					import javascript_catalog
from django.utils.translation 			import ugettext_lazy as _

from . import views

# index_redirect = lambda request: redirect( '/cn/login' )
index_redirect = lambda request: redirect( '/en/login' )

urlpatterns = [
	url(r'^$',						index_redirect , name='index' ),
	url(r'^api/v1',					views.Api.as_view(), name='api'),
	url(r'^dashboard',				views.Dashboard.as_view(), name='dashboard'),
	url(r'^mvc',					views.MVC.as_view(), name='mvc'),
	url(r'^basket',					views.BASKET.as_view(), name='basket'),
	url(r'^funnel/advance',			views.Funnel.as_view(), name='funnel'),
	url(r'^funnel',					views.SimpleFunnel.as_view(), name='funnel'),
	url(r'^changeLang',				views.ChangeLang.as_view(), name='change_lang'),
	url(r'^error',					views.Error.as_view(), name='error'),
	url(r'^register/$', 			views.Register.as_view(), name='register'),
	url(r'^retention$',				views.SimpleRetention.as_view(), name='retention'),
	url(r'^retention/advance',		views.Retention.as_view(), name='advance_retention'),
	url(r'^upload',					views.Upload.as_view(), name='Upload'),
	url(r'^column_list',			views.Column_list.as_view(), name='Column list'),
	url(r'^database',				views.Database.as_view(), name='Database'),
	url(r'^figure_design',			views.Figure_design.as_view(), name='figure_design'),
	url(r'^figure',					views.Figure.as_view(), name='Figure'),
	url(r'^',						include('django.contrib.auth.urls') ),


	#url(r'^.*/$',					index_redirect, name='index'),

]
