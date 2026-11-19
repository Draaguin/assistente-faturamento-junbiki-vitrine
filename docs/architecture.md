# Arquitetura da vitrine

## Camadas do aplicativo completo

A implementação integral segue uma separação que permite testar regras de negócio sem abrir a interface ou conectar a um sistema externo:

1. **Interface desktop** — captura dados do turno e apresenta andamento, resultados e pendências.
2. **Casos de uso** — coordenam cadastro, processamento, auditoria e encerramento.
3. **Domínio** — contém validações de sequência, ciclos, duplicidade e estados.
4. **Persistência e relatórios** — armazenam dados localmente e geram exportações.
5. **Adaptadores externos** — isolam a simulação e a integração corporativa.

## Fronteira pública

Esta vitrine contém uma demonstração simulada e regras de intervalo que não dependem de ambiente corporativo. Os seletores, configurações e fluxos específicos da integração real permanecem privados. Nenhum arquivo público envia comandos a um ERP.

## Ciclo de uma solicitação

1. A interface recebe uma faixa inicial e final.
2. O caso de uso valida o formato e o ciclo.
3. O domínio normaliza para três dígitos e verifica sobreposição.
4. A persistência registra a solicitação e a auditoria.
5. Um adaptador apropriado executa a ação ou a simula.
6. O caso de uso registra o resultado sem acoplar as regras de negócio a objetos externos.

## Princípios usados

- Identificadores e sequências são strings na fronteira da aplicação.
- Mensagens externas são interpretadas conforme a etapa do fluxo.
- Operações externas têm timeout e resultado explícito.
- Credenciais não pertencem ao código-fonte nem aos logs.
- Regras puras são cobertas por testes automatizados.

## Executar

A demonstração em `demo/circular_sequence.py` usa apenas a biblioteca padrão do Python. Execute os testes com:

```bash
python -m unittest discover -s tests -v
```
