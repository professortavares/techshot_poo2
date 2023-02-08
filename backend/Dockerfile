# Para construir a imagem:
# docker build -t techshot_backend .

# Para executar o container:
# docker run -d -p 8000:8000 techshot_backend

# Para executar o container e com o volume mapeado:
# docker run -d -p 8000:8000 -v $(pwd)/volume:/app/volume techshot_backend

# Para executar o container com o modo interativo:
# docker run -it -p 8000:8000 techshot_backend bash

# Para executar o container com o modo interativo e com o volume mapeado:
# docker run -it -p 8000:8000 -v $(pwd)/volume:/app/volume techshot_backend bash

FROM python:3.9-slim

# Cópia dos arquivos do projeto
COPY ./techshot /app/techshot
COPY ./requirements.txt /app/requirements.txt
COPY ./main.py /app/main.py
COPY ./setup.py /app/setup.py
RUN mkdir /app/volume

# Instalação das dependências
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install -e .

# Execução do projeto
CMD uvicorn main:app --host 0.0.0.0 --port 8000