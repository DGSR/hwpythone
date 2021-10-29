class SimplifiedEnum(type):
    """
    metaclass allows to use keys variables without duplications like in Enum
    """
    def __new__(cls: type, name: str, bases: tuple, dct: dict):
        keys_name = '_'+str(name)+'__keys'
        keys = dct.get(keys_name, None)
        if keys:
            dct.update({elem: elem for elem in keys})
            del dct[keys_name]

        cls_instance = super().__new__(cls, name, bases, dct)
        return cls_instance
