# 파이썬 경량화 이미지 사용
FROM python:3.10-slim

# 환경 변수 설정
# Python이 pyc 파일을 쓰지 않도록 방지
ENV PYTHONDONTWRITEBYTECODE=1
# Python이 출력을 버퍼링하지 않도록 하여 로그를 즉시 볼 수 있게 함
ENV PYTHONUNBUFFERED=1

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 라이브러리 업데이트 및 빌드 필수 패키지 설치 후 캐시 삭제 (최적화)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc \
    && rm -rf /var/lib/apt/lists/*

# 패키지 매니저 업그레이드
RUN pip install --no-cache-dir --upgrade pip

# requirements.txt만 먼저 복사하여 의존성 패키지 설치 (Docker 캐시 활용 최적화)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . .

# 컨테이너 외부로 노출할 포트 설정
EXPOSE 8000

# FastAPI(uvicorn) 서버 실행을 위한 명령어
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
