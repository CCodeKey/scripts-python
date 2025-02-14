import os

def listar_arquivos_pastas(diretorio, saida):
    with open(saida, 'w', encoding='utf-8') as arquivo_saida:
        for raiz, pastas, arquivos in os.walk(diretorio):
            nivel = raiz.replace(diretorio, '').count(os.sep)
            indentacao = ' ' * 4 * nivel
            arquivo_saida.write(f"{indentacao}[Pasta] {os.path.basename(raiz)}\n")
            
            sub_indentacao = ' ' * 4 * (nivel + 1)
            for arquivo in arquivos:
                arquivo_saida.write(f"{sub_indentacao}- {arquivo}\n")

if __name__ == "__main__":
    PATH_B = "/media/code/DRIVERS"
    saida_arquivo = "saida.txt"
    listar_arquivos_pastas(PATH_B, saida_arquivo)
    print(f"Listagem concluída! Verifique o arquivo {saida_arquivo}")
