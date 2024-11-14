import pandas as pd

# Definição dos perfis e níveis de habilidades desejados
perfils_habilidades = {
    "Dev BackEnd COBOL": {
        "Configuracao e mudanca": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "Ciclo de vida de software (build, teste e deploy)": 2,
        "COBOL": 3,
        "Projeto de arquiteturas de integracao e seguranca": 1,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 1,
        "Testes de Software Funcionais (Metodologia, tecnicas, ferramentas)": 1,
        "Testes de Performance": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Conhecimento em linguagem SQL": 1,
    },
    "Dev BackEnd JAVA": {
        "Configuracao e mudanca": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "Ciclo de vida de software (build, teste e deploy)": 2,
        "JAVA": 3,
        "Projeto de arquiteturas de integracao e seguranca": 1,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 1,
        "Testes de Software Funcionais (Metodologia, tecnicas, ferramentas)": 1,
        "Testes de Performance": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Conhecimento em linguagem SQL": 1,
    },
    "Dev BackEnd DotNet": {
        "Configuracao e mudanca": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "Ciclo de vida de software (build, teste e deploy)": 2,
        "C++ C# e .NET": 3,
        "Projeto de arquiteturas de integracao e seguranca": 1,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 1,
        "Testes de Software Funcionais (Metodologia, tecnicas, ferramentas)": 1,
        "Testes de Performance": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Conhecimento em linguagem SQL": 1,
    },
    "Dev FrontEnd": {
        "HTML, CSS": 3,
        "Configuracao e mudanca": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "Ciclo de vida de software (build, teste e deploy)": 2,
        "Projeto de arquiteturas de integracao e seguranca": 1,
        "Testes de Software Funcionais (Metodologia, tecnicas, ferramentas)": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Javascript, Typescript": 3,
        "Angular": 2,
        "MFE (micro frontend)": 1,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 1,
    },
    "Dev Mobile Android": {
        "Configuracao e mudanca": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "Ciclo de vida de software (build, teste e deploy)": 2,
        "Desenvolvimento Android": 3,
        "Projeto de arquiteturas de integracao e seguranca": 1,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 1,
        "Testes de Software Funcionais (Metodologia, tecnicas, ferramentas)": 1,
        "Testes de Performance": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Conhecimento em linguagem SQL": 1,
    },
    "Dev Mobile IOS": {
        "Configuracao e mudanca": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "Ciclo de vida de software (build, teste e deploy)": 2,
        "Desenvolvimento IOS": 3,
        "Projeto de arquiteturas de integracao e seguranca": 1,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 1,
        "Testes de Software Funcionais (Metodologia, tecnicas, ferramentas)": 1,
        "Testes de Performance": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Conhecimento em linguagem SQL": 1,
    },
    "Fundamental UX": {
        "Tecnicas de facilitacao": 3,
        "Fundamentos de Design": 3,
        "Pesquisa com usuarios": 3,
        "Ferramentas de prototipacao (ex: Figma)": 3,
        "Validacao com o usuario": 3,
        "Metricas em UX": 3,
        "Metodos ageis": 2,
        "Gestao de fluxo": 2,
        "Gestao de Produto e de Backlog": 2,
        "Politicas de relacionamento com fornecedores": 1,
    },
    "Arquiteto TI": {
        "MFE (micro frontend)": 2,
        "Disciplinas de Suporte ao Desenvolvimento": 2,
        "C++ C# e .NET": 2,
        "JAVA": 2,
        "Outras tecnologias cross plataform - Mobile": 2,
        "Planejamento e producao de sistemas servicos produtos sites e softwares": 2,
        "Projeto de arquiteturas de integracao e seguranca": 2,
        "Revisao de arquiteturas diagnosticar problemas e otimizar solucoes": 2,
        "Elaboracao de diagramas e fluxos utilizando notacao BPMN UML e Archimate e C4 Model": 2,
        "Definicao de solucoes de TI a partir de necessidades de negocio e jornadas do cliente": 2,
        "Definicao da estrutura e o design dos sistemas de software levando em consideracao os requisitos de negocios as restricoes tecnicas e as metas de desempenho": 2,
        "Pratica em implementacao eficiente e correta das solucoes arquiteturais": 2,
        "Revisoes e verificacoes tecnicas quanto a conformidade com os padroes e diretrizes de arquitetura de solucao": 2,
        "Avaliacao de novas tecnologias e ferramentas que possam melhorar a arquitetura e o desempenho dos sistemas existentes": 2,
        "Ciclo de vida de software (build teste e deploy)": 1,
        "Testes de Software Funcionais (Metodologia tecnicas ferramentas)": 1,
        "Ferramentas de seguranca de aplicacoes como SAST DAST e SCA": 1,
        "Estrategias de seguranca para aplicacoes no ciclo DevSecOps": 1,
        "Seguranca de software e desenvolvimento seguro": 1,
        "Arquitetura e Design Seguro de SW": 1,
        "Boas praticas de arquitetura de nuvem": 1,
        "DevSecOps e SRE (Site Reliability Engineering)": 1,
        "Construcao e manutencao dos modelos conceituais logicos e fisicos de dados": 1,
        "Conhecimento em linguagem SQL": 1,
        "Experiência em algum sistema gerenciador de banco de dados e seus utilitarios": 1,
        "Elaboracao de solucoes quanto a implementacao com utilizacao de um SGBD": 1,
    }
}

# Carregar dados das respostas dos empregados a partir de um arquivo CSV
respostas_df = pd.read_csv('https://github.com/sergiacleto/IA_GESTAO_DE_TALENTOS/blob/main/respostas.csv')

# Função para analisar as lacunas de habilidades
def analisar_lacunas(empregado, habilidades_atual):
    perfil = empregado['perfil']
    lacunas = {}
    if perfil in perfils_habilidades:
        habilidades_necessarias = perfils_habilidades[perfil]
        for habilidade, nivel_necessario in habilidades_necessarias.items():
            nivel_atual = habilidades_atual.get(habilidade, 0)
            if nivel_atual < nivel_necessario:
                lacunas[habilidade] = (nivel_atual, nivel_necessario)
    return lacunas

# Analisar as lacunas de habilidades para cada empregado
empregados_lacunas = []
for idx, empregado in respostas_df.iterrows():
    habilidades_atual = respostas_df[respostas_df['id'] == empregado['id']].set_index('habilidade')['nivel'].to_dict()
    lacunas = analisar_lacunas(empregado, habilidades_atual)
    empregados_lacunas.append({
        "id": empregado['id'],
        "nome": empregado['nome'],
        "perfil": empregado['perfil'],
        "lacunas": lacunas
    })

# Exibir as lacunas de habilidades
for empregado in empregados_lacunas:
    print(f"Empregado: {empregado['nome']} (Perfil: {empregado['perfil']})")
    print("Lacunas de Habilidades:")
    for habilidade, (nivel_atual, nivel_necessario) in empregado['lacunas'].items():
        print(f" - {habilidade}: Nível Atual = {nivel_atual}, Nível Necessário = {nivel_necessario}")
    print()

# Gerar recomendações de capacitação
def gerar_recomendacoes(empregado):
    recomendacoes = []
    for habilidade, (nivel_atual, nivel_necessario) in empregado
