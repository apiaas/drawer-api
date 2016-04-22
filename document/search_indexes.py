from haystack import indexes
from .models import Document


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True)
    description = indexes.CharField(model_attr="description")
    processed_text = indexes.CharField(model_attr="processed_text")

    @staticmethod
    def prepare_autocomplete(obj):
        return " ".join((
            obj.description, obj.processed_text
        ))

    def get_model(self):
        return Document

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
