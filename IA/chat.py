import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Dados fictícios de treino
dados = {
    'idade': [25, 30, 35, 28, 22],
    'altura': [170, 180, 160, 175, 168],
    'peso': [70, 80, 60, 75, 65],
    'sexo': ['Masculino', 'Feminino', 'Masculino', 'Masculino', 'Feminino'],
    'atividade_fisica': ['Intermediário', 'Avançado', 'Iniciante', 'Sedentário', 'Intermediário'],
    'objetivo': ['Ganho de massa muscular', 'Emagrecimento', 'Condicionamento Físico', 'Melhora geral da saúde', 'Ganho de massa muscular'],
    'local_treino': ['Academia', 'Casa', 'Parque', 'Academia', 'Casa'],
    'duracao': ['Até 1 hora', 'Até 30 minutos', 'Até 1 hora', 'Mais de 1 hora', 'Até 45 minutos'],
    'titulo': ['Plano para aumento de massa muscular', 'Treino para emagrecimento rápido', 'Treino para resistência cardiovascular', 'Plano de saúde e bem-estar', 'Plano para aumento de massa muscular'],
    'descricao': ['Treino de força com foco em hipertrofia', 'Treino de alta intensidade para queima de gordura', 'Treino cardiovascular e funcional', 'Treino leve e funcional para melhorar saúde', 'Plano de treino com foco em hipertrofia'],
    'link_video': ['https://youtu.be/example1', 'https://youtu.be/example2', 'https://youtu.be/example3', 'https://youtu.be/example4', 'https://youtu.be/example5']
}

# Criação de DataFrame
df = pd.DataFrame(dados)

# Criando os LabelEncoders para todas as variáveis categóricas
le_sexo = LabelEncoder()
le_sexo.fit(['Masculino', 'Feminino'])

le_atividade_fisica = LabelEncoder()
le_atividade_fisica.fit(['Sedentário', 'Iniciante', 'Intermediário', 'Avançado'])

le_objetivo = LabelEncoder()
le_objetivo.fit(['Emagrecimento', 'Ganho de massa muscular', 'Condicionamento Físico', 'Melhora geral da saúde', 'Outro'])

le_local_treino = LabelEncoder()
le_local_treino.fit(['Academia', 'Casa', 'Parque', 'Outro'])

le_duracao = LabelEncoder()
le_duracao.fit(['Até 30 minutos', 'Até 45 minutos', 'Até 1 hora', 'Mais de 1 hora'])

# Transformando as variáveis categóricas do DataFrame
df['sexo'] = le_sexo.transform(df['sexo'])
df['atividade_fisica'] = le_atividade_fisica.transform(df['atividade_fisica'])
df['objetivo'] = le_objetivo.transform(df['objetivo'])
df['local_treino'] = le_local_treino.transform(df['local_treino'])
df['duracao'] = le_duracao.transform(df['duracao'])

# Separando as variáveis preditoras e alvo
X = df[['idade', 'altura', 'peso', 'sexo', 'atividade_fisica', 'objetivo', 'local_treino', 'duracao']]
y = df[['titulo', 'descricao', 'link_video']]

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo de Random Forest
modelo_titulo = RandomForestClassifier(n_estimators=100)
modelo_titulo.fit(X_train, y_train['titulo'])  # Treinando para o título

modelo_descricao = RandomForestClassifier(n_estimators=100)
modelo_descricao.fit(X_train, y_train['descricao'])  # Treinando para a descrição

modelo_link = RandomForestClassifier(n_estimators=100)
modelo_link.fit(X_train, y_train['link_video'])  # Treinando para o link

# Função para prever os resultados
def prever_treino(idade, altura, peso, sexo, atividade_fisica, objetivo, local_treino, duracao):
    entrada = [[idade, altura, peso, le_sexo.transform([sexo])[0], 
                le_atividade_fisica.transform([atividade_fisica])[0], 
                le_objetivo.transform([objetivo])[0], 
                le_local_treino.transform([local_treino])[0], 
                le_duracao.transform([duracao])[0]]]
    
    # Prevendo título, descrição e link
    titulo = modelo_titulo.predict(entrada)[0]
    descricao = modelo_descricao.predict(entrada)[0]
    link_video = modelo_link.predict(entrada)[0]
    
    return titulo, descricao, link_video

# Função para pegar dados do usuário
def coletar_dados_usuario():
    idade = int(input("Digite sua idade: "))
    altura = int(input("Digite sua altura (em cm): "))
    peso = int(input("Digite seu peso (em kg): "))
    sexo = input("Digite seu sexo (Masculino/Feminino): ")
    atividade_fisica = input("Qual seu nível de atividade física? (Sedentário/Iniciante/Intermediário/Avançado): ")
    objetivo = input("Qual seu objetivo? (Emagrecimento/Ganho de massa muscular/Condicionamento Físico/Melhora geral da saúde/Outro): ")
    local_treino = input("Onde você prefere treinar? (Academia/Casa/Parque/Outro): ")
    duracao = input("Qual a duração do treino? (Até 30 minutos/Até 45 minutos/Até 1 hora/Mais de 1 hora): ")
    
    return idade, altura, peso, sexo, atividade_fisica, objetivo, local_treino, duracao

# Receber dados do usuário
idade, altura, peso, sexo, atividade_fisica, objetivo, local_treino, duracao = coletar_dados_usuario()

# Prever o título, descrição e link com os dados inseridos
titulo_previsao, descricao_previsao, link_video_previsao = prever_treino(idade, altura, peso, sexo, atividade_fisica, objetivo, local_treino, duracao)

# Exibir os resultados
print(f"\nTítulo: {titulo_previsao}")
print(f"Descrição: {descricao_previsao}")
print(f"Link do vídeo: {link_video_previsao}")
