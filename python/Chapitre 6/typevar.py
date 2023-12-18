class TypedVar():
    def __init__(self, __value="", __type=str):
        if(type(__value) != __type):
            self._type = type(__value)
        else:
            self._type = __type
        self._value = __value

    def __str__(self):
        return f"<class 'TypedVar' value={self._value} type={self._type}>"
    
    def get(self):
        if(self._type == str):
            return str(self._value)
        elif(self._type == float):
            return float(self._value)
        elif(self._type == int):
            return int(self._value)

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
            except:
                return False
        
    def change(self, element):
        if(type(element) == self._type):
            self._value = element
            return True
        else:
            return False
    
    def force(self, element):
        self._type = type(element)
        self._value = element

if __name__ == "__main__":
    myType = TypedVar(593, int)
    print(myType.erase())
    print(myType, myType.get(), myType.type())