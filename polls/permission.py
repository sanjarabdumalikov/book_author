from rest_framework.permissions import BasePermission

class IsOwnerPermissin(BasePermission):
    def has_permission(self, request, view):
        return super().has_permission(request,view)


    def has_object_permission(self, request, view, obj):
        # print(request.user,obj.user,request.user==obj.user)
        # return super().has_permission(request,view,obj)
        return request.user==obj.user
