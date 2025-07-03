from typing import List, Tuple
from fastapi import UploadFile
from io import BytesIO

async def create_pdf_copies(file: UploadFile) -> List[Tuple[str, BytesIO]]:
    content = await file.read()
    copies = []
    for i in range(1, 4):
        copy_io = BytesIO(content)
        copy_io.seek(0)
        copies.append((f"copy_{i}_{file.filename}", copy_io))
    return copies 