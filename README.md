# Hospital-Data-Analysis-Python

## 📌 Descrição

Este projeto tem como objetivo organizar e analisar dados hospitalares sintéticos, transformando informações brutas em informações mais legíveis e úteis para o usuário.  
A proposta é automatizar a leitura de grandes volumes de dados, permitir buscas específicas e gerar estatísticas básicas sobre atendimentos hospitalares, servindo como um estudo prático de **análise de dados e automação com Python**.

---

## 📂 Estrutura do Projeto

- `data/raw/` → dados brutos, sem modificação  
- `data/processed/` → dados tratados (planejado)  
- `src/` → código-fonte do projeto  

---

## 🔹 Bloco 1 — Perguntas operacionais (início recomendado)

- Quantos atendimentos foram realizados no período?  
- Quantos atendimentos por tipo (`ENCOUNTERCLASS`)?  
- Quantos atendimentos por profissional (`PROVIDER`)?  
- Qual a duração média dos atendimentos (`STOP - START`)?  

👉 Ideais para o primeiro relatório.

---

## 🔹 Bloco 2 — Perguntas financeiras (nível intermediário)

- Qual o custo total dos atendimentos?  
- Diferença entre custo base e custo final?  
- Quanto foi coberto pelos convênios?  
- Quais foram os atendimentos mais caros?  

---

## 🔹 Bloco 3 — Perguntas clínicas (nível avançado)

> Perguntas mais sensíveis e planejadas para etapas futuras do projeto.

- Motivos mais comuns de atendimento  
- Relação entre tipo de atendimento e custo  

---

## ▶️ Como executar o projeto

```bash
python src/main.py
```

# 📎 Observações

- Os dados utilizados são sintéticos e têm finalidade exclusivamente educacional.

- O projeto está em desenvolvimento contínuo, com foco em boas práticas de organização e análise de dados.


---
