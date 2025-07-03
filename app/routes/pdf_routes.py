from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
import zipfile
import openpyxl

router = APIRouter()

def create_dummy_excel1() -> BytesIO:
    excel_buffer = BytesIO()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(["ID", "Name", "Value"])
    ws.append([1, "Item 1A", 123])
    ws.append([2, "Item 1B", 456])
    wb.save(excel_buffer)
    excel_buffer.seek(0)
    return excel_buffer

def create_dummy_excel2() -> BytesIO:
    excel_buffer = BytesIO()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(["ID", "Name", "Value"])
    ws.append([1, "Item 2A", 234])
    ws.append([2, "Item 2B", 122])
    ws.append([3, "Item 2C", 655])
    wb.save(excel_buffer)
    excel_buffer.seek(0)
    return excel_buffer

def create_dummy_text() -> BytesIO:
    text_buffer = BytesIO()
    content = (
        "This is a dummy text file.\n"
        "Line 2: Example data.\n"
        "Line 3: More dummy content. the heart of the bustling city, \n"
    )
    text_buffer.write(content.encode("utf-8"))
    text_buffer.seek(0)
    return text_buffer

def add_file_to_zip(zip_file, filename: str, file_buffer: BytesIO):
    file_buffer.seek(0)
    zip_file.writestr(filename, file_buffer.read())

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    # Accept any file, but you can keep PDF validation if needed
    try:
        zip_buffer = BytesIO()
        with zipfile.ZipFile(zip_buffer, "w") as zip_file:
            excel1 = create_dummy_excel1()
            add_file_to_zip(zip_file, "Standard_Analyses.xlsx", excel1)
            excel2 = create_dummy_excel2()
            add_file_to_zip(zip_file, "Gap_Analyses.xlsx", excel2)
            text_file = create_dummy_text()
            add_file_to_zip(zip_file, "Summary.txt", text_file)
        zip_buffer.seek(0)
        return StreamingResponse(
            zip_buffer,
            media_type="application/x-zip-compressed",
            headers={"Content-Disposition": "attachment; filename=files.zip"}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 