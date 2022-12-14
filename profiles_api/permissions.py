from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Let that the user edit the profile"""
    
    def has_object_permission(self, request, view, obj):
        """Check if the object is try to edit the profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id==request.user.id
        
class UpdateOwnStatus(permissions.BasePermission):
    """Update the own status of feed"""
    def has_object_permission(self, request, view, obj):
        """Check if the object is try to edit the own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile_id==request.user.id
        