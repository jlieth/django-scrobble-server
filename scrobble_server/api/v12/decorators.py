from functools import wraps

from django.http import HttpResponseBadRequest


def required_params(iterable):
    required = set(iterable)

    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            if request.method == "GET":
                given = set(request.GET)
            else:
                given = set(request.POST)
            missing_params = required - given
            if missing_params:
                missing = ", ".join(missing_params)
                return HttpResponseBadRequest(
                    "FAILED missing params in request: {}".format(missing)
                )
            else:
                return func(request, *args, **kwargs)

        return inner

    return decorator
