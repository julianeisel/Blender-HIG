# Sidebar Tabs

## Implementation
Tabs are added to applicable toolbars and property regions by defining a "category" in Python while registering the UI panel. For example:

``` python
class panelName(bpy.types.Panel):
    bl_category = "Category Name"
```

## Guidelines
Tabs are designed to reduce region scrolling and to provide better means of organization for relevant tools and settings. The tabs offer a more compact toolbar, but if used incorrectly can also slow down workflow. Thus using tabs correctly is important.

!!! summary
    1. Make as few tabs as possible, use existing tabs where applicable
    1. Remove/reduce need for scrolling
    1. Make tabs workflow oriented, enabling tab usage without excessive tab switching.

Here are guidelines on when and how to use tabs.

### When to use tabs versus panels
Since multiple panels can be added to the same tab, sometimes it's more appropriate to merely create a new panel within an existing tab than to make a new tab.

### When to make a new tab
If the tools being added clearly belong to a specific workflow or category of tools, and that workflow/category does not yet exist, then it's appropriate to create a new tab. For example, by default there is no _Retopology_ tab, but if an addon offers retopology specific tools, then it's okay for that addon to create a _Retopology_ tab.

#### When to use an existing tab
If the tools being added clearly belong to an existing category, such as any tools dealing with object child-parent relations, then they should be added to the existing tab. For the child-parent object relations example, the tools panel would be added to the _Relations_ tab.

#### When to use existing panel or create a new one
Tabs also introduce the ability to pin a panel, making that panel show in all tabs. Due to this, developers must be aware of when and if to create a new panel within a tab.

If the tools/options being added specifically belong to an existing group of operators, then adding them to the current panel is fine. For example, adding a new type of Grease Pencil stroke should be added to the Grease Pencil panel.

However, if the tools/options being added are only partially related, such as a operator to animate grease pencil strokes, then these should be added to a new panel. Doing so allows users to specifically pin the panels they want, without bringing the other related tools along with it.

Another thing to keep in mind when determining whether to create a new panel or not, length. If adding new operators to an existing panel causes the toolbar to become overly tall, then it's probably necessary/appropriate to create a new panel. Creating a new panel allows part of the toolbar to be collapsed, thus saving space and reducing scroll.

### How addons should use tabs
Addons should make an effort to only create new tabs when necessary. For example, if an addon merely adds a couple operators for creating custom primitives meshes, then the addon should use the existing _Create_ tab.

If an addon provides a much more extensive set of tools/options, then it's appropriate to create a new tab for the addon. All addons should work to fit common naming schemes and such, though, so that multiple similar addons may share the same tab. Tabs work the same way as addon categories. If an identical, or very similar category already exists, then make sure the spelling is identical so as to not create duplicates.
