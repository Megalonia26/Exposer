from django.shortcuts import render

from django.http import HttpResponse

from mediamodels.models import Product

def UserProfiles(request, pk):

    try:
        user_product = Product.objects.filter(user=pk)

        ctx = {
            "userproduct": user_product
        }

        return render(request, "userprofiles/profiles.html", ctx)
    except:
        return HttpResponse(request, "LOL")