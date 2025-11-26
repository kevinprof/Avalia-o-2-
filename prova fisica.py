import time

def limpar_tela():
    print("\n" * 50)

# --- 1. BANCO DE QUESTÕES (9 Itens) ---
# Estrutura: id, tema, nível, conceito (para relatório) e dados da pergunta.
questoes_db = [
    # === NÍVEL DIFÍCIL ===
    {
        'tema': 'mag', 'nivel': 'dificil',
        'conceito': 'Cálculo vetorial da Força Magnética (Lorentz) e trajetórias',
        'texto': "Uma carga q entra com velocidade V em um campo B uniforme, formando um ângulo de 30º. Qual a trajetória descrita?",
        'opcoes': ["Circular", "Retilínea", "Helicoidal", "Parabólica"],
        'correta': 2 # Índice 2 = Helicoidal
    },
    {
        'tema': 'ind', 'nivel': 'dificil',
        'conceito': 'Lei de Lenz e Freio Magnético',
        'texto': "Um ímã cai em um tubo de cobre e atinge velocidade terminal constante. Isso ocorre devido a:",
        'opcoes': ["Atrito com o ar", "Correntes de Foucault (Eddy)", "Atração gravitacional", "Ferromagnetismo do cobre"],
        'correta': 1 # Correntes de Foucault
    },
    {
        'tema': 'cir', 'nivel': 'dificil',
        'conceito': 'Leis de Kirchhoff (Malhas)',
        'texto': "Em um circuito de malha dupla, a corrente no ramo central é zero. Isso implica necessariamente que:",
        'opcoes': ["As fontes têm a mesma FEM", "A ddp nos nós centrais é nula", "Não há resistência no ramo", "Os resistores estão queimados"],
        'correta': 1 # ddp nula
    },

    # === NÍVEL MÉDIO ===
    {
        'tema': 'mag', 'nivel': 'medio',
        'conceito': 'Regra da Mão Direita (Direção da Força)',
        'texto': "Fio com corrente para a direita, campo magnético entrando na tela. A força magnética atua para:",
        'opcoes': ["Cima", "Baixo", "Esquerda", "Direita"],
        'correta': 0 # Cima
    },
    {
        'tema': 'ind', 'nivel': 'medio',
        'conceito': 'Lei de Faraday (Variação de Fluxo)',
        'texto': "Para induzir corrente em uma espira parada, é fundamental:",
        'opcoes': ["Usar um ímã muito forte", "Variar o fluxo magnético através dela", "Aquecer o fio", "Conectar a uma bateria"],
        'correta': 1 # Variar fluxo
    },
    {
        'tema': 'cir', 'nivel': 'medio',
        'conceito': 'Associação Mista e Lei de Ohm',
        'texto': "Dois resistores de 10Ω em paralelo, ligados em série com um de 5Ω. Tensão total de 20V. Qual a corrente total?",
        'opcoes': ["1 A", "2 A", "4 A", "0.5 A"],
        'correta': 1 # Req=10. I=20/10=2A
    },

    # === NÍVEL FÁCIL ===
    {
        'tema': 'mag', 'nivel': 'facil',
        'conceito': 'Propriedades dos Ímãs',
        'texto': "Ao quebrar um ímã em barra ao meio, o que acontece?",
        'opcoes': ["Separam-se os polos Norte e Sul", "Obtém-se dois novos ímãs completos", "O magnetismo desaparece", "Vira um eletroímã"],
        'correta': 1 # Dois novos ímãs
    },
    {
        'tema': 'ind', 'nivel': 'facil',
        'conceito': 'Natureza da Onda Eletromagnética',
        'texto': "Qual destas é uma onda eletromagnética?",
        'opcoes': ["Som", "Ultrassom", "Luz Visível", "Onda na corda"],
        'correta': 2 # Luz
    },
    {
        'tema': 'cir', 'nivel': 'facil',
        'conceito': 'Definição de Resistência',
        'texto': "Qual a unidade de medida da Resistência Elétrica?",
        'opcoes': ["Volt", "Watt", "Ampere", "Ohm"],
        'correta': 3 # Ohm
    }
]

# Nomes amigáveis para exibição
nomes_temas = {
    'mag': 'Campo e Força Magnética',
    'ind': 'Indução e Ondas Eletromagnéticas',
    'cir': 'Circuitos Elétricos'
}

# --- 2. LÓGICA DA PROVA ---

def obter_questao(tema, nivel):
    """Busca a questão específica no banco de dados"""
    for q in questoes_db:
        if q['tema'] == tema and q['nivel'] == nivel:
            return q
    return None

