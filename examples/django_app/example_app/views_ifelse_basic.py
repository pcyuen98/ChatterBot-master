import json
from django.http.response import JsonResponse

class ViewsIfElseBasic:
    
    @staticmethod
    def answerBasicQuestions(request): 
        
        input_data = json.loads(request.body.decode('utf-8'))
        print ("input_data ==>", input_data)        
    
        x = json.dumps(input_data)
        y = json.loads(x)
        text =  y["text"]
        print ("input_data in text ==>", text)

        if not text.lower().find("covid") == -1:
            return JsonResponse({
                'text': [
                    'Total Cases 5,725 (Fri Jan 29 00:00:00 MYT 2021) ' 
               
                ]
            }, status=200)
            
        if not text.lower().find("name") == -1:
            return JsonResponse({
                'text': [
                    'My name is bayibot., what about you?'
                ]
            }, status=200)
            
        if not text.lower().find("where") == -1:
            return JsonResponse({
                'text': [
                    'Somewhere in the universe. What about you?'
                ]
            }, status=200)  
              
        if not text.lower().find("old") == -1:
            return JsonResponse({
                'text': [
                    'I am less than 3 months old'
                ]
            }, status=200)  