import random
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from payment.models import Transactions
import requests
import json

# Create your views here.




merchant = "your merchant or zibal"
callback_url = "http://127.0.0.1/payment/verify/"




def request_view(request):
        MainUrl = "https://gateway.zibal.ir/v1/request"
        amount = "20000"
        data = {
            "merchant":merchant,
	        "amount":amount,
	        "callbackUrl":callback_url,
        }
        generateInvoiceNo = None
        while True:
                generateInvoiceNo = random.randint(100000000000, 999999999999)
                break 
        response = requests.post(url=MainUrl , json = data).json()
        transId =response['trackId']
        transaction=Transactions()
        transaction.Amount = amount
        transaction.Status = 'p'
        transaction.TransCode =transId
        transaction.InvoiceNo = generateInvoiceNo
        transaction.paymentStatus = response['result']
        transaction.save()
        verify(request,transId)
        url = f"https://gateway.zibal.ir/start/{transId}"
        return HttpResponseRedirect(url)
        
        


def verify(request,transId):
    
    MainUrl = "https://gateway.zibal.ir/v1/verify"
    
    data = {
        "merchant":merchant,
        "trackId":transId
    }
    response = requests.post(url=MainUrl , json = data).json()
    print(response)
    #Response Request
    card_number = response.get('cardNumber')
    order_id = response.get('orderId')
    ref_number = response.get('refNumber')
    message = response.get('message')
    result = response.get('result')
    
    trs = Transactions.objects.get(TransCode=transId)
    
    if result == 100:
        trs.Status = 's'
        trs.save()
        return HttpResponse("success payment")
    else:
        trs.Status = 'c'
        trs.save()
        return HttpResponse("failed payment")
    
    
    
     

        
    

    
    
    
    