def fazer_pergunta(questao):
    """Exibe a questão e retorna True se acertou, False se errou"""
    print(f"\n>> {nomes_temas[questao['tema']]} [{questao['nivel'].upper()}]")
    print("-" * 60)
    print(questao['texto'])
    
    for i, opt in enumerate(questao['opcoes']):
        print(f"   {i + 1}) {opt}")
    
    while True:
        try:
            resp = input("\nSua resposta (número): ")
            if not resp.isdigit():
                raise ValueError
            
            resp_int = int(resp) - 1
            if 0 <= resp_int < len(questao['opcoes']):
                return resp_int == questao['correta']
            else:
                print("Número inválido. Escolha uma das opções.")
        except ValueError:
            print("Por favor, digite apenas o número da opção.")

def main():
    # Estado inicial do aluno
    # status: O nível de domínio final (Avançado, Intermediário, Básico, Insuficiente)
    # erros: Lista de conceitos que o aluno errou
    relatorio = {
        'mag': {'status': 'Indefinido', 'erros': [], 'proxima_etapa': 'dificil'},
        'ind': {'status': 'Indefinido', 'erros': [], 'proxima_etapa': 'dificil'},
        'cir': {'status': 'Indefinido', 'erros': [], 'proxima_etapa': 'dificil'}
    }

    print("="*60)
    print("       SISTEMA DE AVALIAÇÃO ADAPTATIVA DE FÍSICA")
    print("="*60)
    nome = input("Digite seu nome completo: ")
    print(f"\nBem-vindo(a), {nome}. A prova começará no nível DIFÍCIL.")
    time.sleep(2)

    # --- FASE 1: NÍVEL DIFÍCIL (Todos os temas) ---
    temas = ['mag', 'ind', 'cir']
    
    print("\n" + "#"*40)
    print(" FASE 1: QUESTÕES DE NÍVEL DIFÍCIL")
    print("#"*40)
    
    for tema in temas:
        q = obter_questao(tema, 'dificil')
        acertou = fazer_pergunta(q)
        
        if acertou:
            relatorio[tema]['status'] = 'Avançado'
            relatorio[tema]['proxima_etapa'] = None # Encerra este tema
            print("Resposta: CORRETA! (Tópico dominado)")
        else:
            relatorio[tema]['erros'].append(q['conceito'])
            relatorio[tema]['proxima_etapa'] = 'medio'
            print("Resposta: INCORRETA.")
        time.sleep(1)

    # --- FASE 2: NÍVEL MÉDIO (Apenas para quem errou a difícil) ---
    # Verifica se existe algum tema pendente para médio
    precisa_medio = any(relatorio[t]['proxima_etapa'] == 'medio' for t in temas)
    
    if precisa_medio:
        print("\n\n" + "#"*40)
        print(" FASE 2: RECUPERAÇÃO (NÍVEL MÉDIO)")
        print(" As questões a seguir são baseadas nos seus erros.")
        print("#"*40)
        time.sleep(2)
        
        for tema in temas:
            if relatorio[tema]['proxima_etapa'] == 'medio':
                q = obter_questao(tema, 'medio')
                acertou = fazer_pergunta(q)
                
                if acertou:
                    relatorio[tema]['status'] = 'Intermediário'
                    relatorio[tema]['proxima_etapa'] = None
                    print("Resposta: CORRETA! (Nível Intermediário garantido)")
                else:
                    relatorio[tema]['erros'].append(q['conceito'])
                    relatorio[tema]['proxima_etapa'] = 'facil'
                    print("Resposta: INCORRETA.")
                time.sleep(1)

    # --- FASE 3: NÍVEL FÁCIL (Apenas para quem errou a média) ---
    precisa_facil = any(relatorio[t]['proxima_etapa'] == 'facil' for t in temas)
    
    if precisa_facil:
        print("\n\n" + "#"*40)
        print(" FASE 3: CONCEITOS BÁSICOS (NÍVEL FÁCIL)")
        print("#"*40)
        time.sleep(2)
        
        for tema in temas:
            if relatorio[tema]['proxima_etapa'] == 'facil':
                q = obter_questao(tema, 'facil')
                acertou = fazer_pergunta(q)
                
                if acertou:
                    relatorio[tema]['status'] = 'Básico'
                    print("Resposta: CORRETA!")
                else:
                    relatorio[tema]['status'] = 'Insuficiente'
                    relatorio[tema]['erros'].append(q['conceito'])
                    print("Resposta: INCORRETA.")
                time.sleep(1)

    # --- RELATÓRIO FINAL ---
    print("\n\n")
    print("="*60)
    print(f"          RELATÓRIO DE DESEMPENHO: {nome.upper()}")
    print("="*60)
    
    for tema in temas:
        dados = relatorio[tema]
        nome_tema = nomes_temas[tema]
        nivel_final = dados['status']
        
        print(f"\nDISCIPLINA: {nome_tema}")
        print(f"STATUS FINAL: {nivel_final.upper()}")
        
        if len(dados['erros']) > 0:
            print("CONCEITOS NÃO DOMINADOS (Para Revisão):")
            for erro in dados['erros']:
                print(f"  [x] {erro}")
        else:
            print("  [v] Nenhum conceito incorreto identificado. Parabéns!")
            
        print("-" * 60)

if __name__ == "__main__":
    main()

    import time

# --- 1. BANCO DE QUESTÕES (9 Itens) ---
questoes_db = [
    # === NÍVEL DIFÍCIL ===
    {
        'tema': 'mag', 'nivel': 'dificil',
        'conceito': 'Cálculo vetorial da Força Magnética (Lorentz) e trajetórias',
        'texto': "Uma carga q entra com velocidade V em um campo B uniforme, formando um ângulo de 30º. Qual a trajetória descrita?",
        'opcoes': ["Circular", "Retilínea", "Helicoidal", "Parabólica"],
        'correta': 2 
    },
    {
        'tema': 'ind', 'nivel': 'dificil',
        'conceito': 'Lei de Lenz e Freio Magnético',
        'texto': "Um ímã cai em um tubo de cobre e atinge velocidade terminal constante. Isso ocorre devido a:",
        'opcoes': ["Atrito com o ar", "Correntes de Foucault (Eddy)", "Atração gravitacional", "Ferromagnetismo do cobre"],
        'correta': 1 
    },
    {
        'tema': 'cir', 'nivel': 'dificil',
        'conceito': 'Leis de Kirchhoff (Malhas)',
        'texto': "Em um circuito de malha dupla, a corrente no ramo central é zero. Isso implica necessariamente que:",
        'opcoes': ["As fontes têm a mesma FEM", "A ddp nos nós centrais é nula", "Não há resistência no ramo", "Os resistores estão queimados"],
        'correta': 1 
    },

    # === NÍVEL MÉDIO ===
    {
        'tema': 'mag', 'nivel': 'medio',
        'conceito': 'Regra da Mão Direita (Direção da Força)',
        'texto': "Fio com corrente para a direita, campo magnético entrando na tela. A força magnética atua para:",
        'opcoes': ["Cima", "Baixo", "Esquerda", "Direita"],
        'correta': 0 
    },
    {
        'tema': 'ind', 'nivel': 'medio',
        'conceito': 'Lei de Faraday (Variação de Fluxo)',
        'texto': "Para induzir corrente em uma espira parada, é fundamental:",
        'opcoes': ["Usar um ímã muito forte", "Variar o fluxo magnético através dela", "Aquecer o fio", "Conectar a uma bateria"],
        'correta': 1 
    },
    {
        'tema': 'cir', 'nivel': 'medio',
        'conceito': 'Associação Mista e Lei de Ohm',
        'texto': "Dois resistores de 10Ω em paralelo, ligados em série com um de 5Ω. Tensão total de 20V. Qual a corrente total?",
        'opcoes': ["1 A", "2 A", "4 A", "0.5 A"],
        'correta': 1 
    },

    # === NÍVEL FÁCIL ===
    {
        'tema': 'mag', 'nivel': 'facil',
        'conceito': 'Propriedades dos Ímãs',
        'texto': "Ao quebrar um ímã em barra ao meio, o que acontece?",
        'opcoes': ["Separam-se os polos Norte e Sul", "Obtém-se dois novos ímãs completos", "O magnetismo desaparece", "Vira um eletroímã"],
        'correta': 1 
    },
    {
        'tema': 'ind', 'nivel': 'facil',
        'conceito': 'Natureza da Onda Eletromagnética',
        'texto': "Qual destas é uma onda eletromagnética?",
        'opcoes': ["Som", "Ultrassom", "Luz Visível", "Onda na corda"],
        'correta': 2 
    },
    {
        'tema': 'cir', 'nivel': 'facil',
        'conceito': 'Definição de Resistência',
        'texto': "Qual a unidade de medida da Resistência Elétrica?",
        'opcoes': ["Volt", "Watt", "Ampere", "Ohm"],
        'correta': 3 
    }
]

nomes_temas = {
    'mag': 'Campo e Força Magnética',
    'ind': 'Indução e Ondas Eletromagnéticas',
    'cir': 'Circuitos Elétricos'
}

def obter_questao(tema, nivel):
    for q in questoes_db:
        if q['tema'] == tema and q['nivel'] == nivel:
            return q
    return None

def fazer_pergunta(questao):
    print(f"\n>> {nomes_temas[questao['tema']]} [{questao['nivel'].upper()}]")
    print("-" * 60)
    print(questao['texto'])
    
    for i, opt in enumerate(questao['opcoes']):
        print(f"   {i + 1}) {opt}")
    
    while True:
        try:
            resp = input("\nSua resposta (número): ")
            if not resp.isdigit():
                raise ValueError
            
            resp_int = int(resp) - 1
            if 0 <= resp_int < len(questao['opcoes']):
                return resp_int == questao['correta']
            else:
                print("Número inválido. Escolha uma das opções.")
        except ValueError:
            print("Por favor, digite apenas o número da opção.")

def main():
    relatorio = {
        'mag': {'status': 'Indefinido', 'erros': [], 'proxima_etapa': 'dificil'},
        'ind': {'status': 'Indefinido', 'erros': [], 'proxima_etapa': 'dificil'},
        'cir': {'status': 'Indefinido', 'erros': [], 'proxima_etapa': 'dificil'}
    }

    print("="*60)
    print("       AVALIAÇÃO FÍSICA")
    print("="*60)
    nome = input("Digite seu nome completo: ")
    print(f"\nBem-vindo(a), {nome}. A prova começará no nível DIFÍCIL.")
    time.sleep(1.5)

    temas = ['mag', 'ind', 'cir']
    
    # --- FASE 1: NÍVEL DIFÍCIL ---
    print("\n" + "#"*40)
    print(" FASE 1: QUESTÕES DE NÍVEL DIFÍCIL")
    print("#"*40)
    
    for tema in temas:
        q = obter_questao(tema, 'dificil')
        acertou = fazer_pergunta(q)
        
        if acertou:
            relatorio[tema]['status'] = 'Avançado'
            relatorio[tema]['proxima_etapa'] = None 
            print("Resposta: CORRETA! (Tópico dominado)")
        else:
            relatorio[tema]['erros'].append(q['conceito'])
            relatorio[tema]['proxima_etapa'] = 'medio'
            print("Resposta: INCORRETA.")
        time.sleep(1)

    # --- FASE 2: NÍVEL MÉDIO ---
    precisa_medio = any(relatorio[t]['proxima_etapa'] == 'medio' for t in temas)
    
    if precisa_medio:
        print("\n\n" + "#"*40)
        print(" FASE 2: RECUPERAÇÃO (NÍVEL MÉDIO)")
        print("#"*40)
        time.sleep(1.5)
        
        for tema in temas:
            if relatorio[tema]['proxima_etapa'] == 'medio':
                q = obter_questao(tema, 'medio')
                acertou = fazer_pergunta(q)
                
                if acertou:
                    relatorio[tema]['status'] = 'Intermediário'
                    relatorio[tema]['proxima_etapa'] = None
                    print("Resposta: CORRETA! (Nível Intermediário garantido)")
                else:
                    relatorio[tema]['erros'].append(q['conceito'])
                    relatorio[tema]['proxima_etapa'] = 'facil'
                    print("Resposta: INCORRETA.")
                time.sleep(1)

    # --- FASE 3: NÍVEL FÁCIL ---
    precisa_facil = any(relatorio[t]['proxima_etapa'] == 'facil' for t in temas)
    
    if precisa_facil:
        print("\n\n" + "#"*40)
        print(" FASE 3: CONCEITOS BÁSICOS (NÍVEL FÁCIL)")
        print("#"*40)
        time.sleep(1.5)
        
        for tema in temas:
            if relatorio[tema]['proxima_etapa'] == 'facil':
                q = obter_questao(tema, 'facil')
                acertou = fazer_pergunta(q)
                
                if acertou:
                    relatorio[tema]['status'] = 'Básico'
                    print("Resposta: CORRETA!")
                else:
                    relatorio[tema]['status'] = 'Insuficiente'
                    relatorio[tema]['erros'].append(q['conceito'])
                    print("Resposta: INCORRETA.")
                time.sleep(1)

    # --- RELATÓRIO FINAL ---
    print("\n\n")
    print("="*60)
    print(f"          RELATÓRIO DE DESEMPENHO: {nome.upper()}")
    print("="*60)
    
    for tema in temas:
        dados = relatorio[tema]
        nome_tema = nomes_temas[tema]
        nivel_final = dados['status']
        
        print(f"\nDISCIPLINA: {nome_tema}")
        print(f"STATUS FINAL: {nivel_final.upper()}")
        
        if len(dados['erros']) > 0:
            print("CONCEITOS NÃO DOMINADOS (Para Revisão):")
            for erro in dados['erros']:
                print(f"  [x] {erro}")
        else:
            print("  [v] Nenhum conceito incorreto identificado. Parabéns!")
            
        print("-" * 60)
    
    input("\nPressione ENTER para fechar o programa...")

if __name__ == "__main__":
    main()