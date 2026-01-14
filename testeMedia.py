import unittest


def calcular_media(notas):
    """
    Recebe uma lista de notas e retorna a média.
    """
    soma = 0
    for nota in notas:
        soma += nota

        
    media = (soma / 3)


    return media




class TestMedia(unittest.TestCase):
    


    def test_media(self):
        self.assertEqual(calcular_media([5, 5, 5]), 5) # soma 15 / 3 = 5
        self.assertEqual(calcular_media([10, 8, 9]), 9) # soma 27 / 3 = 9
        self.assertEqual(calcular_media([7, 8, 9]), 8) # soma 24 / 3 =  8
        self.assertEqual(calcular_media([7, 9, 2]), 6) # soma 18 / 3 = 6       
        self.assertEqual(calcular_media([]), 0)        


if __name__ == '__main__':
    unittest.main()
