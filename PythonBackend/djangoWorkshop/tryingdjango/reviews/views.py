from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from reviews.models import Review

# Create your views here.
class AppDevClubReviewsView(APIView):
    def get(self, request):
        reviews = []
        names = []
        emails = []
        numbers = []
        for review in Review.objects.filter():
            reviews.append("Name:" + review.name_text + " Email:" + review.email_text + " Number: " + review.number_text + " Review: " + review.review_text)
            
        return Response({'reviews': reviews})

class CreateAppDevClubReview(APIView):
    def post(self, request):
        review = request.data['review']
        name = request.data['name']
        email = request.data['email']
        number = request.data['number']
        if review != '':
            new_database_entry = Review(review_text=review, name_text=name, email_text=email, number_text=number)
            new_database_entry.save()
            return Response({'message': 'success'})
        else:
            return Response({'message': 'failure'})