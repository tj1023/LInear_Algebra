import numpy as np


# norm 값 계산해주는 함수
def norm(vector):
    square_sum = 0
    for element in vector:
        square_sum += element ** 2
    return square_sum ** (1 / 2)


# 파일에서 벡터 읽기
f = open("inputfile.txt", 'r')
vectors = []
while True:
    line = f.readline()
    if not line:
        break
    vectors.append(list(map(int, line.split())))
vectors = np.array(vectors)

# Gram-Schmidt 알고리즘
# 1. 첫 벡터 정규화 -> 직교 벡터에 추가
orthogonal_vectors = [vectors[0] / norm(vectors[0])]

# 2. 이후 벡터들 직교성 유지하도록 조정
for i in range(1, len(vectors)):
    vector_i = vectors[i]  # 현재 벡터
    for vector_j in orthogonal_vectors:  # 앞서 처리한 벡터들
        vector_i = vector_i - np.dot(vector_i, vector_j) * vector_j  # 직교 벡터 구하기
    if norm(vector_i) > 0:  # linearly dependent 인 경우 norm 값이 0이므로 제외
        orthogonal_vectors.append(vector_i / norm(vector_i))  # 정규화하여 직교 벡터에 추가

# linearly independent / dependent 판단
if len(orthogonal_vectors) == len(vectors):
    print("linearly independent")
else:
    print("linearly dependent")

# 확인한 벡터 수
print("Number of vectors checked : ", len(orthogonal_vectors))
