# Texto para MP3 (pt-BR, 1.5x)

Aplicação em Python para converter texto em `MP3` usando voz em português do Brasil e velocidade de fala em **1.5x**.

## Requisitos

- Python 3.10+
- Dependências do `requirements.txt`

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

## Uso rápido

O projeto já inclui o arquivo `texto.txt` com o texto fornecido.

```bash
python app.py
```

Isso gera o arquivo `saida.mp3` em pt-BR com velocidade `+50%` (aprox. 1.5x).

## Opções

```bash
python app.py --input texto.txt --output minha_saida.mp3 --voice pt-BR-FranciscaNeural --rate +50%
```

Também é possível passar texto direto:

```bash
python app.py --text "Olá! Este é um teste em português." --output teste.mp3
```
