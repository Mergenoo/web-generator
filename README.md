# E-commerce Store Generator

An AI-powered e-commerce store generator built with FastAPI, Gemini LLM, and Supabase. Generate complete, functional e-commerce stores based on brand guidelines and requirements.

## Features

- 🎨 **AI-Powered Generation**: Uses Google's Gemini LLM to create complete e-commerce stores
- 📱 **Responsive Design**: Generated stores work on desktop, tablet, and mobile
- 🖼️ **Iframe Preview**: Preview generated stores in an interactive iframe with device simulation
- 🎯 **Brand Guidelines Integration**: Incorporates brand personality and design guidelines
- ⚡ **FastAPI Backend**: Modern, fast Python web framework
- 🗄️ **Supabase Ready**: Database configuration included for future expansion

## Tech Stack

- **Backend**: FastAPI, Python 3.8+
- **AI**: Google Gemini LLM
- **Database**: Supabase (PostgreSQL)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Styling**: Custom CSS with modern design patterns

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Supabase account (optional, for future features)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd Web-generator
   ```

2. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   ```bash
   cp env.example .env
   ```

   Edit `.env` and add your API keys:

   ```env
   GEMINI_API_KEY=your_actual_gemini_api_key
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_ANON_KEY=your_supabase_anon_key
   SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
   ```

5. **Run the application**

   ```bash
   python main.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:8000`

## Usage

### Generating a Store

1. **Fill out the form** with your store requirements:

   - Brand Name
   - Product Category
   - Target Audience
   - Price Range
   - Additional Requirements (optional)

2. **Click "Generate Store"** and wait for the AI to create your store

3. **Preview your store** in the interactive iframe with:
   - Device simulation (Desktop/Tablet/Mobile)
   - Zoom controls
   - Full-screen view option

### Store Features

Generated stores include:

- ✅ Responsive header with navigation
- ✅ Hero section with compelling copy
- ✅ Product grid with sample products
- ✅ Product detail modals
- ✅ Shopping cart functionality
- ✅ Mobile-responsive design
- ✅ Interactive elements
- ✅ Brand-consistent styling

## API Endpoints

- `GET /` - Main generator interface
- `POST /generate-store` - Generate new store
- `GET /preview/{store_id}` - Preview generated store
- `GET /store/{store_id}` - Get store HTML
- `GET /stores` - List all generated stores
- `DELETE /stores/{store_id}` - Delete a store

## Brand Guidelines Integration

The system uses the `brand_guidelines.json` file to ensure generated stores match your brand personality:

- **Voice & Tone**: Encouraging, playful, authentic
- **Visual Identity**: Color palette, typography, photography style
- **Brand Application**: Product naming, partnership guidelines

## Supabase Integration

While not actively used in the current version, Supabase is configured for future features:

- Store persistence
- User authentication
- Analytics tracking
- Content management

## Development

### Project Structure

```
Web-generator/
├── main.py                 # FastAPI application
├── brand_guidelines.json   # Brand guidelines
├── requirements.txt        # Python dependencies
├── env.example            # Environment variables template
├── templates/             # HTML templates
│   ├── index.html         # Main generator page
│   └── preview.html       # Store preview page
└── static/                # Static assets
    ├── css/               # Stylesheets
    └── js/                # JavaScript files
```

### Adding New Features

1. **Extend the Gemini prompt** in `main.py` to include new store features
2. **Update templates** to support new UI elements
3. **Add API endpoints** for new functionality
4. **Integrate with Supabase** for data persistence

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the repository or contact the development team.

---

**Note**: This is a demo application. For production use, consider implementing proper security measures, error handling, and database persistence.
