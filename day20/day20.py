#!/usr/bin/env python3


IMG_SIDE = 12
TILE_SIDE = 10

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

def configurations(borders):
    '''
    borders: list of 4 strings representing the 4 borders of a tile.

    return: list of all possible configurations of borders after
    transforms (rotations are always clockwise):
    0: as is
    1: flip horizontally
    2: flip vertically
    3: rotate 90° then flip horizontally
    4: rotate 90° then flip vertically
    5: rotate 90°
    6: rotate 180°
    7: rotate 270°
    '''
    flips = lambda x: (
        [x[0][::-1], x[3], x[2][::-1], x[1]],
        [x[2], x[1][::-1], x[0], x[3][::-1]]
    )
    arrs = []
    for n in range(4):
        arrs.append(borders.copy())
        if not n:
            arrs.extend(flips(borders))
        borders = [borders[3][::-1], borders[0], borders[1][::-1], borders[2]]
        if not n:
            arrs.extend(flips(borders))
    return arrs


def dfs(lines_up, current, conf, image, pos, tiles):
    '''
    Build up the image dictionary in a recursive way, memorizing position,
    id and configuration (applied transformations) for every tile in the map.
    If there are inconsistencies, empty the image dictionary and return.
    '''
    if not image or len(image) == len(tiles):
        return
    for k_nbr, v_nbr in lines_up[current].items():
        way = v_nbr[conf][1]
        if way == 0:
            nbr_pos = pos - IMG_SIDE
        elif way == 1:
            nbr_pos = pos + 1
        elif way == 2:
            nbr_pos = pos + IMG_SIDE
        elif way == 3:
            nbr_pos = pos - 1
        assert 0 <= nbr_pos < IMG_SIDE ** 2
        nbr_conf = v_nbr[conf][2]
        if image.get(nbr_pos, (k_nbr,nbr_conf)) != (k_nbr, nbr_conf):
            image = {}
            return
        else:
            try:
                image[nbr_pos]
                continue
            except KeyError:
                image[nbr_pos] = (k_nbr, nbr_conf)
                dfs(lines_up, k_nbr, nbr_conf, image, nbr_pos, tiles)


def arrange(tile, conf, side=None):
    if not conf:
        return tile
    elif conf == 1:
        return flipH(tile)
    elif conf == 2:
        return flipV(tile)
    elif conf == 3:
        return flipH(rotate(tile, side))
    elif conf == 4:
        return flipV(rotate(tile, side))
    elif conf == 5:
        return rotate(tile, side)
    elif conf == 6:
        return rotate(rotate(tile, side), side)
    elif conf == 7:
        return rotate(rotate(rotate(tile, side), side), side)

def flipH(tile):
    return [ row[::-1] for row in tile ]

def flipV(tile):
    i, j = 0, len(tile) - 1
    while i < j:
        tile[i], tile[j] = tile[j], tile[i]
        i += 1
        j -= 1
    return tile

def rotate(tile, side = None):
    if side is None:
        side = TILE_SIDE
    new = [['' for n in range(side)] for n in range(side)]
    for y, row in enumerate(tile):
        for x, c in enumerate(tile[y]):
            new[x][abs(y - (side - 1))] = tile[y][x]
    for i, row in enumerate(new):
        new[i] = ''.join(row)
    return new


def search_monsters(monster, w, h, img):
    found = 0
    for y, row in enumerate(img):
        if y + h > len(img):
            return found
        for x, c in enumerate(row):
            if x + w > len(row):
                break
            if all(n == '#' for i in range(len(monster)) for n in img[y+monster[i][0]][x+monster[i][1]]):
                found += 1
    return found


