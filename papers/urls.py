from django.urls import path
from .views import paper_list, upload_paper, research_paper_detail

urlpatterns = [
  path('', paper_list,name = 'paper_list'),
  path('upload/',upload_paper, name = "upload_paper"),
  path('<int:pk>/', research_paper_detail, name ="research_paper_detail")
]