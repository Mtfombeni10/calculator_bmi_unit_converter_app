from flask import Flask
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Import blueprints
from application.routes.main import main_bp
from application.routes.calculate import calculate_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key')
    
    # Register custom template filters
    @app.template_filter('format_timestamp')
    def format_timestamp_filter(timestamp):
        """Format timestamp to readable date/time"""
        if timestamp:
            dt = datetime.fromtimestamp(timestamp)
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        return 'N/A'
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(calculate_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    print("=" * 50)
    print("🚀 Calculator App is starting...")
    print("📍 Visit: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)