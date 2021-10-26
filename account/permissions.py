from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.shortcuts import redirect


class AccountAccessMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(), 
            self.get_login_url, self.get_redirect_field_name)

        # if not self.has_permission():
        #     return redirect('core:index')

        return super(AccountAccessMixin, self).dispatch(request, *args, **kwargs)