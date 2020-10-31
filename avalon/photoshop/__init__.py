"""Public API

Anything that isn't defined here is INTERNAL and unreliable for external use.

"""

from .pipeline import (
    ls,
    Creator,
    install,
    containerise
)

from .workio import (
    file_extensions,
    has_unsaved_changes,
    save_file,
    open_file,
    current_file,
    work_root,
)

from .lib import (
    launch,
    app,
    Dispatch,
    maintained_selection,
    maintained_visibility,
    get_layers_in_document,
    get_layers_in_layers,
    get_selected_layers,
    group_selected_layers,
    imprint,
    read,
    get_com_objects,
    import_smart_object,
    replace_smart_object,
    show,
    execute_in_main_thread,
    select_layers
)

__all__ = [
    # pipeline
    "ls",
    "Creator",
    "install",
    "containerise",

    # workfiles
    "file_extensions",
    "has_unsaved_changes",
    "save_file",
    "open_file",
    "current_file",
    "work_root",

    # lib
    "launch",
    "app",
    "Dispatch",
    "maintained_selection",
    "maintained_visibility",
    "get_layers_in_document",
    "get_layers_in_layers",
    "get_selected_layers",
    "group_selected_layers",
    "imprint",
    "read",
    "get_com_objects",
    "import_smart_object",
    "replace_smart_object",
    "show",
    "execute_in_main_thread",
    "select_layers"
]
