#!usr/bin/env python2

from gimpfu import *


def guide_grid(image, drawable, hspace, vspace, percent):
    pdb.gimp_image_undo_group_start(image)
    imageHeight = pdb.gimp_image_height(image)
    imageWidth = pdb.gimp_image_width(image)
    if (percent == 1):
        # Recalculate pixel spacing by percentage.
        hspace = int(hspace * (imageHeight * 0.01))
        vspace = int(vspace * (imageWidth * 0.01))
    # Input validity check.
    if (hspace <= 0 or vspace <= 0):
        return
    # Calculate the number of guides.
    hGuides = int(imageHeight/hspace)
    vGuides = int(imageWidth/vspace)
    # Add guides to image edges.
    for i in range(2):
        pdb.gimp_image_add_hguide(image, i * imageHeight)
        pdb.gimp_image_add_vguide(image, i * imageWidth)
    # Add the horizontal guides.
    for i in range(1, hGuides):
        pdb.gimp_image_add_hguide(image, i * hspace)
    # Add the vertical guides.
    for i in range(1, vGuides):
        pdb.gimp_image_add_vguide(image, i * vspace)
    pdb.gimp_image_undo_group_end(image)


register(
    "python_fu_guide_grid",
    "Guide Grid",
    "Creates a grid of guides with specified spacing.",
    "Theodoros Balasis", "", "2019",
    "Guide Grid",
    "*",
    [
        (PF_IMAGE, "image", "Input Image", None),
        (PF_DRAWABLE, "drawable", "Input Layer", None),
        (PF_INT, "hspace", "Horizontal Spacing", 1),
        (PF_INT, "vspace", "Vertical Spacing", 1),
        (PF_BOOL, "percent", "By percent?", 0)
    ],
    [],
    guide_grid,
    menu="<Image>/Image/Guides"
)

main()
