# 🏥 Sistema de Gerenciamento de Fila Hospitalar (Python)

Sistema de fila de espera hospitalar com priorização automática usando lista encadeada em Python. Gerencia pacientes com cartões **verdes (urgentes)** e **amarelos (não urgentes)** com numeração sequencial distinta.

## 📋 Funcionalidades

- **Sistema de numeração automática**:
  - Cartões verdes: `V1, V2, V3...` (inicia em 1)
  - Cartões amarelos: `A201, A202...` (inicia em 201)
  
- **Priorização inteligente**:
  - Pacientes verdes sempre à frente da fila
  - Pacientes amarelos inseridos após os últimos verdes

- **Operações**:
  - `Adicionar paciente` (com cor do cartão)
  - `Visualizar fila completa` (formato encadeado)
  - `Chamar próximo paciente` (FIFO com prioridade)
  - `Sair do sistema`

## ⚙️ Estrutura do Código

```python
.
├── ElementoDaListaSimples       # Classe do nó (paciente)
│   ├── numero                   # Número do cartão
│   ├── cor                      # V (verde) ou A (amarelo)
│   └── proximo                  # Referência ao próximo nó
│
└── ListaDeEspera                # Lista encadeada principal
    ├── inserirSemPrioridade()   # Para cartões verdes
    ├── inserirComPrioridade()   # Para cartões amarelos
    ├── atenderPaciente()        # Remove o próximo da fila
    └── imprimirListaDeEspera()  # Exibe a fila formatada

## 🚀 Menu Interativo

```python

---------------------- SISTEMA HOSPITAL ----------------------
1 - Adicionar paciente a fila
2 - Mostrar pacientes na fila
3 - Chamar paciente
4 - Fechar programa
Escolher: [1-4]

## 📌 Exemplo de Uso 

```python

>>> Adicionar paciente (opção 1)
Digite a cor do cartão (V para verde e A para amarelo): V
Paciente com cartão V1 adicionado a fila

>>> Mostrar fila (opção 2)
Lista -> (1 V) -> (203 A) -> (2 V) -> None

>>> Chamar paciente (opção 3)
Chamando paciente V1 para atendimento
