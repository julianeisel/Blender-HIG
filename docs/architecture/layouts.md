= Layouts =

== Property Split ==
When to use it, why it makes sense...

== Order of importance ==
[[File:Order of importance.png|frameless|none]]
In general, the most important and most commonly used widgets should be exposed more accessibly. Lesser used widgets should be placed below, or in sub-panels where applicable.
[[File:Checkbox enablers.png|frameless|none]]
In this situation, every setting in the panel depends on the enabling property, so it always accessible in the panel's header.

=== Mode toggling buttons ===
[[File:Mode toggling.png|frameless|none]]
An enum should be exposed with full width at the top of a panel if it meets the following criteria:
# The property plays a significant role in defining the functionality of the panel.
# The name of the property can be inferred from the panel's label. For example, "mode" or "type" properties fit well.
# The text of the choices fits in default width of the UI area for supported screen resolutions.

== Headings ==
Related properties should be grouped with headings where possible. Headings reduce the amount of repetition needed in UI text, meaning it's easier and faster to scan to find what you're looking for.
[[File:Checkbox headings.png|frameless|none]]
This is especially applicable for widgets that contain text, like check-boxes.

== Sub-panels ==
When a label would help give context to multiple buttons, it often makes sense to organize them in a subpanel.
[[File:Sub-panels.png|frameless|none]]
The use of subpanels is generally preferred over a single label button in a row above a block of buttons.

The subpanel title takes only a little more space than a regular label button, it helps organization more, and allows collapsing.

One the other hand, instead of a subpanel with a checkbox in its header and one button inside, it's usually better to align them on the same row with a header.
[[File:Checkbox value.png|frameless|none]]

== Decorators ==
A quick and visual way to animate properties that also provides a visual representation of whether a property is animate-able and its animation state...

== Boxes ==
When to use a box instead of a subpanel...
Box style panels...

== Lists ==
When to use, when to avoid...

Is the same data already represented somewhere else? For instance, collections provide a more integrated way to deal with lists of objects...
