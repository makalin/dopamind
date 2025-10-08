#!/usr/bin/env python3
"""
Dopamind AI Backend - Server Runner
Simple script to run the AI backend server.
"""

import os
import sys
import logging
from api_server import app

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """Main function to run the server."""
    logger.info("Starting Dopamind AI Backend Server...")
    logger.info("Server will be available at: http://localhost:5000")
    logger.info("API Documentation: http://localhost:5000/health")
    
    try:
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=False,  # Set to True for development
            threaded=True
        )
    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
