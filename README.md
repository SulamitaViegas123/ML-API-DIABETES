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

Aplicação usada: 

URL da API:
