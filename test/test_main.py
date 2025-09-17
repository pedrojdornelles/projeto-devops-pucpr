import pytest
from src import main

def test_saudacao():
    nome = "Pedro"
    resultado = main.saudacao(nome)
    assert resultado == "Olá, Pedro! Bem-vindo ao mundo DevOps!"


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
