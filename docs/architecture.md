# System Architecture

## Overview
DockifyFM is designed as a modular system that integrates LastFM and Spotify APIs to create and maintain personalized playlists. The architecture emphasizes reliability, maintainability, and ease of deployment through Docker.

## Core Components

### 1. LastFM Integration
- Fetches user's listening history
- Retrieves recommendations
- Filters songs based on last scrobble date
- Handles LastFM API rate limiting

### 2. Spotify Integration
- Manages authentication and token refresh
- Creates and updates playlists
- Searches for tracks
- Handles Spotify API rate limiting

### 3. Playlist Manager
- Coordinates between LastFM and Spotify
- Implements playlist creation logic
- Manages playlist updates
- Handles track matching between services

### 4. Scheduler
- Manages weekly playlist updates
- Handles execution timing
- Implements retry logic
- Manages error recovery

### 5. State Management
- Tracks playlist state
- Manages API tokens
- Handles configuration
- Maintains execution history

## Data Flow
1. Scheduler triggers weekly update
2. LastFM Integration fetches recommendations
3. Playlist Manager filters songs
4. Spotify Integration creates/updates playlist
5. State Management updates execution history

## Security Considerations
- Secure storage of API keys
- Token management and refresh
- Rate limiting compliance
- Error handling and logging

## Docker Architecture
- Containerized application
- Environment variable management
- Volume management for persistence
- Health checks and monitoring

## Monitoring and Logging
- Playlist update status
- API call metrics
- Error tracking
- Performance monitoring

## Error Handling
- API failure recovery
- Rate limit handling
- Network error management
- Data validation

## Configuration Management
- Environment variables
- API credentials
- Playlist settings
- Update schedule 