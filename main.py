from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.endpoints import router as api_router
import os

app = FastAPI(
    title="Face & Hairstyle Recommender API",
    description="MLOps 기반의 얼굴 인식 및 헤어스타일 추천 API 서버",
    version="1.0.0"
)

# CORS(Cross-Origin Resource Sharing) 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 서빙 세팅
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# API 라우터 등록
app.include_router(api_router, prefix="/api/v1", tags=["inference"])

@app.get("/")
def read_root(request: Request):
    """서버 메인 접속 시 프론트엔드 UI를 렌더링합니다."""
    return templates.TemplateResponse(request=request, name="index.html")
