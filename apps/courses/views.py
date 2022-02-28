from rest_framework import filters, generics, permissions
from rest_framework.exceptions import ValidationError

from apps.cores.paginations import StandardPageNumberPagination
from apps.cores.permissions import IsOwner

from .models import CourseReview
from .serializers import CourseReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    코스 리뷰 리스트 및 생성(정렬 기능 포함)
    """

    name = "Course Review List & Create"
    serializer_class = CourseReviewSerializer
    pagination_class = StandardPageNumberPagination
    throttle_scope = "standard"
    permission_classes = [permissions.IsAuthenticated]
    queryset = CourseReview.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["rating", "created_at"]
    ordering = ["-rating"]

    def perform_create(self, serializer):
        """
        코스 평균 평점, 평점 개수에 셍성되는 리뷰를 반영
        """
        course = serializer.validated_data["course_id"]
        user = self.request.user
        review_queryset = user.user_review.filter(course_id=course)

        if review_queryset.exists():
            raise ValidationError("이미 이 코스에 대한 리뷰가 있습니다!")

        if course.count_review == 0:
            course.avg_rating = serializer.validated_data["rating"]
        else:
            course.avg_rating = round(
                (course.avg_rating + serializer.validated_data["rating"]) / 2, 1
            )

        course.count_review += 1
        course.save()

        serializer.save()


class ReviewDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    """
    코스 리뷰 삭제 및 업데이트
    """

    name = "Course Review Read & Update & Delete"
    serializer_class = CourseReviewSerializer
    permission_classes = [IsOwner]
    throttle_scope = "standard"
    queryset = CourseReview.objects.all()

    def perform_destroy(self, review):
        """
        코스 평균 평점, 리뷰 개수에 삭제되는 리뷰를 반영
        """
        course = review.course_id
        count_review = course.count_review

        if count_review == 1:
            course.avg_rating = 0
        else:
            course.avg_rating = round(
                (course.avg_rating * count_review - review.rating) / (count_review - 1),
                1,
            )
        course.count_review -= 1
        course.save()

        review.delete()

    def perform_update(self, serializer):
        """
        코스 평균 평점에 수정되는 리뷰를 반영
        """
        course = serializer.validated_data["course_id"]
        user = self.request.user
        review = user.user_review.get(course_id=course)
        count_review = course.count_review

        if count_review == 1:
            course.avg_rating = serializer.validated_data["rating"]
        else:
            course.avg_rating = round(
                course.avg_rating * count_review
                - review.rating
                + serializer.validated_data["rating"] / count_review
            )
        course.save()

        serializer.save()
