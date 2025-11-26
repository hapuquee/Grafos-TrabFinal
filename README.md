# Implementação Simples do PageRank

Este projeto contém uma implementação simples e direta do algoritmo PageRank, focando na clareza e compreensão do algoritmo.

## Visão Geral

O PageRank é o algoritmo fundamental usado pelo Google para rankear páginas web. Este script demonstra:

- **Implementação manual do PageRank** usando método das potências
- **Grafo exemplo simples** para fácil compreensão
- **Visualização clara** dos resultados
- **Código comentado** para fins educacionais

## Como Executar

### Pré-requisitos

Instale as dependências necessárias:

```bash
pip install networkx matplotlib numpy scipy
```

### Execução

```bash
python pagerank_simples.py
```

## Saídas do Programa

### 1. Console Output
O programa exibe no terminal:
- Criação do grafo exemplo (nós A, B, C, D)
- Progresso das iterações até convergência
- Ranking final dos nós por importância
- Verificação da soma dos scores

### 2. Arquivo de Visualização
- **Arquivo gerado**: `pagerank_simples.png`
- **Conteúdo**: Grafo com tamanhos dos nós proporcionais ao PageRank
- **Localização**: Mesma pasta do script

## Parâmetros Configuráveis

### Grafo de Exemplo
```python
# Modifique as arestas em criar_grafo_exemplo()
arestas = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'C'), ('B', 'D'),
    # Adicione suas próprias conexões aqui
]
```

### Algoritmo PageRank
```python
scores = calcular_pagerank(grafo, alpha=0.85)
```
- `alpha`: Fator de amortecimento (0.85 = padrão do Google)
- `max_iter`: Máximo de iterações (padrão: 100)
- `tol`: Tolerância para convergência (padrão: 1e-6)

## Conceitos Demonstrados

### 1. **Modelo de Web Realista**
- **Lei de Potência**: Poucos sites têm muitos links
- **Mundo Pequeno**: Caminhos curtos entre sites
- **Hubs**: Sites centrais com alta autoridade

### 2. **Álgebra Linear do PageRank**
- **Matriz de Transição**: Probabilidades de navegação
- **Matriz Google**: Inclui teletransporte aleatório
- **Método das Potências**: Convergência iterativa
- **Dangling Nodes**: Tratamento de páginas sem saída

### 3. **Métricas de Centralidade**
- **PageRank Score**: Importância global do nó
- **In-Degree**: Número de backlinks
- **Autoridade vs Popularidade**: Diferença conceitual

## Interpretação dos Resultados

- **Score alto**: Nó importante na rede
- **Backlinks altos**: Muitas páginas apontam para este nó
- **Convergência rápida**: Rede bem estruturada
- **Diferença mínima**: Validação da implementação manual

## Personalização

Para diferentes experimentos, modifique:

1. **Grafo**: Altere as arestas em `criar_grafo_exemplo()`
2. **Damping factor**: `alpha` (0.1-0.9) - quanto maior, mais importância aos links
3. **Precisão**: `tol` (1e-3 a 1e-9) - precisão da convergência
4. **Iterações**: `max_iter` - limite máximo de iterações

### Exemplo de Grafo Personalizado:
```python
def criar_grafo_exemplo():
    G = nx.DiGraph()
    arestas = [
        ('Google', 'Wikipedia'), ('Google', 'YouTube'),
        ('Wikipedia', 'Google'), ('YouTube', 'Google'),
        ('Facebook', 'Google'), ('Twitter', 'Facebook')
    ]
    G.add_edges_from(arestas)
    return G
```

## Referências Técnicas

- **Page, L. et al.** (1999). The PageRank Citation Ranking
- **Langville, A. & Meyer, C.** (2006). Google's PageRank and Beyond
- **NetworkX Documentation**: PageRank Implementation

