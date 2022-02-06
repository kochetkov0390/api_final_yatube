from rest_framework import viewsets, mixins


class BaseViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    pass
