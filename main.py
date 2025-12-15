import json
from config import TRUSS_SPACING_CM
from model.roof import Roof
from model.truss import TrussGenerator
from visualization.plot_2d import plot_trusses

def main():
    with open("roof.json", "r") as f:
        data = json.load(f)

    roof = Roof(data)
    generator = TrussGenerator(roof, TRUSS_SPACING_CM)
    trusses = generator.generate()

    plot_trusses(trusses)

if __name__ == "__main__":
    main()
