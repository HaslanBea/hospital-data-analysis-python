# Nota e Organizaçao dos arquivos 


### Arquitetura atual

```
src/
├── main.py            # ponto de entrada
├── loader.py          # leitura do CSV
├── models.py          # estruturas (Paciente, Consulta)
├── services.py        # regras de negócio
├── repository.py      # acesso aos dados
└── utils.py           # funções auxiliares
```

## 📁Explicaçao com problemas do mundo real

### 1️⃣ main.py — O gerente do hospital

#### Ele nao faz trabalho pesado, ele escolhe quem vai fazer oque.

Seria tipo o gerente do hospital.

#### No codigo:

- chama as funçoes
- organiza o fluxo
- mostra resultados

### 2️⃣loader.py — A recepção

Ele so vai ler dados nao analisar, cadastrar sem decidir nada de fato.

🔹 def → palavra reservada para criar função <br>
🔹 path → caminho do arquivo (string)

### 3️⃣ models.py Prontuario do paciente

🔹 class → cria um modelo <br>
🔹 Encounter → nome em PascalCase (padrão Python)

### 4️⃣ services.py — Regras do hospital

Aqui mora a inteligência, recebe dados e retorna a resposta.

### 5️⃣ repository.py — Arquivo / banco de dados

Cuida da onde fica os arquivos 

### 6️⃣ utils.py — Ferramentas genéricas

Funçoes reproveitaveis
