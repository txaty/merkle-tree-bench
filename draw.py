from functools import partial

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure


txaty_proof_gen_all = [2352, 5118, 10883, 21324, 42856, 86470, 178578, 358942, 734493, 1520877, 3176012, 6343995, 13685011, 26590701, 55981955, 113353173]
txaty_proof_gen_parallel_all = [19717, 35318, 64952, 111570, 164611, 232532, 322697, 476443, 745326, 1195010, 2040111, 3488114, 6662743, 11398593, 21766570, 41551768]
cbergoon_proof_gen_all = [2502, 6364, 14811, 31017, 70547, 151345, 348514, 874565, 2521951, 7719747, 26018175, 95316725, 355254739, 1383863295, 5416802985, 22259458118]
wealdtech_proof_gen_all = [2269, 5016, 10590, 21840, 45960, 98875, 223991, 550677, 1484146, 4571199, 15548661, 58026425, 225315399, 868889058, 3378439211, 13462518972]
txaty_proof_gen_single = [6153, 9957, 18002, 36752, 70505, 122617, 231687, 378745, 710623, 1412031, 2811667, 5809220, 11246548, 21962968, 43790797, 90331881]
txaty_proof_gen_parallel_single = [21545, 38015, 64679, 105731, 155176, 228758, 344212, 550354, 926139, 1623271, 2881416, 5411962, 10514600, 19331167, 37620382, 74837199]
cbergoon_proof_gen_single = [2436, 5527, 11429, 22837, 45359, 91372, 178967, 355061, 714862, 1442884, 2892521, 5965374, 12383617, 24859955, 48884615, 98070750]
wealdtech_proof_gen_single = [2171, 4543, 9280, 18742, 37733, 76342, 150641, 302570, 605716, 1219518, 2423069, 4854252, 9904926, 19597464, 39747132, 79132694]
txaty_verify = [1236, 1839, 2464, 3066, 3682, 4320, 4910, 5537, 6146, 6814, 7447, 8194, 8788, 9327, 10027, 10586]
cbergoon_verify = [1820, 3802, 5785, 7793, 9887, 12164, 14297, 16959, 20233, 24887, 32211, 45495, 67250, 109546, 194075, 367243]
wealdtech_verify = [1192, 1793, 2415, 3034, 3645, 4265, 4845, 5446, 6087, 6756, 7338, 7922, 8640, 9182, 9762, 10354]

# LEFT_THRESHOLD = 5
# RIGHT_THRESHOLD = 12
# txaty_proof_gen_single = txaty_proof_gen_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]
# txaty_proof_gen_parallel_single = txaty_proof_gen_parallel_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]
# cbergoon_proof_gen_single = cbergoon_proof_gen_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]
# wealdtech_proof_gen_single = wealdtech_proof_gen_single[LEFT_THRESHOLD:RIGHT_THRESHOLD]


x_axis = [i for i in range(1, len(txaty_verify) + 1)]

if __name__ == "__main__":
    # plt.plot(x_axis, proof_gen_times, label="proof_gen_times")
    # plt.plot(x_axis, proof_gen_parallel_times, label="Proof Gen")
    plt.rcParams["font.size"] = "10"
    # plt.fill_between(x_axis, np.log2(txaty_proof_gen_all), "-o", label="txaty/go-merkletree")
    # plt.fill_between(x_axis, np.log2(txaty_proof_gen_parallel_all), "-o", label="txaty/go-merkletree (Parallel)")
    # plt.fill_between(x_axis, np.log2(cbergoon_proof_gen_all), "-o", label="cbergoon/merkletree")
    # plt.fill_between(x_axis, np.log2(wealdtech_proof_gen_all), "-o", label="wealdtech/go-merkletree")
    # plt.semilogy(x_axis, txaty_proof_gen_all, "-o", label="txaty/go-merkletree", color='orange', linewidth=2, base=2)
    # plt.semilogy(x_axis, txaty_proof_gen_parallel_all, "-o", label="txaty/go-merkletree (Parallel)", color='red', linewidth=2, base=2)
    # plt.semilogy(x_axis, cbergoon_proof_gen_all, "-o", label="cbergoon/merkletree", color='green', linewidth=2, base=2)
    # plt.semilogy(x_axis, wealdtech_proof_gen_all, "-o", label="wealdtech/go-merkletree", color='blue', linewidth=2, base=2)    
    # plt.plot(x_axis, txaty_proof_gen_single, "-o", label="txaty/go-merkletree", color='orange', linewidth=2)
    # plt.plot(x_axis, txaty_proof_gen_parallel_single, "-o", label="txaty/go-merkletree (Parallel)", color='red', linewidth=2)
    # plt.plot(x_axis, cbergoon_proof_gen_single, "-o", label="cbergoon/merkletree", color='green', linewidth=2)
    # plt.plot(x_axis, wealdtech_proof_gen_single, "-o", label="wealdtech/go-merkletree", color='blue', linewidth=2)    
    plt.semilogy(x_axis, txaty_verify, "-o", label="txaty/go-merkletree", color='orange', linewidth=2, base=2, zorder=3)
    # plt.plot(x_axis, txaty_proof_gen_parallel_single, "-o", label="txaty/go-merkletree (Parallel)", color='red', linewidth=2)
    plt.semilogy(x_axis, cbergoon_verify, "-o", label="cbergoon/merkletree", color='green', linewidth=2, base=2)
    plt.semilogy(x_axis, wealdtech_verify, "-o", label="wealdtech/go-merkletree", color='blue', linewidth=2, base=2)
    # plt.semilogy(x_axis, txaty_proof_gen_all, "-o", label="txaty/go-merkletree", base=2)
    # plt.semilogy(x_axis, txaty_proof_gen_parallel_all, "-o", label="txaty/go-merkletree (Parallel)",base=2)
    # plt.semilogy(x_axis, cbergoon_proof_gen_all, "-o", label="cbergoon/merkletree",base=2)
    # plt.semilogy(x_axis, wealdtech_proof_gen_all, "-o", label="wealdtech/go-merkletree",base=2)
    plt.ylabel("Time (ns)", fontweight="bold", fontsize=12)
    plt.xlabel("Tree Depth", fontweight="bold", fontsize=12)
    plt.yticks(fontsize=10)
    plt.xticks(fontsize=10)
    plt.grid(True)
    plt.legend(loc='upper left', fontsize=10)
    # plt.title("Proof Generation for All Blocks", fontsize=14)
    plt.title("Proof Verification", fontsize=14)
    # plt.tight_layout()
    # plt.tight_layout()
    # plt.show()
    # plt.savefig("proof_gen.png", dpi=200)
    plt.savefig("proof_verification.png", dpi=200)
