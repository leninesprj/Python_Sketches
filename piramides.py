# Building a pyramid.
# The pyramid is conditioned to be a pyramid-shaped wall - it's flat:
# each lower layer contains one block more than the layer above.

blocks = int(input("Enter the number of blocks: "))

height = 0
blocks_used=0

# Write your code here.
while blocks_used < blocks:
    if blocks < blocks_used:
        continue
    blocks_used += 1
    height += 1
    blocks_used = blocks_used + height

print("The height of the pyramid:", height)
