import json
from profanity_filter.profanity_filter import ProfanityFilter
from django.http.response import JsonResponse

class ViewCheckProfane:
    
    @staticmethod
    def checkProfane(request): 
        
        input_data = json.loads(request.body.decode('utf-8'))
        print ("input_data ==>", input_data)        
    
        x = json.dumps(input_data)
        y = json.loads(x)
        text =  y["text"]
        print ("input_data in text ==>", text)
                
        # << --- START - move this to views_check_profone.py  --->>
        pf = ProfanityFilter()
        isProfane = pf.is_profane(text)                                  
        if (isProfane):
            filtered = pf.censor(text)
            return JsonResponse({
                'text': [
                    'Profane Word detected and filtered. Do you really want to teach the bot this word? Filtered word =' + filtered
                ]
            }, status=200)
        # << --- END - move this to views_check_profone.py  --->>