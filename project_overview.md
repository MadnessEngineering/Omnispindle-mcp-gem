# Omnispindle CLI Bridge - Project Overview

## Purpose
A bridge interface for integrating Omnispindle MCP todo server capabilities with external systems, particularly for Gemini gem integration.

## Core Components

### 1. Todo Management System
- **MongoDB Backend**: Persistent storage for todos and lessons learned
- **Project Validation**: Supports known projects (madness_interactive, omnispindle, swarmonomicon, etc.)
- **Priority System**: Low/Medium/High priority levels
- **Status Tracking**: initial → pending → completed/review workflow
- **Agent Targeting**: Route tasks to specific agents

### 2. Lessons Learned System
- **Knowledge Base**: Store and search technical lessons
- **Categorization**: Tag-based organization by language/technology
- **Full-Text Search**: Query across topics and content

### 3. MQTT Integration
- **Real-time Messaging**: Publish/subscribe to MQTT topics
- **Task Distribution**: Route tasks via MQTT to processing agents
- **Status Updates**: Real-time task status broadcasting

## Key Features

### Todo Operations
```python
# Add todo with project validation
add_todo(description, project, priority="Medium", target_agent="user")

# Query with MongoDB filters
query_todos(filter_dict, projection, limit=100)

# Search with text queries
search_todos(query, fields=["all"], limit=100)

# Status management
list_todos_by_status(status, limit=100)
mark_todo_complete(todo_id)
```

### Lesson Management
```python
# Add lessons learned
add_lesson(language, topic, lesson_learned, tags=[])

# Search knowledge base
search_lessons(query, fields=["topic", "lesson_learned"], limit=100)
```

### MQTT Communication
```python
# Publish messages
mqtt_publish(topic, message, retain=False)

# Get latest messages
mqtt_get(topic)
```

## Project Integration

### Supported Projects
- **madness_interactive**: Main project repository
- **omnispindle**: MCP todo server
- **swarmonomicon**: Rust-based agent system
- **todomill_projectorium**: Task processing pipeline
- **regressiontestkit**: Testing framework
- **dirname**: Directory utilities
- **repo_name**: Generic repository

### Validation Logic
- Fuzzy matching for project names
- Automatic normalization (spaces → underscores, case insensitive)
- Fallback to "madness_interactive" for unknown projects

## Data Structures

### TodoItem
```python
{
    "id": "ObjectId",
    "description": "Task description",
    "project": "validated_project_name",
    "priority": "Low|Medium|High",
    "target_agent": "user",
    "status": "pending",
    "created_at": "datetime",
    "metadata": {"ticket": "", "tags": [], "notes": ""}
}
```

### LessonItem
```python
{
    "id": "ObjectId",
    "language": "technology_name",
    "topic": "brief_title",
    "lesson_learned": "full_content",
    "tags": ["tag1", "tag2"],
    "created_at": "datetime"
}
```

## Environment Configuration
```bash
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=todo_app
MQTT_BROKER=localhost:1883
```

## Error Handling
- Standardized JSON responses with success/error status
- Input validation and sanitization
- MongoDB injection prevention
- Graceful fallbacks for invalid inputs

## Integration Points

### For Gemini Gem
1. **Function Signatures**: Clean async functions with type hints
2. **JSON Responses**: Consistent response format for all operations
3. **Validation**: Built-in input validation and normalization
4. **Error Handling**: Predictable error responses

### For Swarmonomicon
1. **MQTT Topics**: Compatible with existing topic structure
2. **Task Format**: Matches expected task schema
3. **Agent Routing**: Supports agent-specific task queues

### For External Systems
1. **REST API**: HTTP endpoints for all operations
2. **WebSocket**: Real-time updates and communication
3. **CLI Tools**: Command-line interface for testing and automation

## Usage Patterns

### Basic Todo Workflow
```python
# 1. Add todo
todo_id = await add_todo("Implement feature X", "omnispindle", "High")

# 2. Query status
todos = await list_todos_by_status("pending")

# 3. Complete task
await mark_todo_complete(todo_id)
```

### Knowledge Management
```python
# 1. Add lesson
lesson_id = await add_lesson("Python", "Async Patterns", "Use asyncio.gather for parallel execution")

# 2. Search lessons
results = await search_lessons("async python")
```

### Real-time Communication
```python
# 1. Publish task
await mqtt_publish("mcp/todo/new", json.dumps(task_data))

# 2. Get status updates
status = await mqtt_get("response/todo/status")
```

This bridge provides a clean, validated interface between the complex Omnispindle/Swarmonomicon ecosystem and external integrations like Gemini gems. 
