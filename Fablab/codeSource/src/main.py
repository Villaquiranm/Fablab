import sys
from main_controller import *

# Point d'entrée de l'application
def main():
    ctrl = Main_Controller()
    ctrl.main_loop()
    ctrl.on_destroy()





if __name__ == "__main__":
    main()
    sys.exit(0)
