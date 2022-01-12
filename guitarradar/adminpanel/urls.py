from django.urls import path

from .views import list_peding_for_approval, CheckForApprovalGuitarView

urlpatterns = [
    path(
        'list_pending_for_approval/',
        list_peding_for_approval,
        name='list_peding_for_approval'
    ),

    path(
        'check_for_approval/guitar/',
        CheckForApprovalGuitarView.as_view(),
        name='check_for_approval_guitar'
    )
]
