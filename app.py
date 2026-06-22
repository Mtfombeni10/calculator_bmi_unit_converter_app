from flask import Flask
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Import blueprints
from application.routes.main import main_bp
from application.routes.calculate import calculate_bp

def create_app():
    app = Flask(__name__)
    
    # Get configuration from environment variables
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-12345')
    app.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'sqlite:///calculator.db')
    app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'development')
    
    # Register custom template filters
    @app.template_filter('format_timestamp')
    def format_timestamp_filter(timestamp):
        """Format timestamp to readable date/time"""
        if timestamp:
            try:
                dt = datetime.fromtimestamp(float(timestamp))
                return dt.strftime('%Y-%m-%d %H:%M:%S')
            except:
                return 'Invalid date'
        return 'N/A'
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(calculate_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    
    # Get port from environment variable (for deployment)
    port = int(os.getenv('PORT', 5000))
    
    print("=" * 50)
    print("🚀 Calculator App is starting...")
    print("📍 Environment:", app.config['FLASK_ENV'])
    print("📍 Database:", app.config['DATABASE_URL'])
    print("📍 Visit: http://localhost:" + str(port))
    print("=" * 50)
    
    app.run(
        debug=app.config['FLASK_ENV'] == 'development',
        host='0.0.0.0',
        port=port
    )
