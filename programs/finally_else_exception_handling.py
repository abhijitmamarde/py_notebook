class FailedError(Exception):

    def __init__(self):
        super().__init__()

class ExcellentError(Exception):

    def __init__(self):
        super().__init__()

def calc_grade(n1,n2,n3):
    
    avg = int((n1 + n2 + n3)/3)

    if avg == 0:
        raise FailedError()
    if avg >= 75:
        raise ExcellentError()

if True:
    try:
        calc_grade(0,0,0)

    except FailedError:
        print("Failed!")
    except ExcellentError:
        print("Excellent")
    except Exception:
        print("Some unknow exception occured")
    else:
        print("No error occured? condition not handled")
    finally:
        print("Great, now lets calculate your total!")


    print("....END....")

