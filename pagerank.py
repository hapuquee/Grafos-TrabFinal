import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def criar_grafo_exemplo():
    """
    Cria um grafo direcionado com múltiplos nós e arestas para demonstrar o PageRank.
    """
    G = nx.DiGraph()
    
    # Adicionar arestas (links entre páginas)
    # Estrutura base original
    arestas = [
        ('A', 'B'), ('A', 'C'), ('A', 'D'),
        ('B', 'C'), ('B', 'D'), ('B', 'E'),
        ('C', 'A'), ('C', 'D'), ('C', 'F'),
        ('D', 'A'), ('D', 'E'), ('D', 'G'),
        ('E', 'F'), ('E', 'G'), ('E', 'H'),
        ('F', 'A'), ('F', 'C'), ('F', 'I'),
        ('G', 'B'), ('G', 'H'), ('G', 'J'),
        ('H', 'E'), ('H', 'I'), ('H', 'J'),
        ('I', 'F'), ('I', 'J'), ('I', 'A'),
        ('J', 'G'), ('J', 'H'), ('J', 'B')
    ]
    
    G.add_edges_from(arestas)
    
    print(f"Grafo criado com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas")
    print(f"Nós: {list(G.nodes())}")
    print(f"Arestas: {list(G.edges())}")
    
    return G

def calcular_pagerank(G, alpha=0.85, max_iter=100, tol=1e-6):
    """
    Implementação manual do PageRank usando método das potências.
    
    Args:
        G: Grafo NetworkX direcionado
        alpha: Fator de amortecimento (0.85 padrão)
        max_iter: Máximo de iterações
        tol: Tolerância para convergência
    """
    print(f"\n--- Calculando PageRank (alpha={alpha}) ---")
    
    # Obter lista de nós
    nodes = list(G.nodes())
    N = len(nodes)
    
    # Inicializar PageRank: todos os nós começam com 1/N
    pagerank = {node: 1.0/N for node in nodes}
    
    print(f"Valor inicial para cada nó: {1.0/N:.4f}")
    
    # Iterações do algoritmo
    for iteracao in range(max_iter):
        novo_pagerank = {}
        
        # Para cada nó, calcular novo PageRank
        for node in nodes:
            # Termo de teletransporte: (1-alpha)/N
            pr = (1 - alpha) / N
            
            # Somar contribuições dos nós que apontam para este nó
            for predecessor in G.predecessors(node):
                out_degree = G.out_degree(predecessor)
                if out_degree > 0:
                    pr += alpha * (pagerank[predecessor] / out_degree)
            
            novo_pagerank[node] = pr
        
        # Verificar convergência
        erro = sum(abs(novo_pagerank[node] - pagerank[node]) for node in nodes)
        
        if erro < tol:
            print(f"Convergência alcançada na iteração {iteracao + 1}")
            print(f"Erro: {erro:.8f}")
            return novo_pagerank
        
        pagerank = novo_pagerank
        
        # Mostrar progresso a cada 10 iterações
        if (iteracao + 1) % 10 == 0:
            print(f"Iteração {iteracao + 1}: erro = {erro:.8f}")
    
    print("Máximo de iterações atingido")
    return pagerank

def exibir_resultados(pagerank_scores):
    """
    Exibe os resultados do PageRank ordenados por importância.
    """
    print(f"\n--- Resultados do PageRank ---")
    
    # Ordenar por score (maior para menor)
    sorted_scores = sorted(pagerank_scores.items(), key=lambda x: x[1], reverse=True)
    
    print("Ranking de Importância:")
    for rank, (node, score) in enumerate(sorted_scores, 1):
        print(f"#{rank} Nó {node}: {score:.6f} ({score*100:.2f}%)")
    
    # Verificar se a soma é aproximadamente 1
    soma_total = sum(pagerank_scores.values())
    print(f"\nSoma total dos scores: {soma_total:.6f}")
    print("(Deve ser aproximadamente 1.0)")

def visualizar_grafo(G, pagerank_scores):
    """
    Visualiza o grafo com tamanhos proporcionais ao PageRank.
    """
    print(f"\n--- Gerando Visualização ---")
    
    plt.figure(figsize=(10, 8))
    
    # Layout do grafo
    pos = nx.spring_layout(G, seed=42)
    
    # Tamanhos proporcionais ao PageRank (multiplicar por 3000 para visibilidade)
    tamanhos = [pagerank_scores[node] * 3000 for node in G.nodes()]
    
    # Cores baseadas nos scores
    cores = [pagerank_scores[node] for node in G.nodes()]
    
    # Desenhar nós
    nx.draw_networkx_nodes(G, pos, 
                          node_size=tamanhos,
                          node_color=cores,
                          cmap=plt.cm.Reds,
                          alpha=0.8)
    
    # Desenhar arestas
    nx.draw_networkx_edges(G, pos, 
                          arrowstyle='->',
                          arrowsize=20,
                          alpha=0.6)
    
    # Adicionar labels
    nx.draw_networkx_labels(G, pos, 
                           font_size=12, 
                           font_weight='bold')
    
    # Adicionar scores como texto
    for node, (x, y) in pos.items():
        plt.text(x, y-0.1, f'{pagerank_scores[node]:.3f}', 
                ha='center', va='center', fontsize=10,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.7))
    
    plt.title("Visualização do PageRank\n(Tamanho = Importância)", fontsize=14)
    plt.axis('off')
    
    # Salvar visualização
    plt.savefig('/home/hapuque/Downloads/UFAM/grafos/pagerank_simples.png', 
                dpi=300, bbox_inches='tight')
    print("Visualização salva como 'pagerank_simples.png'")
    plt.close()

def main():
    """
    Função principal que executa todo o pipeline do PageRank.
    """
    print("=== IMPLEMENTAÇÃO SIMPLES DO PAGERANK ===")
    
    # 1. Criar grafo
    grafo = criar_grafo_exemplo()
    
    # 2. Calcular PageRank
    scores = calcular_pagerank(grafo, alpha=0.85)
    
    # 3. Exibir resultados
    exibir_resultados(scores)
    
    # 4. Visualizar
    visualizar_grafo(grafo, scores)
    
    print("\n=== EXECUÇÃO CONCLUÍDA ===")

if __name__ == "__main__":
    main()
