# Paradigms

## Non Overlapping

The UI should enable you to view all relevant options and tools at a glance,
without the need for pushing or dragging windows around. For that reason we
default to a subdivided window layout. Blender's subdivision works on three
levels;

1. Screens; the entire window enables you to configure workspaces using multiple
editors.
1. Areas; the container of an editor. Editors can each operate similar to a
stand alone editor, like for modeling, painting or scripting. Editors can both
follow Screen level user context (_Active_ or _Selected_) and offer local
context browsing.
1. Regions; every editor allows further subdivision to provide button/menu
headers, toolbars, channel views, and what more is needed to serve its
functionality.

Blender allows to configure multiple windows/screens too, which will be useful
especially for multi-screen setups, animated windows, showing render output or
for some individual cases when an overlap does provide added benefit.

## Non Blocking

Tools and interface options are being designed to not block the user from using
any other parts of Blender. Blender doesn't pop up requesters that require the
user to fill in data before things execute. The UI should stay responsive by all
means, at least for the common and most used operations. When things
exceptionally do block (while rendering or simulations) it should be clearly
indicated and allow an immediate exit.

## Non Modal

User input should remain as consistent and predictable as possible, not changing
commonly used methods (mouse, keyboard) on the fly. Blender's complexity does
allow some inevitable modes though;

1. Editing modes, like mesh modeling, armature posing, particle hair combing, 3D
texture paint. These now are per-object states though, and not editor dependent
or global.
1. Sticky modes, which remain active without user input. Currently this is only
used for the transform tools, to allow more precise and variable inputs
possible.

All other modes should be default "Temporary" modes, immediately ending the
operation when a user stops with actions (like view rotate). This also implies
that input methods like for polygonal knife cuts should only stick to inputting
polygon points when the user actively does something, like holding a modifier
key.

## Select -> Operate

In Blender you first indicate which data you work on, and then what you want to
do. This follows the non-modal principle; there's no active tool mode you need
to set first to be able to use the tool on what you select after. This concept
enables a fast and flexible work flow.

## Operate -> Settings

Blender's new 'Operator' system allows tools to be adjusted after you've used
them. This prevents annoying popups forcing you to decide settings before you
even know how they'd look like.

!!! example

    _Add Primitive UV Sphere_ adds a sphere immediately with previously used
    settings, the toolbar shows which choices you have and redoes the operation
    immediately on changing values.

We will extend this method to all tools, also the more complex ones. Obviously,
in cases where tools heavily depend on Temporary Modes like painting, the tool
settings should be available to adjust before the tool gets used. Also in this
case you will be able to redo the last action with different settings freely.

## Separated Data Properties from Tools

Button windows are now separated in either Property lists/bars or Tool
lists/bars. In this case "Tools" is defined to operate on Screen-wide or
Editor-wide context (selections, activated items). Button views that show
properties will still get the options to edit the data itself, like remove, copy
or add ("operators" too).

## Installation Free

Blender should run "out of the box" for a new install, not requiring root access
to the system either.

## Blender is for Artists

Blender is a tool allowing artists to create content, and not a coders API!
That's quite obvious, but it provides emphasis on functionality for things that
first-most *work* and improve the creation process.  
Of course Blender should be very flexible to configure and extend to serve many
workflow issues, for that high-end and accessible (scripting) APIs have to be
available.
