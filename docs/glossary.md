# Glossary

With the complexity of the Blender project comes the need of a common language
with clearly defined terms. The glossary here should help establishing this.

There is another [glossary in the Blender
Manual](https://docs.blender.org/manual/en/latest/glossary/index.html), but it
contains mostly general terms for the computer graphics context. Here the focus
is more on establishing clear technical definitions of the terms used to
communicate user interaction concepts. So it is less broad, more technical and
targeted at a different audience.

## General Terms

_Human Interface Guidelines_, _HIG_
:   !!! quote
        <small>https://en.wikipedia.org/wiki/Human_interface_guidelines</small>

        _Human interface guidelines are software development documents which
        offer application developers a set of recommendations. Their aim is to
        improve the experience for the users by making application interfaces
        more intuitive, learnable, and consistent.  
        [...]  
        This means both applying the same visual design and creating consistent
        access to and behaviour of common elements of the interface – from
        simple ones such as buttons and icons up to more complex constructions,
        such as dialog boxes._

_User Interface_, _UI_
:   !!! quote
        <small>https://en.wikipedia.org/wiki/User_interface</small>

        _In the field of human–computer interaction, the User Interface is the
        space where interactions between humans and machines occur. The goal of
        this interaction is to allow effective operation and control of the
        machine from the human end, whilst the machine simultaneously feeds back
        information that aids the operators’ decision-making process._

_Usability_
: !!! quote
        <small>ISO 9241-11:2018, sec. 3.1.1</small>

        _Extent to which a system, product or service can be used by specified
        users to achieve specified goals with effectiveness, efficiency and
        satisfaction in a specified context of use._

_User Experience_
: !!! quote
        <small>ISO 9241-210:2010, sec. 2.15</small>

        _Person's perceptions and responses resulting from the use and/or
        anticipated use of a product, system or service._
    While usability is focused on effectiveness, efficiency and satisfaction
    ''during'' usage, UX includes more emotional aspects of the usage, but also
    from expected and past usages. So for example the feelings invoked in a
    (potential) user when hearing the word Blender, or when visiting the
    website, are part of the UX. Usability is much more narrow and as such part
    of the entire UX.

_Modal_
:   TODO

## Actions

_Tweak Event_ { #tweak-event }
:   A tweak event is sent when a mouse button was pressed and the mouse moved a
    certain minimum distance before the release event. The exact event type is
    in fact chosen based on the movement direction, allowing different
    operations to execute depending if you dragged north, north-west, west,
    south-west, ...

    Confusingly we also use the term _drag_, but it refers to a slightly
    different action, see [_Drag Event_](#drag-event). Terminology could be
    improved here.

_Drag Event_ { #drag-event }
:   A drag event is sent when a keyboard key was pressed and the mouse moved a
    certain minimum distance before the release event.
    Confusingly we also use the term _tweak_, but it refers to a slightly
    different action, see [_Tweak Event_](#tweak-event). Terminology could be
    improved here.

_Click Event_
:   TODO

_Operator_
:   TODO

_Tool_
:   TODO

## Features

## Patterns
