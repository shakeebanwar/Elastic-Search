import json
from .models import ElasticDemo

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *


class NewsDocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        
        model = ElasticDemo
        document = NewsDocument
        fields = (
            'id',
            'title',
            'content',
            
        )


