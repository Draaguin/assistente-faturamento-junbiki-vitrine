# Assistente de Faturamento Junbiki — vitrine

Este repositório é uma apresentação pública e sanitizada de um projeto de automação de processos operacionais desenvolvido em Python.

A versão completa contém integração ERP específica para um ambiente corporativo. Para preservar informações operacionais, este repositório público **não inclui** seletores de tela, nomes de transações, credenciais, contatos, códigos de materiais, dados de produção nem capturas de tela internas. A integração real permanece fora desta vitrine.

## O que o projeto demonstra

- Interface desktop para registrar turnos e atividades;
- Regras de domínio separadas da interface e da automação externa;
- Controle de intervalos circulares de três dígitos, ciclos e duplicidades;
- Persistência local, histórico de auditoria e relatórios;
- Adaptadores separados para simulação e sistemas externos;
- Testes automatizados para regras independentes do ERP.

## Estrutura pública

- `demo/circular_sequence.py`: exemplo executável, independente de SAP/ERP, para intervalos circulares de 000 a 999;
- `tests/test_circular_sequence.py`: testes das regras de normalização, virada de ciclo e sobreposição;
- `docs/architecture.md`: visão geral da arquitetura e das fronteiras de segurança.

## Executar a demonstração

Requer Python 3.10 ou superior. Não há dependências de terceiros.

```bash
python -m unittest discover -s tests -v
python demo/circular_sequence.py
```

Exemplos de faixas circulares válidas incluem `850–040` e `999–000`. Saltos entre faixas são aceitos; sobreposição no mesmo ciclo é rejeitada.

## Limites

Esta vitrine é uma demonstração técnica e não é o aplicativo de produção. Ela não se conecta a ERP, não envia comandos externos e não substitui o sistema VBA usado na operação. A integração real precisa de ambiente autorizado, configuração corporativa e validação no sistema de destino.

## Créditos

Idealização e validação operacional: Christian Farias.
