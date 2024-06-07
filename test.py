import unittest
from Persona import *

class TestElemento(unittest.TestCase):
    def test_persona_correcto(self):
        persona = Persona ("Daniel" , "Avila", 21 , "Turismo", "Castaño")
        self.assertEqual(persona.get_nombre(), "Daniel")
        self.assertEqual(persona.get_apellidos(), "Avila")
        self.assertEqual(persona.get_edad(), 21)
        self.assertEqual(persona.get_oficio(), "Turismo")
        self.assertEqual(persona.get_color_pelo(), "Castaño")




    def test_comprobar_errores(self):
          with self.assertRaises(Exception) as cm :
            Persona ("Daniel_" , "Avila", 21 , "Turismo", "Castaño")
            self.assertEqual(len(cm.exception.args), 1)
            self.assertEqual(cm.exception.args[0], "Los caracteres - o _ no son válidos")


          with self.assertRaises(Exception) as cm :
            Persona ("Daniel_" , "Avila@", 21 , "Turismo", "Castaño")
            self.assertEqual(len(cm.exception.args), 1)
            self.assertEqual(cm.exception.args[0], "Los caracteres - o _ no son válidos")



          with self.assertRaises(Exception) as cm :
              Persona ("Daniel_" , "Avila@", 1121 , "Turismo", "Castaño")
              self.assertEqual(len(cm.exception.args), 1)
              self.assertEqual(cm.exception.args[0], "Edad no posible")










if __name__ == '__main__':
    unittest.main()