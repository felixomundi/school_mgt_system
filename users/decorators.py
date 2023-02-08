from django.shortcuts import redirect
from django.contrib import messages

def user_is_superuser(function=None, redirect_url='/home'):
    """
    Decorator for views that checks that the user is superuser, redirecting
    to the superuser homepage if necessary by default.
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_superuser:
                messages.error(request, "You are not authorized to access this page!")
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator


def user_is_lecturer(function=None, redirect_url='/staff_home'):
    """
    Decorator for views that checks that the user is lecturer, redirecting
    to the lecturer homepage if necessary by default.
    """
    
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_lecturer:
                messages.error(request, "You are not authorized to access this page!")
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator



def user_is_student(function=None, redirect_url='/student_home'):
    """
    Decorator for views that checks that the user is student, redirecting
    to the student homepage if necessary by default.
    """
    
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_student:
                messages.error(request, "You are not authorized to access this page!")
                return redirect(redirect_url)
                
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    if function:
        return decorator(function)

    return decorator