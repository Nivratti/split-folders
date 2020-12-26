import split

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
split.ratio(
    "E:/python/projects/CartoonGAN/parts/split-folders/demo-images",
    output="output",
    seed=1337,
    ratio=(.8, .1, .1),
    group_prefix=None
) # default values
