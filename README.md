# Hospital-Data-Analysis-Python

## 📌 Descrição

Este projeto tem como objetivo organizar e analisar dados hospitalares sintéticos, transformando informações brutas em dados mais legíveis e úteis para o usuário.

A proposta é praticar **manipulação de arquivos, lógica de programação e regras de negócio em Python**, caminhando para automação de análises, geração de estatísticas e visualização de informações no terminal (e futuramente em interfaces).

> ⚠️ Projeto em fase inicial: a estrutura e o escopo estão definidos, e o código será implementado de forma incremental.

---

## 📂 Estrutura do Projeto (Planejada)

- `data/raw/` → dados brutos, sem modificação  
- `data/processed/` → dados tratados (planejado)  
- `src/` → código-fonte do projeto  

---

## 🔹 Bloco 1 — Perguntas operacionais (início recomendado)

- ✅ Quantos atendimentos foram realizados no período?  
- ✅Quantos atendimentos por tipo (`ENCOUNTERCLASS`)?  
- ✅Quantos atendimentos por profissional (`PROVIDER`)?  
- ✅Qual a duração média dos atendimentos (`STOP - START`)?  

👉 Ideais para o primeiro relatório e validação da lógica do sistema.

---

## 🔹 Bloco 2 — Perguntas financeiras (nível intermediário)

- ✅Qual o custo total dos atendimentos?  
- ✅Diferença entre custo base e custo final?  
- ✅Quanto foi coberto media pelos convênios?  
- Quais foram os atendimentos mais caros?  

#### O projeto calcula métricas financeiras básicas, como diferença entre custo base e custo final, valor coberto por convênios e custo efetivo ao paciente.

---

## 🔹 Bloco 3 — Perguntas clínicas (nível avançado)

> Perguntas planejadas para etapas futuras do projeto.

- Motivos mais comuns de atendimento  
- Relação entre tipo de atendimento e custo  

---

## ▶️ Execução (futura)

```bash
python src/main.py
```

---
# 📎 Observações

- Os dados utilizados são sintéticos e têm finalidade exclusivamente educacional.

- O projeto está em desenvolvimento contínuo, com foco em aprendizado prático, organização de código e evolução gradual das funcionalidades.

---


