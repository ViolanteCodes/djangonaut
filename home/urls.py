from django.urls import path

from .views import event_calendar, EventDetailView, EventListView, SessionListView, SessionDetailView

urlpatterns = [
    path('calendar/', event_calendar, name="calendar"),
    path('events/', EventListView.as_view(), name="event_list"),
    path('events/<int:year>/<int:month>/<slug:slug>/', EventDetailView.as_view(), name="event_detail"),
    path('sessions/', SessionListView.as_view(), name="session_list"),
    path('sessions/<slug:slug>/', SessionDetailView.as_view(), name="session_detail"),
]
