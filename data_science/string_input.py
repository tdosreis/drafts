def input_strings(*arrays,ref_array):
    
    assert _length_sum(arrays) == len(ref_array)
    
    ref = ref_array.copy()

    d = _gen_dictionary(*arrays,ref_array=ref_array)
    
    refs = list(d.keys())
    
    for r in refs:
        ref[ref==r] = d.get(r)
    
    return ref

def _length_sum(arr):
    if len(arr)== 1:
        return len(arr[0])
    else:
        return len(arr[0]) + _length_sum(arr[1:])
    
# _length_sum = lambda l: len(l[0]) + _length_sum(l[1:]) if l else 0

def _gen_dictionary(*arrays,ref_array):
    index = list(set(ref_array))
    return {i: a for (a,i) in zip(arrays,index)}
