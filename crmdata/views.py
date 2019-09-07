from crmdata.models import Actor, Event, Media, Precinct, Contacts
from rest_framework import viewsets
from crmdata.serializers import ActorSerializer, EventSerializer, MediaSerializer, PrecinctSerializer, ContactsSerializer



class ActorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


class PrecinctViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Precinct.objects.all()
    serializer_class = PrecinctSerializer

class ContactsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer