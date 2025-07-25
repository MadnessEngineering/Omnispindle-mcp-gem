"""
Omnispindle CLI Bridge - Essential Tool Functions
A simplified interface for MCP todo and lesson management tools
"""

import json
import os
import logging
from typing import Optional, Dict, List
from dotenv import load_dotenv
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# MongoDB configuration
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
MONGODB_DB = os.getenv("MONGODB_DB", "todo_app")

# Create MongoDB connection
mongo_client = MongoClient(MONGODB_URI)
db = mongo_client[MONGODB_DB]
collection = db["todos"]
lessons_collection = db["lessons_learned"]

# Core tool functions for MCP integration

async def add_todo(description: str, project: str, priority: str = "Medium", target_agent: str = "user", metadata: dict = None) -> str:
    """
    Add a new todo item

    Args:
        description: Task description
        project: Project name (Madness_interactive, Omnispindle, Swarmonomicon, etc.)
        priority: "Low"|"Medium"|"High" (default: Medium)
        target_agent: Target agent for the task (default: user)
        metadata: Additional metadata like ticket numbers, tags, notes

    Returns:
        JSON string with todo_id, description, and project
    """
    # Implementation would call the actual add_todo function
    pass

async def query_todos(query_or_filter=None, fields_or_projection=None, limit: int = 100) -> str:
    """
    Query or search todos with flexible options

    Args:
        query_or_filter: MongoDB query dict or text string to search
        fields_or_projection: MongoDB projection dict or list of fields to search
        limit: Max results (default: 100)

    Returns:
        JSON string with count and items/matches
    """
    pass

async def update_todo(todo_id: str, updates: dict) -> str:
    """
    Update todo fields

    Args:
        todo_id: ID of todo to update
        updates: Fields to change {field: new_value}

    Returns:
        JSON string with success status and message
    """
    pass

async def mark_todo_complete(todo_id: str) -> str:
    """
    Mark todo as completed

    Args:
        todo_id: ID of todo to complete

    Returns:
        JSON string with todo_id and completed_at timestamp
    """
    pass

async def list_todos_by_status(status: str, limit: int = 100) -> str:
    """
    List todos by status

    Args:
        status: "initial"|"pending"|"completed"|"review"
        limit: Max results (default: 100)

    Returns:
        JSON string with count, status, and items
    """
    pass

async def add_lesson(language: str, topic: str, lesson_learned: str, tags: list = None) -> str:
    """
    Create a new lesson learned entry

    Args:
        language: Technology or language name
        topic: Brief title/subject
        lesson_learned: Full lesson content
        tags: Optional categorization tags

    Returns:
        JSON string with lesson_id and topic
    """
    pass

async def search_lessons(query: str, fields: list = None, limit: int = 100) -> str:
    """
    Search lessons by text

    Args:
        query: Text to search for
        fields: Fields to search in (default: ["topic", "lesson_learned"])
        limit: Max results (default: 100)

    Returns:
        JSON string with count, query, and matches
    """
    pass

async def mqtt_publish(topic: str, message: str, retain: bool = False) -> str:
    """
    Publish MQTT message

    Args:
        topic: Topic path to publish to
        message: Content to send
        retain: Keep for new subscribers (default: false)

    Returns:
        JSON string with success status
    """
    pass

async def mqtt_get(topic: str) -> str:
    """
    Get latest MQTT message

    Args:
        topic: Topic to retrieve from

    Returns:
        JSON string with success status and data
    """
    pass

# Project validation helper
def validate_project_name(project: str) -> str:
    """
    Validate and normalize project names

    Known projects: Madness_interactive, Omnispindle, Swarmonomicon,
    todomill_projectorium, RegressionTestKit, Dirname, Repo_name
    """
    known_projects = [
        "madness_interactive", "omnispindle", "swarmonomicon",
        "todomill_projectorium", "regressiontestkit", "dirname", "repo_name"
    ]

    project_lower = project.lower()

    # Direct match
    if project_lower in known_projects:
        return project_lower

    # Partial matching for common variations
    for known in known_projects:
        if project_lower in known or known in project_lower:
            return known

    # Default fallback
    return "madness_interactive"

# Tool registry for easy access
AVAILABLES = {
    "add_todo": add_todo,
    "query_todos": query_todos,
    "update_todo": update_todo,
    "mark_todo_complete": mark_todo_complete,
    "list_todos_by_status": list_todos_by_status,
    "add_lesson": add_lesson,
    "search_lessons": search_lessons,
    "mqtt_publish": mqtt_publish,
    "mqtt_get": mqtt_get,
}
