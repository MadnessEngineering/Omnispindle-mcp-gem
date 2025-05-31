# Omnispindle CLI Bridge

A streamlined interface for integrating Omnispindle MCP todo server capabilities with external systems, particularly designed for Gemini gem integration.

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Environment Setup
```bash
# .env file
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=todo_app
MQTT_BROKER=localhost:1883
```

### Basic Usage
```python
from omnispindle_init import add_todo_tool, query_todos_tool

# Add a todo
result = await add_todo_tool(
    description="Implement new feature",
    project="omnispindle",
    priority="High"
)

# Query todos
todos = await query_todos_tool(
    query_or_filter={"status": "pending"},
    limit=10
)
```

## Core Features

### 🎯 Todo Management
- **Project Validation**: Automatic validation against known projects
- **Priority System**: Low/Medium/High priority levels
- **Status Tracking**: Complete workflow management
- **Agent Routing**: Target specific processing agents

### 📚 Knowledge Base
- **Lessons Learned**: Store and search technical knowledge
- **Tag-based Organization**: Categorize by technology/language
- **Full-text Search**: Query across all content

### 🔄 Real-time Integration
- **MQTT Messaging**: Publish/subscribe to task updates
- **WebSocket Support**: Live communication channels
- **Event Broadcasting**: Real-time status updates

## API Reference

### Todo Operations
```python
# Add todo
add_todo_tool(description, project, priority="Medium", target_agent="user", metadata=None)

# Query todos
query_todos_tool(query_or_filter=None, fields_or_projection=None, limit=100)

# Update todo
update_todo_tool(todo_id, updates)

# Mark complete
mark_todo_complete_tool(todo_id)

# List by status
list_todos_by_status_tool(status, limit=100)
```

### Lesson Management
```python
# Add lesson
add_lesson_tool(language, topic, lesson_learned, tags=None)

# Search lessons
search_lessons_tool(query, fields=None, limit=100)
```

### MQTT Communication
```python
# Publish message
mqtt_publish_tool(topic, message, retain=False)

# Get latest message
mqtt_get_tool(topic)
```

## Supported Projects

The bridge validates and normalizes project names for:
- `madness_interactive` - Main project repository
- `omnispindle` - MCP todo server
- `swarmonomicon` - Rust-based agent system
- `todomill_projectorium` - Task processing pipeline
- `regressiontestkit` - Testing framework
- `dirname` - Directory utilities
- `repo_name` - Generic repository

## Data Formats

### Todo Item
```json
{
  "id": "unique_id",
  "description": "Task description",
  "project": "validated_project_name",
  "priority": "Low|Medium|High",
  "target_agent": "user",
  "status": "pending",
  "created_at": "2024-01-01T00:00:00Z",
  "metadata": {
    "ticket": "PROJ-123",
    "tags": ["feature", "urgent"],
    "notes": "Additional context"
  }
}
```

### Lesson Item
```json
{
  "id": "unique_id",
  "language": "Python",
  "topic": "Async Patterns",
  "lesson_learned": "Use asyncio.gather() for parallel execution",
  "tags": ["async", "performance"],
  "created_at": "2024-01-01T00:00:00Z"
}
```

## Integration Examples

### Gemini Gem Integration
```python
# In your gem
from omnispindle_cli_bridge import AVAILABLE_TOOLS

# Use any tool
result = await AVAILABLE_TOOLS["add_todo"](
    "Implement OAuth integration",
    "my_project",
    "High"
)
```

### MQTT Task Distribution
```python
# Publish task to specific agent
await mqtt_publish_tool(
    "mcp/todo/greeter",
    json.dumps({
        "description": "Welcome new user",
        "priority": "Medium"
    })
)
```

### Knowledge Base Queries
```python
# Search for Python lessons
lessons = await search_lessons_tool(
    "python async",
    fields=["topic", "lesson_learned"],
    limit=5
)
```

## Error Handling

All functions return standardized JSON responses:

### Success Response
```json
{
  "success": true,
  "message": "Operation completed",
  "data": { ... }
}
```

### Error Response
```json
{
  "success": false,
  "error": "validation_error",
  "message": "Invalid project name"
}
```

## Development

### Running Tests
```bash
pytest tests/ -v
```

### Code Formatting
```bash
black omnispindle_init.py tools_summary.py
```

### Type Checking
```bash
mypy omnispindle_init.py
```

## Architecture

The bridge sits between external systems (like Gemini gems) and the Omnispindle/Swarmonomicon ecosystem:

```
[Gemini Gem] → [CLI Bridge] → [MongoDB/MQTT] → [Swarmonomicon Agents]
```

Key design principles:
- **Clean Interfaces**: Simple async functions with type hints
- **Input Validation**: Automatic sanitization and normalization
- **Error Resilience**: Graceful handling of invalid inputs
- **Consistent Responses**: Standardized JSON format for all operations

## License

MIT License - see LICENSE file for details.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request

For more information about the broader ecosystem, see:
- [Omnispindle Documentation](../Omnispindle/README.md)
- [Swarmonomicon Project](../Swarmonomicon/README.md) 
