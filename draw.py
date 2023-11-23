import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# txaty_proof_gen_all = [2352, 5118, 10883, 21324, 42856, 86470, 178578, 358942, 734493, 1520877, 3176012, 6343995, 13685011, 26590701, 55981955, 113353173]
# txaty_proof_gen_parallel_all = [19717, 35318, 64952, 111570, 164611, 232532, 322697, 476443, 745326, 1195010, 2040111, 3488114, 6662743, 11398593, 21766570, 41551768]
# cbergoon_proof_gen_all = [2502, 6364, 14811, 31017, 70547, 151345, 348514, 874565, 2521951, 7719747, 26018175, 95316725, 355254739, 1383863295, 5416802985, 22259458118]
# wealdtech_proof_gen_all = [2269, 5016, 10590, 21840, 45960, 98875, 223991, 550677, 1484146, 4571199, 15548661, 58026425, 225315399, 868889058, 3378439211, 13462518972]
# txaty_proof_gen_single = [6153, 9957, 18002, 36752, 70505, 122617, 231687, 378745, 710623, 1412031, 2811667, 5809220, 11246548, 21962968, 43790797, 90331881]
# txaty_proof_gen_parallel_single = [21545, 38015, 64679, 105731, 155176, 228758, 344212, 550354, 926139, 1623271, 2881416, 5411962, 10514600, 19331167, 37620382, 74837199]
# cbergoon_proof_gen_single = [2436, 5527, 11429, 22837, 45359, 91372, 178967, 355061, 714862, 1442884, 2892521, 5965374, 12383617, 24859955, 48884615, 98070750]
# wealdtech_proof_gen_single = [2171, 4543, 9280, 18742, 37733, 76342, 150641, 302570, 605716, 1219518, 2423069, 4854252, 9904926, 19597464, 39747132, 79132694]
# txaty_verify = [1236, 1839, 2464, 3066, 3682, 4320, 4910, 5537, 6146, 6814, 7447, 8194, 8788, 9327, 10027, 10586]
# cbergoon_verify = [1820, 3802, 5785, 7793, 9887, 12164, 14297, 16959, 20233, 24887, 32211, 45495, 67250, 109546, 194075, 367243]
# wealdtech_verify = [1192, 1793, 2415, 3034, 3645, 4265, 4845, 5446, 6087, 6756, 7338, 7922, 8640, 9182, 9762, 10354]
txaty_proof_gen_all = [1827, 3981, 8220, 16647, 33713, 67603, 137337, 274263, 554707, 1131566, 2332726, 5010428,
                       10694700, 21508258, 46088669, 96713810, 220444567, 475300155]
txaty_proof_gen_parallel_all = [15324, 27150, 52932, 101029, 148554, 208522, 296577, 409535, 605298, 949092, 1588533,
                                2756362, 5044146, 8638146, 16154967, 31140110, 66998718, 139837808]
cbergoon_proof_gen_all = [1953, 4979, 11601, 24292, 56130, 119258, 267440, 649713, 1911629, 5690264, 18825167, 67826628,
                          250663994, 979589732, 3789822708, 15638533893, 66456101971, 359397309304]
wealdtech_proof_gen_all = [1779, 3926, 8349, 17191, 36421, 78194, 178620, 441342, 1226537, 3793499, 12983764, 47180416,
                           179594119, 703603668, 2775491740, 10986580866, 43808882206, 187204778186]
txaty_proof_gen_single = [3504, 7585, 10035, 20291, 37800, 74347, 149056, 259569, 505783, 999594, 1993451, 3966579,
                          8131812, 16196440, 32640968, 65971359, 135357700, 276682365]
txaty_proof_gen_parallel_single = [9177, 21083, 42763, 82212, 125903, 172305, 242156, 344661, 487312, 687187, 1022766,
                                   1771015, 2917188, 5309760, 10490605, 22495208, 50515227, 125372482]
cbergoon_proof_gen_single = [1849, 4302, 9009, 18059, 36123, 71146, 141386, 279580, 563511, 1134745, 2267595, 4790391,
                             9598958, 18968197, 37658031, 76950032, 154022972, 313622148]
wealdtech_proof_gen_single = [1664, 3554, 7242, 14609, 29598, 58742, 117850, 235527, 471669, 944040, 1901234, 3789042,
                              7767292, 15373027, 30654346, 62830339, 125100856, 253123392]
