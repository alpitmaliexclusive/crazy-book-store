from django.urls import path, include
from . import views

urlpatterns = [
    # Home Page
    path('',views.index,name='index'),

    # For User 
    path('signup/',views.signup,name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),

    # For Books
    path('add-new-book/', views.new_book, name="new_book"),
    path('edit-book/<int:id>/', views.edit_book,name='edit_book'),
    path('delete-book/delete/<int:id>/',views.delete_book,name='delete_book'),
    path('book-list/', views.book_list, name="book_list"),

    # For Review
    path('add-new-review/', views.new_review, name="new_review"),
    path('edit-review/<int:id>/', views.edit_review,name='edit_review'),
    path('delete-review/delete/<int:id>/',views.delete_review,name='delete_review'),
    path('review-list/', views.review_list, name="review_list"),
    
    # For topic
    path('add-new-topic/', views.new_topic, name="new_topic"),
    path('edit-topic/<int:id>/', views.edit_topic,name='edit_topic'),
    path('delete-topic/delete/<int:id>/',views.delete_topic,name='delete_topic'),
    path('topic-list/', views.topic_list, name="topic_list"),

    # For Entry
    path('add-new-entry/', views.new_entry, name="new_entry"),
    path('edit-entry/<int:id>/', views.edit_entry,name='edit_entry'),
    path('delete-entry/delete/<int:id>/',views.delete_entry,name='delete_entry'),
    path('entry-list/', views.entry_list, name="entry_list"),


    
     
]