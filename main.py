# Custom macros. Restart server after editing (`mkdocs serve`).

def define_env(env):
  "Hook function"

  '''
   Create an developer.blender.org link. E.g. {{Phab("T1234")}} becomes a
   markdown link to https://developer.blender.org/T1234.
   :param disply_str: The text to display (instead of whatever string was passed
                      as first parameter).
  '''
  @env.macro
  def Phab(num:str, display_str:str = None):
    if not display_str:
      display_str = num
    return "[" + display_str + "](https://developer.blender.org/" + num + ")"