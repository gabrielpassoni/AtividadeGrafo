def criar_grafo():
    return {}

def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
        print(f"Vértice {vertice} foi adicionado!")
    else:
        print("O vértice adicionado já existe!")

def inserir_aresta(grafo, origem, destino, nao_direcionado=True):
    if origem not in grafo or destino not in grafo:
        print(f"\n❌ Erro: Um ou ambos os vértices ('{origem}', '{destino}') não existem! Insira-os primeiro.")
        return

    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado and origem not in grafo[destino]:
        grafo[destino].append(origem)
    print(f"\nA aresta entre '{origem}' e '{destino}' foi adicionada!")

def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice in grafo:
        for outro in list(grafo.keys()):
            if vertice in grafo[outro]:
                grafo[outro].remove(vertice)
        del grafo[vertice]
        print(f"Vértice {vertice} foi removido!")
    else:
        print(f"O vértice {vertice} não existe!")

def remover_aresta(grafo, origem, destino, nao_direcionado=True):
    # Verifica se a origem existe e se o destino é vizinho dela
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)
        if nao_direcionado and destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)
        print(f"A aresta entre '{origem}' e '{destino}' foi removida!")
    else:
        print(f"A aresta entre '{origem}' e '{destino}' não existe.")

def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []

def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos do vértice '{vertice}': {vizinhos(grafo, vertice)}")
    else:
        print(f"O vértice '{vertice}' não existe.")

def exibir_grafo(grafo):
    if not grafo:
        print("O grafo está vazio.")
        return
    for v, viz in grafo.items():
        print(f"{v} --> {viz}")

def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        print("A aresta em questão existe!")
        return True
    else:
        print("A aresta em questão não existe!")
        return False

def grau_vertices(grafo):
    graus = {}
    for u in grafo:
        saida = len(grafo[u])
        entrada = sum(1 for v in grafo if u in grafo[v])
        total = entrada + saida
        graus[u] = {"saida": saida, "entrada": entrada, "total": total}
    return graus

def percurso_valido(grafo, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if not (u in grafo and v in grafo[u]):
            print(f"O percurso {caminho} não é possível (falha com os vértices '{u}' e '{v}').")
            return False
    print(f"O percurso {caminho} é possível.")
    return True

def main():
    grafo = None

    while True:
        print("""
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        [1] - Criar Grafo
        [2] - Inserir Vértice
        [3] - Inserir Aresta
        [4] - Remover Vértice
        [5] - Remover Aresta
        [6] - Calcular Grau
        [7] - Verificar Aresta
        [8] - Verificar Vizinhos
        [9] - Verificar Percurso
        [10] - Exibir Grafo
        [0] - Sair
        -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        """)

        escolha = input("Digite o número da opção desejada: ")

        if escolha == "1":
            grafo = criar_grafo()
            print("Grafo criado/reinicializado com sucesso!")
            
        elif escolha in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            if grafo is None:
                print("\n⚠️ ATENÇÃO: Você precisa criar o grafo primeiro! Escolha a opção [1].")
            else:
                if escolha == "2":
                    v = input("Digite o nome do vértice a ser inserido: ")
                    inserir_vertice(grafo, v)
                elif escolha == "3":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    inserir_aresta(grafo, u, v)
                elif escolha == "4":
                    v = input("Digite o nome do vértice a ser removido: ")
                    remover_vertice(grafo, v)
                elif escolha == "5":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    remover_aresta(grafo, u, v)
                elif escolha == "6":
                    v = input("Digite o nome do vértice para calcular o grau: ")
                    if v in grafo:
                        graus = grau_vertices(grafo)
                        print(f"O grau do vértice '{v}' é {graus[v]['total']}.")
                    else:
                        print(f"O vértice '{v}' não existe.")
                elif escolha == "7":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    existe_aresta(grafo, u, v)
                elif escolha == "8":
                    u = input("Digite o vértice para listar os vizinhos: ")
                    listar_vizinhos(grafo, u)
                elif escolha == "9":
                    entrada = input("Digite o percurso, separado por vírgulas (A,B,C etc): ").strip()
                    percurso = [x.strip() for x in entrada.split(",")]
                    percurso_valido(grafo, percurso)
                elif escolha == "10":
                    exibir_grafo(grafo)

        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()