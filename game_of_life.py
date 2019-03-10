import numpy as np
import matplotlib.pyplot as plt
from IPython.display import HTML
import matplotlib.pyplot as plt
import matplotlib.animation as animation


seeds = {
    "diehard": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 1],
    ],
    "boat": [[1, 1, 0], [1, 0, 1], [0, 1, 0]],
    "r_pentomino": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
    "pentadecathlon": [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    "beacon": [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1]],
    "acorn": [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 0, 1, 1, 1]],
    "spaceship": [[0, 0, 1, 1, 0], [1, 1, 0, 1, 1], [1, 1, 1, 1, 0], [0, 1, 1, 0, 0]],
    "block_switch_engine": [
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
    ],
    "infinite": [
        [1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
    ],
}


def survival(x: int, y: int, universe: np.array) -> int:
    """
    input:
        x: x coordinate of cell in the universe
        y: y coordinate of cell in the universe
        universe: universe of cells
    returns:
        int: the new value of cell at (x,y) 
    """
    num_neighbours = (
        np.sum(universe[max(x - 1, 0) : x + 2, max(y - 1, 0) : y + 2]) - universe[x, y]
    )
    # The rules of life
    if universe[x, y] == 1 and num_neighbours < 2:
        return 0  # Dead from starvation
    elif universe[x, y] == 1 and (num_neighbours == 2 or num_neighbours == 3):
        return 1  # Continue living
    elif universe[x, y] == 1 and num_neighbours > 3:
        return 0  # Dead from overcrowding
    elif universe[x, y] == 0 and num_neighbours == 3:
        return 1
    else:
        return 0


def generation(universe: np.array) -> np.array:
    """
    Get the next generation of universe
    input:
        universe: old universe
    returns:
        new_universe: new universe with new cell
    """
    new_universe = np.copy(universe)
    # Apply the survival function to get the new cell value
    for i in range(universe.shape[0]):
        for j in range(universe.shape[1]):
            new_universe[i, j] = survival(i, j, universe)
    return new_universe


def generate_first_universe(
    universe_shape: tuple = (20, 10),
    seed_position: tuple = (0, 0),
    seed: list = seeds["diehard"],
) -> np.array:
    universe = np.zeros(shape=universe_shape)
    x_start, y_start = seed_position
    seed_array = np.array(seed)
    x_end, y_end = x_start + seed_array.shape[0], y_start + seed_array.shape[1]
    # Finally attach the seed to the universe at star and end position
    universe[x_start:x_end, y_start:y_end] = seed_array
    return universe

def matplot_animation(first_universe: np.array,cmap="Purples",uni_cycle:int=30):
    universe = first_universe
    quality = 200
    fig = plt.figure(dpi=200)
    plt.axis("off")
    ims = []
    for i in range(uni_cycle):
        ims.append((plt.imshow(generate_first_universe(), cmap=cmap),))
        universe = generation(universe)
    im_ani = animation.ArtistAnimation(fig,ims, interval=200, blit=True)
    
    return im_ani

if __name__ == "__main__":
    pl_anm = matplot_animation(generate_first_universe())
    HTML(pl_anm.to_jshtml())

   
