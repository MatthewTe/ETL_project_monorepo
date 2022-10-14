from django.shortcuts import render, redirect

# The root url redirect:
def root_url_redirect(request):
    "A view that auto-redirects to the swagger UI from the root '/' url"
    return redirect("schema-swagger-ui")
    