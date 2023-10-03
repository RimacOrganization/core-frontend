
class ProcessFront:

    def process(self):
        try:
            for i in range (10,20):
                print(f"process {i}")
        except Exception as e:
            print(e)

ProcessFront().process()            