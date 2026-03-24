# Analisador de Municípios IBGE

Script Python que lê dados públicos de municípios brasileiros, processa as informações e gera um relatório JSON com estatísticas por região.

## Funcionalidades
- Leitura de dados reais em CSV
- Identificação do município mais populoso
- Soma da população por região
- Listagem de municípios por região
- Geração de relatório estruturado em JSON
- Tratamento de erros de leitura e formato

## Tecnologias
- Python 3.9+
- Módulos `csv` e `json` (biblioteca padrão)

## Como executar
```bash
python main.py
```

O relatório será gerado em `relatorio.json`.

## Estrutura do projeto
```
analisador-municipios-ibge/
├── dados/
│   └── municipios.csv
├── modelos/
│   └── municipio.py
├── main.py
└── README.md
```
