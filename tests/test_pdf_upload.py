import pytest
from fastapi.testclient import TestClient
from app.main import app
import io

client = TestClient(app)

def test_upload_pdf():
    pdf_content = b'%PDF-1.4 test pdf content'
    files = {'file': ('test.pdf', io.BytesIO(pdf_content), 'application/pdf')}
    response = client.post('/upload-pdf', files=files)
    assert response.status_code == 200
    data = response.json()
    assert 'filenames' in data
    assert 'files' in data
    assert len(data['filenames']) == 3
    assert len(data['files']) == 3 