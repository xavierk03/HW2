document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const loading = document.getElementById('loading');
    const resultCard = document.getElementById('result-card');
    const btnReset = document.getElementById('reset-btn');

    // Drag and drop setup
    dropZone.addEventListener('click', () => fileInput.click());

    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        
        if (e.dataTransfer.files.length) {
            handleFile(e.dataTransfer.files[0]);
        }
    });

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length) {
            handleFile(e.target.files[0]);
        }
    });

    // Reset UI to upload again
    btnReset.addEventListener('click', () => {
        resultCard.classList.add('hidden');
        dropZone.classList.remove('hidden');
        fileInput.value = '';
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('이미지 파일 형식만 업로드 가능합니다.');
            return;
        }

        // Show loading state
        dropZone.classList.add('hidden');
        loading.classList.remove('hidden');

        const formData = new FormData();
        formData.append('file', file);

        fetch('/api/v1/predict/hairstyle', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) throw new Error('서버 처리 중 오류가 발생했습니다.');
            return response.json();
        })
        .then(data => {
            // Hide loading, show result UI
            loading.classList.add('hidden');
            resultCard.classList.remove('hidden');
            
            // Populating UI with inference result
            document.getElementById('face-shape').textContent = data.prediction.face_shape;
            document.getElementById('hair-style').textContent = data.prediction.recommended_hairstyle;
            document.getElementById('confidence').textContent = Math.round(data.prediction.confidence * 100) + '%';
        })
        .catch(error => {
            alert(error.message);
            loading.classList.add('hidden');
            dropZone.classList.remove('hidden');
        });
    }
});
