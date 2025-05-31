# Omnispindle CLI Bridge - Gemini Knowledge Repository

A curated collection of documentation and code examples for integrating Omnispindle MCP todo server capabilities with Gemini via gems. At the time of writing, Gemini does not support MCP integration, so this repository serves as a bridge to allow Gemini(or any other LLM) to interact with the Omnispindle ecosystem via a little copy-paste.

## Purpose

This project houses the documentation needed to understand and integrate with the Omnispindle ecosystem. It's designed to be fed into Gemini gems as a knowledge package, providing:

- Function signatures and interfaces
- Usage examples and patterns
- Project validation logic
- Data structure definitions

## Repository Contents

### 📋 Core Interface Files
- **`omnispindle_init.py`** - Function signatures for MCP integration
- **`tools_summary.py`** - shows the LLM the validation logic
- **`requirements.txt`** - Dependencies for understanding the ecosystem

### 📚 Documentation Files
- **`README_Omnispindle.txt`** - Original Omnispindle project documentation
- **`README_Swarmonomicon.txt`** - Swarmonomicon project overview
<!-- TODO: Add madness_interactive project overview -->
- **`README_TodoMill.txt`** - TodoMill project overview
- **`README_RegressionTestKit.txt`** - RegressionTestKit project overview
- **`README_Dirname.txt`** - Dirname project overview
- **`project_overview.txt`** - Comprehensive system architecture

### 🎯 Gemini Integration Files
- **`prompt_file_no_upload.md`** - Prompt template for creating our MCP CLI bridge gem

### 🎯 For Gemini Integration

When creating a Gemini gem that needs to interact with the Omnispindle ecosystem, feed these files to provide context on:

1. **Available Functions**: Todo management, lessons learned, MQTT pub/sub
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
mqtt_get_tool(topic) # sub -C(ount) 1 to get a single message
```

## Supported Projects

The system validates and works with these projects:
- `madness_interactive` - Main project repository
- `omnispindle` - MCP todo server
- `swarmonomicon` - Rust-based agent system
- `todomill_projectorium` - Task processing pipeline
- `regressiontestkit` - Testing framework
 scope.availableProjects = [
  "regressiontestkit",
  "madness_interactive",
  "omnispindle",
  "swarmonomicon",
  "balena_device_management",
  "cogwyrm",
  "docker_implementation",
  "documentation",
  "eventghost-rust",
  "fastmcp",
  "hammerghost",
  "hammerspoon",
  "quality_assurance",
  "inventorium",
  "spindlewrit"
]
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
3. **Use the prompt template** in `prompt_file_no_upload.md` to create your MCP CLI bridge gem

---

**Note**: This is a knowledge repository, not executable code. Use these files to understand the Omnispindle ecosystem when building Gemini gems that need MCP integration.
