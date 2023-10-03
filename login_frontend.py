
class LoginFrontEnd:

    def initial_session(self):
        try:
            print("Start session frontend")
            print("... process ...")
        except Exception as e:
            print(e)
    
    def close_session(self):
        try:
            print("Close session frontend")
        except Exception as e:
            print(e)

LoginFrontEnd().initial_session()            
LoginFrontEnd().close_session()