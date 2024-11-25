import random

# Data konfigurasi
DOSEN = ['Dosen A', 'Dosen B', 'Dosen C']
KELAS = ['Kelas 1', 'Kelas 2', 'Kelas 3']
PELAJARAN = ['Matematika', 'Fisika', 'Kimia']
WAKTU = ['08:00', '10:00', '13:00', '15:00']

# Parameter algoritma genetika
POPULASI_SIZE = 50
GENERASI_MAX = 100
MUTASI_RATE = 0.1

# Representasi individu (jadwal)
def buat_individu():
    return [
        {
            "dosen": random.choice(DOSEN),
            "kelas": random.choice(KELAS),
            "pelajaran": random.choice(PELAJARAN),
            "waktu": random.choice(WAKTU)
        }
        for _ in range(len(PELAJARAN) * len(KELAS))
    ]

# Evaluasi fitness (menghitung jumlah konflik)
def evaluasi_fitness(individu):
    konflik = 0
    for i, jadwal1 in enumerate(individu):
        for j, jadwal2 in enumerate(individu):
            if i >= j:
                continue
            # Konflik waktu di kelas yang sama
            if jadwal1["kelas"] == jadwal2["kelas"] and jadwal1["waktu"] == jadwal2["waktu"]:
                konflik += 1
            # Konflik dosen pada waktu yang sama
            if jadwal1["dosen"] == jadwal2["dosen"] and jadwal1["waktu"] == jadwal2["waktu"]:
                konflik += 1
    return -konflik

# Seleksi (roulette wheel selection)
def seleksi(populasi):
    fitness_total = sum(evaluasi_fitness(individu) for individu in populasi)
    probabilitas = [
        (evaluasi_fitness(individu) / fitness_total) for individu in populasi
    ]
    return random.choices(populasi, weights=probabilitas, k=2)

# Crossover (pertukaran bagian individu)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutasi (modifikasi kecil pada individu)
def mutasi(individu):
    if random.random() < MUTASI_RATE:
        indeks = random.randint(0, len(individu) - 1)
        individu[indeks]["waktu"] = random.choice(WAKTU)
    return individu

# Algoritma Genetika
def algoritma_genetika():
    populasi = [buat_individu() for _ in range(POPULASI_SIZE)]
    for generasi in range(GENERASI_MAX):
        populasi = sorted(populasi, key=evaluasi_fitness, reverse=True)
        if evaluasi_fitness(populasi[0]) == 0:  # Solusi optimal ditemukan
            break
        next_gen = []
        while len(next_gen) < POPULASI_SIZE:
            parent1, parent2 = seleksi(populasi)
            child1, child2 = crossover(parent1, parent2)
            next_gen.append(mutasi(child1))
            next_gen.append(mutasi(child2))
        populasi = next_gen
        print(f"Generasi {generasi + 1}: Fitness terbaik = {evaluasi_fitness(populasi[0])}")
    return populasi[0]

# Menjalankan algoritma
jadwal_terbaik = algoritma_genetika()

# Output jadwal terbaik
for jadwal in jadwal_terbaik:
    print(jadwal)
