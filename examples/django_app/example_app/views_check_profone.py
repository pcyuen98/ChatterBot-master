import json

class ViewCheckProfane:
    
    @staticmethod
    def checkProfane(request): 
        
        input_data = json.loads(request.body.decode('utf-8'))
        print ("input_data ==>", input_data)        
    
        x = json.dumps(input_data)
        y = json.loads(x)
        text =  y["text"]
        print ("input_data in text ==>", text)