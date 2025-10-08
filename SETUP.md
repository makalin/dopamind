# 🧠 Dopamind - Setup Guide

## Overview

Dopamind is a Flutter application with a Python AI backend that simulates social media dopamine responses without the addictive content. This guide will help you set up the complete development environment.

## Prerequisites

### System Requirements
- **Flutter**: 3.0.0 or higher
- **Dart**: 3.0.0 or higher
- **Python**: 3.8 or higher
- **Node.js**: 16.0 or higher (for build tools)
- **Git**: Latest version

### Platform Support
- **iOS**: 12.0 or higher
- **Android**: API level 21 (Android 5.0) or higher
- **Web**: Modern browsers (Chrome, Firefox, Safari, Edge)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/makalin/dopamind.git
cd dopamind
```

### 2. Flutter Setup

#### Install Flutter
1. Download Flutter SDK from [flutter.dev](https://flutter.dev/docs/get-started/install)
2. Extract to your desired location (e.g., `~/development/flutter`)
3. Add Flutter to your PATH:

```bash
# Add to ~/.bashrc, ~/.zshrc, or equivalent
export PATH="$PATH:~/development/flutter/bin"
```

#### Verify Flutter Installation
```bash
flutter doctor
```

#### Install Dependencies
```bash
# Navigate to the Flutter project directory
cd /path/to/dopamind

# Get Flutter dependencies
flutter pub get

# Generate model files (if needed)
flutter packages pub run build_runner build
```

### 3. Python AI Backend Setup

#### Create Virtual Environment
```bash
cd ai_backend
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

#### Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### Verify Installation
```bash
python -c "import tensorflow as tf; print('TensorFlow version:', tf.__version__)"
python -c "import flask; print('Flask version:', flask.__version__)"
```

### 4. Database Setup

The app uses SQLite for local storage. No additional setup is required as the database is created automatically on first run.

### 5. Asset Setup

Create the following directories and add your assets:

```bash
mkdir -p assets/animations
mkdir -p assets/sounds
mkdir -p assets/images
mkdir -p assets/icons
mkdir -p assets/fonts
```

#### Required Sound Files
Add these sound files to `assets/sounds/`:
- `like.mp3`
- `comment.mp3`
- `share.mp3`
- `achievement.mp3`
- `connection.mp3`
- `discovery.mp3`
- `streak.mp3`
- `milestone.mp3`
- `dopamine_boost.mp3`
- `session_start.mp3`
- `session_end.mp3`

#### Required Font Files
Add Inter font files to `assets/fonts/`:
- `Inter-Regular.ttf`
- `Inter-Medium.ttf`
- `Inter-SemiBold.ttf`
- `Inter-Bold.ttf`

## Running the Application

### 1. Start the AI Backend

```bash
cd ai_backend
python run_server.py
```

The backend will be available at `http://localhost:5000`

### 2. Run the Flutter App

#### For Development
```bash
# Debug mode
flutter run

# Release mode
flutter run --release
```

#### For Specific Platforms
```bash
# iOS (requires Xcode on macOS)
flutter run -d ios

# Android
flutter run -d android

# Web
flutter run -d web

# Desktop
flutter run -d macos  # macOS
flutter run -d windows  # Windows
flutter run -d linux  # Linux
```

### 3. Build for Production

#### Android APK
```bash
flutter build apk --release
```

#### iOS App
```bash
flutter build ios --release
```

#### Web App
```bash
flutter build web --release
```

## Configuration

### 1. Flutter Configuration

#### Update API Endpoint
Edit `lib/services/api_service.dart` to point to your AI backend:

```dart
static const String baseUrl = 'http://localhost:5000';
```

#### Environment Variables
Create `.env` file in the project root:

```env
API_BASE_URL=http://localhost:5000
DEBUG_MODE=true
ENABLE_ANALYTICS=true
```

### 2. AI Backend Configuration

#### Environment Variables
Create `.env` file in `ai_backend/`:

```env
FLASK_ENV=development
FLASK_DEBUG=True
HOST=0.0.0.0
PORT=5000
```

#### Model Configuration
Edit `ai_backend/emotion_engine.py` to adjust AI parameters:

```python
# Dopamine baseline levels
self.baseline_dopamine = 0.3
self.peak_dopamine = 0.8

# Learning rate for adaptive learning
self.learning_rate = 0.1
```

## Development

### 1. Code Generation

Generate model files after making changes to data models:

```bash
flutter packages pub run build_runner build
```

### 2. Testing

#### Flutter Tests
```bash
# Run all tests
flutter test

# Run specific test file
flutter test test/widget_test.dart
```

#### Python Tests
```bash
cd ai_backend
python -m pytest tests/
```

### 3. Linting

#### Flutter Linting
```bash
flutter analyze
```

#### Python Linting
```bash
cd ai_backend
flake8 .
black .
```

## Troubleshooting

### Common Issues

#### 1. Flutter Doctor Issues
```bash
# Update Flutter
flutter upgrade

# Clean and get dependencies
flutter clean
flutter pub get
```

#### 2. Python Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### 3. Database Issues
```bash
# Delete app data and restart
flutter clean
flutter pub get
```

#### 4. Build Issues
```bash
# Clean build cache
flutter clean
flutter pub get
flutter build apk --release
```

### Platform-Specific Issues

#### iOS
- Ensure Xcode is installed and updated
- Run `pod install` in `ios/` directory
- Check iOS deployment target in `ios/Runner.xcworkspace`

#### Android
- Ensure Android SDK is installed
- Check `android/app/build.gradle` for correct SDK versions
- Verify `android/app/src/main/AndroidManifest.xml`

#### Web
- Ensure Chrome is installed for testing
- Check `web/index.html` for correct configuration

## Deployment

### 1. Flutter Web Deployment

#### Build for Web
```bash
flutter build web --release
```

#### Deploy to Firebase Hosting
```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login to Firebase
firebase login

# Initialize Firebase
firebase init hosting

# Deploy
firebase deploy
```

### 2. Mobile App Deployment

#### Android Play Store
1. Build release APK/AAB
2. Upload to Google Play Console
3. Follow Play Store guidelines

#### iOS App Store
1. Build iOS app in Xcode
2. Archive and upload to App Store Connect
3. Follow App Store guidelines

### 3. AI Backend Deployment

#### Using Docker
```bash
# Build Docker image
docker build -t dopamind-ai .

# Run container
docker run -p 5000:5000 dopamind-ai
```

#### Using Cloud Services
- **Heroku**: Deploy using Heroku CLI
- **AWS**: Use Elastic Beanstalk or ECS
- **Google Cloud**: Use App Engine or Cloud Run
- **Azure**: Use App Service or Container Instances

## Contributing

### 1. Development Workflow
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

### 2. Code Style
- Follow Flutter/Dart style guide
- Follow Python PEP 8
- Use meaningful commit messages
- Add tests for new features

### 3. Documentation
- Update README.md for new features
- Add inline code comments
- Update API documentation

## Support

### Getting Help
- Check the [Issues](https://github.com/makalin/dopamind/issues) page
- Join our [Discord](https://discord.gg/dopamind) community
- Email: support@dopamind.app

### Reporting Bugs
1. Check existing issues first
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy coding! 🧠✨**
