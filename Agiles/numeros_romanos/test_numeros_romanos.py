from numeros_romanos import decimal_to_roman
def test_1_es_I():
    assert decimal_to_roman(1) == "I"

def test_2_es_II():
    assert decimal_to_roman(2) == "II"

def test_3_es_III():
    assert decimal_to_roman(3) == "III"

def test_4_es_IV():
    assert decimal_to_roman(4) == "IV"

def test_5_es_V():
    assert decimal_to_roman(5) == "V"
