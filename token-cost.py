from docling.document_converter import DocumentConverter
import tiktoken


def estimate_cost(text, model_name="gpt-4o"):
    pricing = {
            "gpt-4o": 2.50,
            "gpt-4o-mini": 0.15,
            "gpt-3.5-turbo": 0.50
        }

    encoding = tiktoken.encoding_for_model(model_name)
    tokens = encoding.encode(text)
    total_tokens = len(tokens)

    cost = (total_tokens / 1_000_000) * pricing.get(model_name, 0)

    return total_tokens, cost


source = "https://arxiv.org/pdf/2408.09869"
converter = DocumentConverter()
doc = converter.convert(source).document
doc_exp = doc.export_to_markdown()


tokens, price = estimate_cost(doc_exp, "gpt-4o")

print(f"📊 Relatório de Processamento:")
print(f"--- Tokens detectados: {tokens}")
print(f"--- Custo estimado (Input): ${price:.4f}")
