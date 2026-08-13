FROM python:3.12-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    ca-certificates \
    unixodbc \
    unixodbc-dev

RUN curl -sSL -O https://packages.microsoft.com/config/debian/12/packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && rm packages-microsoft-prod.deb

RUN apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
