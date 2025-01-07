POST /chats

a new chat is created — similar to how a new task is created, a new chat defined the following schema:

> Note that a PDF file can be added as a thread_input.

```json
{
  "thread_input": {
    "type": "object",
    "properties": {
      "pdf": { "type": "file" }
    }
  },
  "user_message_input": {
    "type": "object",
    "properties": {
      "text": {
        "type": "string"
      }
    }
  },
  "assistant_message_output": {
    "type": "object",
    "properties": {
      "text": {
        "type": "string"
      }
    }
  }
}
```

```json
{
  "chat_id": "string"
}
```

POST /chats/{chat_id}/threads

creates a new thread and set inputs variables.

optionally, a user_message_input could be provided as well, for convenience (not shown below).

```json 
{
  "thread_input": {
    "pdf": {
      "url": "https://example.com/pdf.pdf"
    }
  }
}
```

return a new thread object. 

```json
{
  "thread_id": "12345",
  "created_at": "2025-01-06T14:42:00Z"
}
```

POST /chats/{chat_id}/threads/{thread_id}/user_messages 

add a user_message to the thread.

```json
{
  "user_message_input": {
    "text": "Summarize this PDF."
  }
}
```

return a assistant_message answer. 

```json
{
  "assistant_message_output": {
    "text": "The first page of the PDF is a table of contents.",
  },
  "thread": {
    "thread_id": "12345",
    "last_updated": "2025-01-06T14:42:00Z"
  }
}

POST /chats/{chat_id}/threads/{thread_id}/user_messages

add a user_message to the thread.

```json
{
  "user_message_input": {
    "text": "And write the summary in French."
  }
}
```

return a assistant_message answer. 

```json
{
    "assistant_message_output": {
        "text": "La première page du PDF est une table des matières."
    },
    "thread": {
        "thread_id": "12345",
        "last_updated": "2025-01-06T14:43:00Z"
    }
}
```