# learn about difference between copy & deepcopy

import copy

setting = {
    "theme": "dark",
    "options": {"font": "Arial", "size": 12}
}

shallow = copy.copy(setting)
deep = copy.deepcopy(setting)

shallow["options"]["size"] = "20"

print("Original:", setting)
print("Copy:", shallow)
print("Deep copy:", deep)


# another example
default_config = {
    "window": {"width": 800, "height": 400},
    "security": {"login_required": True}
}

shallow_conf = copy.copy(default_config)
safe_copy = copy.deepcopy(default_config)
safe_copy["window"]["width"] = 600

print("\n\ndefault config:", default_config)
print("shallow config:", shallow_conf)
print("safe_copy config:", safe_copy)

