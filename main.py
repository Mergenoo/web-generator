from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import uuid
from typing import Optional

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-pro')

app = FastAPI(title="E-commerce Store Generator", version="1.0.0")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

# Store generated stores in memory (in production, use database)
generated_stores = {}

class StoreGenerationRequest(BaseModel):
    brand_name: str
    product_category: str
    target_audience: str
    price_range: str
    additional_requirements: Optional[str] = None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Main page with store generator form"""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-store")
async def generate_store(request: StoreGenerationRequest):
    """Generate e-commerce store using Gemini LLM"""
    try:
        # Load brand guidelines
        with open("brand_guidelines.json", "r") as f:
            brand_guidelines = json.load(f)
        
        # Create prompt for Gemini
        prompt = f"""
        Create a complete e-commerce store for {request.brand_name} based on these requirements:
        
        Brand Name: {request.brand_name}
        Product Category: {request.product_category}
        Target Audience: {request.target_audience}
        Price Range: {request.price_range}
        Additional Requirements: {request.additional_requirements or "None"}
        
        Use these brand guidelines as inspiration for the design and content:
        {json.dumps(brand_guidelines, indent=2)}
        
        Generate a complete HTML e-commerce store with:
        1. Modern, responsive design using CSS Grid/Flexbox
        2. Header with navigation and shopping cart
        3. Hero section with compelling copy
        4. Product grid with at least 6 sample products
        5. Product detail modal/popup
        6. Footer with contact information
        7. Mobile-responsive design
        8. Interactive elements (add to cart, product filtering)
        9. Color scheme and typography that matches the brand personality
        
        Return ONLY the complete HTML code with embedded CSS and JavaScript.
        Make it functional and ready to display in an iframe.
        """
        
        # Generate store with Gemini
        response = model.generate_content(prompt)
        store_html = response.text
        
        # Generate unique ID for the store
        store_id = str(uuid.uuid4())
        generated_stores[store_id] = {
            "html": store_html,
            "brand_name": request.brand_name,
            "product_category": request.product_category,
            "created_at": str(uuid.uuid4())  # Simple timestamp
        }
        
        return {
            "store_id": store_id,
            "message": "Store generated successfully!",
            "preview_url": f"/preview/{store_id}"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating store: {str(e)}")

@app.get("/preview/{store_id}", response_class=HTMLResponse)
async def preview_store(request: Request, store_id: str):
    """Preview page with iframe showing the generated store"""
    if store_id not in generated_stores:
        raise HTTPException(status_code=404, detail="Store not found")
    
    store_data = generated_stores[store_id]
    return templates.TemplateResponse("preview.html", {
        "request": request,
        "store_id": store_id,
        "brand_name": store_data["brand_name"],
        "product_category": store_data["product_category"]
    })

@app.get("/store/{store_id}")
async def get_store(store_id: str):
    """Get the generated store HTML"""
    if store_id not in generated_stores:
        raise HTTPException(status_code=404, detail="Store not found")
    
    store_html = generated_stores[store_id]["html"]
    return HTMLResponse(content=store_html, media_type="text/html")

@app.get("/stores")
async def list_stores():
    """List all generated stores"""
    stores = []
    for store_id, store_data in generated_stores.items():
        stores.append({
            "store_id": store_id,
            "brand_name": store_data["brand_name"],
            "product_category": store_data["product_category"],
            "created_at": store_data["created_at"],
            "preview_url": f"/preview/{store_id}"
        })
    return {"stores": stores}

@app.delete("/stores/{store_id}")
async def delete_store(store_id: str):
    """Delete a generated store"""
    if store_id not in generated_stores:
        raise HTTPException(status_code=404, detail="Store not found")
    
    del generated_stores[store_id]
    return {"message": "Store deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 