txaty_verify = [946.7, 1426, 1929, 2408, 2867, 3336, 3820, 4300, 4812, 5264, 5808, 6338, 6820, 7165, 7674, 8199, 8706,
                9330]
cbergoon_verify = [1403, 2969, 4539, 6166, 7817, 9405, 11208, 13303, 15799, 19221, 24782, 34269, 50164, 83995, 146504,
                   274354, 524420, 1351583]
wealdtech_verify = [918.1, 1402, 1875, 2356, 2830, 3300, 3810, 4283, 4758, 5215, 5702, 6198, 6791, 7188, 7625, 8120,
                    8590, 9175]

# LEFT_THRESHOLD = 5
# RIGHT_THRESHOLD = 12
# txaty_proof_gen_single = txaty_proof_gen_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]
# txaty_proof_gen_parallel_single = txaty_proof_gen_parallel_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]
# cbergoon_proof_gen_single = cbergoon_proof_gen_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]
# wealdtech_proof_gen_single = wealdtech_proof_gen_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]


x_axis = [i for i in range(1, len(txaty_verify) + 1)]


def plot_proof_gen_all():
    ax = plt.figure().gca()  # get current axis
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.rcParams["font.size"] = "10"
    plt.semilogy(x_axis, cbergoon_proof_gen_all, "-o", label="cbergoon/merkletree", base=2, color="green")
    plt.semilogy(x_axis, wealdtech_proof_gen_all, "-o", label="wealdtech/go-merkletree", base=2, color="blue")
    plt.semilogy(x_axis, txaty_proof_gen_all, "-o", label="txaty/go-merkletree", base=2, color="orange")
    plt.semilogy(x_axis, txaty_proof_gen_parallel_all, "-o", label="txaty/go-merkletree (Parallel)", base=2,
                 color="red")
    plt.ylabel("Time (ns)", fontweight="bold", fontsize=12)
    plt.xlabel("Tree Depth", fontweight="bold", fontsize=12)
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True)
    plt.legend(loc='upper left', fontsize=10)
    plt.title("Proof Generation for All Blocks", fontsize=14)
    plt.savefig("proof_gen_all.png", dpi=200)


def plot_proof_gen_single():
    ax = plt.figure().gca()  # get current axis
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.rcParams["font.size"] = "10"
    plt.semilogy(x_axis, cbergoon_proof_gen_single, "-o", label="cbergoon/merkletree", base=2, color="green")
    plt.semilogy(x_axis, wealdtech_proof_gen_single, "-o", label="wealdtech/go-merkletree", base=2, color="blue")
    plt.semilogy(x_axis, txaty_proof_gen_single, "-o", label="txaty/go-merkletree", base=2, color="orange")
    plt.semilogy(x_axis, txaty_proof_gen_parallel_single, "-o", label="txaty/go-merkletree (Parallel)", base=2,
                 color="red")
    plt.ylabel("Time (ns)", fontweight="bold", fontsize=12)
    plt.xlabel("Tree Depth", fontweight="bold", fontsize=12)
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True)
    plt.legend(loc='upper left', fontsize=10)
    plt.title("Proof Generation for a Single Block", fontsize=14)
    plt.savefig("proof_gen_single.png", dpi=200)


def plot_proof_verification():
    ax = plt.figure().gca()  # get current axis
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.rcParams["font.size"] = "10"
    plt.semilogy(x_axis, cbergoon_verify, "-o", label="cbergoon/merkletree", color='green', linewidth=2, base=2)
    plt.semilogy(x_axis, wealdtech_verify, "-o", label="wealdtech/go-merkletree", color='blue', linewidth=2, base=2)
    plt.semilogy(x_axis, txaty_verify, "-o", label="txaty/go-merkletree", color='orange', linewidth=2, base=2, zorder=3)
    plt.ylabel("Time (ns)", fontweight="bold", fontsize=12)
    plt.xlabel("Tree Depth", fontweight="bold", fontsize=12)
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True)
    plt.legend(loc='upper left', fontsize=10)
    plt.title("Proof Verification", fontsize=14)
    plt.savefig("proof_verification.png", dpi=200)


if __name__ == "__main__":
    plot_proof_gen_all()
    plot_proof_gen_single()
    plot_proof_verification()
