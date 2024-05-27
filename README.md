# CLI para Download de Imagens

Este script em Python oferece uma interface de linha de comando (CLI) para baixar uma ou várias imagens a partir de links.

## Requisitos

- Python 3.x
- Bibliotecas Python: argparse, os, requests

## Instalação

1. Clone este repositório ou faça o download do arquivo `download_images.py`.
2. Certifique-se de ter Python instalado em seu sistema.
3. Instale as dependências necessárias executando o seguinte comando:

    ```
    pip install -r requirements.txt
    ```

## Uso

### Sintaxe

```
python download_images.py [-h] (-l LINKS [LINKS ...] | -u URL)
```

### Argumentos

- `-h`, `--help`: Exibe a mensagem de ajuda e sai.
- `-l LINKS [LINKS ...]`, `--links LINKS [LINKS ...]`: Links das imagens a serem baixadas.
- `-u URL`, `--url URL`: Link da imagem a ser baixada.

### Exemplos

1. Baixar uma única imagem:

    ```
    python download_images.py -u https://example.com/image.jpg
    ```

2. Baixar várias imagens:

    ```
    python download_images.py -l https://example.com/image1.jpg https://example.com/image2.jpg
    ```

## Funcionamento

O script permite baixar imagens a partir de URLs fornecidas via linha de comando. Ele suporta tanto o fornecimento de um único link quanto de vários links simultaneamente. As imagens são salvas na pasta `img`, criada automaticamente, com nomes padrão ou numerados, dependendo do modo de download escolhido.
