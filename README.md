# API de Machine Learning

## 📌 Descrição
Este projeto treina um modelo de Machine Learning e disponibiliza uma API para previsões via HTTP

---

## 🚀Como rodar

```bash
pip install -r requirements.txt
python app.py
```

Acesse:
http://127.0.0.1:5000/

---

## 🔮 Endpoint de previsão

POST: http://127.0.0.1:5000/predict

Exemplo JSON:
```json
{
  "features": [6,148,72,35,0,33.6,0.627,50]
}
```

Resposta esperada:
```json
{
  "prediction": 1,
  "resultado": "Diabetes"
}
```

---

## ☁️Deploy na nuvem

Aplicação usada: OCI
Devido a limitações de recursos da instância gratuita (memória insuficiente para instalação do Docker), o deploy foi testado parcialmente.

A API pode ser executada localmente com:
pip install -r requirements.txt
python app.py

E via Docker com:
docker build -t ml-api .
docker run -p 5000:5000 ml-api

---

# 👥 Integrantes

| RM | Nome |
|---|---|
| RM560914 | Lucas Siqueira de Almeida |
| RM561090 | Matteus Viegas dos Santos |
| RM561089 | Sulamita Viegas dos Santos |

---
