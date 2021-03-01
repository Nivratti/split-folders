import split

# Split with a ratio.
# To only split into training and validation set, set a tuple to `ratio`, i.e, `(.8, .2)`.
split.ratio(
    "dataset_sample/",
    output="output",
    seed=1337,
    ratio=(.6, .2, .2),
    move=False,
    group_prefix=None
) # default values
