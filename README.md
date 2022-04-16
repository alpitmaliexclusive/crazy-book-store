
## Create Project Directory
 -> First open your particular windows/macos/ubuntu 
 os terminal or cmd prompt or write Directory name like "crazy_book_club".
 
## Create Virtual Enviorment 
Create and active a virtual environment “cbc_env” for your Crazy Book Club application
- first fall check python terminal in python package list "pip list" 
- if you don't have virtualenv library:
  - then install "pip install virtualenv"
- then after just write few command in your terminal and a virtualenv after env name "virtualenv cbc_env"
- for env activation just write virtualenv
  - if you are using macos/linux system: source venv/bin/activate
  - if you are using windows system: venv\Script\activate  

  
## Now install latest Python one of famous library
pip install django 

  
## Create a new Django project “crazy_book_club”
write command for new project Create: django-admin startproject crazy_book_club
## Create a project database by using manage.py.
lets move in current project directory: cd crazy_book_club
 - then after write command step by step for creating database:
  1)  "python manage.py makemigrations".
  2)  "python manage.py migrate".
## Use browser to check that your server is running alright
- for check project server running like: "python manage.py runserver"
## Create a model “Book” for a book
- first create your project application:
  - write command : "python manage.py startapp books" then after this application name put in your setting.py file in INSTALLED_APPS
- Each book must have a “name” field (type: CharField), an “authors” field (JSONField for a list of names), and a “year_published” field (type: Integer). (0,5 points)
    - name = models.CharField(max_length=100, null=True)
    - author = models.JSONField()  
    - year_published = models.IntegerField()


- Each book should have the fields date_added and date_modified (DateTimeField) that are automatically maintained by the system. (0,5 points)  
  - date_added = models.DateTimeField(auto_now_add=True)
  - date_modified = models.DateTimeField(auto_now=True)
    
- Each book should have an operation returning a string representation of the book model. (0,5 points)
  - def __str__(self):
      -  return str(self.name)
      
- The book model should be appropriately commented. (0,5 points)
  - Have no much better idea....






## Working with Django models and database.
- Activate the “Book” model. 
  - first command : python manage.py makemigrations
  - second command : python manage.py migrate

- Update the database.
  - 
 - What would you do when modifying the data your application handles? (0,5 points)
   - I will register my application in the book model book application admin.py file in
     - admin.site.register(Book)


## Create a superuser and register your “Book” model with the admin site. Add a couple of books by using the admin site.
- for superuser Create command : python manage.py createsueruser
- then after terminal asking few details like:
  - username (leave blank to use 'admin'): admin
 - Email address: admin@gmail.com
 - Password: admin
 - Password (again): admin
   - The password is too similar to the username.
   - This password is too short. It must contain at least 8 characters.
   - This password is too common.
   - Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.



## Create a model “Review” for a review. (2 points)
- Each review must have a “my_review” field (type: TextField), a “stars” field (type: IntegerField), and a “unfinished” field (type: BooleanField). (0,5 points)
  - my_review =  models.TextField(max_length=300, null=True, blank=True)
  - stars = models.IntegerField()
  - unfinished = models.BooleanField(default=False)

- Each review should also have the fields date_added and date_modified (DateTimeField). (0,5 points)
  - date_added = models.DateTimeField(auto_now_add=True)
  - date_modified = models.DateTimeField(auto_now=True)

- The review must have a foreign key “book” (type: ForeignKey) pointing to a book. (0,5 points)
  - book = models.ForeignKey(Book, on_delete=models.CASCADE)
  
## Use Django shell to (1 point)
 - Create Book Model object by python terminal.
   - first write command: 
    - from books.models import Book, Review
       # for one Book create
     - book = Book.objects.create(name="Theory of relativity", year_published='2022',author={'name':'Albert Einstien', 'university':{'name':'MIT', 'PHD':'Python For DataScience'}})
     - book.save() # for one book particular instance save 
     - Book.objects.all() # for All Book object list get
     - Book.objects.filter(author__name="Vikas Sir") # for particuler table filter by table field value

 - List all your reviews related to a certain book. Utilize the foreign key relationship
   - Review.objects.all() # for all book review list

