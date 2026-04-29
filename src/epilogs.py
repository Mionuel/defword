# \b character prevent click from messing with the formatting
define_examples = """
\b
Examples:
  defword define apple                      # Simple English definition
  defword define orange -o es               # Spanish definition
  defword define calcio -it -o es           # Define an italian word in spanish 
  defword define lemon -o es -o fr -o de    # Translate to multiple languages at once
  defword define banana --no-cache          # Ignore the cached responses for this definition
"""

history_examples = """
\b
Examples:
    defword history            # Show last 5 lookups
    defword history -l n       # Show last n lookups
    defword history -o n       # Show the oldest n lookups
    defword history -d         # Find duplicate lookups    
    defword history --clear    # Wipe the history
"""

cache_examples = """
\b
Examples:
    defword cache -c    # Clear out the cached responses
"""