from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers
from rest_framework import status



class question(APIView):

    def get(self, request, format=None):

        q = models.Question_set.objects.get(id=1).questions

        serializer = serializers.questionSerializer(q, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class start_chat(APIView):

    def get(self, requset, format=None):

        first_question = models.Question_set.objects.get(id=1).questions[0]
        print(first_question)
        serializer = serializers.questionSerializer(first_question)

        return Response(serializer.data, status=status.HTTP_200_OK)

        




class caht(APIView):

    def post(self, requset, diary_id, format=None):

        pass


