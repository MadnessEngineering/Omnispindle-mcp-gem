"""
Omnispindle Tools Summary - Key Functions and Validation Logic
Extracted from the full tools.py implementation
"""

import json
import logging
from datetime import datetime
from typing import Optional, Dict, List, Any
from pymongo import MongoClient
from bson import ObjectId

# Project validation constants
KNOWN_PROJECTS = [
    "madness_interactive", "omnispindle", "swarmonomicon", 
    "todomill_projectorium", "regressiontestkit", "dirname", "repo_name"
]

def validate_project_name(project: str) -> str:
    """
    Validate and normalize project names with fuzzy matching
    
    Args:
        project: Raw project name input
        
    Returns:
        Normalized project name or default fallback
    """
    if not project:
        return "madness_interactive"
    
    project_clean = project.lower().strip().replace("-", "_").replace(" ", "_")
    
    # Direct match
    if project_clean in KNOWN_PROJECTS:
        return project_clean
    
    # Fuzzy matching for common variations
    for known in KNOWN_PROJECTS:
        if project_clean in known or known in project_clean:
            return known
        
        # Check for partial matches (at least 3 characters)
        if len(project_clean) >= 3:
            if project_clean[:3] == known[:3] or project_clean[-3:] == known[-3:]:
                return known
    
    # Default fallback
    return "madness_interactive"

# Core data structures
class TodoItem:
    """Simplified todo item structure"""
    def __init__(self, description: str, project: str, priority: str = "Medium", 
                 target_agent: str = "user", metadata: dict = None):
        self.id = str(ObjectId())
        self.description = description
        self.project = validate_project_name(project)
        self.priority = priority
        self.target_agent = target_agent
        self.status = "pending"
        self.created_at = datetime.utcnow()
        self.metadata = metadata or {}

class LessonItem:
    """Simplified lesson learned structure"""
    def __init__(self, language: str, topic: str, lesson_learned: str, tags: list = None):
        self.id = str(ObjectId())
        self.language = language
        self.topic = topic
        self.lesson_learned = lesson_learned
        self.tags = tags or []
        self.created_at = datetime.utcnow()

# Key function signatures from tools.py

async def add_todo(description: str, project: str, priority: str = "Medium", 
                  target_agent: str = "user", metadata: dict = None) -> str:
    """
    Add a new todo item to the database
    
    Validation:
    - description: required, non-empty string
    - project: validated against KNOWN_PROJECTS list
    - priority: "Low"|"Medium"|"High"
    - target_agent: defaults to "user"
    - metadata: optional dict with ticket, tags, notes
    
    Returns: JSON with success status and todo data
    """
    pass

async def query_todos(filter_dict: dict = None, projection: dict = None, 
                     limit: int = 100) -> dict:
    """
    Query todos with MongoDB filter and projection
    
    Args:
        filter_dict: MongoDB query filter
        projection: Fields to include/exclude
        limit: Maximum results to return
        
    Returns: Dict with count and items
    """
    pass

async def search_todos(query: str, fields: list = None, limit: int = 100) -> str:
    """
    Full-text search across todo fields
    
    Args:
        query: Search text (supports "project:ProjectName" format)
        fields: Fields to search in or "all" for all text fields
        limit: Maximum results
        
    Returns: JSON with count, query, and matches
    """
    pass

async def update_todo(todo_id: str, updates: dict) -> str:
    """
    Update specific fields of a todo item
    
    Args:
        todo_id: MongoDB ObjectId as string
        updates: Dict of field->value updates
        
    Returns: JSON with success status
    """
    pass

async def mark_todo_complete(todo_id: str) -> str:
    """
    Mark todo as completed with timestamp
    
    Args:
        todo_id: MongoDB ObjectId as string
        
    Returns: JSON with todo_id and completed_at
    """
    pass

async def list_todos_by_status(status: str, limit: int = 100) -> str:
    """
    List todos filtered by status
    
    Args:
        status: "initial"|"pending"|"completed"|"review"
        limit: Maximum results
        
    Returns: JSON with count, status, items, and project breakdown
    """
    pass

async def add_lesson(language: str, topic: str, lesson_learned: str, 
                    tags: list = None) -> str:
    """
    Add a new lesson learned entry
    
    Args:
        language: Technology/language name
        topic: Brief title
        lesson_learned: Full lesson content
        tags: Optional categorization tags
        
    Returns: JSON with lesson_id and topic
    """
    pass

async def search_lessons(query: str, fields: list = None, limit: int = 100) -> str:
    """
    Search lessons by text content
    
    Args:
        query: Search text
        fields: Fields to search (default: ["topic", "lesson_learned"])
        limit: Maximum results
        
    Returns: JSON with count, query, and matches
    """
    pass

async def list_project_todos(project: str, limit: int = 5) -> str:
    """
    List recent todos for a specific project
    
    Args:
        project: Project name (will be validated)
        limit: Maximum results
        
    Returns: JSON with count, project, and items
    """
    pass

# MQTT integration functions
async def mqtt_publish(topic: str, message: str, retain: bool = False) -> str:
    """
    Publish message to MQTT broker
    
    Args:
        topic: MQTT topic path
        message: Message content
        retain: Whether to retain message
        
    Returns: JSON with success status
    """
    pass

async def mqtt_get(topic: str) -> str:
    """
    Get latest message from MQTT topic
    
    Args:
        topic: MQTT topic path
        
    Returns: Latest message content or None
    """
    pass

# Error handling patterns
def create_error_response(message: str, error_type: str = "error") -> str:
    """Create standardized error response"""
    return json.dumps({
        "success": False,
        "error": error_type,
        "message": message
    })

def create_success_response(data: Any, message: str = "Success") -> str:
    """Create standardized success response"""
    return json.dumps({
        "success": True,
        "message": message,
        "data": data
    }, default=str)

# Validation helpers
def validate_priority(priority: str) -> str:
    """Validate priority level"""
    valid_priorities = ["Low", "Medium", "High"]
    return priority if priority in valid_priorities else "Medium"

def validate_status(status: str) -> str:
    """Validate todo status"""
    valid_statuses = ["initial", "pending", "completed", "review"]
    return status if status in valid_statuses else "pending"

def sanitize_mongo_query(query: dict) -> dict:
    """Sanitize MongoDB query to prevent injection"""
    # Remove potentially dangerous operators
    dangerous_ops = ["$where", "$eval", "$expr"]
    cleaned = {}
    
    for key, value in query.items():
        if key not in dangerous_ops:
            cleaned[key] = value
    
    return cleaned 
