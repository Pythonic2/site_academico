FROM python:alpine
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
ENV PORT=8000
ENV DEBUG=0

# Expõe a porta 8000
EXPOSE 8000

# Inicia o servidor do Django
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]
