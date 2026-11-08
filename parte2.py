def criar_grafo():
    matriz = []
    vertices = []
    return matriz, vertices

def inserir_vertice(matriz, vertices, vertice):
    if vertice in vertices:
        print("\nO vértice adicionado já EXISTE!")
        return
    vertices.append(vertice)

    for linha in matriz:
        linha.append(0)
    nova_linha = [0] * len(vertices)
    matriz.append(nova_linha)
    print(f"\nVértice {vertice} foi ADICIONADO!")

def remover_vertice(matriz, vertices, vertice):
    if vertice not in vertices:
        print(f"\nO vértice {vertice} NÃO EXISTE")
        return
    idx = vertices.index(vertice)
    vertices.pop(idx)
    matriz.pop(idx)
    for linha in matriz:
        linha.pop(idx)
    print(f"\nVértice {vertice} foi REMOVIDO!")

def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=True):
    if origem not in vertices or destino not in vertices:
        print(f"\n❌ Erro: Um ou ambos os vértices ('{origem}', '{destino}') não existem! Insira-os primeiro.")
        return

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1
    print(f"\nA aresta entre '{origem}' e '{destino}' foi ADICIONADA!")

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=True):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        
        # Verifica se a aresta realmente existe antes de remover
        if matriz[i][j] == 1:
            matriz[i][j] = 0
            if nao_direcionado:
                matriz[j][i] = 0
            print(f"\nA aresta entre '{origem}' e '{destino}' foi REMOVIDA!")
        else:
            print(f"\nA aresta entre '{origem}' e '{destino}' NÃO EXISTE.")
    else:
        print("\nUm ou ambos os vértices NÃO EXISTEM.")

def existe_aresta(matriz, vertices, origem, destino):
    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        if matriz[i][j] == 1:
            print("\nA aresta em questão EXISTE!")
            return True
    print("\nA aresta em questão NÃO EXISTE!")
    return False

def vizinhos(matriz, vertices, vertice):
    if vertice not in vertices:
        return []
    idx = vertices.index(vertice)
    return [vertices[j] for j in range(len(vertices)) if matriz[idx][j] == 1]

def listar_vizinhos(matriz, vertices, vertice):
    if vertice in vertices:
        v_list = vizinhos(matriz, vertices, vertice)
        print(f"\nVizinhos do vértice '{vertice}': {v_list}")
    else:
        print(f"\nO vértice '{vertice}' NÃO EXISTE.")

def grau_vertices(matriz, vertices):
    graus = {}
    for i, v in enumerate(vertices):
        saida = sum(matriz[i])
        entrada = sum(matriz[j][i] for j in range(len(vertices)))
        total = saida + entrada
        graus[v] = {"saida": saida, "entrada": entrada, "total": total}
    return graus

def percurso_valido(matriz, vertices, caminho):
    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i + 1]
        if u not in vertices or v not in vertices:
            print(f"\nO percurso {caminho} não é possível (vértice inexistente).")
            return False
        
        iu = vertices.index(u)
        iv = vertices.index(v)
        if matriz[iu][iv] == 0:
            print(f"\nO percurso {caminho} não é possível (falha com os vértices '{u}' e '{v}').")
            return False
            
    print(f"\nO percurso {caminho} é POSSÍVEL.")
    return True

def exibir_grafo(matriz, vertices):
    if not vertices:
        print("\nO grafo está VAZIO.")
        return

    print("\n--- MATRIZ ADJACÊNCIA ---")
    print("    " + "  ".join(str(v) for v in vertices))
    for i, v in enumerate(vertices):
        print(f"{v}: {matriz[i]}")

def main():
    matriz = None
    vertices = None

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
            matriz, vertices = criar_grafo()
            print("\nGrafo criado/reinicializado com sucesso!")
            
        elif escolha in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            if matriz is None or vertices is None:
                print("\n⚠️ ATENÇÃO: Você precisa criar o grafo primeiro! Escolha a opção [1].")
            else:
                if escolha == "2":
                    v = input("Digite o nome do vértice a ser inserido: ")
                    inserir_vertice(matriz, vertices, v)
                elif escolha == "3":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    inserir_aresta(matriz, vertices, u, v)
                elif escolha == "4":
                    v = input("Digite o nome do vértice a ser removido: ")
                    remover_vertice(matriz, vertices, v)
                elif escolha == "5":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    remover_aresta(matriz, vertices, u, v)
                elif escolha == "6":
                    v = input("Digite o nome do vértice para calcular o grau: ")
                    if v in vertices:
                        graus = grau_vertices(matriz, vertices)
                        print(f"\nO grau do vértice '{v}' é {graus[v]['total']}")
                    else:
                        print(f"\nO vértice '{v}' NÃO EXISTE.")
                elif escolha == "7":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    existe_aresta(matriz, vertices, u, v)
                elif escolha == "8":
                    u = input("Digite o vértice para listar os vizinhos: ")
                    listar_vizinhos(matriz, vertices, u)
                elif escolha == "9":
                    entrada = input("Digite o percurso, separado por vírgulas (A,B,C etc): ").strip()
                    percurso = [x.strip() for x in entrada.split(",")]
                    percurso_valido(matriz, vertices, percurso)
                elif escolha == "10":
                    exibir_grafo(matriz, vertices)

        elif escolha == "0":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()