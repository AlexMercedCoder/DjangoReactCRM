from crmdata.models import Actor, Event, Media, Precinct, Contacts
from rest_framework import serializers


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ['first_name','last_name', 'phone','email','address','town','state','zip_code','events','volunteer','staff','donor','voter','donor','voter','journalist','precinct']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['name','address','town','state','zip_code','when']

class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ['name','phone','email','reps']

class PrecinctSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Precinct
        fields = ['number','town','state']

class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = ['when','who_reached_out','target','notes']