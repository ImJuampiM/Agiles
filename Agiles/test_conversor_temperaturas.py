import pytest
from conversor_temperaturas import celsius_to_fahrenheit, fahrenheit_to_celsius # type: ignore


class TestConvertidorTemperaturas:
    def test_cero_celsius_es_32_fahrenheit(self):
        assert celsius_to_fahrenheit(0) == 32

    def test_cero_fahrenheit_es_32_celsius(self):
        assert fahrenheit_to_celsius(32) == 0

    def test_100_celsius_es_212_fahrenheit(self):
        assert celsius_to_fahrenheit(100) == 212

    def test_temperatura_negativa_celsius_a_fahrenheit(self):
        assert celsius_to_fahrenheit(-40) == -40

    def test_valor_no_numerico_lanza_excepcion(self):
        with pytest.raises(TypeError):
            celsius_to_fahrenheit("caliente")