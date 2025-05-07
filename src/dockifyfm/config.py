"""
Configuration management for DockifyFM
"""

import os
from typing import Optional
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    """Application settings"""
    
    # LastFM Configuration
    lastfm_api_key: str = Field(..., env='LASTFM_API_KEY')
    lastfm_api_secret: str = Field(..., env='LASTFM_API_SECRET')
    lastfm_username: str = Field(..., env='LASTFM_USERNAME')
    
    # Spotify Configuration
    spotify_client_id: str = Field(..., env='SPOTIFY_CLIENT_ID')
    spotify_client_secret: str = Field(..., env='SPOTIFY_CLIENT_SECRET')
    spotify_redirect_uri: str = Field(..., env='SPOTIFY_REDIRECT_URI')
    spotify_username: str = Field(..., env='SPOTIFY_USERNAME')
    
    # Playlist Configuration
    playlist_name: str = Field('Rediscovered Tracks', env='PLAYLIST_NAME')
    playlist_description: str = Field(
        'Rediscovered tracks from LastFM recommendations',
        env='PLAYLIST_DESCRIPTION'
    )
    playlist_public: bool = Field(False, env='PLAYLIST_PUBLIC')
    
    # Application Configuration
    log_level: str = Field('INFO', env='LOG_LEVEL')
    update_frequency: str = Field('weekly', env='UPDATE_FREQUENCY')
    max_tracks: int = Field(100, env='MAX_TRACKS')
    min_years_since_last_played: int = Field(5, env='MIN_YEARS_SINCE_LAST_PLAYED')
    
    class Config:
        env_file = '.env'
        case_sensitive = True

# Global settings instance
settings: Optional[Settings] = None

def get_settings() -> Settings:
    """Get or create settings instance"""
    global settings
    if settings is None:
        settings = Settings()
    return settings 