class TypedVar():
    def __init__(self, __value="", __type=str):
        if(__value != ""):
            if(type(__value) != __type):
                self._type = type(eval(__value))
                self._value = eval(__value)
                print('TypeError : Bad type !')
            else:
                self._type = __type
                self._value = __value
        else:
            self._value = __value
            self._type = __type

    def __str__(self):
        return f"<class 'TypedVar' value={self._value} type={self._type}>"
    
    def get(self):
        return self._value

    def erase(self):
        self._value = None
        self._type = None

    def type(self, newType=None):
        if(newType==None):
            return self._type
        else:
            try:
                if(newType == str):
                    self._value = str(self._value)
                    self._type = str
                    return True
                elif(newType == int):
                    self._value = int(self._value)
                    self._type = int
                    return True
                elif(newType == list):
                    self._value = list(self._value)
                    self._type = list
                    return True
                elif(newType == dict):
                    self._value = dict(self._value)
                    self._type = dict
                    return True
            except:
                return False
        
    def change(self, element):
        if(type(element) == self._type):
            self._value = element
            return True
        else:
            if((self._type == dict or self._type == list) and type(element) == str):
                try:
                    self._value = eval(element)
                except:
                    return False
            return False
    
    def force(self, element):
        self._type = type(eval(element))
        self._value = eval(element)

if __name__ == "__main__":
    myType = TypedVar("", list)
    myType.change(input("Nom : "))
    print(myType.get()[1])
    print(myType)