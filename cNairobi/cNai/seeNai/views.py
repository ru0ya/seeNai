from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from seeNai.models import Matwana, StreetFood, TouristDestination


@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        session_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        
        print(phone_number)
        
        response = ""

        if text == "":
            response = "CON Karibu Kenya! \n  What would you love to explore in Nairobi?\n"
            response += "1. Experience Ma3 culture \n"
            response += "2. Tourist Destinations Nairobi\n"
            response += "3. Experience Nairobi street food \n"
            response += "4. Visit our website \n"
        
        elif text ==  "1":
            response = "END  Here is a list of best matatus in Nairobi \n"
            results = Matwana.objects.all()
            for i in results:
                response +=  i.name + "-" +  i.route  + "Kes:" +  str(i.price) +   "\n"
        
        elif text == "2":
            response = "END  Here is a list of best tourist destinations in Nairobi \n"
            results = TouristDestination.objects.all()
            for i in results:
                response +=  i.name + "-" + "serving" +  i.location + "- Ksh."  + str(i.average_price) + "\n"
        
        elif text == "3":
            response = "END  Here is a list of best street food in Nairobi \n"
            results = StreetFood.objects.all()
            for i in results:
                response += i.name + "- Ksh." + str(i.average_price) + "\n"
        
        elif text == "4":
            response = "END Visit our website at www.seeNai.com"
        
        return HttpResponse(response)