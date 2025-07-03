# Policy Extraction FastAPI

A production-ready FastAPI application to upload a PDF and receive three exact copies in response.

## Features
- Upload a PDF and get three copies in response
- Modular structure (API, logic, utils, config, schemas, error handling)
- Logging with auto-deletion after 10 days
- Dockerized (Dockerfile & docker-compose)
- CORS enabled
- Pydantic validation
- Exception handling
- Unit test scaffolding

## Setup

1. **Clone the repo**
2. **Install dependencies**
   ```
   python -m venv venv
   pip install -r requirements.txt
   pip install pydantic-settings
   ```
3. **Set environment variables**
   - Copy `.env.example` to `.env` and edit as needed

4. **Run the app**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   hit api at-
   http://127.0.0.1:8000/docs
   ```

## Docker

Build and run with Docker Compose:
```bash
docker-compose up --build
```

## API Documentation

### POST `/upload-pdf`

Upload a PDF file and receive 3 pdf file in a ZIP archive.

#### Request
- **Method**: POST
- **Content-Type**: `multipart/form-data`
- **Endpoint**: `/upload-pdf`

#### Request Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | UploadFile | Yes | PDF file to be processed |

#### Request Example
```javascript
// JavaScript/Fetch API Example
const formData = new FormData();
formData.append('file', pdfFile); // pdfFile should be a File object

const response = await fetch('/upload-pdf', {
  method: 'POST',
  body: formData
});

if (response.ok) {
  const blob = await response.blob();
  // Handle the ZIP file download
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'pdf_copies.zip';
  a.click();
}
```

#### Response
- **Content-Type**: `application/x-zip-compressed`
- **Response Type**: StreamingResponse (ZIP file)
- **Headers**: 
  - `Content-Disposition`: `attachment; filename=pdf_copies.zip`

#### Response Content
The response is a ZIP file containing multiple copies of the uploaded PDF with different filenames.

#### Error Responses
| Status Code | Description |
|-------------|-------------|
| 400 | Only PDF files are allowed |
| 500 | Internal server error during processing |

#### Error Response Format
```json
{
  "detail": "Error message description"
}
```

## Testing

```bash
pytest
``` 