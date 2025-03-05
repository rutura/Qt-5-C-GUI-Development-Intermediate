# Undo/Redo Functionality in the PySide6 Painter Application

This document explains the implementation of undo/redo functionality in the PySide6 Painter Application using the Command pattern with QUndoStack.

## Overview

The undo/redo functionality is implemented using Qt's built-in `QUndoStack` class and a set of command classes that implement the Command design pattern. Each user action that modifies the scene (adding shapes, removing items, moving objects) is represented by a command that knows how to undo and redo that specific action.

## Key Components

### 1. QUndoStack

The `QUndoStack` class manages a stack of command objects. When a command is executed, it's pushed onto the stack. The stack keeps track of the command sequence and allows undoing/redoing operations in the correct order.

### 2. Command Classes

The application uses three main command classes:

- **AddCommand**: Handles adding items to the scene
- **RemoveCommand**: Handles removing items from the scene
- **MoveCommand**: Handles moving items in the scene

Each command class implements:
- `undo()`: Reverses the action
- `redo()`: Applies the action

### 3. Integration Points

Undo/redo capabilities are integrated at these key points:

- **Adding shapes**: When shapes are drawn or dropped into the scene
- **Removing shapes**: When the Delete key is pressed
- **Moving shapes**: When shapes are dragged with the cursor tool

## Usage

The undo/redo functionality is accessed through:

1. Edit menu commands:
   - **Undo**: Reverts the last action
   - **Redo**: Re-applies the last undone action

2. Keyboard shortcuts:
   - **Ctrl+Z**: Undo
   - **Ctrl+Y**: Redo

## Implementation Details

### Command Pattern

The Command pattern encapsulates a request as an object, allowing:
- Parameterization of clients with different requests
- Queuing of requests
- Logging of requests
- Support for undoable operations

### Code Structure

1. **commands.py**: Contains the command classes
2. **scene.py**: Creates and manages the undo stack and generates commands 
3. **mainwindow.py**: Connects UI actions to undo/redo operations

### Technical Considerations

- Commands store references to the modified items and their properties
- Position changes track both old and new positions
- The scene maintains lists to track selection state during moves

## Extending the System

To add new undoable operations:

1. Create a new command class that inherits from `QUndoCommand`
2. Implement the `undo()` and `redo()` methods
3. Create and push the command to the undo stack when the action occurs

## Example Command Flow

1. User draws a rectangle:
   - `Scene.mouseReleaseEvent()` creates a `ResizableRectItem`
   - An `AddCommand` is created with the item
   - The command is pushed to the undo stack
   - The `redo()` method is automatically called, adding the item to the scene

2. User presses Undo:
   - `undo_stack.undo()` is called
   - The `undo()` method of the `AddCommand` is executed
   - The rectangle is removed from the scene

3. User presses Redo:
   - `undo_stack.redo()` is called
   - The `redo()` method of the `AddCommand` is executed
   - The rectangle is added back to the scene