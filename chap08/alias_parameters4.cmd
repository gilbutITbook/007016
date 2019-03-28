>>> from typing import List, Any
>>> def remove_last_item(L: List[Any]) -> None:
...     """마지막 항목을 삭제한 리스트 L을 반환한다.
...
...     전제 조건: len(L) >= 0
...
...     >>> remove_last_item([1, 3, 2, 4])
...     """
...     del L[-1]
