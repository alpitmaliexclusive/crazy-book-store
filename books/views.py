from django.shortcuts import render

from books.forms import BookForm, EntryForm, ReviewForm, SignUpForm, TopicForm

from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Home Page Function
@login_required
def index(request):
    return render(request,'base.html')


# User Signup Function
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })    


# Add Book Function
@login_required
def new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')                     
    else:
        form = BookForm()       
    return render(request,'new_book.html',{'form':form})


# Books List Function
@login_required
def book_list(request):
    context = {'books': Book.objects.all()}
    return render(request, "book.html", context)


# Book Edit Function
@login_required
def edit_book(request,id):
    book = Book.objects.get(pk=id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    return render(request,'new_book.html',{'form':form})



# Book Delete Function
@login_required(login_url='administration:login')             
def delete_book(request,id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('book_list')    

# Add Review Function
@login_required
def new_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.book
            obj.save(['book'])
            return redirect('review_list')                     
    else:
        form = ReviewForm()       
    return render(request,'new_review.html',{'form':form})


# Review List Function
@login_required
def review_list(request):
    context = {'reviews': Review.objects.all()}
    return render(request, "review.html", context)


# Review Edit Function
@login_required
def edit_review(request,id):
    review = Review.objects.get(pk=id)
    form = ReviewForm(instance=review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    return render(request,'new_review.html',{'form':form})


# Review Delete Function
@login_required          
def delete_review(request,id):
    faq = Review.objects.get(pk=id)
    faq.delete()
    return redirect('review_list') 

    
# Add Topic Function
@login_required
def new_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.owner
            obj.save(['owner'])
            return redirect('topic_list')                     
    else:
        form = TopicForm()       
    return render(request,'new_topic.html',{'form':form})


# Topic List Function
@login_required
def topic_list(request):
    context = {'topics': Topic.objects.all()}
    return render(request, "topic.html", context)


# Topic Edit Function
@login_required
def edit_topic(request,id):
    topic = Topic.objects.get(pk=id)
    form = TopicForm(instance=topic)
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('topic_list')
    return render(request,'new_topic.html',{'form':form})


# Topic Delete Function
@login_required          
def delete_topic(request,id):
    topic = Topic.objects.get(pk=id)
    topic.delete()
    return redirect('topic_list')    
       

# Add Entry Function
@login_required
def new_entry(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_list')                     
    else:
        form = EntryForm()       
    return render(request,'new_entry.html',{'form':form})


# Entry List Function
@login_required
def entry_list(request):
    context = {'entries': Entry.objects.all()}
    return render(request, "entry.html", context)


# Entry Edit Function
@login_required
def edit_entry(request,id):
    entry = Entry.objects.get(pk=id)
    form = EntryForm(instance=entry)
    if request.method == 'POST':
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_list')
    return render(request,'new_entry.html',{'form':form})


# Entry Delete Function
@login_required          
def delete_entry(request,id):
    entry = Entry.objects.get(pk=id)
    entry.delete()
    return redirect('entry_list')    


