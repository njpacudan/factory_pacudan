import store
import random
random.shuffle(store.vehicle)
random.shuffle(store.brand)
random.shuffle(store.truckwheels)
i = store.vehicle[0]
y = store.truckwheels[0]
z = store.brand[0]
if i == "motor":
    wheels = 2
elif i == "car":
    wheels = 4
elif i == "truck":
    wheels = y
