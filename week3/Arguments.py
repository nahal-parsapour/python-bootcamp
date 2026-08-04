# Arguments (*args, **kwargs)

# *args
def total(*args):
    return sum(args)

print("total:", total(1, 2, 3, 4, 5))

# **kwargs
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

user_info(name="John", age=20, city="New York")

# *args + **kwargs
def config(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

config(1, 2, 3, mode="dark", version=6)

# Example: app config
def app_settings(**kwargs):
    defaults = {"theme": "dark", "language": "en", "autosave": True}
    defaults.update(kwargs)
    return defaults

print(app_settings(theme="light", autosave=False))