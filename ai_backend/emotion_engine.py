"""
Dopamind AI Backend - Emotion Simulation Engine
Simulates emotional responses and dopamine patterns for the Dopamind app.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from datetime import datetime, timedelta
import json
import random
from dataclasses import dataclass
from enum import Enum

class EmotionType(Enum):
    HAPPY = "happy"
    EXCITED = "excited"
    CALM = "calm"
    FOCUSED = "focused"
    ANXIOUS = "anxious"
    FRUSTRATED = "frustrated"
    CONTENT = "content"
    ENERGETIC = "energetic"
    TIRED = "tired"
    SAD = "sad"

class RewardType(Enum):
    LIKE = "like"
    COMMENT = "comment"
    SHARE = "share"
    ACHIEVEMENT = "achievement"
    CONNECTION = "connection"
    DISCOVERY = "discovery"
    STREAK = "streak"
    MILESTONE = "milestone"

@dataclass
class EmotionState:
    emotion: EmotionType
    intensity: float  # 0.0 to 1.0
    confidence: float  # 0.0 to 1.0
    timestamp: datetime
    context: Dict[str, any]

@dataclass
class DopamineResponse:
    baseline: float
    peak: float
    duration: float  # in seconds
    decay_rate: float
    emotional_impact: float

class EmotionSimulator:
    """Simulates emotional responses based on user interactions and context."""
    
    def __init__(self):
        self.emotion_weights = self._initialize_emotion_weights()
        self.dopamine_baseline = 0.3
        self.learning_rate = 0.1
        
    def _initialize_emotion_weights(self) -> Dict[EmotionType, float]:
        """Initialize base emotion weights."""
        return {
            EmotionType.HAPPY: 0.7,
            EmotionType.EXCITED: 0.6,
            EmotionType.CALM: 0.5,
            EmotionType.FOCUSED: 0.8,
            EmotionType.ANXIOUS: 0.3,
            EmotionType.FRUSTRATED: 0.2,
            EmotionType.CONTENT: 0.6,
            EmotionType.ENERGETIC: 0.7,
            EmotionType.TIRED: 0.4,
            EmotionType.SAD: 0.2,
        }
    
    def simulate_emotion_response(
        self, 
        reward_type: RewardType,
        user_context: Dict[str, any],
        session_history: List[Dict[str, any]] = None
    ) -> EmotionState:
        """Simulate emotional response to a reward."""
        
        # Get base emotion for reward type
        base_emotion = self._get_reward_emotion(reward_type)
        
        # Calculate intensity based on context
        intensity = self._calculate_emotion_intensity(
            reward_type, user_context, session_history
        )
        
        # Add some randomness for realism
        intensity += random.uniform(-0.1, 0.1)
        intensity = np.clip(intensity, 0.0, 1.0)
        
        # Calculate confidence based on consistency
        confidence = self._calculate_confidence(session_history)
        
        return EmotionState(
            emotion=base_emotion,
            intensity=intensity,
            confidence=confidence,
            timestamp=datetime.now(),
            context=user_context
        )
    
    def _get_reward_emotion(self, reward_type: RewardType) -> EmotionType:
        """Map reward types to primary emotions."""
        emotion_map = {
            RewardType.LIKE: EmotionType.HAPPY,
            RewardType.COMMENT: EmotionType.EXCITED,
            RewardType.SHARE: EmotionType.ENERGETIC,
            RewardType.ACHIEVEMENT: EmotionType.EXCITED,
            RewardType.CONNECTION: EmotionType.HAPPY,
            RewardType.DISCOVERY: EmotionType.FOCUSED,
            RewardType.STREAK: EmotionType.ENERGETIC,
            RewardType.MILESTONE: EmotionType.EXCITED,
        }
        return emotion_map.get(reward_type, EmotionType.HAPPY)
    
    def _calculate_emotion_intensity(
        self, 
        reward_type: RewardType,
        user_context: Dict[str, any],
        session_history: List[Dict[str, any]] = None
    ) -> float:
        """Calculate emotion intensity based on various factors."""
        
        base_intensity = 0.5
        
        # Reward type modifier
        reward_modifiers = {
            RewardType.LIKE: 0.3,
            RewardType.COMMENT: 0.5,
            RewardType.SHARE: 0.7,
            RewardType.ACHIEVEMENT: 0.8,
            RewardType.CONNECTION: 0.6,
            RewardType.DISCOVERY: 0.6,
            RewardType.STREAK: 0.7,
            RewardType.MILESTONE: 0.9,
        }
        
        intensity = base_intensity + reward_modifiers.get(reward_type, 0.5)
        
        # User context modifiers
        if user_context.get('fatigue_level', 0) > 0.7:
            intensity *= 0.8  # Reduce intensity when tired
        
        if user_context.get('stress_level', 0) > 0.6:
            intensity *= 0.9  # Slightly reduce when stressed
        
        if user_context.get('mood', 'neutral') == 'positive':
            intensity *= 1.1  # Boost when in good mood
        
        # Session history modifiers
        if session_history:
            recent_rewards = [r for r in session_history[-5:] if r.get('type') == reward_type.value]
            if len(recent_rewards) > 2:
                intensity *= 0.9  # Diminishing returns for repeated rewards
        
        return np.clip(intensity, 0.0, 1.0)
    
    def _calculate_confidence(self, session_history: List[Dict[str, any]] = None) -> float:
        """Calculate confidence in emotion prediction."""
        if not session_history:
            return 0.5
        
        # More data = higher confidence
        data_points = len(session_history)
        confidence = min(0.9, 0.3 + (data_points * 0.1))
        
        return confidence

class DopamineSimulator:
    """Simulates dopamine release patterns and responses."""
    
    def __init__(self):
        self.baseline_dopamine = 0.3
        self.peak_dopamine = 0.8
        self.decay_rate = 0.1
        
    def simulate_dopamine_response(
        self,
        reward_type: RewardType,
        emotion_state: EmotionState,
        user_context: Dict[str, any]
    ) -> DopamineResponse:
        """Simulate dopamine response to a reward."""
        
        # Calculate baseline dopamine
        baseline = self._calculate_baseline_dopamine(user_context)
        
        # Calculate peak dopamine based on reward and emotion
        peak = self._calculate_peak_dopamine(reward_type, emotion_state)
        
        # Calculate duration based on reward type
        duration = self._calculate_duration(reward_type)
        
        # Calculate decay rate
        decay_rate = self._calculate_decay_rate(emotion_state.intensity)
        
        # Calculate emotional impact
        emotional_impact = emotion_state.intensity * emotion_state.confidence
        
        return DopamineResponse(
            baseline=baseline,
            peak=peak,
            duration=duration,
            decay_rate=decay_rate,
            emotional_impact=emotional_impact
        )
    
    def _calculate_baseline_dopamine(self, user_context: Dict[str, any]) -> float:
        """Calculate baseline dopamine level."""
        baseline = self.baseline_dopamine
        
        # Adjust based on user state
        if user_context.get('fatigue_level', 0) > 0.7:
            baseline *= 0.8
        
        if user_context.get('stress_level', 0) > 0.6:
            baseline *= 0.9
        
        if user_context.get('mood', 'neutral') == 'positive':
            baseline *= 1.1
        
        return np.clip(baseline, 0.1, 0.5)
    
    def _calculate_peak_dopamine(
        self, 
        reward_type: RewardType, 
        emotion_state: EmotionState
    ) -> float:
        """Calculate peak dopamine level."""
        
        reward_peaks = {
            RewardType.LIKE: 0.6,
            RewardType.COMMENT: 0.7,
            RewardType.SHARE: 0.8,
            RewardType.ACHIEVEMENT: 0.9,
            RewardType.CONNECTION: 0.7,
            RewardType.DISCOVERY: 0.8,
            RewardType.STREAK: 0.8,
            RewardType.MILESTONE: 0.95,
        }
        
        base_peak = reward_peaks.get(reward_type, 0.6)
        
        # Adjust based on emotion intensity
        peak = base_peak * (0.5 + emotion_state.intensity * 0.5)
        
        return np.clip(peak, 0.3, 1.0)
    
    def _calculate_duration(self, reward_type: RewardType) -> float:
        """Calculate dopamine response duration."""
        durations = {
            RewardType.LIKE: 2.0,
            RewardType.COMMENT: 3.0,
            RewardType.SHARE: 4.0,
            RewardType.ACHIEVEMENT: 5.0,
            RewardType.CONNECTION: 3.5,
            RewardType.DISCOVERY: 4.5,
            RewardType.STREAK: 5.0,
            RewardType.MILESTONE: 6.0,
        }
        
        return durations.get(reward_type, 3.0)
    
    def _calculate_decay_rate(self, emotion_intensity: float) -> float:
        """Calculate dopamine decay rate."""
        # Higher intensity emotions decay faster
        return 0.05 + (emotion_intensity * 0.1)

class AdaptiveLearningEngine:
    """Learns from user patterns to improve emotion simulation."""
    
    def __init__(self):
        self.user_patterns = {}
        self.learning_rate = 0.1
        
    def update_patterns(
        self, 
        user_id: str, 
        emotion_state: EmotionState, 
        reward_type: RewardType,
        actual_response: Dict[str, any] = None
    ):
        """Update user patterns based on new data."""
        
        if user_id not in self.user_patterns:
            self.user_patterns[user_id] = {
                'emotion_preferences': {},
                'reward_sensitivity': {},
                'temporal_patterns': {},
                'context_sensitivity': {}
            }
        
        patterns = self.user_patterns[user_id]
        
        # Update emotion preferences
        emotion_key = f"{reward_type.value}_{emotion_state.emotion.value}"
        if emotion_key not in patterns['emotion_preferences']:
            patterns['emotion_preferences'][emotion_key] = []
        
        patterns['emotion_preferences'][emotion_key].append({
            'intensity': emotion_state.intensity,
            'confidence': emotion_state.confidence,
            'timestamp': emotion_state.timestamp
        })
        
        # Keep only recent data (last 100 entries)
        if len(patterns['emotion_preferences'][emotion_key]) > 100:
            patterns['emotion_preferences'][emotion_key] = \
                patterns['emotion_preferences'][emotion_key][-100:]
    
    def get_personalized_prediction(
        self, 
        user_id: str, 
        reward_type: RewardType,
        context: Dict[str, any]
    ) -> Tuple[EmotionState, DopamineResponse]:
        """Get personalized emotion and dopamine predictions."""
        
        if user_id not in self.user_patterns:
            # Use default predictions for new users
            emotion_sim = EmotionSimulator()
            dopamine_sim = DopamineSimulator()
            
            emotion_state = emotion_sim.simulate_emotion_response(
                reward_type, context
            )
            dopamine_response = dopamine_sim.simulate_dopamine_response(
                reward_type, emotion_state, context
            )
            
            return emotion_state, dopamine_response
        
        # Use learned patterns for existing users
        patterns = self.user_patterns[user_id]
        
        # Get historical data for this reward type
        emotion_key = f"{reward_type.value}_*"
        historical_data = []
        
        for key, data in patterns['emotion_preferences'].items():
            if key.startswith(reward_type.value):
                historical_data.extend(data)
        
        if not historical_data:
            # Fallback to default if no historical data
            emotion_sim = EmotionSimulator()
            dopamine_sim = DopamineSimulator()
            
            emotion_state = emotion_sim.simulate_emotion_response(
                reward_type, context
            )
            dopamine_response = dopamine_sim.simulate_dopamine_response(
                reward_type, emotion_state, context
            )
            
            return emotion_state, dopamine_response
        
        # Calculate personalized predictions
        avg_intensity = np.mean([d['intensity'] for d in historical_data])
        avg_confidence = np.mean([d['confidence'] for d in historical_data])
        
        # Apply context adjustments
        context_adjustment = self._calculate_context_adjustment(context, patterns)
        adjusted_intensity = avg_intensity * context_adjustment
        
        emotion_state = EmotionState(
            emotion=EmotionType.HAPPY,  # Default, could be learned
            intensity=np.clip(adjusted_intensity, 0.0, 1.0),
            confidence=np.clip(avg_confidence, 0.0, 1.0),
            timestamp=datetime.now(),
            context=context
        )
        
        dopamine_sim = DopamineSimulator()
        dopamine_response = dopamine_sim.simulate_dopamine_response(
            reward_type, emotion_state, context
        )
        
        return emotion_state, dopamine_response
    
    def _calculate_context_adjustment(
        self, 
        context: Dict[str, any], 
        patterns: Dict[str, any]
    ) -> float:
        """Calculate context-based adjustment factor."""
        adjustment = 1.0
        
        # Time-based adjustments
        current_hour = datetime.now().hour
        if current_hour in [9, 10, 11, 14, 15, 16]:  # Peak hours
            adjustment *= 1.1
        elif current_hour in [22, 23, 0, 1, 2, 3, 4, 5]:  # Late night/early morning
            adjustment *= 0.9
        
        # Fatigue adjustments
        if context.get('fatigue_level', 0) > 0.7:
            adjustment *= 0.8
        
        # Stress adjustments
        if context.get('stress_level', 0) > 0.6:
            adjustment *= 0.9
        
        return adjustment

class EmotionAIAnalytics:
    """Provides analytics and insights from emotion data."""
    
    def __init__(self):
        self.data = []
    
    def add_emotion_data(self, emotion_state: EmotionState, reward_type: RewardType):
        """Add new emotion data for analysis."""
        self.data.append({
            'emotion': emotion_state.emotion.value,
            'intensity': emotion_state.intensity,
            'confidence': emotion_state.confidence,
            'reward_type': reward_type.value,
            'timestamp': emotion_state.timestamp
        })
    
    def get_emotion_trends(self, days: int = 7) -> Dict[str, any]:
        """Get emotion trends over specified days."""
        cutoff_date = datetime.now() - timedelta(days=days)
        recent_data = [
            d for d in self.data 
            if d['timestamp'] >= cutoff_date
        ]
        
        if not recent_data:
            return {'error': 'No data available'}
        
        df = pd.DataFrame(recent_data)
        
        # Calculate trends
        emotion_counts = df['emotion'].value_counts()
        avg_intensity = df['intensity'].mean()
        avg_confidence = df['confidence'].mean()
        
        # Calculate daily patterns
        df['date'] = df['timestamp'].dt.date
        daily_patterns = df.groupby('date').agg({
            'intensity': 'mean',
            'confidence': 'mean',
            'emotion': 'count'
        }).to_dict('index')
        
        return {
            'emotion_distribution': emotion_counts.to_dict(),
            'average_intensity': avg_intensity,
            'average_confidence': avg_confidence,
            'daily_patterns': daily_patterns,
            'total_entries': len(recent_data)
        }
    
    def get_insights(self) -> List[str]:
        """Generate insights from emotion data."""
        insights = []
        
        if not self.data:
            return ['No data available for insights']
        
        df = pd.DataFrame(self.data)
        
        # Intensity insights
        avg_intensity = df['intensity'].mean()
        if avg_intensity > 0.7:
            insights.append("You're experiencing high emotional intensity - great for engagement!")
        elif avg_intensity < 0.4:
            insights.append("Your emotional responses are quite calm - consider trying different reward types")
        
        # Emotion diversity
        unique_emotions = df['emotion'].nunique()
        if unique_emotions < 3:
            insights.append("Try exploring different types of interactions for more emotional variety")
        
        # Confidence insights
        avg_confidence = df['confidence'].mean()
        if avg_confidence > 0.8:
            insights.append("The AI is very confident in predicting your emotional responses")
        elif avg_confidence < 0.5:
            insights.append("More data would help improve emotion prediction accuracy")
        
        return insights

# Main API class
class DopamindAI:
    """Main AI engine for Dopamind emotion simulation."""
    
    def __init__(self):
        self.emotion_simulator = EmotionSimulator()
        self.dopamine_simulator = DopamineSimulator()
        self.learning_engine = AdaptiveLearningEngine()
        self.analytics = EmotionAIAnalytics()
    
    def process_reward(
        self, 
        user_id: str,
        reward_type: str,
        context: Dict[str, any],
        session_history: List[Dict[str, any]] = None
    ) -> Dict[str, any]:
        """Process a reward and return emotion/dopamine predictions."""
        
        try:
            reward_enum = RewardType(reward_type)
        except ValueError:
            return {'error': f'Invalid reward type: {reward_type}'}
        
        # Get personalized predictions
        emotion_state, dopamine_response = self.learning_engine.get_personalized_prediction(
            user_id, reward_enum, context
        )
        
        # Update learning patterns
        self.learning_engine.update_patterns(
            user_id, emotion_state, reward_enum
        )
        
        # Add to analytics
        self.analytics.add_emotion_data(emotion_state, reward_enum)
        
        # Return results
        return {
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
            'context': context,
            'user_id': user_id
        }
    
    def get_analytics(self, user_id: str, days: int = 7) -> Dict[str, any]:
        """Get analytics for a specific user."""
        trends = self.analytics.get_emotion_trends(days)
        insights = self.analytics.get_insights()
        
        return {
            'trends': trends,
            'insights': insights,
            'user_id': user_id,
            'days': days
        }
    
    def get_insights(self) -> List[str]:
        """Get general insights from all data."""
        return self.analytics.get_insights()

# Example usage
if __name__ == "__main__":
    ai = DopamindAI()
    
    # Example reward processing
    result = ai.process_reward(
        user_id="user123",
        reward_type="like",
        context={
            'fatigue_level': 0.3,
            'stress_level': 0.2,
            'mood': 'positive'
        }
    )
    
    print("Reward Processing Result:")
    print(json.dumps(result, indent=2, default=str))
