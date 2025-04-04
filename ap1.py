def jogo_perguntas():
    # Inicializando os pontos para cada área
    desenvolvimento = 0
    produto = 0
    qualidade = 0

    # Perguntas de Desenvolvimento de Software
    print("Área: Desenvolvimento de Software")
    desenvolvimento += int(input("1. Gosto de programar e resolver problemas com código (1-5): "))
    desenvolvimento += int(input("2. Tenho interesse em criar aplicativos e sites (1-5): "))
    desenvolvimento += int(input("3. Gosto de aprender novas linguagens de programação (1-5): "))
    desenvolvimento += int(input("4. Prefiro trabalhar com lógica e estruturação de código (1-5): "))
    desenvolvimento += int(input("5. Tenho paciência para depurar erros e otimizar código (1-5): "))

    # Perguntas da Área de Produto
    print("\nÁrea: Produtos")
    produto += int(input("1. Gosto de pensar na experiência do usuário ao usar um sistema (1-5): "))
    produto += int(input("2. Tenho interesse em pesquisa de mercado e comportamento do usuário (1-5): "))
    produto += int(input("3. Me interesso por criar soluções inovadoras e intuitivas (1-5): "))
    produto += int(input("4. Gosto de trabalhar com design, wireframes ou prototipagem (1-5): "))
    produto += int(input("5. Quero entender e definir estratégias para melhorar produtos digitais (1-5): "))

    # Perguntas da Área de Qualidade
    print("\nÁrea: Qualidade")
    qualidade += int(input("1. Gosto de testar e garantir que sistemas funcionem corretamente (1-5): "))
    qualidade += int(input("2. Tenho interesse em encontrar erros e melhorar a estabilidade dos produtos (1-5): "))
    qualidade += int(input("3. Acredito que testes automatizados ajudam a evitar falhas em sistemas (1-5): "))
    qualidade += int(input("4. Gosto de seguir padrões e documentar processos para garantir qualidade (1-5): "))
    qualidade += int(input("5. Quero trabalhar garantindo que um software funcione bem para todos os usuários (1-5): "))

    # Determinando a área de maior afinidade
    areas = {
        "Desenvolvimento de Software": desenvolvimento,
        "Produto": produto,
        "Qualidade": qualidade
    }

    maior_pontuacao = max(areas.values())
    areas_empatadas = [area for area, pontuacao in areas.items() if pontuacao == maior_pontuacao]

    # Resultado
    if len(areas_empatadas) > 1:
        print(f"\nÁreas empatadas: {', '.join(areas_empatadas)}")
    else:
        print(f"\nA área mais afinada com seu perfil é: {areas_empatadas[0]}")

# Executar o jogo
jogo_perguntas()