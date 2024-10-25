class MyError(Exception):
    def __init__(self, code=0, msg="Исключение MyError"):
        self.code = code
        self.message =str(msg)
    def __str__(self):
        txt=self.message+"\nКод ошибки: "+str(self.code)
        return txt
try:
    print("Cоздаем собственную ошибку")
    try:
        raise MyError(123)
    except MyError as error:
        print(error)
        error.code=321
        error.message="Та же ошибка MyError"
        raise
except Exception as error:
    print(error)