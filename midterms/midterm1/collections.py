cans_int = int(input("Enter number of cans: "))

boxes_int = cans_int // (6 * 4)
packs_int = (cans_int // 6) % 4
extra_cans = cans_int % 6

print(f"{boxes_int} boxe(s), {packs_int} pack(s), and {extra_cans} can(s)")