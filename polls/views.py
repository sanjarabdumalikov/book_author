from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import bookModel,authorModel
from rest_framework.response import Response
from .serializers import BookSerializer,authorSerializer
# Create your views here.
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

#
# # class AllBookView(generics.ListAPIView):
#     queryset = bookModel.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = (IsAuthenticated,)

class DetailBookView(generics.RetrieveAPIView):
    queryset = bookModel.objects.all()
    serializer_class = BookSerializer



class AllCreateBookView(generics.ListCreateAPIView):
    queryset = bookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated

# class UpdateBookView(generics.UpdateAPIView):
#     queryset = bookModel.objects.all()
#     serializer_class = BookSerializer

class DetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = bookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = IsAuthenticated



# class AllBookView(APIView):
#     def get(self,request,*args,**kwargs):
#         all_book = bookModel.objects.all()
#         serializer = BookSerializer(all_book,many=True)
#         return Response(serializer.data)



# class DetailBookView(APIView):
#     def get(self,request,*args,**kwargs):
#         book = get_object_or_404(bookModel,pk=kwargs['book_id'])
#         serializer = BookSerializer(book)
#         return Response(serializer.data)





# class CreateBookView(generics.CreateAPIView):
#     queryset = bookModel.objects.all()
#     serializer_class = BookSerializer
#



# class CreateBookView(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = BookSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)


# class UpdateBookView(APIView):
#     def patch(self,request,*args,**kwargs):
#         instance = get_object_or_404(bookModel,pk=kwargs['book_id'])
#         serializer = BookSerializer(instance,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# class DeleteBookView(generics.DestroyAPIView):
#     queryset = bookModel.objects.all()
#     serializer_class = BookSerializer


# class DeleteBookView(APIView):
#     def delete(self,request,*args,**kwargs):
#         instance = get_object_or_404(bookModel,pk=kwargs['book_id'])
#         instance.delete()
#         return Response({'m':'success'},status=status.HTTP_204_NO_CONTENT)
# Create your views here.









class AuthorView(APIView):

    def get(self, request, *args, **kwargs):
        book = authorModel.objects.all()
        serializer = authorSerializer(book, many=True)
        return Response(serializer.data)


class DetailAuthorView(APIView):
    def get(self, request, *args, **kwargs):
        book = get_object_or_404(authorModel, pk=kwargs['author_id'])
        serializer = authorSerializer(book)
        return Response(serializer.data)


class CreateAuthorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = authorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateAuthorView(APIView):
    def patch(self, request, *args, **kwargs):
        instance = get_object_or_404(authorModel, pk=kwargs['author_id'])
        serializer = authorSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAuthorView(APIView):
    def delete(self, request, *args, **kwargs):
        deleter = get_object_or_404(authorModel, pk=kwargs['author_id'])
        deleter.delete()
        return Response({'massage': 'success'}, status=status.HTTP_204_NO_CONTENT)
