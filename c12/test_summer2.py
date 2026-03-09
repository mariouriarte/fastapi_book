from unittest import mock
# from . import mod1
# from . import mod2
import mod1
import mod2

## Esto funcionaria si en c12 existiera __init__.py indicando 
## que c12 es un modulo dentro de la carpeta superior, en ese 
## caso las rutas de import cambiarian a from . import mod1 etc...
# def test_summer_a():
#      with mock.patch.object(mod2.mod1, 'preamble', return_value=""):
#          assert "11" == mod2.summer(5, 6)

def test_summer_a():                                                 
     with mock.patch("mod1.preamble", return_value=""): 
         assert "11" == mod2.summer(5, 6)

# favorito
def test_summer_b():
    with mock.patch("mod1.preamble") as mock_preamble:
        mock_preamble.return_value=""
        assert "11" == mod2.summer(5,6)

@mock.patch("mod1.preamble", return_value="")
def test_summer_c(mock_preamble):
    assert "11" == mod2.summer(5,6)

# favorito, llamada mas limpia
@mock.patch("mod1.preamble")
def test_caller_d(mock_preamble):
    mock_preamble.return_value = ""
    assert "11" == mod2.summer(5,6)       
