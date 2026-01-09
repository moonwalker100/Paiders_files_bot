# Use slim Python 3.13 image
FROM python:3.13-slim-bookworm

# Set working directory
WORKDIR /app

# Install build tools and dependencies for TgCrypto
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    python3-dev \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for Docker cache efficiency)
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your bot code
COPY . .

# Set default command to run your bot
CMD ["python3", "main.py"]
