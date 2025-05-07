# Command Specifications

## Command Interface
All commands must implement the following interface:

```python
class Command:
    def execute(self, context: CommandContext) -> CommandResult:
        """
        Execute the command with the given context.
        
        Args:
            context: The execution context containing state and parameters
            
        Returns:
            CommandResult containing execution status and output
        """
        pass
```

## Command Context
The command context provides:
- API credentials and tokens
- User preferences
- Playlist configuration
- Execution history
- Error state

## Command Result
Command results include:
- Success/failure status
- Updated playlist information
- Error messages (if any)
- Execution metadata

## Available Commands

### 1. LastFM Commands
- `fetch_recommendations`: Get LastFM recommendations
- `get_user_history`: Fetch user's scrobble history
- `filter_old_tracks`: Filter tracks not scrobbled in 5 years

### 2. Spotify Commands
- `create_playlist`: Create new Spotify playlist
- `update_playlist`: Update existing playlist
- `search_tracks`: Search for tracks on Spotify
- `add_tracks`: Add tracks to playlist

### 3. Playlist Management
- `sync_playlist`: Synchronize LastFM and Spotify
- `refresh_playlist`: Weekly playlist refresh
- `validate_tracks`: Validate track availability

### 4. System Commands
- `check_health`: System health check
- `update_tokens`: Refresh API tokens
- `log_status`: Log execution status

## Command Execution Flow
1. Validate API credentials
2. Fetch LastFM recommendations
3. Filter tracks by scrobble date
4. Search tracks on Spotify
5. Create/update playlist
6. Log execution results

## Error Handling
- API rate limiting
- Authentication failures
- Track matching errors
- Network issues
- Token expiration

## Security
- API key management
- Token refresh handling
- Rate limit compliance
- Error logging

## Best Practices
- Implement retry logic
- Handle API rate limits
- Validate track matches
- Log all operations
- Monitor execution time 