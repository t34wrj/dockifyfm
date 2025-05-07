# API Documentation

## Overview
DockifyFM integrates with LastFM and Spotify APIs to create and maintain personalized playlists. This documentation covers the API endpoints and integration points.

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication
All API requests require authentication using API keys:
```
Authorization: Bearer <api_key>
```

## Endpoints

### Commands

#### Execute Command
```http
POST /commands/execute
Content-Type: application/json

{
    "command": "string",
    "parameters": {
        "key": "value"
    }
}
```

Response:
```json
{
    "status": "success",
    "result": {
        "output": "string",
        "metadata": {}
    }
}
```

#### List Available Commands
```http
GET /commands
```

Response:
```json
{
    "commands": [
        {
            "name": "string",
            "description": "string",
            "parameters": {}
        }
    ]
}
```

### System

#### Get System Status
```http
GET /system/status
```

Response:
```json
{
    "status": "operational",
    "version": "string",
    "uptime": "string"
}
```

#### Update Configuration
```http
PUT /system/config
Content-Type: application/json

{
    "key": "value"
}
```

## Error Responses
All error responses follow this format:
```json
{
    "error": {
        "code": "string",
        "message": "string",
        "details": {}
    }
}
```

## Rate Limiting
- 100 requests per minute per API key
- Rate limit headers included in responses

## WebSocket API
For real-time updates and command execution:

```javascript
const ws = new WebSocket('ws://localhost:8000/ws');

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // Handle message
};
```

## SDK Support
Official SDKs available for:
- Python
- JavaScript/TypeScript
- Go
- Java

## Best Practices
1. Always handle rate limiting
2. Implement proper error handling
3. Use appropriate timeouts
4. Cache responses when possible
5. Monitor API usage

## LastFM API Integration

### Authentication
```python
import pylast

network = pylast.LastFMNetwork(
    api_key=LASTFM_API_KEY,
    api_secret=LASTFM_API_SECRET
)
```

### Key Endpoints

#### Get User Recommendations
```python
user = network.get_user(LASTFM_USERNAME)
recommendations = user.get_recommended_tracks()
```

#### Get User History
```python
user = network.get_user(LASTFM_USERNAME)
recent_tracks = user.get_recent_tracks(limit=1000)
```

## Spotify API Integration

### Authentication
```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope='playlist-modify-public playlist-modify-private'
))
```

### Key Endpoints

#### Create Playlist
```python
playlist = sp.user_playlist_create(
    user=SPOTIFY_USERNAME,
    name=PLAYLIST_NAME,
    public=False
)
```

#### Update Playlist
```python
sp.playlist_replace_items(
    playlist_id=playlist_id,
    items=track_uris
)
```

#### Search Tracks
```python
results = sp.search(
    q=f"track:{track_name} artist:{artist_name}",
    type="track",
    limit=1
)
```

## Error Handling

### LastFM API Errors
```json
{
    "error": {
        "code": "number",
        "message": "string"
    }
}
```

### Spotify API Errors
```json
{
    "error": {
        "status": "number",
        "message": "string"
    }
}
```

## Rate Limiting

### LastFM
- 5 requests per second
- Implement exponential backoff

### Spotify
- 25 requests per second
- Implement token refresh

## Best Practices
1. Cache API responses when possible
2. Implement retry logic with backoff
3. Handle token refresh automatically
4. Log all API interactions
5. Monitor rate limits

## Webhook Support
For real-time updates:

```python
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # Handle webhook data
    return jsonify({"status": "success"})
```

## SDK Support
- pylast for LastFM
- spotipy for Spotify
- requests for custom endpoints 