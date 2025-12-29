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



🧩 O exercício que você deve fazer agora (sem código)

Pegue UMA pergunta do Bloco 1 do seu README e escreva apenas isso, em texto:

1️⃣ Qual é a pergunta?  Quantos atendimentos foram realizados no período?
2️⃣ O que entra? encouters.csv
3️⃣ O que sai? o valor em numero da quantidade 
4️⃣ Quais são os passos (em português)? 
 - Abrir o arquivo
 - Ler linha por linha 
 - enquanto le, guarda o valor em uma const
 - quando  tiver todas as linhas, subtrai uma que seria o cabeçalho
 - mostra o valor na tela

5️⃣ Isso pertence a qual arquivo? (loader, service, main?)
loader

💬 Quando voltar pra mim

Me mande apenas o texto, tipo:

Problema:
Entrada:
Saída:
Passos:
Arquivo responsável:
