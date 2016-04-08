def VectorAdd(v,w):
	return [v_i + w_i for v_i, w_i in zip(v,w)]

def VectorSubstract(v,w):
	return [v_i - w_i for v_i, w_i in zip(v,w)]

def VectorSum(v,w):
	result = vectors[0]
	for vector in vectors[1:]:
		result = vectorAdd(result, vector)
	return result

def ScalarMultiply(c,v):
	return [c * v_i for v_i in v]

def VectorMean(vectors):
	n = len(vectors)
	return scalarMultiply(1/n,vectorSum(vectors))

def Dot(v,w):
	return sum(v_i * w_i for v_i, w_i in zip(v,w))

def SumOfSquares(v):
	return Dot(v,v)

def Magnitud(v):
	return math.sqrt(SumOfSquares(v))

def SquaredDistance(v,w):
	return SumOfSquares(VectorSubstract(v,w))

def Distance(v,w):
	return Magnitud(VectorSubstract(v,w))