FROM python:3.9
WORKDIR /code
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD streamlit run app.py --server.port $PORT --server.address 0.0.0.0
