from hero import *

# --------------------------MAIN-------------------------
myhero1 = Hero("Vurdalak", 5, "Ork")
myhero2 = Hero("Aleksander", 4, "Human")

myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
myhero1.set_health (60)
myhero1.show_hero()