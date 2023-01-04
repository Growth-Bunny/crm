

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # path("404",views.Error404,name="404"),
    path('', views.home,name="home"),
    # path('accounts/login/',auth_views.LoginView.as_view(template_name='homepage/login.html',authentication_form=LoginForm),name="login"),
    path('login/', views.admin_login,name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    # path('signup/', views.signup,name="signup"),
    path('registration/', views.customerregistrationView.as_view(), name='signup'),


    ############################ Profile Url ######################

    path("profile/",views.profile,name="profile"),


    ############################ End Profile Url ######################


    ######################## User url #######################
    
    path('add_lead/', views.leadView.as_view(), name='add_lead'),
    path('edit_lead/', views.edit_view, name='edit_view'),
    path('update_lead/', views.update_lead, name='update_lead'),
    path('mylead/', views.mylead, name='mylead'),
    path('notification/', views.notification, name='notification'),
    #path('add_user/',views.add_user,name="add_user"),
    path('user_dashboard/',views.user_Dashboard,name="user_dashboard"),
    path('customer_list/',views.customer_list,name="customer_list"),

    ######################## End User url #######################
    path('upload/csv',views.upload_csv,name="upload_csv"),


    ########################### LEAD URL #################################

    


    ###########################END LEAD URL #################################
    

    path("agent/list",views.agent_list,name="agentlist"),

    path("agent_lead_veiw",views.agent_lead_view,name="agent_lead_view")
]