### Test Exmaple ######
book = Book.objects.create(name="Theory of relativity", year_published='2022',author={'name':'Albert Einstien', 'university':{'name':'MIT', 'PHD':'Python For DataScience'}})
>>> book.save()
>>> book
<Book: Theory of relativity>
>>> Book.objects.all()
<QuerySet [<Book: Theory of relativity>]>
>>> Book.objects.filter(author__name="Albert Einstien")
<QuerySet [<Book: Theory of relativity>]>
>>> Book.objects.filter(author__university__PHD="Python For DataScience")
<QuerySet [<Book: Theory of relativity>]>
>>> Review.objects.all()
<QuerySet [<Review: Jordar...Lecture ape sir - 5 - True>]     
     
## Urls and routing (2 points)
- Create a file urls.py into the directory crazy_book_clubs. In that file, assign the app_name to crazy_books_clubs. Add the url pattern to the home page of the site. (0.5 points)
  - from django.contrib import admin
  - from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('books.urls')) # just include books application urls
    ]

- Modify the urls.py file in the directory crazy_book_club so that it also refers the new file you just created above. (0.5 points)
  - Have no good ansewer but, we also included.

- What are the responsibilities or tasks these files take care of? (2 * 0.5 = 1 point)
  - When a user requests a page from your Django-powered site, this is the algorithm the system follows to determine which Python code to execute:
  - Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL, matching against path_info.

- 
  
## Add a view to the Crazy Book Club Home Page (1 point)
 - Write a view function for your site’s home page. (0.5 points)
   -@login_required
    def index(request):
        return render(request,'base.html')
 - What is the purpose of this function? (0.5 points)
   - Django views are part of the user interface — they usually render the HTML/CSS/Javascript in your Template files into what you see in your browser when you render a web page
   - The classes documented below provide a way for users to use functions provided by the underlying database as annotations, aggregations, or filters in Django. Functions are also expressions, so they can be used and combined with other expressions like aggregate functions.
   

## Add a template to the Crazy Book Club Home Page (1 point)
- Write a template file for your site’s home page. (0.5 points)
  - first create one directory for "templates"
  - there templates in first create base.html file this file use for home page it's main 
    parent html template.
    

## What is the purpose of this file? (0.5 points)
  - Being a web framework, Django needs a convenient way to generate HTML dynamically. The most common approach relies on templates. A template contains the static parts of the desired HTML output as well as some special syntax describing how dynamic content will be inserted. For a hands-on example of creating HTML pages with templates, see Tutorial 3.

A Django project can be configured with one or several template engines (or even zero if you don’t use templates). Django ships built-in backends for its own template system, creatively called the Django template language (DTL), and for the popular alternative Jinja2. Backends for other template languages may be available from third-parties. You can also write your own custom backend, see Custom template backend

Django defines a standard API for loading and rendering templates regardless of the backend. Loading consists of finding the template for a given identifier and preprocessing it, usually compiling it to an in-memory representation. Rendering means interpolating the template with context data and returning the resulting string.

The Django template language is Django’s own template system. Until Django 1.8 it was the only built-in option available. It’s a good template library even though it’s fairly opinionated and sports a few idiosyncrasies. If you don’t have a pressing reason to choose another backend, you should use the DTL, especially if you’re writing a pluggable application and you intend to distribute templates. Django’s contrib apps that include templates, like django.contrib.admin, use the DTL.

For historical reasons, both the generic support for template engines and the implementation of the Django template language live in the django.template namespace.


## What is the routine for adding web pages into a Django application? What are the benefits of it? (2 * 0.5 = 1 point)
 - Templates. Every web framework needs a convenient way to generate HTML files and in Django the approach is to use templates: individual HTML files.

 
