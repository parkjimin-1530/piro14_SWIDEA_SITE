from django.urls import path
from . import views
app_name = "page"

urlpatterns = [
    path("", view=views.idea_list, name="idea_list"),
    path("idea/<int:pk>/", view=views.idea_detail, name="idea_detail"),
    path("idea/create/", view=views.idea_create, name="idea_create"),
    path("idea/update/<int:pk>/", view=views.idea_update, name="idea_update"),
    path("idea/<int:pk>/delete/", view=views.idea_delete, name="idea_delete"),
    
    path("devtool/", view=views.devtool_list, name="devtool_list"),
    path("devtool/<int:pk>/", view=views.devtool_detail, name="devtool_detail"),
    path("devtool/create/", view=views.devtool_create, name="devtool_create"),
    path("devtool/update/<int:pk>/",
         view=views.devtool_update, name="devtool_update"),    
    path("devtool/<int:pk>/delete/",
         view=views.devtool_delete, name="devtool_delete"),
]

