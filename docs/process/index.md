# General

The UI module overlaps with all other modules. The communication during UI
development has to be particularly good to avoid conflicts.  
Most points here are good practice for other areas as well.

* For non-trivial changes, create a design task as explained
  [below](#design-task).
* For bigger projects (rule of thumb: takes longer than one release cycle to
  develop), create an {{Phab("project/", "own project")}}.  
  The UI project should link to it in the navigation menu and the roadmap. Make
  sure the project visibility is set to _Public (No Login Required)_.
* When committing a change, link to all design tasks and patches in the commit
  description. __For every change the rationales should be explicit__ or at
  least easy to reach via the commit description, no matter how obvious they
  seem to be.
* Immediately after committing and pushing a change, add it to the [release
  notes](https://wiki.blender.org/wiki/Reference/Release_Notes) if needed.  
  For bigger changes this should already be prepared prior to pushing.

## Submitting Patches

For patches that need UI team involvement:

 * __Always__ add the _User Interface_ project tag.
 * If you want the patch to be reviewed for a certain release:
    * Add a _TO DO_ task and add the patch revision(s) as _Related Object_. For
      example: {{Phab("T80338")}}, {{Phab("T77824")}}.
    * Notify the UI team about this. They have to discuss if this is a
      reasonable target and will assign it to the release column on the
      workboard if so.
    * As long as the task is not in the release column, it's __not__ a release
      target for the UI team. Check with the team again if it appears like they
      didn't act on your request.


## Design Task

* A design task must always mention the motivation or rationale for a proposed
  change.
* A design task for non-trivial changes must always contain a definition of
  done. That is, it must be clear at which point it's fine for the developers to
  move on to other projects as opposed to doing further iterations.

## Definition of Done

User interface development typically happens in an iterative fashion. There
never is a clear finish line, but at some point it has to be drawn.

## Controversial Changes

## Dealing with Feedback
