
import pymupdf


def extract_text_from_pdf(file_content: bytes):
    """
    Extract text from a PDF file page by page.
    """

    extracted_pages = []

    # pymupdf open PDF from its binary content
    # PyMuPDF opens the PDF directly from memory. no need to store on disk
    with pymupdf.open(
        stream=file_content,
        filetype="pdf"
    ) as pdf_document:

        # Iterate through every page
        for page_number, page in enumerate(pdf_document, start=1):

            # Extract text from the current page
            page_text = page.get_text()

            extracted_pages.append({
                "page_number": page_number,
                "text": page_text
            })

    return extracted_pages
