def get_key(frame, event, arg):
    if event in {"c_call", "c_return"}:
        return f"{arg.__module__}.{arg.__name__}"
    else:
        module_name = frame.f_globals.get("__name__", "")
        class_name = ""
        if "self" in frame.f_locals:
            class_name = type(frame.f_locals["self"]).__name__
        elif "cls" in frame.f_locals:
            class_name = frame.f_locals["cls"].__name__
        func_name = frame.f_code.co_name if frame and frame.f_code and frame.f_code.co_name else None
        return f"{module_name}.{class_name}.{func_name}"
