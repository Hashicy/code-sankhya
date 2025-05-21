# backend/utils/parser.py

import ast

class LoopDepthVisitor(ast.NodeVisitor):
    def __init__(self):
        self.depths = []
        self.current_depth = 0

    def generic_visit(self, node):
        if isinstance(node, (ast.For, ast.While)):
            self.current_depth += 1
            self.depths.append(self.current_depth)
            super().generic_visit(node)
            self.current_depth -= 1
        else:
            super().generic_visit(node)

def extract_loops(tree):
    visitor = LoopDepthVisitor()
    visitor.visit(tree)
    return visitor.depths
