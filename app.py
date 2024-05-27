import argparse
import os
import requests

def download_image(url, filename):
    try:
        # Faz o pedido GET para obter a imagem
        response = requests.get(url)
        # Verifica se a resposta foi bem-sucedida
        if response.status_code == 200:
            # Verifica se a pasta "img" existe, e a cria se não existir
            if not os.path.exists("img"):
                os.makedirs("img")
            # Caminho completo para o arquivo de imagem na pasta "img"
            filepath = os.path.join("img", filename)
            # Abre o arquivo no modo de escrita binária e escreve os dados da imagem
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print("Download concluído! Imagem salva em:", filepath)
        else:
            print("Falha ao baixar a imagem. Código de status:", response.status_code)
    except Exception as e:
        print("Ocorreu um erro:", str(e))

def main():
    # Configuração do argumento da linha de comando
    parser = argparse.ArgumentParser(description="CLI para baixar uma ou várias imagens a partir de links.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-l", "--links", nargs='+', type=str, help="Links das imagens a serem baixadas")
    group.add_argument("-u", "--url", type=str, help="Link da imagem a ser baixada")

    args = parser.parse_args()

    # Se um único link foi fornecido usando o parâmetro -u
    if args.url:
        # Extrai a extensão do arquivo da URL
        ext = os.path.splitext(args.url)[1]
        # Nome do arquivo de imagem
        filename = f"ref_pixel_art{ext}"
        # Chama a função para baixar a imagem
        download_image(args.url, filename)

    # Se vários links foram fornecidos usando o parâmetro -l
    if args.links:
        # Contador para renomear as imagens
        counter = 1
        for url in args.links:
            # Extrai a extensão do arquivo da URL
            ext = os.path.splitext(url)[1]
            # Nome do arquivo de imagem renomeado
            filename = f"ref_pixel_art_{counter}{ext}"
            # Chama a função para baixar a imagem
            download_image(url, filename)
            # Incrementa o contador
            counter += 1

if __name__ == "__main__":
    main()
