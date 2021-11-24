from .models import Account

def get_user(request):
    try:
        result = Account.objects.get(pk=request.user.pk)
        user = {
            "user": {
                "type_user": result.type_user  
            }
        }
        return user
    except:
        return {
            "user": ""
        }

