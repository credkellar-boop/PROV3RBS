import os
from livekit import api

def generate_video_token(room_name: str, identity: str) -> str:
    """Generates a LiveKit JWT token for video study rooms."""
    api_key = os.getenv("LIVEKIT_API_KEY")
    api_secret = os.getenv("LIVEKIT_API_SECRET")
    
    if not api_key or not api_secret:
        raise ValueError("LiveKit credentials are missing from environment.")

    token = api.AccessToken(api_key, api_secret) \
        .with_identity(identity) \
        .with_grants(api.VideoGrant(room_join=True, room=room_name))
        
    return token.to_jwt()
  
