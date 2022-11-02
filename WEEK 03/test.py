# k-medoid clustering
start_time = time.time()

kmd = pyclust.KMedoids(n_clusters=4, n_trials=50)
kmd.fit(ksample.values)

end_time = time.time()

# print processing time
print('처리시간 : ', end_time - start_time)