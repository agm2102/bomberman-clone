import os
import argparse

# Extensões de imagem suportadas
EXTENSOES = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.tif'}

def renomear_imagens(pasta, prefixo='img', inicio=1, digitos=3):
    """
    Renomeia todas as imagens de uma pasta com números em sequência.

    Args:
        pasta:   Caminho da pasta com as imagens
        prefixo: Prefixo do nome do arquivo (padrão: 'img')
        inicio:  Número inicial da sequência (padrão: 1)
        digitos: Quantidade de dígitos no número (padrão: 3 → 001, 002...)
    """
    if not os.path.isdir(pasta):
        print(f"❌ Pasta não encontrada: {pasta}")
        return

    # Lista apenas arquivos de imagem, ordenados pelo nome atual
    arquivos = sorted([
        f for f in os.listdir(pasta)
        if os.path.isfile(os.path.join(pasta, f))
        and os.path.splitext(f)[1].lower() in EXTENSOES
    ])

    if not arquivos:
        print("⚠️  Nenhuma imagem encontrada na pasta.")
        return

    print(f"📁 Pasta: {pasta}")
    print(f"🖼️  {len(arquivos)} imagem(ns) encontrada(s)\n")

    contador = inicio
    for arquivo in arquivos:
        extensao = os.path.splitext(arquivo)[1].lower()
        novo_nome = f"{prefixo}{str(contador).zfill(digitos)}{extensao}"
        origem = os.path.join(pasta, arquivo)
        destino = os.path.join(pasta, novo_nome)

        # Evita sobrescrever arquivo existente com nome diferente
        if origem == destino:
            print(f"  ✅ Sem alteração: {arquivo}")
        elif os.path.exists(destino):
            print(f"  ⚠️  Conflito (já existe): {novo_nome} — pulando '{arquivo}'")
        else:
            os.rename(origem, destino)
            print(f"  🔄 {arquivo}  →  {novo_nome}")

        contador += 1

    print(f"\n✅ Concluído! {contador - inicio} imagem(ns) renomeada(s).")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Renomeia imagens de uma pasta com números em sequência."
    )
    parser.add_argument(
        "pasta",
        nargs="?",
        default=".",
        help="Caminho da pasta com as imagens (padrão: pasta atual)"
    )
    parser.add_argument(
        "--prefixo", "-p",
        default="number",
        help="Prefixo do nome do arquivo (padrão: 'img')"
    )
    parser.add_argument(
        "--inicio", "-i",
        type=int,
        default=0,
        help="Número inicial da sequência (padrão: 1)"
    )
    parser.add_argument(
        "--digitos", "-d",
        type=int,
        default=2,
        help="Quantidade de dígitos no número (padrão: 3)"
    )

    args = parser.parse_args()
    renomear_imagens(args.pasta, args.prefixo, args.inicio, args.digitos)