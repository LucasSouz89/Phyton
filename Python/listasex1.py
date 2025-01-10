projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto:
        print(f"Projetos: {projeto}")
    else:
        print("Projeto não disponivel.")