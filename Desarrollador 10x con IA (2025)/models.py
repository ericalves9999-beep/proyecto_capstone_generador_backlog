from dataclasses import dataclass
from typing import List, Optional

@dataclass
class WorkItem:
    id: str
    work_item_type: str      
    title: str
    description: str
    state: str
    iteration_path: str
    parent: Optional[str]