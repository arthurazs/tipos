import pytest
from tipos.transformador import TipoTransformador


# @pytest.fixture
# def tipo_0():
#     return TipoTransformador(0)
#
# @pytest.fixture
# def tipo_1():
#     return TipoTransformador(1)

class TestTipo:
    @pytest.mark.parametrize("test_input, expected", [(0, TipoTransformador(0)), (1, TipoTransformador(1))])
    def test_criacao_tipo_objeto(self, test_input: int, expected: TipoTransformador) -> None:
        assert expected == TipoTransformador(test_input)

    @pytest.mark.parametrize("test_input, expected", [(0, TipoTransformador(1)), (1, TipoTransformador(0))])
    def test_criacao_tipo_objeto_diferente(self, test_input: int, expected: TipoTransformador) -> None:
        assert expected != TipoTransformador(test_input)

    @pytest.mark.parametrize("test_input, expected", [(0, 0), (1, 1)])
    def test_criacao_tipo_value(self, test_input: int, expected: int) -> None:
        assert expected == TipoTransformador(test_input).value

    @pytest.mark.parametrize("test_input, expected", [(0, 'OLEO'), (1, 'SECO')])
    def test_criacao_tipo_name(self, test_input: int, expected: str) -> None:
        assert expected == TipoTransformador(test_input).name

    @pytest.mark.parametrize("test_input", [2, 3, 4])
    def test_criacao_tipo_erro(self, test_input: int) -> None:
        with pytest.raises(ValueError):
            TipoTransformador(test_input)


class TestTransformador:
    pass
