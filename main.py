import os, datetime, numpy
from sys import maxsize
from itertools import permutations

os.system('cls')
# berat_barang = [3, 1, 3, 4, 2]
# nilai_barang = [2, 2, 4, 5, 3]

def grafik():
    gambar = '''
    ..                                            .
    --                                           --
    --                                           --
    --                                           --
    --                                           --
    --                                           --
    -- -- ----.   ----- -----. ----- .----- ----- -- .-.
    --... -----. ..-.-- --..-- --.-- --..-. --.-- --.--
    ----  -- --. .-. -- --  -- -- -- .-  -. -. .- ----
    ---   -- --.  .---- --  -- -.-   ..---. -.    -.-.
    -.-   -- --. ..---- --  --  .--  ----.. -.    -.-.
    ----  -- --. .-. -- --  -- ...-- --  -. -. .. ----
    ----. -- --. .-. -- --  -- -. -- --  -. -. -- --...
    -- -- -- --. ..---- ----.. ----- ----.. ----- -- --
    -. .- -. --. .----- -----  ----. .----. ----- .- .-.
                        --
                        --
                        --   -----.    ------ .----. .----.
                            ..---..    ------ ------ ------
                            ...  -.      --  .-.  -- --  --
                            ... ...      --  .-.  -- --  --
                            ...  ..      --   --  -. --  --
                            ...          --   ...    --  --
                             -.----.     --    -..   --  --
                             ----.-.     --     --.  ------
                            ... .-.      --     .--. -----.
                            ... ...      --   .. ..- --
                            ... ...      --  ..-  -- --
                            ... ...      --  .-.  -- --
                            .......      --  .--..-- --
                            .-----.      --   -----. --
                             .....       ..    ....  ..'''    
    print(gambar)

def inputknapsack(berat_barang, nilai_barang, rumah):
    try:
        banyak_rumah = int(input("Banyak Rumah: "))
        kapasitas = int(input("Kapasitas Muatan: "))
        abjad = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for x in range(banyak_rumah):
            if x != 0:
                list_data(berat_barang, nilai_barang, rumah)
            weight = int(input(f"Masukkan berat barang rumah ke {x + 1} [Kg]: "))
            value = int(input(f"Masukkan nilai barang rumah ke {x + 1} [Rp]: "))
            berat_barang.append(weight)
            nilai_barang.append(value)
            rumah.append(abjad[x])
        list_data(berat_barang, nilai_barang, rumah)
        n = input('Tekan ENTER untuk melanjutkan: ')
        inputtravelling(berat_barang, nilai_barang, banyak_rumah, rumah, kapasitas)
    except ValueError:
        print("\n[ Inputan Salah ]")
        n = input('Tekan ENTER untuk kembali: ')

def list_data(berat_barang, nilai_barang, rumah):
    os.system('cls')
    print("[ Data Rumah ]\n")
    print("Nama Rumah   ~~>", rumah)
    print("Berat Barang ~~>", berat_barang)
    print("Nilai Barang ~~>", nilai_barang)


def inputtravelling(berat_barang, nilai_barang, banyak_rumah, rumah, kapasitas):
    try:
        graph_lite = []
        graph_lite = numpy.zeros(dtype=int, shape=(banyak_rumah, banyak_rumah))
        
        for a in range(banyak_rumah-1):
            for b in range(a+1, banyak_rumah):
                jarakab = int(input(f"Masukan jarak rumah {rumah[a]} menuju {rumah[b]}: "))
                graph_lite[a, b] = jarakab
                graph_lite[b, a] = jarakab

        graph = []
        for i in graph_lite:
            data = []
            for j in i:
                data.append(j)
            graph.append(data)

        n = input('Tekan ENTER: ')
        print('\n===> GRAPH <===')
        for i in graph:
            print(i)
        n = input('Tekan ENTER untuk menuju knapsack: ')
        knapsack(berat_barang, nilai_barang, rumah, kapasitas, graph, tabel = [])
    except ValueError:
        print("\n[ Inputan Salah ]")
        n = input('Tekan ENTER untuk kembali: ')

