from datetime import datetime
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsNotNightTime(BasePermission):
    message = "밤 10시부터 아침 7시까지는 게시판을 이용할 수 없습니다."

    def has_permission(self, request, view):
        now_hour = datetime.now().hour

        # 밤 10시 이상 또는 아침 7시 전이면 접근 제한
        if now_hour >= 22 or now_hour < 7:
            return False

        return True


class IsOwnerOrReadOnly(BasePermission):
    message = "게시글 작성자만 수정 또는 삭제할 수 있습니다."

    def has_object_permission(self, request, view, obj):
        # 읽기 요청은 누구나 가능(GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # 수정/삭제는 게시글 작성자만 가능(PUT, PATCH, DELETE)
        return obj.writer == request.user