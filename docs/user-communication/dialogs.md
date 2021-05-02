# Dialogs

## Modal Dialogs

Modal dialogs are popups that interrupt the user's work and _require_ the user to take action. The window showing the dialog does not allow other interaction meanwhile.

* Modal dialogs are not great design and should be avoided. If users face them often they will get the habit of just "clicking them away", possibly resulting in destructive actions.
* In some cases they are however acceptable as a way to prevent serious errors. Typically if there's the potential of data-loss.
* A modal dialog should not be the only way to prevent data-loss. Users may still just "click away" a confirmation dialog without much thinking.

!!! example
    * Auto-saves and _Recover Last Session_ can be used to prevent data-loss when users accidentally closed Blender without saving, ignoring the confirmation prompt.
    * When a user overrides files in Blender's File Browser, the overridden files are moved to the system trash by default, despite the confirmation prompt _(Note: Not actually the case at the time of writing)_.
* If there is no such secondary way to recover from errors, a modal dialog must not have a default action (the action that happens when pressing ++enter++, typically visualized by a button with a blue background).

## References

* Aza Raskin, [_Never Use a Warning When you Mean Undo_](https://alistapart.com/article/neveruseawarning/)
* Jakob Nielsen, [_Confirmation Dialogs Can Prevent User Errors — If Not Overused_](https://www.nngroup.com/articles/confirmation-dialog/)
* Jef Raskin, The Humane Interface (ISBN 0-201-37937-6)