def knapsack(berat_barang, nilai_barang, rumah, kapasitas, graph, tabel):
    cap = kapasitas
    for baris in range(len(nilai_barang)+1):
        baris_sementara = []
        for kolom in range(cap+1):
            if baris == 0:
                baris_sementara.append(0)
            else:
                if berat_barang[baris-1] > kolom:
                    baris_sementara.append(tabel[baris-1][kolom])
                else:
                    nilai = max(tabel[baris-1][kolom], nilai_barang[baris-1]+tabel[baris-1][kolom - berat_barang[baris-1]])
                    baris_sementara.append(nilai)
        tabel.append(baris_sementara)

    list_data(berat_barang, nilai_barang, rumah)
    print('\n[ Tabel Knapsack ]\n')
    for i in tabel:
        print(i)
    maksimal = tabel[-1][-1]
    print("\nNilai max =", maksimal)
    n = input("~~> Tekan ENTER: ")
    house_seeker(berat_barang, nilai_barang, rumah, graph, tabel, maksimal)

def house_seeker(berat_barang, nilai_barang, rumah, graph, tabel, maksimal):
    import os
    os.system('cls')
    berat_barang_baru, nilai_barang_baru, rumah_baru = [], [], []
    i, j = 1, 1
    nilai = 0    

    while nilai != tabel[-1][-1]:
        if tabel[-i][-j] > tabel[-i-1][-j]:
            nilai += nilai_barang[-i]
            berat_barang_baru.append(berat_barang[-i])
            nilai_barang_baru.append(nilai_barang[-i])
            rumah_baru.append(rumah[-i])
            j += berat_barang[-i]
        i += 1

    berat_barang = berat_barang_baru[::-1]
    nilai_barang = nilai_barang_baru[::-1]
    rumah = rumah_baru[::-1]
    print('[ List Rumah Yang Terpilih ]\n')
    print('Nama Rumah  ', rumah)
    print('Berat Barang', berat_barang)
    print('Nilai Barang', nilai_barang)
    n = input('Tekan ENTER untuk menuju TSP: ')
    change_graph(rumah, graph, nilai_barang, berat_barang, maksimal)

def change_graph(rumah, graph, nilai_barang, berat_barang, maksimal):
    os.system('cls')
    graph_baru = []
    abjad = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    target = []

    for i in range(len(abjad)):
        if abjad[i] in rumah:
            target.append(i)

    for i in range(len(graph)):
        if i in target:
            baris = []
            for j in range(len(graph)):
                if j in target:
                    baris.append(graph[i][j])
            graph_baru.append(baris)

    print('===> [ GRAPH LAMA ] <===')
    for i in graph:
        print(i)
    print('\n===> [ GRAPH BARU ] <===')
    for i in graph_baru:
        print(i)
    n = input('Tekan ENTER: ')
    travellingSalesmanProblem(graph_baru, rumah, nilai_barang, berat_barang, maksimal)


def travellingSalesmanProblem(graph, rumah, nilai_barang, berat_barang, maksimal, start = 0):
    verteks = []
    for i in range(len(rumah)):
        if i != start:
            verteks.append(i)

    lintasan_minimum = maxsize
    lintasan = []
    permutasi = permutations(verteks)

    for i in permutasi:
        minimum_saat_ini = 0
        detail = [rumah[x] for x in i]
        detail.insert(0, rumah[0])
        detail.append(rumah[0])
        print('lintasan node: ', detail)
        k = start
        for j in i:
            minimum_saat_ini += graph[k][j]
            print(f'Jarak rumah [{rumah[k]}] ke rumah [{rumah[j]}]', graph[k][j])
            k = j
        minimum_saat_ini += graph[k][start]
        print(f'Jarak rumah [{rumah[k]}] ke rumah [{rumah[start]}]', graph[k][start])
        print('Total lintasan adalah: ', minimum_saat_ini)
        print(f'Selesai\n')
        if minimum_saat_ini < lintasan_minimum:
            lintasan_minimum = minimum_saat_ini
            lintasan = detail
    print('\nLintasan node:', lintasan)
    print('Jarak Minimum  ~~>', lintasan_minimum)
    s = input("Tekan Enter Untuk Melihat Hasil Akhir")
    list_data(berat_barang, nilai_barang, rumah)
    print("Nilai Maksimal ~~>", maksimal)
    print('\nLintasan node:', lintasan)
    print('Jarak Minimum  ~~>', lintasan_minimum)
    n = input('Klik ENTER untuk kembali ke menu utama: ')


while True:
    os.system('cls')
    grafik()
    print(f">>>{str(datetime.date.today()): ^14}<<<")
    print("1. Gunakan Program\n0. Keluar Program\n")
    opsi = input("Pilih Opsi Program : ")
    if opsi == '1':
        inputknapsack(berat_barang = [], nilai_barang = [], rumah = [])
    elif opsi == '0':
        exit()
    else: 
        print(" [ Inputan Salah ] ") 
        n = input(" ~~> Tekan ENTER untuk kembali ")