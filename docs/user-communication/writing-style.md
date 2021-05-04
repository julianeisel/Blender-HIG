!!! check inline end "Guideline Status: Approved"

# Writing Style

## Common Rules

* Use American English.
* Keep text short and to the point.
* Do not use abbreviations like _verts_, _VGroups_, _loc_, _rot_, _scale_
  always use plain words like _vertices_, _vertex groups_, _location_,
  _rotation_, _scale_.
* Do not use English contractions like _aren’t_, _can’t_, etc. Better to keep
  full spelling, _are not_ or _cannot_ are not that much longer, and it helps
  keeping consistent styling over the whole UI.
* Capitalize titles. Entity names are not titles.
    * Entity names are not titles and should __not__ be capitalized.

        !!! example
            Do __not__ capitalize _mesh_, _object_, _vertex group_, etc.
        ??? info "Rationale"
            _Why are entity names no titles?_

            It is often hard to decide if something is an entity name. This
            guideline is definitely arguable, but avoids many fuzzy cases.
<!--
* Entities (like data-blocks) should be title cased, even in tooltips.
  However, this is a fuzzy rule; it's not always clear if something is an
  entity, so it's better not to use such emphasis if you are unsure.
* Terms like Object, Point Cloud, Workspace
 -->
* “Channel" identifiers, like _X_, _Y_, _Z_, _R_, _G_, _B_, etc. are always
  capitalized.
* Do not use implementation specific language.

    !!! example
        * Use _data-block_, __not__ _ID_.
        * Do __not__ use terms like _flag_, _string_, _RNA_, _DNA_.

* Don't use pronouns, such as _you_. This sounds like an accusation towards the
  user.

    !!! example

        === "Good"
            _The mesh is very dense_
        === "Bad"
            _Your mesh is very dense_

* Use the ampersand (_&_) in labels, but _and_ in text (e.g. tooltip
  descriptions).
* Text should generally __not__ contain:
   * Code snippets.
   * Anything with very involved details (e.g. troubleshooting, corner cases
     that might not work, etc.).
* Formatting with new lines (`\n`) and bullet points (`\u2022`) is fine.


## UI labels
* Must use English _MLA_ title case (see [this
  overview](https://titlecaseconverter.com/rules/#MLA), also
  {{Phab("T79589")}}).

    !!! example
        * _Like in This Example_
        * _Set Offset from Cursor_
        * _Alexander and the Terrible, Horrible, No Good, Very Bad Day_
        * _Be Careful What You Wish For_

* An operation that opens a new popup or window should end with an ellipsis
  (_..._).
* Avoid redundancy. E.g. do __not__ use _Enable_, _Activate_ or _Is_ for boolean
  properties.

    !!! example

        === "Good"
            * [ ] _Simple_
            * [ ] _Awesomnizer_
        === "Bad"
            * [ ] _Is Simple_
            * [ ] _Enable Awesomnizer_

