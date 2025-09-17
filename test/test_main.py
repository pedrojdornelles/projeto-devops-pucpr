import pytest
from src import main

def test_saudacao():
    nome = "Pedro"
    resultado = main.saudacao(nome)
    assert "Pedro" in resultado
    assert "Bem-vindo ao mundo DevOps" in resultado

def test_mostrar_info_sistema(capsys):
    main.mostrar_info_sistema()
    captured = capsys.readouterr()
    assert "Sistema operacional:" in captured.out
    assert "Versão do Python:" in captured.out
    assert "Data/Hora atual:" in captured.out

def test_contagem(capsys):
    main.contagem()
    captured = capsys.readouterr()
    for i in range(1, 8):
        assert f"Número {i}" in captured.out

def test_somar():
    assert main.somar(2, 3) == 5
    assert main.somar(-1, 1) == 0
    assert main.somar(0, 0) == 0

def test_eh_par():
    assert main.eh_par(2) is True
    assert main.eh_par(3) is False
    assert main.eh_par(0) is True