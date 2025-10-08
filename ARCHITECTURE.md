# 🧠 Dopamind - Architecture Documentation

## Overview

Dopamind is a cross-platform application that simulates social media dopamine responses without the addictive content. The architecture consists of a Flutter frontend, Python AI backend, and SQLite database.

## System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Flutter App   │◄──►│  Python AI API  │◄──►│  SQLite DB      │
│   (Frontend)    │    │   (Backend)     │    │  (Local Storage)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Audio/Haptic   │    │  ML Models      │    │  Analytics      │
│  Feedback       │    │  (TensorFlow)   │    │  Engine         │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Frontend Architecture (Flutter)

### Core Components

#### 1. State Management
- **Provider Pattern**: Used for state management across the app
- **DopamineProvider**: Manages dopamine levels and reward processing
- **SessionProvider**: Handles session state and history
- **MoodProvider**: Manages mood tracking and analytics

#### 2. Data Layer
```
lib/
├── models/           # Data models
│   ├── user.dart
│   ├── session.dart
│   ├── mood.dart
│   └── dopamine_score.dart
├── services/         # Business logic
│   ├── database_service.dart
│   ├── dopamine_engine.dart
│   └── feedback_service.dart
└── providers/        # State management
    ├── dopamine_provider.dart
    ├── session_provider.dart
    └── mood_provider.dart
```

#### 3. UI Layer
```
lib/
├── screens/          # Main screens
│   ├── home_screen.dart
│   ├── splash_screen.dart
│   └── settings_screen.dart
├── widgets/          # Reusable components
│   ├── dopamine_pulse.dart
│   ├── focus_mode_selector.dart
│   ├── session_controls.dart
│   ├── dopamine_feed.dart
│   ├── mood_tracker.dart
│   ├── analytics_dashboard.dart
│   └── reflection_session.dart
└── utils/           # Utilities
    └── theme.dart
```

### Key Features

#### 1. Dopamine Simulation
- **Real-time dopamine level tracking**
- **Visual pulse animations**
- **Adaptive intensity based on user behavior**
- **Decay simulation over time**

#### 2. Focus Modes
- **Achievement Mode**: Goal-oriented interactions
- **Connection Mode**: Social interaction simulation
- **Discovery Mode**: Learning and exploration

#### 3. Mood Tracking
- **Real-time mood logging**
- **Intensity measurement (1-10 scale)**
- **Context tracking (triggers, environment)**
- **Historical mood analysis**

#### 4. Analytics Dashboard
- **Session statistics**
- **Dopamine trend visualization**
- **Mood distribution charts**
- **Personalized insights**

## Backend Architecture (Python)

### Core Components

#### 1. Emotion Simulation Engine
```python
class EmotionSimulator:
    - simulate_emotion_response()
    - calculate_emotion_intensity()
    - get_reward_emotion()
```

#### 2. Dopamine Response Engine
```python
class DopamineSimulator:
    - simulate_dopamine_response()
    - calculate_baseline_dopamine()
    - calculate_peak_dopamine()
```

#### 3. Adaptive Learning System
```python
class AdaptiveLearningEngine:
    - update_patterns()
    - get_personalized_prediction()
    - calculate_context_adjustment()
```

#### 4. Analytics Engine
```python
class EmotionAIAnalytics:
    - get_emotion_trends()
    - get_insights()
    - add_emotion_data()
```

### API Endpoints

#### Core Endpoints
- `POST /api/process-reward`: Process reward interactions
- `GET /api/analytics/{user_id}`: Get user analytics
- `POST /api/emotion-prediction`: Predict emotional responses
- `POST /api/session-summary`: Generate session summaries

#### Utility Endpoints
- `GET /health`: Health check
- `GET /api/insights`: General insights
- `POST /api/batch-process`: Batch processing

### Machine Learning Models

#### 1. Emotion Classification
- **Input**: Reward type, user context, session history
- **Output**: Emotion type, intensity, confidence
- **Algorithm**: Custom neural network with attention mechanism

#### 2. Dopamine Response Prediction
- **Input**: Emotion state, reward type, user context
- **Output**: Dopamine baseline, peak, duration, decay rate
- **Algorithm**: Regression model with temporal features

#### 3. Adaptive Learning
- **Input**: User interaction history
- **Output**: Personalized prediction models
- **Algorithm**: Online learning with user-specific weights

## Database Schema

### Tables

#### 1. Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    avatar TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    preferences TEXT NOT NULL,
    total_sessions INTEGER NOT NULL DEFAULT 0,
    average_dopamine_score REAL NOT NULL DEFAULT 0.0,
    streak_days INTEGER NOT NULL DEFAULT 0
);
```

#### 2. Sessions Table
```sql
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    focus_mode TEXT NOT NULL,
    status TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT,
    duration INTEGER NOT NULL DEFAULT 0,
    dopamine_score REAL NOT NULL DEFAULT 0.0,
    interactions INTEGER NOT NULL DEFAULT 0,
    likes INTEGER NOT NULL DEFAULT 0,
    comments INTEGER NOT NULL DEFAULT 0,
    shares INTEGER NOT NULL DEFAULT 0,
    metadata TEXT NOT NULL,
    reflection TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

