#!/usr/bin/env python3
"""
E-commerce Store Generator Startup Script
"""

import os
import sys
from dotenv import load_dotenv

def check_environment():
    """Check if required environment variables are set"""
    load_dotenv()
    
    required_vars = ['GEMINI_API_KEY']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please create a .env file with your API keys:")
        print("   cp env.example .env")
        print("   # Then edit .env and add your actual API keys")
        return False
    
    print("✅ Environment variables loaded successfully")
    return True

def main():
    """Main startup function"""
    print("🚀 Starting E-commerce Store Generator...")
    print("=" * 50)
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Check if brand guidelines exist
    if not os.path.exists('brand_guidelines.json'):
        print("❌ brand_guidelines.json not found")
        print("   Please ensure the brand guidelines file exists")
        sys.exit(1)
    
    print("✅ Brand guidelines found")
    print("=" * 50)
    
    # Import and run the FastAPI app
    try:
        from main import app
        import uvicorn
        
        print("🌐 Starting server at http://localhost:8000")
        print("📖 API documentation at http://localhost:8000/docs")
        print("=" * 50)
        
        uvicorn.run(
            "main:app", 
            host="0.0.0.0", 
            port=8000,
            reload=True
        )
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Please ensure all dependencies are installed:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Startup error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 