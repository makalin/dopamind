# 🧠 Dopamind AI Backend API Documentation

## Overview

The Dopamind AI Backend provides REST API endpoints for emotion simulation, dopamine response prediction, and user analytics. The backend uses machine learning to simulate realistic emotional responses to social media-like interactions.

## Base URL

```
http://localhost:5000
```

## Authentication

Currently, the API does not require authentication. In production, implement proper authentication mechanisms.

## Endpoints

### Health Check

#### GET /health

Check if the API server is running.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.000Z",
  "version": "1.0.0"
}
```

### Process Reward

#### POST /api/process-reward

Process a reward interaction and return emotion/dopamine predictions.

**Request Body:**
```json
{
  "user_id": "user123",
  "reward_type": "like",
  "context": {
    "fatigue_level": 0.3,
    "stress_level": 0.2,
    "mood": "positive",
    "time_of_day": "morning"
  },
  "session_history": [
    {
      "type": "like",
      "timestamp": "2024-01-15T10:25:00.000Z",
      "intensity": 0.7
    }
  ]
}
```

**Response:**
```json
{
  "emotion": {
    "type": "happy",
    "intensity": 0.75,
    "confidence": 0.85,
    "timestamp": "2024-01-15T10:30:00.000Z"
  },
  "dopamine": {
    "baseline": 0.3,
    "peak": 0.8,
    "duration": 3.0,
    "decay_rate": 0.1,
    "emotional_impact": 0.65
  },
  "context": {
    "fatigue_level": 0.3,
    "stress_level": 0.2,
    "mood": "positive"
  },
  "user_id": "user123"
}
```

**Valid Reward Types:**
- `like`
- `comment`
- `share`
- `achievement`
- `connection`
- `discovery`
- `streak`
- `milestone`

### Get User Analytics

#### GET /api/analytics/{user_id}

Get analytics and insights for a specific user.

**Query Parameters:**
- `days` (optional): Number of days to analyze (default: 7)

**Example:**
```
GET /api/analytics/user123?days=14
```

**Response:**
```json
{
  "trends": {
    "emotion_distribution": {
      "happy": 45,
      "excited": 30,
      "calm": 25
    },
    "average_intensity": 0.65,
    "average_confidence": 0.78,
    "daily_patterns": {
      "2024-01-14": {
        "intensity": 0.7,
        "confidence": 0.8,
        "emotion": 12
      }
    },
    "total_entries": 150
  },
  "insights": [
    "You're experiencing high emotional intensity - great for engagement!",
    "Try exploring different types of interactions for more emotional variety"
  ],
  "user_id": "user123",
  "days": 14
}
```

### Get General Insights

#### GET /api/insights

Get general insights from all user data.

**Response:**
```json
{
  "insights": [
    "High engagement patterns detected across users",
    "Discovery rewards show highest emotional impact",
    "Morning sessions tend to have higher dopamine responses"
  ],
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### Predict Emotion

#### POST /api/emotion-prediction

Predict emotional response for a given context without processing the reward.

**Request Body:**
```json
{
  "user_id": "user123",
  "reward_type": "achievement",
  "context": {
    "fatigue_level": 0.1,
    "stress_level": 0.3,
    "mood": "excited"
  }
}
```

**Response:**
```json
{
  "emotion": {
    "type": "excited",
    "intensity": 0.85,
    "confidence": 0.9,
    "timestamp": "2024-01-15T10:30:00.000Z"
  },
  "dopamine": {
    "baseline": 0.35,
    "peak": 0.9,
    "duration": 5.0,
    "decay_rate": 0.12,
    "emotional_impact": 0.77
  },
  "user_id": "user123"
}
```

### Session Summary

#### POST /api/session-summary

Get a comprehensive summary of a completed session.

**Request Body:**
```json
{
  "user_id": "user123",
  "session_data": {
    "duration": 300,
    "rewards": [
      {
        "type": "like",
        "intensity": 0.7,
        "timestamp": "2024-01-15T10:25:00.000Z"
      },
      {
        "type": "comment",
        "intensity": 0.8,
        "timestamp": "2024-01-15T10:27:00.000Z"
      }
    ],
    "focus_mode": "achievement"
  }
}
```

**Response:**
```json
{
  "user_id": "user123",
  "session_metrics": {
    "total_rewards": 2,
    "average_intensity": 0.75,
    "session_duration": 300,
    "dopamine_trend": "increasing"
  },
  "insights": [
    "High engagement session - great dopamine response!",
    "Dopamine levels increased during session - great momentum!"
  ],
  "recommendations": [
    "Try longer sessions for better habit formation",
    "Consider trying share rewards for different emotional responses"
  ],
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### Batch Process Rewards

#### POST /api/batch-process

Process multiple rewards in a single request.

**Request Body:**
```json
{
  "rewards": [
    {
      "user_id": "user123",
      "reward_type": "like",
      "context": {
        "fatigue_level": 0.3,
        "mood": "positive"
      }
    },
    {
      "user_id": "user123",
      "reward_type": "comment",
      "context": {
        "fatigue_level": 0.2,
        "mood": "excited"
      }
    }
  ]
}
```

**Response:**
```json
{
  "results": [
    {
      "emotion": {
        "type": "happy",
        "intensity": 0.7,
        "confidence": 0.8,
        "timestamp": "2024-01-15T10:30:00.000Z"
      },
      "dopamine": {
        "baseline": 0.3,
        "peak": 0.7,
        "duration": 2.0,
        "decay_rate": 0.1,
        "emotional_impact": 0.56
      },
      "context": {
        "fatigue_level": 0.3,
        "mood": "positive"
      },
      "user_id": "user123"
    }
  ],
  "total_processed": 2,
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

## Data Models

### Emotion Types

```json
{
  "happy": "Positive, joyful emotion",
  "excited": "High energy, enthusiastic",
  "calm": "Peaceful, relaxed state",
  "focused": "Concentrated attention",
  "anxious": "Worried, nervous feeling",
  "frustrated": "Annoyed, irritated",
  "content": "Satisfied, pleased",
  "energetic": "High energy, active",
  "tired": "Low energy, fatigued",
  "sad": "Unhappy, melancholy"
}
```

### Context Parameters

```json
{
  "fatigue_level": "0.0-1.0, user's fatigue level",
  "stress_level": "0.0-1.0, user's stress level",
  "mood": "positive|neutral|negative, current mood",
  "time_of_day": "morning|afternoon|evening|night",
  "session_duration": "seconds, current session length",
  "previous_rewards": "array, recent reward history"
}
```

### Dopamine Response

```json
{
  "baseline": "0.0-1.0, baseline dopamine level",
  "peak": "0.0-1.0, peak dopamine level",
  "duration": "seconds, how long the response lasts",
  "decay_rate": "0.0-1.0, how quickly it fades",
  "emotional_impact": "0.0-1.0, emotional significance"
}
```

## Error Handling

### Error Response Format

```json
{
  "error": "Error type",
  "message": "Detailed error message",
  "timestamp": "2024-01-15T10:30:00.000Z"
}
```

### Common Error Codes

- `400 Bad Request`: Invalid request data
- `404 Not Found`: Endpoint not found
- `500 Internal Server Error`: Server error

### Example Error Responses

```json
{
  "error": "Missing required field: user_id",
  "message": "The user_id field is required for this endpoint"
}
```

```json
{
  "error": "Invalid reward type",
  "message": "Invalid reward type. Must be one of: like, comment, share, achievement, connection, discovery, streak, milestone"
}
```

## Rate Limiting

Currently, no rate limiting is implemented. In production, implement appropriate rate limiting based on your needs.

## CORS

CORS is enabled for all origins in development. Configure appropriately for production.

## Examples

### Flutter Integration

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

class DopamindAPI {
  static const String baseUrl = 'http://localhost:5000';
  
  static Future<Map<String, dynamic>> processReward({
    required String userId,
    required String rewardType,
    required Map<String, dynamic> context,
  }) async {
    final response = await http.post(
      Uri.parse('$baseUrl/api/process-reward'),
      headers: {'Content-Type': 'application/json'},
      body: json.encode({
        'user_id': userId,
        'reward_type': rewardType,
        'context': context,
      }),
    );
    
    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to process reward');
    }
  }
}
```

### Python Integration

```python
import requests
import json

class DopamindAPI:
    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url
    
    def process_reward(self, user_id, reward_type, context):
        response = requests.post(
            f'{self.base_url}/api/process-reward',
            json={
                'user_id': user_id,
                'reward_type': reward_type,
                'context': context
            }
        )
        return response.json()
```

## Testing

### Using curl

```bash
# Health check
curl http://localhost:5000/health

# Process reward
curl -X POST http://localhost:5000/api/process-reward \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "test_user",
    "reward_type": "like",
    "context": {
      "fatigue_level": 0.3,
      "mood": "positive"
    }
  }'
```

### Using Postman

1. Import the API collection
2. Set base URL to `http://localhost:5000`
3. Test endpoints with sample data

## Production Considerations

1. **Authentication**: Implement proper authentication
2. **Rate Limiting**: Add rate limiting for API endpoints
3. **Logging**: Implement comprehensive logging
4. **Monitoring**: Add health checks and monitoring
5. **Security**: Implement HTTPS and security headers
6. **Scaling**: Consider load balancing and horizontal scaling

---

**For more information, visit the [GitHub repository](https://github.com/makalin/dopamind) or contact support.**
