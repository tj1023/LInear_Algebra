import random


# 벡터간 거리 return 함수
def distance(a, b):
    dis = 0
    for i in range(5):
        dis += (int(a[i]) - int(b[i])) ** 2
    return dis ** (1 / 2)


# 각 벡터를 가까운 벡터 클러스터에 할당
def assign_to_cluster():
    clusters_index = [0] * k
    clusters = [[] for _ in range(k)]
    for vector in vectors:
        min_dis = distance(vector, center_vectors[0])
        select_i = 0
        for j in range(k):
            if min_dis > distance(vector, center_vectors[j]):
                min_dis = distance(vector, center_vectors[j])
                select_i = j
        clusters[select_i].append(vector)
        clusters_index[select_i] += 1
    return clusters, clusters_index


# 중심점 업데이트
def update_center_vectors():
    for i in range(k):
        mean = [0] * 5
        if clusters_index[i] == 0:
            continue
        for j in range(clusters_index[i]):
            for l in range(5):
                mean[l] += int(clusters[i][j][l]) / clusters_index[i]
        center_vectors[i] = mean


# 입력 받기
filename, k, iterations = input().split()
k = int(k)
iterations = int(iterations)
f = open(filename, 'r')

# 초기화
vectors = []
while True:
    str = f.readline()
    if not str:
        break
    vectors.append(str.split())
clusters = [[] for _ in range(k)]
center_vectors = []
for i in range(k):
    center_vectors.append(vectors[random.randrange(0, len(vectors))])

# 반복
count = 0
for i in range(iterations):
    actual_iteration = i + 1
    prev_centers = center_vectors.copy()
    clusters, clusters_index = assign_to_cluster()
    update_center_vectors()
    if prev_centers == center_vectors:
        count += 1
    else:
        count = 0
    if count >= 10:
        break

# 출력
print("# of actual iteration : ", actual_iteration)
print("representative : ", end=' ')
for i in range(k):
    print("(", end=' ')
    for j in range(5):
        if j == 4:
            print("%.1f" % center_vectors[i][j], end=' ')
        else:
            print("%.1f" % center_vectors[i][j], end=', ')
    if i == k - 1:
        print(")")
    else:
        print("),", end=' ')
for i in range(k):
    print("# of vectors for cluster %d : %d" % (i + 1, clusters_index[i]))
