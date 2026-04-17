import argparse
import asyncio
from pathlib import Path

import edge_tts


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Converte texto em áudio MP3 (pt-BR) com velocidade ajustável."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default=Path("texto.txt"),
        help="Arquivo de texto de entrada (padrão: texto.txt)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("saida.mp3"),
        help="Arquivo MP3 de saída (padrão: saida.mp3)",
    )
    parser.add_argument(
        "--voice",
        default="pt-BR-FranciscaNeural",
        help="Voz do Azure/Edge TTS (padrão: pt-BR-FranciscaNeural)",
    )
    parser.add_argument(
        "--rate",
        default="+50%",
        help="Velocidade da fala (padrão: +50%%, equivalente a 1.5x)",
    )
    parser.add_argument(
        "--text",
        default=None,
        help="Texto direto via linha de comando. Se informado, ignora --input.",
    )
    return parser.parse_args()


def obter_texto(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()

    if not args.input.exists():
        raise FileNotFoundError(
            f"Arquivo de entrada não encontrado: {args.input.resolve()}"
        )

    texto = args.input.read_text(encoding="utf-8").strip()
    if not texto:
        raise ValueError("O texto de entrada está vazio.")
    return texto


async def gerar_mp3(texto: str, saida: Path, voz: str, velocidade: str) -> None:
    comunicador = edge_tts.Communicate(texto, voice=voz, rate=velocidade)
    await comunicador.save(str(saida))


def main() -> None:
    args = parse_args()
    texto = obter_texto(args)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    asyncio.run(gerar_mp3(texto, args.output, args.voice, args.rate))

    print("MP3 gerado com sucesso!")
    print(f"Arquivo: {args.output.resolve()}")
    print(f"Voz: {args.voice}")
    print(f"Velocidade: {args.rate} (aprox. 1.5x)")


if __name__ == "__main__":
    main()
