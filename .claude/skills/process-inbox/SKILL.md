---
name: process-inbox
description: Analyze and prioritize files in Needs_Action folder
---

# Process Inbox Skill

## What to do:
1. Read all .md files in /Needs_Action
2. Categorize each by priority (HIGH/MEDIUM/LOW)
3. Create summary showing:
   - HIGH priority items first
   - MEDIUM priority next
   - LOW priority last
4. Suggest action for each file

## Priority rules:
- HIGH: .pdf, .docx, or keywords: urgent, payment, invoice
- MEDIUM: .txt, .md, general files
- LOW: .jpg, .png, empty files