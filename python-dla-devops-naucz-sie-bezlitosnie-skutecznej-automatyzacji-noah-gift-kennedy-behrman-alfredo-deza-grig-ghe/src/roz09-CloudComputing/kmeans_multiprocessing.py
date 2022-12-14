from multiprocessing import Pool
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans
import time

def do_kmeans(n_samples):
    """klasteryzacja KMeans na wygenerowanych danych"""

    X,_ = make_blobs(n_samples, centers=3, n_features=10,
                random_state=0)
    kmeans = KMeans(n_clusters=3)
    t0 = time.time()
    kmeans.fit(X)
        print(f"Obliczenia dla klastra KMeans zakończono w czasie {time.time()-t0}")

def main():
    """Uruchomienie wszystkiego"""

    count = 10
    t0 = time.time()
    with Pool(count) as p:
        p.map(do_kmeans, [100000,100000,100000,100000,100000,
                    100000,100000,100000,100000,100000])
    
    print(f"Wykonano {count} obliczeń klastrów KMeans w łącznym czasie: {time.time()-t0}")


if __name__ == "__main__":
    main()