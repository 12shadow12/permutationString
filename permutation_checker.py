def permutation_check(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        a = sorted(str1)
        str1 = " ".join(a)
        print(str1)
        b = sorted(str2)
        str2 = " ".join(b)
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return False
        return True
        
print(permutation_check("dog", "god"))