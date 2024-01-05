import unittest

# Asegúrate de importar las funciones correctamente, ajusta las rutas de importación según sea necesario.
from juego import valor_mano, codificar_mano, codificar_estado

class TestFuncionesAuxiliares(unittest.TestCase):

    def test_valor_mano_sin_ases(self):
        mano = [('J', 'Picas'), ('K', 'Corazones')]
        valor, soft = valor_mano(mano)
        self.assertEqual(valor, 20)
        self.assertFalse(soft)

    def test_valor_mano_con_ases_soft(self):
        mano = [('A', 'Diamantes'), ('9', 'Tréboles')]
        valor, soft = valor_mano(mano)
        self.assertEqual(valor, 20)
        self.assertTrue(soft)

    def test_valor_mano_con_ases_hard(self):
        mano = [('A', 'Diamantes'), ('9', 'Tréboles'), ('3', 'Picas')]
        valor, soft = valor_mano(mano)
        self.assertEqual(valor, 13)
        self.assertFalse(soft)

    def test_valor_mano_con_multiples_ases(self):
        mano = [('A', 'Diamantes'), ('A', 'Tréboles'), ('9', 'Picas')]
        valor, soft = valor_mano(mano)
        self.assertEqual(valor, 21)
        self.assertTrue(soft)

    def test_codificar_mano(self):
        mano = [('A', 'Diamantes'), ('9', 'Tréboles'), ('9', 'Picas')]
        codificacion = codificar_mano(mano)
        self.assertEqual(codificacion, [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1])

    def test_codificar_estado(self):
        mano_jugador = [('A', 'Diamantes'), ('9', 'Tréboles')]
        mano_crupier = [('K', 'Corazones'), ('4', 'Picas')]
        estado_codificado = codificar_estado(mano_jugador, mano_crupier)
        print('ESTADO:',estado_codificado)
        self.assertEqual(estado_codificado, [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])

if __name__ == '__main__':
    unittest.main()
