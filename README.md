# Omnispindle CLI Bridge - Gemini Knowledge Repository

A curated collection of documentation and code examples for integrating Omnispindle MCP todo server capabilities with Gemini gems. This repository serves as a clean, organized knowledge base that can be fed directly into Gemini's interface.

## Purpose

This project houses the essential files and documentation needed to understand and integrate with the Omnispindle ecosystem. It's designed to be fed into Gemini gems as a complete knowledge package, providing:

- Clean function signatures and interfaces
- Comprehensive documentation
- Usage examples and patterns
- Project validation logic
- Data structure definitions

## Repository Contents

### 📋 Core Interface Files
- **`omnispindle_init.py`** - Clean async function signatures for MCP integration
- **`tools_summary.py`** - Key function signatures and validation logic
- **`requirements.txt`** - Dependencies for understanding the ecosystem

### 📚 Documentation Files
- **`README_Omnispindle.txt`** - Original Omnispindle project documentation
- **`README_Swarmonomicon.txt`** - Swarmonomicon project overview
- **`project_overview.txt`** - Comprehensive system architecture

### 🎯 For Gemini Integration

When creating a Gemini gem that needs to interact with the Omnispindle ecosystem, feed these files to provide context on:

1. **Available Functions**: Todo management, lessons learned, MQTT communication
2. **Project Validation**: Supported projects and naming conventions
3. **Data Formats**: Expected input/output structures
4. **Integration Patterns**: How to properly interface with the MCP server

## Key Functions Available

### Todo Management
```python
add_todo_tool(description, project, priority="Medium", target_agent="user", metadata=None)
query_todos_tool(query_or_filter=None, fields_or_projection=None, limit=100)
update_todo_tool(todo_id, updates)
mark_todo_complete_tool(todo_id)
list_todos_by_status_tool(status, limit=100)
list_project_todos_tool(project, limit=5)
```

### Knowledge Base
```python
add_lesson_tool(language, topic, lesson_learned, tags=None)
search_lessons_tool(query, fields=None, limit=100)
list_lessons_tool(limit=100)
get_lesson_tool(lesson_id)
```

### MQTT Communication
```python
mqtt_publish_tool(topic, message, retain=False)
mqtt_get_tool(topic)
```

## Supported Projects

The system validates and works with these projects:
- `madness_interactive` - Main project repository
- `omnispindle` - MCP todo server
- `swarmonomicon` - Rust-based agent system
- `todomill_projectorium` - Task processing pipeline
- `regressiontestkit` - Testing framework
- `dirname` - Directory utilities
- `repo_name` - Generic repository

## Data Structures

### Todo Item Format
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

### Lesson Item Format
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

## Usage in Gemini Gems

When creating a gem that needs MCP integration:

1. **Feed this entire repository** to Gemini for context
2. **Reference the function signatures** in `omnispindle_init.py`
3. **Use the validation logic** from `tools_summary.py`
4. **Follow the data formats** specified above
5. **Understand the ecosystem** through the documentation files

## Environment Context

The MCP server expects these environment variables:
```bash
MONGODB_URI=mongodb://localhost:27017
MONGODB_DB=todo_app
MQTT_BROKER=localhost:1883
```

## Error Handling Pattern

All functions return standardized responses:

**Success:**
```json
{"success": true, "message": "Operation completed", "data": {...}}
```

**Error:**
```json
{"success": false, "error": "validation_error", "message": "Invalid project name"}
```

## Example Gemini Gem Usage

When building a gem, you might use this knowledge like:

```
Your job is to act as a syntax bridge for my CLI paste in based MCP 
implementation for working with AIs that don't have native MCP access. You 
have access to an MCP server and understand the command line oriented 
JSON syntax as demonstrated in the examples provided by the user.

Available functions:
- add_todo_tool(description, project, priority, target_agent, metadata)
- query_todos_tool(query_or_filter, fields_or_projection, limit)
- search_lessons_tool(query, fields, limit)
- mqtt_publish_tool(topic, message, retain)

Supported projects: madness_interactive, omnispindle, swarmonomicon, 
todomill_projectorium, regressiontestkit, dirname, repo_name
```

---

**Note**: This is a knowledge repository, not executable code. Use these files to understand the Omnispindle ecosystem when building Gemini gems that need MCP integration. 
