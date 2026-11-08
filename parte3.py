def criar_grafo():
    return [], []

def inserir_vertice(vertices, vertice):
    if vertice in vertices:
        print(f"\nO vértice {vertice} adicionado já EXISTE!")
        return
    vertices.append(vertice)
    print(f"\nVértice {vertice} foi ADICIONADO!")

def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=True):
    if origem not in vertices or destino not in vertices:
        print(f"\n❌ Erro: Um ou ambos os vértices ('{origem}', '{destino}') não existem! Insira-os primeiro.")
        return

    if nao_direcionado:
        if [origem, destino] in arestas or [destino, origem] in arestas:
            print(f"\nA aresta entre '{origem}' e '{destino}' já EXISTE!")
            return
    else:
        if [origem, destino] in arestas:
            print(f"\nA aresta entre '{origem}' e '{destino}' já EXISTE!")
            return

    arestas.append([origem, destino])
    if nao_direcionado and origem != destino:
        arestas.append([destino, origem])
    print(f"\nA aresta entre '{origem}' e '{destino}' foi ADICIONADA!")

def remover_aresta(arestas, origem, destino, nao_direcionado=True):
    # Verifica se a aresta existe antes de tentar remover
    existe = False
    if nao_direcionado:
        if [origem, destino] in arestas or [destino, origem] in arestas:
            existe = True
    else:
        if [origem, destino] in arestas:
            existe = True

    if not existe:
        print(f"\nA aresta entre '{origem}' e '{destino}' NÃO EXISTE.")
        return

    # Realiza a remoção de fato
    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
    if nao_direcionado and [destino, origem] in arestas:
        arestas.remove([destino, origem])
        
    print(f"\nA aresta entre '{origem}' e '{destino}' foi REMOVIDA!")
    
def remover_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"\nO vértice '{vertice}' NÃO EXISTE.")
        return
    vertices.remove(vertice)
    arestas[:] = [a for a in arestas if a[0] != vertice and a[1] != vertice]
    print(f"\nVértice {vertice} foi REMOVIDO!")

def existe_aresta(arestas, origem, destino):
    return [origem, destino] in arestas or [destino, origem] in arestas

def vizinhos(vertices, arestas, vertice):
    lista_vizinhos = []
    for a in arestas:
        if a[0] == vertice:
            if a[1] not in lista_vizinhos:
                lista_vizinhos.append(a[1])
    return lista_vizinhos

def grau_vertices(vertices, arestas):
    graus = {}
    for v in vertices:
        saida = sum(1 for a in arestas if a[0] == v)
        entrada = sum(1 for a in arestas if a[1] == v)
        total = saida + entrada
        graus[v] = {"saida": saida, "entrada": entrada, "total": total}
    return graus

def percurso_valido(arestas, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(arestas, caminho[i], caminho[i+1]):
            return False
    return True

def listar_vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"\nO vértice '{vertice}' NÃO EXISTE.")
        return
    v_list = vizinhos(vertices, arestas, vertice)
    print(f"\nVizinhos do vértice '{vertice}': {v_list}")

def exibir_grafo(vertices, arestas):
    if not vertices and not arestas:
        print("\nO grafo está VAZIO.")
        return
    print("\n--- LISTA DE VÉRTICES ---")
    print(vertices)
    print("--- LISTA DE ARESTAS ---")
    print(arestas)

def main():
    vertices, arestas = None, None

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
            vertices, arestas = criar_grafo()
            print("\nGrafo criado/reinicializado com sucesso!")

        elif escolha in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            if vertices is None or arestas is None:
                print("\n⚠️ ATENÇÃO: Você precisa criar o grafo primeiro! Escolha a opção [1].")
            else:
                if escolha == "2":
                    v = input("Digite o nome do vértice a ser inserido: ")
                    inserir_vertice(vertices, v)
                elif escolha == "3":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    inserir_aresta(vertices, arestas, u, v)
                elif escolha == "4":
                    v = input("Digite o nome do vértice a ser removido: ")
                    remover_vertice(vertices, arestas, v)
                elif escolha == "5":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    remover_aresta(arestas, u, v)
                elif escolha == "6":
                    v = input("Digite o nome do vértice para calcular o grau: ")
                    if v not in vertices:
                        print(f"\nO vértice '{v}' NÃO EXISTE.")
                    else:
                        graus = grau_vertices(vertices, arestas)
                        print(f"\nO grau do vértice '{v}' é {graus[v]['total']}")
                elif escolha == "7":
                    u = input("Digite o primeiro vértice: ")
                    v = input("Digite o segundo vértice: ")
                    if existe_aresta(arestas, u, v):
                        print("\nA aresta em questão EXISTE!")
                    else:
                        print("\nA aresta em questão NÃO EXISTE!")
                elif escolha == "8":
                    u = input("Digite o vértice para listar os vizinhos: ")
                    listar_vizinhos(vertices, arestas, u)
                elif escolha == "9":
                    entrada = input("Digite o percurso, separado por vírgulas (A,B,C etc): ").strip()
                    percurso = [x.strip() for x in entrada.split(",")]
                    if not all(node in vertices for node in percurso):
                        print(f"\nO percurso {percurso} não é possível (vértice inexistente).")
                    else:
                        if percurso_valido(arestas, percurso):
                            print(f"\nO percurso {percurso} é POSSÍVEL.")
                        else:
                            print(f"\nO percurso {percurso} não é possível (falha nas arestas).")
                elif escolha == "10":
                    exibir_grafo(vertices, arestas)

        elif escolha == "0":
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()