#### 3. Moods Table
```sql
CREATE TABLE moods (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    mood TEXT NOT NULL,
    intensity INTEGER NOT NULL,
    timestamp TEXT NOT NULL,
    note TEXT,
    context TEXT NOT NULL,
    dopamine_level REAL,
    trigger TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

#### 4. Dopamine Scores Table
```sql
CREATE TABLE dopamine_scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    reward_type TEXT NOT NULL,
    intensity REAL NOT NULL,
    timestamp TEXT NOT NULL,
    metadata TEXT NOT NULL,
    description TEXT,
    is_positive INTEGER NOT NULL,
    duration REAL NOT NULL,
    FOREIGN KEY (session_id) REFERENCES sessions (id)
);
```

## Data Flow

### 1. User Interaction Flow
```
User Action → Flutter App → Provider → Database → AI Backend → Response → UI Update
```

### 2. Reward Processing Flow
```
Reward Trigger → Dopamine Engine → AI Backend → Emotion Prediction → Feedback Service → UI Animation
```

### 3. Analytics Flow
```
Session Data → Analytics Engine → Trend Calculation → Insight Generation → Dashboard Update
```

## Security Considerations

### 1. Data Privacy
- **Local Storage**: All user data stored locally in SQLite
- **No Cloud Sync**: No data transmitted to external servers
- **Encryption**: Sensitive data encrypted at rest

### 2. API Security
- **Input Validation**: All API inputs validated and sanitized
- **Rate Limiting**: Implemented to prevent abuse
- **CORS**: Configured for secure cross-origin requests

### 3. User Privacy
- **Anonymous Usage**: No personal information required
- **Opt-in Analytics**: User controls data sharing
- **Data Retention**: Configurable data retention policies

## Performance Optimization

### 1. Frontend Optimization
- **Lazy Loading**: Widgets loaded on demand
- **State Management**: Efficient state updates
- **Animation Performance**: Hardware-accelerated animations
- **Memory Management**: Proper disposal of resources

### 2. Backend Optimization
- **Caching**: Frequently accessed data cached
- **Batch Processing**: Multiple requests processed together
- **Model Optimization**: Lightweight ML models
- **Database Indexing**: Optimized database queries

### 3. Database Optimization
- **Indexes**: Strategic indexes on frequently queried columns
- **Query Optimization**: Efficient SQL queries
- **Data Archiving**: Old data archived to maintain performance

## Scalability Considerations

### 1. Horizontal Scaling
- **Load Balancing**: Multiple backend instances
- **Database Sharding**: User data partitioned
- **CDN**: Static assets served from CDN

### 2. Vertical Scaling
- **Resource Monitoring**: CPU, memory, disk usage
- **Auto-scaling**: Automatic resource adjustment
- **Performance Metrics**: Real-time performance monitoring

## Deployment Architecture

### 1. Development Environment
```
Local Machine:
├── Flutter App (Debug)
├── Python Backend (Flask)
├── SQLite Database
└── Development Tools
```

### 2. Production Environment
```
Cloud Infrastructure:
├── Flutter Web App (CDN)
├── Python Backend (Container)
├── Database (Managed Service)
├── Load Balancer
└── Monitoring & Logging
```

### 3. Mobile Deployment
```
App Stores:
├── iOS App Store
├── Google Play Store
├── Code Signing
└── Release Management
```

## Monitoring & Analytics

### 1. Application Metrics
- **User Engagement**: Session duration, interaction frequency
- **Performance**: App startup time, response times
- **Errors**: Crash reports, exception tracking
- **Usage Patterns**: Feature usage, user behavior

### 2. AI Model Metrics
- **Prediction Accuracy**: Model performance tracking
- **Learning Progress**: Adaptive learning effectiveness
- **User Satisfaction**: Feedback and rating analysis
- **Model Drift**: Performance degradation detection

### 3. System Health
- **API Health**: Endpoint availability and response times
- **Database Performance**: Query performance, connection pools
- **Resource Usage**: CPU, memory, disk utilization
- **Error Rates**: System error frequency and types

## Future Enhancements

### 1. Advanced AI Features
- **Multi-modal Input**: Voice, gesture, biometric data
- **Predictive Analytics**: Proactive mood and behavior prediction
- **Personalized Models**: User-specific AI model training
- **Real-time Adaptation**: Dynamic model updates

### 2. Platform Expansion
- **Desktop Apps**: Native desktop applications
- **Smartwatch Integration**: Wearable device support
- **VR/AR Support**: Immersive experience modes
- **IoT Integration**: Smart home device connectivity

### 3. Social Features
- **Anonymous Sharing**: Privacy-preserving data sharing
- **Community Insights**: Aggregated, anonymized insights
- **Peer Support**: Community-driven support features
- **Expert Integration**: Professional mental health integration

---

**This architecture provides a solid foundation for Dopamind's current functionality while allowing for future growth and enhancement.**
