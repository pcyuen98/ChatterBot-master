import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from profanity_filter import ProfanityFilter
import json
from langdetect import detect

class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        print ("---post 1")
        input_data = json.loads(request.body.decode('utf-8'))
        print ("---post 1 input_data==", input_data)
        
    
        
        pf = ProfanityFilter()
        x = json.dumps(input_data)
        y = json.loads(x)
        text =  y["text"]
        print ("---post 1 text==", text)
        isProfane = pf.is_profane(text)

        if (isProfane):
            filtered = pf.censor(text)
            return JsonResponse({
                'text': [
                    'Profane Word detected and filtered. Do you really want to teach the bot this word? Filtered word =' + filtered
                ]
            }, status=200)
        
        print(detect(text))
        langDetected = detect(text)

        supportedLang = ['nl', 'sl', 'en']

        isSupported = any(langDetected in s for s in supportedLang)
        
        print("spelling ==" , langDetected , isSupported)
        
        if (isSupported == False):
            filtered = pf.censor(text)
            return JsonResponse({
                'text': [
                    'Bot only able to understand English, could you re-type? =' + text
                ]
            }, status=200)
            
        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)
       
        
       
         
        response = self.chatterbot.get_response(input_data)
       
        response_data = response.serialize()      

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
