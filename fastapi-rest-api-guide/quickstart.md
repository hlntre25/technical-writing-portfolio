# Quick Start

This guide will get you up and running with the Portfolio Document API in under 5 minutes.

## Prerequisites

- You have `curl` installed.
- You have a basic understanding of REST APIs.

## 1. Create a Document

First, let's create a new document. Open your terminal and run the following `curl` command:

```bash
curl -X POST "http://localhost:8000/documents" \
-H "Content-Type: application/json" \
-d '{
  "title": "My First Document",
  "format": "md"
}'
```

You will receive a response similar to this, which includes the unique ID of your new document:

```json
{
  "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
  "title": "My First Document",
  "format": "md",
  "template": null,
  "status": "completed"
}
```

Copy the `id` from the response. You'll need it for the next step.

## 2. Retrieve the Document

Now, use the `id` you copied to retrieve the document you just created. Replace `YOUR_DOCUMENT_ID` with your actual ID.

```bash
curl -X GET http://localhost:8000/documents/YOUR_DOCUMENT_ID
```

The API will return the full document object.

## 3. List All Documents

To see all the documents currently in the system, run this command:

```bash
curl -X GET http://localhost:8000/documents
```

This will return a list containing the document you created.

That's it! You've successfully interacted with the core functions of the API.
