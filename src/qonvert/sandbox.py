class Punto:
    """Clase Punto"""
    def __init__(self, x, y):
        """Punto con sus respectivas coordenadas"""
        self.x = x      
        self.y = y      

    def get_value(self):
        if type(self.__x) != int and type(self.__x) != float:
            raise ("el tipo de x no es el que se esperaba")
        return (self.__x, self.__y)

         if type(self.__y) != int and type(self.__y) != float:
            raise ("el tipo de y no es el que se esperaba")
        return (self.__x, self.__y)

    def set_value(self, new_value):
        self.__value = new_value if type(new_value) == int or type(new_value) == float else 0


    value = property(get_value)