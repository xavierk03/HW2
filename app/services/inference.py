import random

def predict_face_shape_and_hairstyle(image_bytes: bytes) -> dict:
    """
    가상의 모델 추론 로직.
    실제 MLOps 파이프라인에서 PyTorch/TensorFlow 모델 코드로 대체될 영역입니다.
    """
    face_shapes = ["계란형", "둥근형", "각진형", "역삼각형"]
    hairstyles = {
        "계란형": ["가르마 펌", "댄디 컷", "리프 컷", "가일 펌"],
        "둥근형": ["포마드 투블럭", "애즈 펌", "스왓 컷", "드롭 컷"],
        "각진형": ["소프트 투블럭", "크롭 컷", "가일 컷", "슬릭 백"],
        "역삼각형": ["쉐도우 펌", "히피 펌", "시스루 뱅", "스핀스왈로 펌"]
    }

    # 이미지 바이트 길이를 이용해 임의로 얼굴형 결정 (테스트용)
    length = len(image_bytes)
    shape = face_shapes[length % len(face_shapes)]
    
    # 해당 얼굴형에 어울리는 헤어스타일 중 하나를 랜덤으로 추천
    style = random.choice(hairstyles[shape])

    return {
        "face_shape": shape,
        "recommended_hairstyle": style,
        "confidence": round(random.uniform(0.75, 0.99), 2)
    }
