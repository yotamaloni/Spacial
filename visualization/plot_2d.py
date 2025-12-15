import matplotlib.pyplot as plt

def plot_trusses(trusses):
    plt.figure(figsize=(10, 6))

    for truss in trusses:
        z_vals = [p.z for p in truss.points]
        z_min, z_max = min(z_vals), max(z_vals)

        plt.plot([truss.x, truss.x], [z_min, z_max], "k-", linewidth=2)
        for z in z_vals:
            plt.scatter(truss.x, z, color="red")

    plt.xlabel("X (cm)")
    plt.ylabel("Z (cm)")
    plt.title("Roof Truss Placement")
    plt.grid(True)
    plt.show()
