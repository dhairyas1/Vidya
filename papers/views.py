from django.shortcuts import render, redirect, get_object_or_404
from .models import ResearchPaper, Comment
from .forms import ResearchPaperForm, CommentForm


def paper_list(request):
  papers = ResearchPaper.objects.all()
  return render(request, 'papers/paper_list.html',{"papers":papers})

def upload_paper(request):
  if request.method == 'POST':
      form = ResearchPaperForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return redirect('paper_list')  # Redirect to the list of papers after upload
  else:
      form = ResearchPaperForm()
  return render(request, 'papers/upload_paper.html', {'form': form})

def research_paper_detail(request, pk):
    paper = get_object_or_404(ResearchPaper, pk = pk)
    comments= paper.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.paper = paper
            comment.author = request.user
            comment.save()
            return redirect('research_paper_detail', pk=paper.pk)
    else:
        form = CommentForm()
    return render(request, 'papers/paper_detail.html', {'paper': paper, 'comments': comments, 'form': form})
