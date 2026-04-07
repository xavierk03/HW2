from fastapi import APIRouter, File, UploadFile, HTTPException
from app.services.inference import predict_face_shape_and_hairstyle

router = APIRouter()

@router.post("/predict/hairstyle")
async def get_hairstyle_recommendation(file: UploadFile = File(...)):
    """
    클라이언트에서 업로드한 이미지 파일을 받아 헤어스타일을 추천해주는 엔드포인트입니다.
    """
    # 단순 파일 확장자 및 타입 체크
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="유효하지 않은 파일입니다. 이미지 파일을 업로드해주세요.")

    try:
        # 업로드된 이미지 바이너리 읽기
        content = await file.read()
        
        # 모델 추론 서비스 호출
        result = predict_face_shape_and_hairstyle(content)
        
        return {
            "filename": file.filename,
            "prediction": result,
            "status": "success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"추론 과정에서 오류가 발생했습니다: {str(e)}")
