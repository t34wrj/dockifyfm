# DockifyFM

## Overview
DockifyFM is an automated system that creates and maintains a Spotify playlist based on LastFM recommendations. The system identifies songs that haven't been scrobbled in the last 5 years and creates a fresh playlist weekly, helping users rediscover their forgotten music.

## Features
- Weekly playlist refresh based on LastFM recommendations
- Filters songs not scrobbled in the last 5 years
- Automatic Spotify playlist creation and updates
- Integration with LastFM and Spotify APIs
- Dockerized for easy deployment

## Project Structure
```
.
├── README.md           # Project documentation
├── CONTRIBUTING.md     # Contribution guidelines
├── docs/              # Detailed documentation
│   ├── architecture.md # System architecture
│   ├── commands.md    # Command specifications
│   └── api.md         # API documentation
├── src/               # Source code
├── tests/             # Test files
├── docker/            # Docker configuration
├── requirements.txt   # Python dependencies
└── docker-compose.yml # Docker compose configuration
```

## Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Docker and Docker Compose
- LastFM API key
- Spotify API credentials

### Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

### Docker Setup
```bash
docker-compose up -d
```

## Configuration
Create a `.env` file with the following variables:
```
LASTFM_API_KEY=your_lastfm_api_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_REDIRECT_URI=your_redirect_uri
LASTFM_USERNAME=your_lastfm_username
SPOTIFY_USERNAME=your_spotify_username
PLAYLIST_NAME=your_playlist_name
```

## Development
- Follow the coding standards outlined in CONTRIBUTING.md
- Write tests for new features
- Update documentation as needed

## Documentation
Detailed documentation can be found in the `docs/` directory:
- Architecture overview
- Command specifications
- API documentation

## License
[Specify your license here]

## Contact
[Your contact information] 