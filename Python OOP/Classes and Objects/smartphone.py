class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.is_on = False
        self.apps = []

    def power(self):
        self.is_on = not self.is_on

    def install(self, app, memory_decrease):
        if not self.is_on:
            return f"Turn on your phone to install {app}"

        if memory_decrease > self.memory:
            return f"Not enough memory to install {app}"

        self.memory -= memory_decrease
        self.apps.append(app)
        return f"Installing {app}"

    def status(self):
        apps_count = len(self.apps)
        return f"Total apps: {apps_count}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
