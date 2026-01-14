"""
Simple File Watcher - Bronze Tier
Watches Inbox folder and creates task files
"""

import time
from pathlib import Path
from datetime import datetime

class AutomatedWatcher:
    def __init__(self, vault_path):
        self.vault = Path(vault_path)
        self.inbox = self.vault / 'Inbox'
        self.needs_action = self.vault / 'Needs_Action'
        self.processed = set()
        
        print("🤖 AI Employee Watcher Started!")
        print(f"📁 Watching: {self.inbox}")
        print("📝 Task creation only (no Claude trigger)\n")
    
    def create_task_file(self, file_path):
        """Create task file in Needs_Action"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        task_file = self.needs_action / f'TASK_{timestamp}_{file_path.name}.md'
        
        content = f"""---
type: file_detected
original_file: {file_path.name}
detected_at: {datetime.now().isoformat()}
size: {file_path.stat().st_size}
status: pending
---

# New File Detected

**File**: {file_path.name}  
**Size**: {file_path.stat().st_size} bytes  
**Time**: {datetime.now().strftime('%I:%M %p')}

## Actions:
- [ ] Review file
- [ ] Process or archive
"""
        
        task_file.write_text(content, encoding='utf-8')
        print(f"✅ Task created: {task_file.name}")
    
    def run(self):
        """Main watch loop"""
        print("👀 Monitoring... (Ctrl+C to stop)\n")
        
        while True:
            try:
                for file_path in self.inbox.glob('*'):
                    if file_path.is_file() and file_path.name not in self.processed:
                        print(f"🔔 New file detected: {file_path.name}")
                        
                        self.create_task_file(file_path)
                        self.processed.add(file_path.name)
                
                time.sleep(5)
                
            except KeyboardInterrupt:
                print("\n🛑 Watcher stopped")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
                time.sleep(10)

if __name__ == '__main__':
    vault = r'C:\Users\COMTECH\Desktop\AI_Employee_Vault'
    watcher = AutomatedWatcher(vault)
    watcher.run()
