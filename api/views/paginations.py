from rest_framework.pagination import PageNumberPagination


class NotePageNumberPagination(PageNumberPagination):
    page_size = 9

class CompanyPageNumberPagination(PageNumberPagination):
    page_size = 10

class JobPageNumberPagination(PageNumberPagination):
    page_size = 10