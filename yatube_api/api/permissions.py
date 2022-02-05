from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Проверяем на возможность редактирования и удаления объектов."""

    def has_object_permission(self, request, view, obj):
        return (
            (request.method in ('GET', 'POST'))
            or (obj.author == request.user)
        )
