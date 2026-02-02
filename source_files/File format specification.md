# JSON
```json
{
  "questions": [
    {
      "id": "integer_question_id",
      "title": "question_title",
      "options": [
        { "id": "string_id", "text": "option_text" },
        "..."
      ],
      "correct_option_ids": ["ids from options"]
    },
    "..."
  ]
}
```

# CSV
```csv
id,title,options,correct_option_ids
integer_question_id,title,"option_id:option_text|option_id:option_text",correct_option_id|correct_option_id
```