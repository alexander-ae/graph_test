from graphene_django import DjangoObjectType
import graphene
from .models import Books

class CategoryType(DjangoObjectType):
    class Meta:
        model =
class BookType(DjangoObjectType):
    class Meta:
        model = Books


class Query(graphene.ObjectType):
    books = graphene.List(BookType)
    book = graphene.Field(BookType,
                              isbn=graphene.String(),
                              title=graphene.String())

    def resolve_books(self, info):
        return Books.objects.all()

    def resolve_book(self, info, **kwargs):
        isbn = kwargs.get('isbn')

        if isbn:
            return Books.objects.get(isbn=isbn)

        return None


schema = graphene.Schema(query=Query)
