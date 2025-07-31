# Omnispindle CLI Bridge - OpenAI GPTs Knowledge Repository

A curated collection of documentation and code examples for integrating Omnispindle MCP todo server capabilities with OpenAI GPTs. This repository serves as a knowledge base to allow GPTs to interact with the Omnispindle ecosystem.

## AI Model Integration Docs

- [Claude Agents](./README_Claude.md)
- [OpenAI GPTs](./README_GPT.md) (You are here)
- [Goose AI](./README_Goose.md)
- [Gemini Gems](./README.md)

## Purpose

This project houses the documentation needed to understand and integrate with the Omnispindle ecosystem. It's designed to be used as a knowledge source for custom GPTs, providing:

- Function signatures and interfaces for custom actions
- Usage examples and patterns
- Project validation logic
- Data structure definitions

## Usage with Custom GPTs

To integrate with OpenAI GPTs, you can create custom actions that call the Omnispindle MCP server. Use the files in this repository to define the OpenAPI schema for your custom actions and provide context to the GPT on:

1.  **Available Functions**: Todo management, lessons learned, MQTT pub/sub
2.  **Project Validation**: Supported projects and naming conventions
3.  **Data Formats**: Expected input/output structures for API calls
4.  **Integration Patterns**: How to properly interface with the MCP server

---

**Note**: This is a knowledge repository, not executable code. Use these files to build custom GPTs with actions that can interface with the Omnispindle ecosystem. 
