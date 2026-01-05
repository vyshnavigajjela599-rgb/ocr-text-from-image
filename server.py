from mcp.server.fastmcp import FastMCP
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

mcp = FastMCP("OCR MCP Server")

@mcp.tool()
def extract_text(image_path: str) -> str:
    """
    Extract text from an image using Tesseract OCR.
    """
    img = Image.open(image_path)
    return pytesseract.image_to_string(img)

if __name__ == "__main__":
    mcp.run()
