import unittest
from tipos.transformador import TipoTransformador


class TestesBasicosTipoTransformador(unittest.TestCase):

    def test_criacao_tipo_0_objeto(self) -> None:
        tipo = TipoTransformador(0)
        self.assertEqual(TipoTransformador(0), tipo)

    def test_criacao_tipo_0_objeto_diferente(self) -> None:
        tipo = TipoTransformador(0)
        self.assertNotEqual(TipoTransformador(1), tipo)

    def test_criacao_tipo_0_value(self) -> None:
        variavel = 0
        tipo = TipoTransformador(variavel)
        self.assertEqual(variavel, tipo.value)

    def test_criacao_tipo_0_name(self) -> None:
        tipo = TipoTransformador(0)
        self.assertEqual('OLEO', tipo.name)

    def test_criacao_tipo_1_objeto(self) -> None:
        tipo = TipoTransformador(1)
        self.assertEqual(TipoTransformador(1), tipo)

    def test_criacao_tipo_1_objeto_diferente(self) -> None:
        tipo = TipoTransformador(1)
        self.assertNotEqual(TipoTransformador(0), tipo)

    def test_criacao_tipo_1_value(self) -> None:
        variavel = 1
        tipo = TipoTransformador(variavel)
        self.assertEqual(variavel, tipo.value)

    def test_criacao_tipo_1_name(self) -> None:
        tipo = TipoTransformador(1)
        self.assertEqual('SECO', tipo.name)

    def test_criacao_tipo_erro(self) -> None:
        with self.assertRaises(ValueError):
            TipoTransformador(2)


if __name__ == '__main__':
    unittest.main()
