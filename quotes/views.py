from .models import Quote
from .serializers import QuoteSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


@api_view(["GET"])
def random_quote(request):
    quote = Quote.objects.order_by("?").first()
    if quote is None:
        return Response({"detail": "Abhi koi quote nahi hai."}, status=status.HTTP_404_NOT_FOUND)

    serializer = QuoteSerializer(quote)
    return Response(serializer.data)