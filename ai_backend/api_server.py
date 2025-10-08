"""
Dopamind AI Backend - Flask API Server
Provides REST API endpoints for emotion simulation and analytics.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
from emotion_engine import DopamindAI, RewardType, EmotionType
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for Flutter app

# Initialize AI engine
ai_engine = DopamindAI()

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/api/process-reward', methods=['POST'])
def process_reward():
    """Process a reward and return emotion/dopamine predictions."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['user_id', 'reward_type', 'context']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Validate reward type
        valid_rewards = [rt.value for rt in RewardType]
        if data['reward_type'] not in valid_rewards:
            return jsonify({
                'error': f'Invalid reward type. Must be one of: {valid_rewards}'
            }), 400
        
        # Process the reward
        result = ai_engine.process_reward(
            user_id=data['user_id'],
            reward_type=data['reward_type'],
            context=data['context'],
            session_history=data.get('session_history', [])
        )
        
        logger.info(f"Processed reward for user {data['user_id']}: {data['reward_type']}")
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error processing reward: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.route('/api/analytics/<user_id>', methods=['GET'])
def get_user_analytics(user_id):
    """Get analytics for a specific user."""
    try:
        days = request.args.get('days', 7, type=int)
        
        analytics = ai_engine.get_analytics(user_id, days)
        
        logger.info(f"Retrieved analytics for user {user_id} ({days} days)")
        
        return jsonify(analytics)
        
    except Exception as e:
        logger.error(f"Error getting analytics for user {user_id}: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.route('/api/insights', methods=['GET'])
def get_insights():
    """Get general insights from all data."""
    try:
        insights = ai_engine.get_insights()
        
        return jsonify({
            'insights': insights,
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error getting insights: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.route('/api/emotion-prediction', methods=['POST'])
def predict_emotion():
    """Predict emotion response for a given context."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['user_id', 'reward_type', 'context']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400
        
        # Validate reward type
        valid_rewards = [rt.value for rt in RewardType]
        if data['reward_type'] not in valid_rewards:
            return jsonify({
                'error': f'Invalid reward type. Must be one of: {valid_rewards}'
            }), 400
        
        # Get prediction
        emotion_state, dopamine_response = ai_engine.learning_engine.get_personalized_prediction(
            data['user_id'],
            RewardType(data['reward_type']),
            data['context']
        )
        
        result = {
            'emotion': {
                'type': emotion_state.emotion.value,
                'intensity': emotion_state.intensity,
                'confidence': emotion_state.confidence,
                'timestamp': emotion_state.timestamp.isoformat()
            },
            'dopamine': {
                'baseline': dopamine_response.baseline,
                'peak': dopamine_response.peak,
                'duration': dopamine_response.duration,
                'decay_rate': dopamine_response.decay_rate,
                'emotional_impact': dopamine_response.emotional_impact
            },
            'user_id': data['user_id']
        }
        
        logger.info(f"Generated emotion prediction for user {data['user_id']}")
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Error predicting emotion: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.route('/api/session-summary', methods=['POST'])
def get_session_summary():
    """Get a summary of a completed session."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['user_id', 'session_data']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'error': f'Missing required field: {field}'
                }), 400
        
        session_data = data['session_data']
        
        # Calculate session metrics
        total_rewards = len(session_data.get('rewards', []))
        avg_intensity = sum(r.get('intensity', 0) for r in session_data.get('rewards', [])) / max(total_rewards, 1)
        session_duration = session_data.get('duration', 0)
        
        # Generate insights
        insights = []
        if avg_intensity > 0.7:
            insights.append("High engagement session - great dopamine response!")
        elif avg_intensity < 0.4:
            insights.append("Calm session - good for mindfulness practice")
        
        if total_rewards > 10:
            insights.append("Very active session - lots of interactions")
        elif total_rewards < 3:
            insights.append("Minimal session - consider longer engagement")
        
        if session_duration > 300:  # 5 minutes
            insights.append("Long session - good for building habits")
        
        # Calculate dopamine trend
        rewards = session_data.get('rewards', [])
        if len(rewards) > 1:
            first_half = rewards[:len(rewards)//2]
            second_half = rewards[len(rewards)//2:]
            
            first_avg = sum(r.get('intensity', 0) for r in first_half) / max(len(first_half), 1)
            second_avg = sum(r.get('intensity', 0) for r in second_half) / max(len(second_half), 1)
            
            if second_avg > first_avg * 1.1:
                insights.append("Dopamine levels increased during session - great momentum!")
            elif second_avg < first_avg * 0.9:
                insights.append("Dopamine levels decreased - consider taking breaks")
        
        summary = {
            'user_id': data['user_id'],
            'session_metrics': {
                'total_rewards': total_rewards,
                'average_intensity': avg_intensity,
                'session_duration': session_duration,
                'dopamine_trend': 'increasing' if len(rewards) > 1 and second_avg > first_avg else 'stable'
            },
            'insights': insights,
            'recommendations': _generate_recommendations(session_data),
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"Generated session summary for user {data['user_id']}")
        
        return jsonify(summary)
        
    except Exception as e:
        logger.error(f"Error generating session summary: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

def _generate_recommendations(session_data):
    """Generate personalized recommendations based on session data."""
    recommendations = []
    
    rewards = session_data.get('rewards', [])
    if not rewards:
        return ["Try interacting more to get better insights"]
    
    # Analyze reward types
    reward_types = [r.get('type', '') for r in rewards]
    type_counts = {}
    for rt in reward_types:
        type_counts[rt] = type_counts.get(rt, 0) + 1
    
    # Find most/least used reward types
    if type_counts:
        most_used = max(type_counts, key=type_counts.get)
        least_used = min(type_counts, key=type_counts.get)
        
        if type_counts[most_used] > len(rewards) * 0.6:
            recommendations.append(f"You used {most_used} rewards frequently - try exploring {least_used} for variety")
        
        if type_counts[least_used] == 0:
            recommendations.append(f"Consider trying {least_used} rewards for different emotional responses")
    
    # Time-based recommendations
    session_duration = session_data.get('duration', 0)
    if session_duration < 60:  # Less than 1 minute
        recommendations.append("Try longer sessions for better habit formation")
    elif session_duration > 1800:  # More than 30 minutes
        recommendations.append("Consider shorter, more focused sessions")
    
    # Intensity recommendations
    avg_intensity = sum(r.get('intensity', 0) for r in rewards) / len(rewards)
    if avg_intensity > 0.8:
        recommendations.append("High intensity session - great for building excitement!")
    elif avg_intensity < 0.3:
        recommendations.append("Low intensity session - good for calm, mindful practice")
    
    return recommendations

@app.route('/api/batch-process', methods=['POST'])
def batch_process_rewards():
    """Process multiple rewards in a batch."""
    try:
        data = request.get_json()
        
        if 'rewards' not in data:
            return jsonify({
                'error': 'Missing required field: rewards'
            }), 400
        
        results = []
        for reward_data in data['rewards']:
            try:
                result = ai_engine.process_reward(
                    user_id=reward_data['user_id'],
                    reward_type=reward_data['reward_type'],
                    context=reward_data['context'],
                    session_history=reward_data.get('session_history', [])
                )
                results.append(result)
            except Exception as e:
                logger.error(f"Error processing reward in batch: {str(e)}")
                results.append({
                    'error': str(e),
                    'reward_data': reward_data
                })
        
        return jsonify({
            'results': results,
            'total_processed': len(results),
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Error in batch processing: {str(e)}")
        return jsonify({
            'error': 'Internal server error',
            'message': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'The requested endpoint does not exist'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500

if __name__ == '__main__':
    logger.info("Starting Dopamind AI Backend Server...")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
