# Usa una imagen oficial de Python
FROM python:3.11-slim

# Setea el directorio de trabajo
WORKDIR /app

# Copia los archivos al contenedor
COPY . /app/

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone el puerto usado por Django
EXPOSE 8000

# Comando de inicio
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