## Working with a parent template (2 points)
 - Create a parent (base) template for your Crazy Book Club site. (0.5 points)
   - parent base also created in templates folder "base.html"
   
## What are the benefits of inheriting a parent template? (0.5 points)
 - The most powerful – and thus the most complex – part of Django's template engine is template inheritance. Template inheritance allows you to build a base “skeleton” template that contains all the common elements of your site and defines blocks that child templates can override. This template, which we'll call base


 
## Modify your Home Page template so that it inherits from your parent template. (0.5 points)
 - base.html
 - book.html
 - review.html
 - edit_book.html
 - edit_review.html
 - new_book.html
 - new_review.html
 - login.html
 - signup.html
 - password_change_done.html
 - password_change_form.html
 - password_reset_complete.html
 - password_reset_confirm.html
 - password_reset_done.html
 - password_reset_email.html
 - password_reset_form.html
 
## What is the benefit of using a url name in a template tag? (0.5 points)
 - By assigning the url a name you can use this value as a reference in view methods and templates, which means any future changes made to the url path, automatically updates all url definitions in view methods and templates.





## Implement two pages that display data: The page that lists all books and a page that displays all reviews for a particular book.
 - Define urls for the book and the reviews pages. (2 * 0,5 = 1 point)
 - Book Add Url:
   - path('add-new-book/', views.new_book, name="new_book"),
 - Book Edit Url:
   - path('edit/<int:id>',views.edit,name='edit'),  
 - Book Delete Url:
   - path('delete-book/delete/<int:id>/',views.delete_book,name='delete_book'),
 - Book List Url:
   - path('book-list/', views.book_list, name="book_list"),  
 - Reviews Add Url:
   - path('add-new-review/', views.new_review, name="new_review"), 
 - Reviews Edit Url:
   - path('edit-review/<int:id>/', views.edit_review,name='edit_review'), 
- Reviews Delete Url:
   - path('delete-review/delete/<int:id>/',views.delete_review,name='delete_review'), 
- Reviews List Url:
   - path('review-list/', views.review_list, name="review_list"), 
  

 - Create views for the book and for the reviews pages. (2 * 0,5 = 1 point)
   - all views function added in views.py file 

## Implement two pages that allow users to add a new book data, and new review data: (5 points)
  - Create the book form and the review form, which are based on the book model and review model. Save the as forms.py. (0.5 * 2 = 1 point)
    - first install one django third-party libraries for forms "crispy_forms" then after add in INSTALLED_APPS.
    - forms.py file in create "BookForm":
      - class BookForm(forms.ModelForm):
            author = forms.JSONField(max_length=1024)

            class Meta:
              model = Book
              fields = "__all__"
              widgets = {
                    'author': JSONEditorWidget
                }
    - Note : where we use widgets for JSOFIELD for inuput type 
    - Note: jsonwidegt field install from this site:
      - https://paulgrajewski.medium.com/django-json-field-9f8dcde5af71

  - Define the new urls for new_book page and the new_review page to the file urls.py (0.5 * 2 = 1 point)  
    - path('add-new-book/', views.new_book, name="new_book"), # for New Book Add
    - path('add-new-review/', views.new_review, name="new_review"), # for New Review Add

  - Create two view functions. The first one new_book function, which handle the request for the new_book page, and processing of any data submitted through the form and redirect the user back to the books page. The second function is new_review function, which handle the request for the new_review page, and processes the submitted data and redirect the user back to a specific book page (0.5 * 2 = 1 point)
    
    - views.py file in declare function for add new book "new_book":  
      - def new_book(request):
          if request.method == "POST":
              form = BookForm(request.POST)
              if form.is_valid():
                  form.save()
                  return redirect('book_list')                     
          else:
              form = BookForm()       
          return render(request,'new_book.html',{'form':form})

    - views.py file in declare function for add new review "new_review":
       - def new_review(request):
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

  - Create two templates to display the forms you have created earlier (new_book.html, and new_review.html). (0.5*2=1 point):
    - templates folder in created two file "new_book.html" or "new_review.html" for add new book or review.


  - Finally link the new_book page to the Books page, and the new_review page to each book page. (0.5*2=1 point) 
    - New Book add after creating All Books page template name "book.html"
      - views.py file in declare function for all books "book_list":
          - def book_list(request):
              context = {'books': Book.objects.all()}
              return render(request, "book.html", context)
    

    - New Review add after creating All Reviews page template name "review.html"
      - views.py file in declare function for all books "review_list":
          - def review_list(request):
                context = {'reviews': Review.objects.all()}
                return render(request, "review.html", context)
          

