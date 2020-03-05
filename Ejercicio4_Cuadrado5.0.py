'''4. Crea la versión 5.0 de la clase Rectángulo, de manera que:

Sustituya los assert por excepciones:
cuando se le asigne al rectángulo un valor que no sea entero en el lado o en el ancho tiene que lanzar la excepción
"TypeError".
crea una excepción propia para cuando el rectángulo sobrepasa las dimensiones permitidas: "DimensionRectanguloError".

Tenga un método (guardar) para guardar en un fichero el objeto actual usando pickle. Razona si el nombre de ese fichero
 se le debe pasar al método como parámetro o se debe pedir desde el teclado. Se debería de pasar por parametro puesto que
 esta no es una clase que deba o vaya a interactuar con el usuario.

Tenga un método (recuperar) para recuperar un objeto Rectángulo almacenado en un fichero usando pickle. Razona si el
 nombre de ese fichero se le debe pasar al método como parámetro o se debe pedir desde el teclado y si el método debe
 ser estático o no.'''



import pickle

class DimensionRectanguloError(Exception):
    pass


class Rectangulo:
    """
    Versión 5.0.
    Esta clase representa objetos de tipo rectángulo.
    Acciones: cálculo del perímetro, área, dibujar, comparar, guardar , recuperar
    Mejoras respecto a la versión 3.01:
    - Añadimos destructor.
    - Ponemos assert.
    - Sobrecargamos operador *.
    """
    lado_maximo = 10  # lado máximo del rectángulo
    __num_creados = 0  # contador de rectángulos creados

    def __init__(self, base, altura):
        """
        Constructor de la clase.
        :param base: base del rectángulo.
        :param altura: altura del rectángulo.
        """
        self.__base = 1
        self.__altura = 1
        Rectangulo.__num_creados += 1
        # por si hubiera errores en los parámetros hemos dado valor inicial
        self.base = base
        self.altura = altura

    def __del__(self):
        Rectangulo.__num_creados -= 1

    # propiedades

    def guardar(self,fichero):
        db={}
        db['altura'] = self.altura
        db['base'] = self.base

        archivo_g = open(fichero, 'ab')

        pickle.dump(db,archivo_g)
        archivo_g.close()

    def recuperar(self,fichero):
        archivo_g = open(fichero, 'rb')
        db = pickle.load(archivo_g)
        self.altura = db['altura']
        self.base = db['base']

        archivo_g.close()

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        if(self.es_lado_correcto(value)):
            self.__base = value
        else:
            raise TypeError

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        if (self.es_lado_correcto(value)):
            self.__altura = value
        else:
            raise TypeError

    # resto métodos

    @staticmethod
    def num_creados():
        return Rectangulo.__num_creados

    @staticmethod
    def es_lado_correcto(value):
        return type(value) == type(1) and 0 < value <= Rectangulo.lado_maximo

    def perimetro(self):
        """
        :return: perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def area(self):
        """
        :return: área del rectángulo.
        """
        return self.base * self.altura

    def compara(self, otro):
        """
        Compara nuestro rectángulo con otro.
        :param otro: objeto con el que comparamos el actual.
        :return: >0 si mayor, 0 si igual, <0 si menor.
        """
        return self.area() - otro.area()

    def es_gemelo(self, otro):
        """
        Comprueba si el objeto pasado es el mismo rectángulo, o sea,
        tiene la misma base y altura.
        :param otro: objeto con el que comparamos el actual.
        :return: True o False
        """
        return self.base == otro.base and self.altura == otro.altura

    def muestra(self):
        """
        Muestra en pantalla el rectángulo.
        """
        print(self)

    # métodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        str = str[:-1]
        return str

    def __mul__(self, other):
        """
        Multiplica la base si no se pasa del lado máximo, en ese caso lo
        hace con la altura.
        :param other: Valor entero positivo
        :return: Otro rectángulo con la superficie original*other.
        """
        assert type(other) == type(1) and other > 0  # operando correcto
        assert self.base * other <= Rectangulo.lado_maximo or self.altura * other <= Rectangulo.lado_maximo
        if self.base * other <= Rectangulo.lado_maximo:
            return Rectangulo(self.base * other, self.altura)
        else:
            return Rectangulo(self.base, self.altura * other)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() < other.area()

    def __le__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() <= other.area()

    def __eq__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() == other.area()


if __name__ == "__main__":
    r1 = Rectangulo(4, 1)
    print(r1)
    r1.altura += 2
    r1.base += 2
    print(r1)
    r1.recuperar('pickle')
    print(r1)


    '''r2 = Rectangulo(3, 2)
    print(f"Probamos clase rectángulo con r1: ({r1.base},{r1.altura}) y "
          f"r2: ({r2.base},{r2.altura})\n")
    # mostramos
    r1.muestra()
    print()
    r2.muestra()
    # comparamos
    print("Resultado de comparar r1 con r2:", r1.compara(r2))
    print("¿Son gemelos?", r1.es_gemelo(r2))
    # magnitudes
    print("Área r1:", r1.area(), "Perímetro r1:", r1.perimetro())
    print("Área r2:", r2.area(), "Perímetro r2:", r2.perimetro())
    # accedemos a variables de instancia de clase
    print("Rectángulos creados", Rectangulo.num_creados())'''
