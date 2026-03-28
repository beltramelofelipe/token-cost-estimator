import sys
from docling.document_converter import DocumentConverter
import tiktoken


# Preços de input em USD por 1 milhão de tokens (atualizado 2025)
PRICING = {
    "gpt-4o":          2.50,
    "gpt-4o-mini":     0.15,
    "gpt-4-turbo":     10.00,
    "gpt-3.5-turbo":   0.50,
}

DEFAULT_MODEL = "gpt-4o"
DEFAULT_SOURCE = "https://arxiv.org/pdf/2408.09869"


def convert_document(source: str) -> str:
    """Converte um PDF (URL ou caminho local) para Markdown."""
    converter = DocumentConverter()
    result = converter.convert(source)
    return result.document.export_to_markdown()


def estimate_cost(text: str, model_name: str = DEFAULT_MODEL) -> tuple[int, float]:
    """
    Conta tokens e estima custo de input para o modelo informado.

    Retorna:
        (total_tokens, cost_usd)
    """
    if model_name not in PRICING:
        supported = ", ".join(PRICING.keys())
        raise ValueError(f"Modelo '{model_name}' não suportado. Use: {supported}")

    if not text.strip():
        raise ValueError("O texto fornecido está vazio.")

    encoding = tiktoken.encoding_for_model(model_name)
    total_tokens = len(encoding.encode(text))
    cost = (total_tokens / 1_000_000) * PRICING[model_name]

    return total_tokens, cost


def print_report(source: str, model_name: str, total_tokens: int, cost: float) -> None:
    """Exibe o relatório de processamento."""
    print("\n📊 Relatório de Processamento")
    print(f"   Fonte  : {source}")
    print(f"   Modelo : {model_name}  (${PRICING[model_name]:.2f} / 1M tokens)")
    print(f"   Tokens : {total_tokens:,}")
    print(f"   Custo  : ${cost:.4f} USD\n")


if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_SOURCE
    model_name = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_MODEL

    try:
        print(f"⏳ Convertendo documento: {source}")
        markdown = convert_document(source)

        tokens, cost = estimate_cost(markdown, model_name)
        print_report(source, model_name, tokens, cost)

    except ValueError as e:
        print(f"❌ Erro de validação: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}", file=sys.stderr)
        sys.exit(1)
