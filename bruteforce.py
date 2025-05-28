from itertools import permutations
import numpy as np
import time

# Matriks jarak antar kota (contoh 5 kota)
distance_matrix = np.array([
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
])

cities = list(range(len(distance_matrix)))

def tsp_bruteforce():
    start_time = time.time()
    min_distance = float('inf')
    best_route = None
    
    for perm in permutations(cities[1:]):  # Fix kota awal (0)
        route = (0,) + perm + (0,)
        distance = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))
        
        if distance < min_distance:
            min_distance = distance
            best_route = route
    
    end_time = time.time()
    return best_route, min_distance, end_time - start_time

def tsp_nearest_neighbor():
    start_time = time.time()
    unvisited = set(cities)
    current_city = 0  # Mulai dari kota pertama
    unvisited.remove(current_city)
    route = [current_city]
    total_distance = 0
    
    while unvisited:
        nearest_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        total_distance += distance_matrix[current_city][nearest_city]
        route.append(nearest_city)
        unvisited.remove(nearest_city)
        current_city = nearest_city
    
    # Kembali ke kota awal
    total_distance += distance_matrix[current_city][0]
    route.append(0)
    
    end_time = time.time()
    return route, total_distance, end_time - start_time

# Menjalankan algoritma
brute_route, brute_distance, brute_time = tsp_bruteforce()
nn_route, nn_distance, nn_time = tsp_nearest_neighbor()

print(f"Brute Force: Rute {brute_route}, Jarak {brute_distance}, Waktu {brute_time:.6f} detik")
print(f"Nearest Neighbor: Rute {nn_route}, Jarak {nn_distance}, Waktu {nn_time:.6f} detik")
