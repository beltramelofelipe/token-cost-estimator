# 📊 LLM Cost Estimator & Document Converter

Este projeto combina o poder do **Docling** (IBM) com o **Tiktoken** (OpenAI) para converter documentos complexos (como PDFs científicos) e calcular precisamente o custo de processamento desses dados em modelos de linguagem de grande escala (LLMs).

## 🚀 Funcionalidades

- **Extração Inteligente:** Converte documentos PDF de URLs ou arquivos locais para Markdown, preservando a estrutura.
- **Tokenização Oficial:** Utiliza o `tiktoken` para garantir que a contagem de tokens seja idêntica à realizada pela API da OpenAI.
- **Cálculo Financeiro:** Estima o custo de _Input_ (entrada) com base em preços atualizados por milhão de tokens.

---

## 🛠️ Tecnologias Utilizadas

| Biblioteca   | Finalidade                                                      |
| :----------- | :-------------------------------------------------------------- |
| **Docling**  | Conversão de PDF/Documentos para formatos amigáveis (Markdown). |
| **Tiktoken** | Tokenização rápida e precisa para modelos GPT.                  |
| **Python**   | Linguagem de script principal.                                  |

---

## 📖 Como Funciona

### 1. Fluxo de Conversão

O código utiliza o `DocumentConverter` para processar a fonte (neste caso, um artigo do ArXiv). Ele ignora ruídos visuais e foca no conteúdo textual e estrutural, exportando-o para Markdown.

### 2. Lógica de Tokenização

A função `estimate_cost` identifica o _encoding_ específico do modelo escolhido (ex: `o200k_base` para o `gpt-4o`). A palavra é quebrada em subunidades chamadas **tokens**.

O cálculo do custo segue a fórmula:
$$Custo = \left( \frac{\text{Total de Tokens}}{1.000.000} \right) \times \text{Preço do Modelo por 1M}$$

---

## ⚙️ Configuração e Instalação

### Pré-requisitos

Certifique-se de ter o Python 3.10 ou superior instalado.

### Instalação das Dependências

```bash
pip install docling tiktoken
```
