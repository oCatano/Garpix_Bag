from rectpack import newPacker


def packerr(rectangles, bins):
    packer = newPacker()

    # Add the rectangles to packing queue
    for r in rectangles:
        packer.add_rect(*r)

    # Add the bins where the rectangles will be placed
    for b in bins:
        packer.add_bin(*b)

    # Start packing
    packer.pack()

    for abin in packer:
        print(abin.bid)  # Bin id if it has one
        for rect in abin:
            print(rect)

    all_rects = packer.rect_list()
    for rect in all_rects:
        print(rect)
    #  b, x, y, w, h, rid = rect
    return packer


def get_ground_rectangles(towers):
    ground_rectangles = []
    for i in towers:
        ground_rectangles.append([i[0][2][0], i[0][2][1], i[0][3][1]])
    return ground_rectangles


if __name__ == '__main__':
    pass
