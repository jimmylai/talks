from dataclasses import dataclass, field
from typing import Dict, Callable
from types import FrameType
from helpers import get_key
import time

@dataclass
class Node:
    key: str  # module_name.class_name.function_name
    time: int = 0
    children: Dict[str, "Node"] = field(default_factory=dict)


class Profiler:
    def __init__(self, timer):
        self.timestamp = 0
        self.root = Node("")
        self.nodes: Dict[FrameType, Node] = {}
        self.timer: Callable[[], int] = timer

    def callback(self, frame, event, arg):
        time_delta = self.timer() - self.timestamp
        parent_frame = frame.f_back
        key = get_key(frame, event, arg)
        print(key, event)
        if event in {"call", "c_call"}:
            if parent_frame is None or parent_frame not in self.nodes:
                parent_node = self.root
                self.timestamp = self.timer()
            else:
                parent_node = self.nodes[parent_frame] if event == "call" else self.nodes[frame]
                parent_node.time += time_delta

            if event == "c_call" or frame.f_lasti == -1:
                # the frame was called for the first time
                # The frame of generator/coroutine can be called multiple times
                if key not in parent_node.children:
                    parent_node.children[key] = Node(key)
                node = parent_node.children[key]
                if event == "c_call":
                    self.nodes[id(arg)] = node
                else:
                    self.nodes[frame] = node
        elif event in ("return", "c_return"):
            node = None
            if event == "return" and frame in self.nodes:
                node = self.nodes[frame]
            elif event == "c_return" and id(arg) in self.nodes:
                node = self.nodes[id(arg)]
            if node:
                node.time += time_delta
        self.timestamp = self.timer()

