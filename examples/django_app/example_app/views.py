from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from profanity_filter import ProfanityFilter
import json

from example_app.views_check_profone import ViewCheckProfane
from example_app.views_ifelse_basic import ViewsIfElseBasic
from example_app.views_check_lang import ViewCheckLang



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
        input_data = json.loads(request.body.decode('utf-8'))
        print ("input_data ==>", input_data)        
    
        x = json.dumps(input_data)
        y = json.loads(x)
        text =  y["text"]
        print ("input_data in text ==>", text)
        
        answerStr = ViewsIfElseBasic.answerBasicQuestions(request)
        answerStr = ViewCheckProfane.checkProfane(request)
        answerStr = ViewCheckLang.checkLang(request)
        print ("answerBasicQuestions ==>", answerStr)
        if answerStr != None:
            return answerStr   

        
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