## Allow users to edit their book review data: (2 points)    
   - Create the required route that allows user to edit a specific review. Create the required edit_review() view function, which allows a user  (0.5 points)
     - we use for authenticated user can edit reviews a using "@login_required" decorator


   - Create the edit_review function, that returns a form for editing the review. (0.5 points)  
     - def edit_review(request,id):
          review = Review.objects.get(pk=id)
          form = ReviewForm(instance=review)
          if request.method == 'POST':
              form = ReviewForm(request.POST, instance=review)
              if form.is_valid():
                  form.save()
                  return redirect('review_list')
          return render(request,'new_review.html',{'form':form})

   - Create the edit_review template. (0.5 point)
     - templates folder in created one file for "edit_review.html"      
   

   - include the edit_review page link in each review page. (0.5 point)
     - user can edit particuler book review id wise can edit.

## Use the developer tools of your browser to (2 * 0,5 = 1 point)
   - inspect the html structure of one of the forms generated by Django
   - [![Screenshot-from-2022-03-15-18-36-17.png](https://i.postimg.cc/TwF5Y9ph/Screenshot-from-2022-03-15-18-36-17.png)](https://postimg.cc/R61Zgw1z)
   - inspect the network traffic that follows clicking the Add… button
   - [![Screenshot-from-2022-03-15-18-45-27.png](https://i.postimg.cc/GmfCfSNB/Screenshot-from-2022-03-15-18-45-27.png)](https://postimg.cc/k2Wz6w79)


## Visit the website https://www.djangoproject.com and answer the following questions. (4 * 0,5 = 2 points)
   - What is the purpose of the website?
     - As you can probably tell by now, the main purpose of a website is to have the ability to express yourself however you want. Both businesses and        individuals value this. It is why businesses use it to grow their brand and individuals use it to bring their personality to their own safe space online.
   
   - What does the website contain?
     - A web page may contain text, graphics, and hyperlinks to other web pages and files. A web page is often used to provide information to viewers, including pictures or videos to help illustrate important topics. A web page may also be used as a method to sell products or services to viewers.
   
   - How would the site to help you to get started working with Django forms?  
     - https://www.geeksforgeeks.org/django-forms/


   - Utilize the API documentations. What are the alternatives of rendering a form as a series of <p> tags i.e. using the as_p() operation?
     - Django forms are an advanced set of HTML forms that can be created using python and support all features of HTML forms in a pythonic way. Rendering Django Forms in the template may seem messy at times but with proper knowledge of Django Forms and attributes of fields, one can easily create excellent Form with all powerful features. In this article, Form is rendered as paragraphs in the template
      
     
## Visit the following links and answers the following questions (1.5 points)

 - https://docs.djangoproject.com/en/3.2/ref/contrib/auth/
    - Using the first link, explain what the component auth includes. Find out what functions, fields, and attributes you may use. (1 point) 
    
  - authenticate(request, remote_user)¶

    The username passed as remote_user is considered trusted. This method returns the user object with the given username, creating a new user object if create_unknown_user is True.

    Returns None if create_unknown_user is False and a User object with the given username is not found in the database.

    request is an HttpRequest and may be None if it wasn’t provided to authenticate() (which passes it on to the backend).

    - Explain in your own words what is the purpose of the second link. (0.5 point)
    
    - I don't have idea









      








   