import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

dados = pd.read_excel("cornelioprocopio.xlsx")

segmento = dados["segmento"].value_counts()

ramoDeAtividade = dados["ramo_de_atividade"].value_counts()

bairro = dados["bairro"].value_counts()
bairroMaiorQue10 = bairro[bairro>10]



st.title("Projeto Analisia\n")
st.subheader("\nGráfico de análise da densidade das empresas por área: ")
# Criar o gráfico de barras 
fig, ax = plt.subplots(figsize=(10, 6))
bairroMaiorQue10.plot(kind='bar', color='skyblue', ax=ax)
plt.xlabel('Bairro')
plt.ylabel('Número de Empresas')
plt.title('Número de Empresas por Bairro (Bairros com mais de 10 empresas)')
plt.xticks(rotation=90)
plt.tight_layout()

# Exibir o gráfico usando Streamlit
st.pyplot(fig)

st.subheader('Análise de Empresas por Bairro')

# Exibir os dados
st.write('**Concentração no Centro:** O bairro Centro possui o maior número de empresas, com um total de 2231. Isso sugere que é uma área comercial importante na cidade, com muitas oportunidades de negócios e atividades econômicas.')

st.write('**Diversidade nos bairros residenciais:** Alguns bairros, como Vila Independência, Jardim Primavera e Jardim Panorama, também têm um número considerável de empresas, apesar de serem mais residenciais. Isso pode indicar uma mistura de atividades comerciais e residenciais nessas áreas.')

st.write('**Bairros com menor número de empresas:** Por outro lado, há vários bairros com um número relativamente baixo de empresas, como Jardim Bela Vista. Isso pode refletir uma menor atividade econômica nessas áreas ou uma concentração de empresas em outros lugares da cidade.')

st.write('**Padrões de distribuição geográfica:** Alguns bairros estão próximos uns dos outros e têm números semelhantes de empresas, o que pode indicar padrões de desenvolvimento urbano ou influência de fatores geográficos na localização das empresas.')

st.write('**Oportunidades de desenvolvimento:** Bairros com um número menor de empresas podem representar oportunidades para o desenvolvimento econômico local, seja através de incentivos para novos negócios ou iniciativas de revitalização urbana.')

# Exibir os dados de empresas por segmento
st.title("\nDistribuição de empresas por segmento na cidade de Cornélio Procópio:\n")
st.subheader("Número de Empresas por Segmento:")
dados_por_segmento = {
    'Serviços': 2291,
    'Comércio': 1683,
    'Indústria': 386,
    'Construção Civil': 329,
    'Agropecuária': 39
}
st.write(pd.DataFrame(dados_por_segmento.items(), columns=['Segmento', 'Número de Empresas']))

# Análise detalhada por segmento
st.subheader("\nAnálise detalhada por segmento:\n")
st.write("**Serviços:** Com 2.291 empresas, o setor de serviços é o mais representado na cidade. Isso sugere uma forte presença de atividades relacionadas a serviços, como educação, saúde, tecnologia, entre outros.")

st.write("**Comércio:** Com 1.683 empresas, o setor de comércio também é significativo em Cornélio Procópio. Isso indica uma variedade de lojas, supermercados, e outras empresas relacionadas ao comércio varejista e atacadista na cidade.")

st.write("**Indústria:** Embora com um número menor de empresas em comparação com os setores de serviços e comércio, a indústria ainda contribui com 386 empresas para a economia local. Isso pode incluir empresas de manufatura, produção e processamento de alimentos, entre outros.")

st.write("**Construção Civil:** Com 329 empresas, o setor da construção civil desempenha um papel importante na cidade, refletindo atividades relacionadas à construção de residências, edifícios comerciais, infraestrutura e obras públicas.")

st.write("**Agropecuária:** Com 39 empresas, o setor agropecuário é o menos representado na cidade. Isso pode indicar uma menor ênfase na agricultura e pecuária dentro do município.")



# Exibindo o gráfico de barras dos segmentos
st.title("\nGráfico de Distribuição de Empresas por Segmento:\n")
fig2, ax2 = plt.subplots(figsize=(10, 6))
plt.barh(list(dados_por_segmento.keys()), list(dados_por_segmento.values()), color='skyblue')
plt.xlabel('Número de Empresas')
plt.ylabel('Segmento')
plt.title('Número de Empresas por Segmento')
plt.gca().invert_yaxis()  # Inverter o eixo y para que os segmentos com mais empresas fiquem no topo
st.pyplot(fig2)

st.write("\nDiversificação Econômica: A cidade possui uma ampla diversificação econômica, com representação significativa em vários setores, incluindo serviços, varejo, indústria, educação e saúde. Isso indica uma economia robusta e resiliente, menos suscetível a flutuações em um único setor.")

st.write("\nPapel dos Serviços: Os serviços emergem como o setor dominante, com destaque para serviços administrativos, saúde, educação e outros serviços diversos. Isso reflete a crescente importância dos serviços na economia moderna, tanto em termos de emprego quanto de contribuição para o PIB.")

st.write("\nImportância do Comércio: O setor de varejo também é significativo, refletindo uma forte demanda por bens de consumo na cidade. Isso sugere uma atividade comercial vibrante e uma comunidade consumidora ativa.")

st.write("\nSetores Industriais e Agropecuários: Embora representem uma parte menor da economia em termos de número de empresas, os setores industriais e agropecuários ainda desempenham papéis importantes na cidade. Eles contribuem para a produção local, emprego e diversificação econômica.")

st.write("\nPotencial de Crescimento: Alguns setores, como química, petroquímica, siderurgia, indústria automotiva e mineração, possuem uma representação relativamente pequena na cidade. Isso pode indicar oportunidades de crescimento e desenvolvimento futuro, desde que haja investimento e apoio adequados.")