def run():
    with open('input.txt') as fh:
        ts = fh.read().split('\n\n')
    tiles = {}
    for t in ts:
        if t.startswith('Tile '):
            tiles[int(t[5:9])] = t[11:].split('\n')

    # borders = { tile_id: [all possible tile's border configurations], ... }
    # border configuration = [border north, east, south, west] for every possible flip and/or rotation
    # every configuration has its own index (see the function 'configurations')
    borders = {}
    for id_, tile in tiles.items():
        n = tile[0]
        s = tile[-1]
        w = ''.join((tile[n][0] for n in range(len(tile))))
        e = ''.join((tile[n][-1] for n in range(len(tile))))
        borders[id_] = configurations([n, e, s, w])

    # lines_up = {
    #     tile_id: {
    #         neighbour_id: [(tile_configuration_index, tile_border_index, neighbour_configuration_index), ... ]
    #     },
    #     ...
    # }
    lines_up = {}
    for id_, possible_bords in borders.items():
        for i, bords in enumerate(possible_bords):
            for j, b in enumerate(bords):
                for other, other_poss_bords in borders.items():
                    if other != id_:
                        for k, other_bords in enumerate(other_poss_bords):
                            if b == other_bords[(j + 2) % len(other_bords)]:
                                try:
                                    lines_up[id_][other].append((i, j, k))
                                except KeyError:
                                    try:
                                        lines_up[id_][other] = [(i, j, k)]
                                    except KeyError:
                                        lines_up[id_] = {other: [(i, j, k)]}
           
    # luckily, every possible neighbour is a neighbour, so the corner tiles
    # all have just 2 neighbours, while all other tiles have more
    corners = [k for k, v in lines_up.items() if len(v) == 2]

    r = 1
    for c in corners:
        r *= c
    print(r)  # first answer

    # to visualize corner tiles's ids, their neighbours and how they can be combined.
    # for c in corners:
    #     print(f'\n\n\n{c}\n')
    #     for k, v in lines_up[c].items():
    #         print(f'{k}: {v}\n')
    #     print('\n')
    #     for neighbours in lines_up[c]:
    #         print(f'{neighbours}\n')
    #         for k, v in lines_up[neighbours].items():
    #             print(f'{k}: {v}\n')

    # Begin to rebuild the image: we arbitrarily start in a corner, find
    # the neighbours's ids and which sides of the starting tile can
    # be aligned with the neighbours in the various configurations
    start = corners[0]
    start_nbrs = list(lines_up[start])
    start_borders = list(
        map(
            lambda x, y: {x[1], y[1]},
            lines_up[start][start_nbrs[0]], lines_up[start][start_nbrs[1]]
        )
    )
    # iterate over all possible border configurations of the starting tile
    # and for each one start a depth first search in the tiles's graph.
    # the idea is that there should be only one possible way to correctly
    # wedge in all the tiles in a specific chain of tile's configurations
    # (or, if there are more, they are equivalent)
    for i, start_bords in enumerate(start_borders):
        # img_map = {
        #     integer_coords: (tile_id, tile_configuration_index),
        #     ...
        # }
        img_map = {}
        # find the position of the starting tile based on which borders are
        # aligned to the neighbours's ones in the current configuration
        # (every start_bords corresponds to a different starting tile's
        # configuration)
        if start_bords == {1, 2}:
            start_pos = 0
        elif start_bords == {2, 3}:
            start_pos = IMG_SIDE - 1
        elif start_bords == {0, 1}:
            start_pos = (IMG_SIDE - 1) * IMG_SIDE
        elif start_bords == {3, 0}:
            start_pos = (IMG_SIDE - 1) * IMG_SIDE + IMG_SIDE - 1
        img_map[start_pos] = (start, i)

        dfs(lines_up, start, i, img_map, start_pos, tiles)
        # if the map is complete, we're good to go, otherwise let's try
        # the next configuration of the starting tile
        if len(img_map) == len(tiles):
            break

    assert len(img_map) == len(tiles)

    # sort the tiles and apply to each one the appropriate transforms
    img = [
        arrange(tiles[id_], conf) for n in range(IMG_SIDE**2) for id_, conf in (img_map[n],)
    ]
    # prune the tiles's borders
    for i, tile in enumerate(img):
        img[i] = [ row[1:-1] for row in tile[1:-1] ]

    # build a list of strings that hold the entire image
    image = []
    for n in range(IMG_SIDE):
        for y in range(TILE_SIDE-2):
            image.append(''.join(img[m + n*IMG_SIDE][y] for m in range(IMG_SIDE)))
   
    # to see the image as a whole:
    # print('\n'.join(image))

    # Uff, that took some time! Now we are ready to look for the monsters...
    m_w = len(monster[0])
    m_h = len(monster)
    m = []
    for y in range(m_h):
        for x in range(m_w):
            if monster[y][x] == '#':
                m.append((y, x))
    monsters_found = []
    for n in range(8):
        monsters_found.append(search_monsters(m, m_w, m_h, arrange(image, n, len(image))))
    monsters = max(monsters_found) * len(m)

    print(sum(row.count('#') for row in image) - monsters)  # second answer


if __name__ == '__main__':
    run()
