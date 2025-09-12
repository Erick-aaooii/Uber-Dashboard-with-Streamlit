# Uber Dashboard com Streamlit

Este projeto é um dashboard interativo desenvolvido com [Streamlit](https://streamlit.io/) para análise de dados de corridas Uber na região NCR. Ele permite visualizar KPIs, gráficos e estatísticas relevantes a partir de um dataset real.

## Como rodar o projeto

### 1. Pré-requisitos
- Python 3.11+
- [Streamlit](https://streamlit.io/)
- Instalar dependências do `requirements.txt`

### 2. Instalação

Clone o repositório e instale as dependências:
```bash
pip install -r [requirements.txt](http://_vscodecontentref_/0)
```

### 3. Executando localmente

```bash
streamlit run [main.py](http://_vscodecontentref_/1)
```

 O dashboard será iniciado em http://localhost:8501

### 4. Executando com Docker

```bash
docker build -t uber-dashboard .
docker run -p 8501:8501 uber-dashboard
```

## Estrutura dos arquivos

- ```main.py:``` Ponto de entrada do projeto. Executa a função principal do dashboard.
- ```requirements.txt:``` Lista de dependências Python necessárias.
- ```dockerfile:``` Permite criar um container Docker para rodar o dashboard.
- ```src/pages/page.py:``` Contém a função show_page() que monta a interface principal do dashboard.
- ```src/utils/kpis.py:``` Funções para cálculo dos KPIs (total de corridas, completadas, canceladas, etc).
- ```src/utils/charts.py:``` Funções para geração dos gráficos (pizza, barra, linha) usando Plotly.
- ```src/data/ncr_ride_bookings.csv:``` Base de dados utilizada para análise.
- ```src/assets/uber.png:``` Ícone utilizado no dashboard.

### Como utilizar

1. Ao iniciar o dashboard, você verá métricas principais como total de corridas, completadas, canceladas e distância média.
2. Abaixo, são exibidas análises detalhadas, como horários de pico, principais locais de embarque/desembarque, distribuição de métodos de pagamento e motivos de cancelamento.
3. Os gráficos são interativos e permitem explorar os dados de forma visual.

### Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

```bash
Basta copiar e colar esse conteúdo no seu arquivo [readme.md](http://_vscodecontentref_/2).
```