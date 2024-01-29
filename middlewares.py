class  PracticeMiddleware:


    # initializze the class
    def __init__(self,get_response):
        self.get_response=get_response

        # loops through order of request 
        def __call__(self,request):
            if request.method=='GET':
                print("Middleware logic for GET")

            elif request.method=='POST':
                print("Middleware logic for POST")

            elif request.method=='UPDATE':
                print("Middleware logic for UPDATE")
            
            elif request.method=='DESTROY':
                print("Middleware logic for DESTROY")
            
            response=self.get_response(request)
            return response