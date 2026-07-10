FROM selenium/standalone-chromium:4.45.0-20260606

USER root

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install uv --break-system-packages

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

ENV UV_PROJECT_ENVIRONMENT=/app/.venv
ENV UV_CACHE_DIR=/tmp/uv-cache
ENV UV_LINK_MODE=copy
ENV HOME=/tmp
ENV XDG_CACHE_HOME=/tmp/.cache
ENV XDG_CONFIG_HOME=/tmp/.config
ENV VIRTUAL_ENV=

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen

RUN mkdir -p /tmp/.cache /tmp/.config \
    && chmod -R 777 /app/.venv /tmp/uv-cache /tmp/.cache /tmp/.config

COPY . .

CMD ["uv", "run", "pytest"]
