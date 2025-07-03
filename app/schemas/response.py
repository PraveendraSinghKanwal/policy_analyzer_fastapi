from pydantic import BaseModel
from typing import List

class PDFCopiesResponse(BaseModel):
    filenames: List[str]
    files: List[bytes] 