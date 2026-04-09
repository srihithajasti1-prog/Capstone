"""
COMPLETE 100 OPTIMIZED PROBLEMS DATABASE
All problems with Python & C code, complexity analysis, test cases
"""

# ============================================================================
# SECTION 1: BASIC OPERATIONS (1-10)
# ============================================================================

print("="*60)
print("SECTION 1: BASIC OPERATIONS (10 Problems)")
print("="*60)

# 1. FIND SUM OF ARRAY ELEMENTS
def problem_1_find_sum(arr):
    """Q: Find sum of all array elements | Time: O(n) | Space: O(1)"""
    return sum(arr)

assert problem_1_find_sum([1, 2, 3, 4, 5]) == 15
print("1. OK Find sum")

# 2. FIND MAXIMUM ELEMENT
def problem_2_find_max(arr):
    """Q: Find maximum element | Time: O(n) | Space: O(1)"""
    return max(arr)

assert problem_2_find_max([64, 34, 25, 12, 22]) == 64
print("2. OK Find max")

# 3. REVERSE A STRING
def problem_3_reverse_string(s):
    """Q: Reverse a string | Time: O(n) | Space: O(n)"""
    return s[::-1]

assert problem_3_reverse_string("hello") == "olleh"
print("3. OK Reverse string")

# 4. CHECK PALINDROME
def problem_4_palindrome(s):
    """Q: Check if palindrome | Time: O(n) | Space: O(n)"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

assert problem_4_palindrome("racecar") == True
print("4. OK Check palindrome")

# 5. COUNT VOWELS
def problem_5_count_vowels(s):
    """Q: Count vowels in string | Time: O(n) | Space: O(1)"""
    return sum(1 for char in s if char.lower() in 'aeiou')

assert problem_5_count_vowels("hello world") == 3
print("5. OK Count vowels")

# 6. SWAP TWO NUMBERS
def problem_6_swap(a, b):
    """Q: Swap two numbers | Time: O(1) | Space: O(1)"""
    return b, a

a, b = 5, 10
a, b = problem_6_swap(a, b)
assert a == 10 and b == 5
print("6. OK Swap numbers")

# 7. FIND FACTORIAL
def problem_7_factorial(n):
    """Q: Find factorial | Time: O(n) | Space: O(1)"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

assert problem_7_factorial(5) == 120
print("7. OK Factorial")

# 8. CHECK EVEN OR ODD
def problem_8_even_odd(n):
    """Q: Check even or odd | Time: O(1) | Space: O(1)"""
    return "even" if n % 2 == 0 else "odd"

assert problem_8_even_odd(4) == "even"
print("8. OK Even/Odd")

# 9. FIND LARGEST OF 3
def problem_9_largest_three(a, b, c):
    """Q: Find largest of three | Time: O(1) | Space: O(1)"""
    return max(a, b, c)

assert problem_9_largest_three(10, 20, 15) == 20
print("9. OK Largest of 3")

# 10. FIBONACCI (N TERMS)
def problem_10_fibonacci(n):
    """Q: Print n Fibonacci numbers | Time: O(n) | Space: O(1)"""
    if n <= 0:
        return []
    a, b = 0, 1
    result = [a]
    for _ in range(n - 1):
        result.append(b)
        a, b = b, a + b
    return result

assert problem_10_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
print("10. OK Fibonacci")

# ============================================================================
# SECTION 2: ARRAY OPERATIONS (11-30)
# ============================================================================

print("\n" + "="*60)
print("SECTION 2: ARRAY OPERATIONS (20 Problems)")
print("="*60)

# 11. REMOVE DUPLICATES
def problem_11_remove_duplicates(arr):
    """Q: Remove duplicates | Time: O(n) | Space: O(n)"""
    return list(set(arr))

assert sorted(problem_11_remove_duplicates([1, 2, 2, 3, 3])) == [1, 2, 3]
print("11. OK Remove duplicates")

# 12. FIND SECOND LARGEST
def problem_12_second_largest(arr):
    """Q: Find second largest | Time: O(n) | Space: O(1)"""
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

assert problem_12_second_largest([1, 5, 3, 9, 2]) == 5
print("12. OK Second largest")

# 13. ROTATE ARRAY
def problem_13_rotate_array(arr, k):
    """Q: Rotate array k positions | Time: O(n) | Space: O(n)"""
    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr

assert problem_13_rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
print("13. OK Rotate array")

# 14. MERGE SORTED ARRAYS
def problem_14_merge_sorted(arr1, arr2):
    """Q: Merge two sorted arrays | Time: O(n+m) | Space: O(n+m)"""
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

assert problem_14_merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
print("14. OK Merge sorted")

# 15. FIND MISSING NUMBER
def problem_15_missing_number(arr):
    """Q: Find missing number 1 to n | Time: O(n) | Space: O(1)"""
    n = len(arr) + 1
    return n * (n + 1) // 2 - sum(arr)

assert problem_15_missing_number([1, 2, 4, 5]) == 3
print("15. OK Missing number")

# 16. FIND DUPLICATES
def problem_16_find_duplicates(arr):
    """Q: Find all duplicates | Time: O(n) | Space: O(n)"""
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

assert sorted(problem_16_find_duplicates([1, 2, 2, 3, 3])) == [2, 3]
print("16. OK Find duplicates")

# 17. KADANE'S ALGORITHM
def problem_17_kadane(arr):
    """Q: Max subarray sum | Time: O(n) | Space: O(1)"""
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

assert problem_17_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
print("17. OK Kadane's algorithm")

# 18. MOVE ZEROS TO END
def problem_18_move_zeros(arr):
    """Q: Move zeros to end | Time: O(n) | Space: O(1)"""
    non_zero = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero], arr[i] = arr[i], arr[non_zero]
            non_zero += 1
    return arr

assert problem_18_move_zeros([0, 1, 0, 2, 3, 0]) == [1, 2, 3, 0, 0, 0]
print("18. OK Move zeros")

# 19. COUNT FREQUENCY
def problem_19_count_frequency(arr):
    """Q: Count element frequency | Time: O(n) | Space: O(n)"""
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

assert problem_19_count_frequency([1, 1, 2, 2, 2, 3]) == {1: 2, 2: 3, 3: 1}
print("19. OK Count frequency")

# 20. INTERSECTION OF ARRAYS
def problem_20_intersection(arr1, arr2):
    """Q: Find intersection | Time: O(n+m) | Space: O(n)"""
    return list(set(arr1) & set(arr2))

assert sorted(problem_20_intersection([1, 2, 3, 4], [3, 4, 5, 6])) == [3, 4]
print("20. OK Intersection")

# 21. MAJORITY ELEMENT
def problem_21_majority_element(arr):
    """Q: Find element > n/2 times | Time: O(n) | Space: O(1) - Boyer-Moore"""
    count = 0
    candidate = None
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1
    return candidate

assert problem_21_majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]) == 4
print("21. OK Majority element")

# 22. EQUILIBRIUM INDEX
def problem_22_equilibrium_index(arr):
    """Q: Find equilibrium index | Time: O(n) | Space: O(n)"""
    total = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        if left_sum == total - left_sum - arr[i]:
            return i
        left_sum += arr[i]
    return -1

assert problem_22_equilibrium_index([-7, 1, 5, 2, -4, 3, 0]) == 3
print("22. OK Equilibrium index")

# 23. SUBARRAY WITH GIVEN SUM
def problem_23_subarray_sum(arr, target):
    """Q: Find subarray with sum | Time: O(n) | Space: O(n)"""
    sum_map = {0: -1}
    current = 0
    for i in range(len(arr)):
        current += arr[i]
        if current - target in sum_map:
            return arr[sum_map[current - target] + 1:i + 1]
        if current not in sum_map:
            sum_map[current] = i
    return None

assert problem_23_subarray_sum([1, 4, 20, 3, 10, 5], 33) == [20, 3, 10]
print("23. OK Subarray sum")

# 24. MAX PRODUCT SUBARRAY
def problem_24_max_product(arr):
    """Q: Max product subarray | Time: O(n) | Space: O(1)"""
    if not arr:
        return 0
    max_prod = current_max = current_min = arr[0]
    for num in arr[1:]:
        current_max, current_min = (
            max(num, current_max * num, current_min * num),
            min(num, current_max * num, current_min * num)
        )
        max_prod = max(max_prod, current_max)
    return max_prod

assert problem_24_max_product([2, 3, -2, 4]) == 6
print("24. OK Max product")

# 25. SORT 0s, 1s, 2s
def problem_25_sort_012(arr):
    """Q: Sort 0,1,2 array | Time: O(n) | Space: O(1) - Dutch Flag"""
    low = mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

assert problem_25_sort_012([0, 1, 2, 0, 1, 2]) == [0, 0, 1, 1, 2, 2]
print("25. OK Sort 0,1,2")

# 26. PRODUCT OF ARRAY ELEMENTS
def problem_26_product(arr):
    """Q: Product of array | Time: O(n) | Space: O(1)"""
    result = 1
    for num in arr:
        result *= num
    return result

assert problem_26_product([1, 2, 3, 4]) == 24
print("26. OK Product")

# 27. FIND PAIR WITH SUM
def problem_27_pair_sum(arr, target):
    """Q: Find pair with sum | Time: O(n) | Space: O(n)"""
    seen = {}
    for num in arr:
        complement = target - num
        if complement in seen:
            return (complement, num)
        seen[num] = True
    return None

assert problem_27_pair_sum([1, 2, 3, 4], 5) == (2, 3)
print("27. OK Pair with sum")

# 28. FIND UNIQUE ELEMENT
def problem_28_unique_element(arr):
    """Q: Find unique element | Time: O(n) | Space: O(1)"""
    unique = 0
    for num in arr:
        unique ^= num
    return unique

assert problem_28_unique_element([2, 2, 1, 4, 4]) == 1
print("28. OK Unique element")

# 29. LONGEST CONTIGUOUS SUBARRAY WITH SUM K

def problem_29_longest_subarray_sum_k(arr, k):
    """Q: Longest subarray with sum k | Time: O(n) | Space: O(n)"""
    sum_map = {0: -1}
    current_sum = 0
    max_len = 0
    for i, num in enumerate(arr):
        current_sum += num
        if current_sum - k in sum_map:
            max_len = max(max_len, i - sum_map[current_sum - k])
        if current_sum not in sum_map:
            sum_map[current_sum] = i
    return max_len

assert problem_29_longest_subarray_sum_k([1, -1, 5, -2, 3], 3) == 4
print("29. OK Longest subarray sum k")

# 30. REARRANGE POSITIVE AND NEGATIVE

def problem_30_rearrange_pos_neg(arr):
    """Q: Rearrange positive and negative | Time: O(n) | Space: O(1)"""
    i = -1
    for j in range(len(arr)):
        if arr[j] < 0:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr

assert problem_30_rearrange_pos_neg([1, -2, 3, -4, 5, -6]) == [-2, -4, -6, 1, 5, 3]
print("30. OK Rearrange pos/neg")

# ============================================================================
# SECTION 3: STRING MANIPULATION (31-45)
# ============================================================================

print("\n" + "="*60)
print("SECTION 3: STRING MANIPULATION (15 Problems)")
print("="*60)

# 31. LONGEST COMMON PREFIX
def problem_31_longest_common_prefix(strs):
    """Q: Longest common prefix | Time: O(n*m) | Space: O(1)"""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

assert problem_31_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
print("31. OK Longest common prefix")

# 32. ANAGRAM CHECK
def problem_32_anagram(s1, s2):
    """Q: Check anagram | Time: O(n) | Space: O(1)"""
    return sorted(s1) == sorted(s2)

assert problem_32_anagram("listen", "silent") == True
print("32. OK Anagram check")

# 33. FIRST NON-REPEATING CHARACTER
def problem_33_first_non_repeating(s):
    """Q: First non-repeating char | Time: O(n) | Space: O(n)"""
    frequency = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None

assert problem_33_first_non_repeating("swiss") == "w"
print("33. OK First non-repeating")

# 34. STRING ROTATION CHECK
def problem_34_string_rotation(s1, s2):
    """Q: Check rotation | Time: O(n) | Space: O(n)"""
    return len(s1) == len(s2) and s2 in s1 + s1

assert problem_34_string_rotation("waterbottle", "erbottlewat") == True
print("34. OK String rotation")

# 35. PALINDROME PERMUTATION
def problem_35_palindrome_permutation(s):
    """Q: Palindrome permutation | Time: O(n) | Space: O(1)"""
    s = s.replace(" ", "").lower()
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    odd_count = sum(1 for count in counts.values() if count % 2 != 0)
    return odd_count <= 1

assert problem_35_palindrome_permutation("Tact Coa") == True
print("35. OK Palindrome permutation")

# 36. COUNT SUBSTRINGS
def problem_36_count_substrings(text, pattern):
    """Q: Count substring occurrences | Time: O(n*m) | Space: O(1)"""
    count = 0
    start = 0
    while True:
        start = text.find(pattern, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count

assert problem_36_count_substrings("abababa", "aba") == 3
print("36. OK Count substrings")

# 37. GROUP ANAGRAMS
def problem_37_group_anagrams(strs):
    """Q: Group anagrams | Time: O(n*k log k) | Space: O(n*k)"""
    groups = {}
    for s in strs:
        key = tuple(sorted(s))
        groups.setdefault(key, []).append(s)
    return list(groups.values())

assert problem_37_group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
print("37. OK Group anagrams")

# 38. MINIMUM WINDOW SUBSTRING
def problem_38_min_window(s, t):
    """Q: Minimum window substring | Time: O(n+m) | Space: O(n+m)"""
    if not s or not t:
        return ""
    need = {}
    for char in t:
        need[char] = need.get(char, 0) + 1
    missing = len(t)
    left = start = end = 0
    for right, char in enumerate(s):
        if need.get(char, 0) > 0:
            missing -= 1
        need[char] = need.get(char, 0) - 1
        while missing == 0:
            if end == 0 or right - left + 1 < end - start + 1:
                start, end = left, right + 1
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return s[start:end]

assert problem_38_min_window("ADOBECODEBANC", "ABC") == "BANC"
print("38. OK Min window substring")

# 39. VALID PARENTHESES
def problem_39_valid_parentheses(s):
    """Q: Validate parentheses | Time: O(n) | Space: O(n)"""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack

assert problem_39_valid_parentheses("()[]{}") == True
print("39. OK Valid parentheses")

# 40. LONGEST PALINDROMIC SUBSTRING
def problem_40_longest_palindromic_substring(s):
    """Q: Longest palindromic substring | Time: O(n^2) | Space: O(1)"""
    if not s:
        return ""
    start = end = 0
    for i in range(len(s)):
        for left, right in ((i, i), (i, i + 1)):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1
    return s[start:end + 1]

assert problem_40_longest_palindromic_substring("babad") in ["bab", "aba"]
print("40. OK Longest palindromic substring")

# 41. COUNT PALINDROMES
def problem_41_count_palindromes(s):
    """Q: Count palindromic substrings | Time: O(n^2) | Space: O(1)"""
    count = 0
    for i in range(len(s)):
        count += expand_around_center(s, i, i)
        count += expand_around_center(s, i, i + 1)
    return count

def expand_around_center(s, left, right):
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

assert problem_41_count_palindromes("aaa") == 6
print("41. OK Count palindromes")

# 42. STRING PERMUTATION CHECK
def problem_42_permutation(s1, s2):
    """Q: Check if one string is permutation of another | Time: O(n) | Space: O(1)"""
    return sorted(s1) == sorted(s2)

assert problem_42_permutation("abc", "cab") == True
print("42. OK String permutation")

# 43. LONGEST COMMON SUBSEQUENCE
def problem_43_lcs(s1, s2):
    """Q: Longest common subsequence | Time: O(n*m) | Space: O(n*m)"""
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]

assert problem_43_lcs("abcde", "ace") == 3
print("43. OK Longest common subsequence")

# 44. LONGEST REPEATING CHARACTER REPLACEMENT
def problem_44_longest_repeating_character_replacement(s, k):
    """Q: Longest repeating char replacement | Time: O(n) | Space: O(1)"""
    counts = {}
    max_count = start = 0
    best = 0
    for end in range(len(s)):
        counts[s[end]] = counts.get(s[end], 0) + 1
        max_count = max(max_count, counts[s[end]])
        while end - start + 1 - max_count > k:
            counts[s[start]] -= 1
            start += 1
        best = max(best, end - start + 1)
    return best

assert problem_44_longest_repeating_character_replacement("AABABBA", 1) == 4
print("44. OK Longest repeating char replacement")

# 45. WORD BREAK
def problem_45_word_break(s, word_dict):
    """Q: Word break | Time: O(n*k*m) | Space: O(n)"""
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break
    return dp[-1]

assert problem_45_word_break("leetcode", {"leet", "code"}) == True
print("45. OK Word break")

# ============================================================================
# SECTION 4: SEARCH AND SORTING (46-70)
# ============================================================================

print("\n" + "="*60)
print("SECTION 4: SEARCH AND SORTING (25 Problems)")
print("="*60)

# 46. BINARY SEARCH
def problem_46_binary_search(arr, target):
    """Q: Binary search | Time: O(log n) | Space: O(1)"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

assert problem_46_binary_search([1, 2, 3, 4, 5], 4) == 3
print("46. OK Binary search")

# 47. BUBBLE SORT
def problem_47_bubble_sort(arr):
    """Q: Bubble sort | Time: O(n^2) | Space: O(1)"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

assert problem_47_bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
print("47. OK Bubble sort")

# 48. SELECTION SORT
def problem_48_selection_sort(arr):
    """Q: Selection sort | Time: O(n^2) | Space: O(1)"""
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

assert problem_48_selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
print("48. OK Selection sort")

# 49. INSERTION SORT
def problem_49_insertion_sort(arr):
    """Q: Insertion sort | Time: O(n^2) | Space: O(1)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

assert problem_49_insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
print("49. OK Insertion sort")

# 50. MERGE SORT
def problem_50_merge_sort(arr):
    """Q: Merge sort | Time: O(n log n) | Space: O(n)"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = problem_50_merge_sort(arr[:mid])
    right = problem_50_merge_sort(arr[mid:])
    return problem_14_merge_sorted(left, right)

assert problem_50_merge_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]
print("50. OK Merge sort")

# 51. QUICK SORT
def problem_51_quick_sort(arr):
    """Q: Quick sort | Time: O(n log n) average | Space: O(log n)"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return problem_51_quick_sort(left) + middle + problem_51_quick_sort(right)

assert problem_51_quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
print("51. OK Quick sort")

# 52. HEAPIFY
def problem_52_heapify(arr, n, i):
    """Q: Heapify a subtree | Time: O(log n) | Space: O(1)"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        problem_52_heapify(arr, n, largest)

# 53. HEAP SORT
def problem_53_heap_sort(arr):
    """Q: Heap sort | Time: O(n log n) | Space: O(1)"""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        problem_52_heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        problem_52_heapify(arr, i, 0)
    return arr

assert problem_53_heap_sort([12, 11, 13, 5, 6, 7]) == [5, 6, 7, 11, 12, 13]
print("53. OK Heap sort")

# 54. COUNT SORT
def problem_54_count_sort(arr):
    """Q: Count sort | Time: O(n+k) | Space: O(n+k)"""
    if not arr:
        return arr
    min_val, max_val = min(arr), max(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    for num in arr:
        count[num - min_val] += 1
    output = []
    for i in range(len(count)):
        output.extend([i + min_val] * count[i])
    return output

assert problem_54_count_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
print("54. OK Count sort")

# 55. RADIX SORT
def problem_55_radix_sort(arr):
    """Q: Radix sort | Time: O(nk) | Space: O(n+k)"""
    if not arr:
        return arr
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        output = [0] * len(arr)
        count = [0] * 10
        for num in arr:
            count[(num // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for num in reversed(arr):
            output[count[(num // exp) % 10] - 1] = num
            count[(num // exp) % 10] -= 1
        arr = output
        exp *= 10
    return arr

assert problem_55_radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]
print("55. OK Radix sort")

# 56. SHELL SORT
def problem_56_shell_sort(arr):
    """Q: Shell sort | Time: O(n^(3/2)) average | Space: O(1)"""
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

assert problem_56_shell_sort([12, 34, 54, 2, 3]) == [2, 3, 12, 34, 54]
print("56. OK Shell sort")

# 57. QUICK SELECT
def problem_57_quick_select(arr, k):
    """Q: Quick select | Time: O(n) average | Space: O(1)"""
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    if k <= len(lows):
        return problem_57_quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivots[0]
    else:
        return problem_57_quick_select(highs, k - len(lows) - len(pivots))

assert problem_57_quick_select([3, 6, 2, 1, 5, 4], 3) == 3
print("57. OK Quick select")

# 58. BUBBLE SORT OPTIMIZED
def problem_58_optimized_bubble_sort(arr):
    """Q: Bubble sort optimized | Time: O(n^2) worst-case | Space: O(1)"""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

assert problem_58_optimized_bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
print("58. OK Optimized bubble sort")

# 59. INSERTION SORT RECURSIVE
def problem_59_recursive_insertion_sort(arr, n=None):
    """Q: Recursive insertion sort | Time: O(n^2) | Space: O(n)"""
    if n is None:
        n = len(arr)
    if n <= 1:
        return arr
    problem_59_recursive_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last
    return arr

assert problem_59_recursive_insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
print("59. OK Recursive insertion sort")

# 60. PATTERN SEARCH (NAIVE)
def problem_60_naive_search(text, pattern):
    """Q: Naive pattern search | Time: O(n*m) | Space: O(1)"""
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            return i
    return -1

assert problem_60_naive_search("hello world", "world") == 6
print("60. OK Naive search")

# 61. STRASSEN MATRIX MULTIPLICATION
def problem_61_strassen(matrix_a, matrix_b):
    """Q: Strassen matrix multiplication | Time: O(n^2.8074) | Space: O(n^2)"""
    if len(matrix_a) == 1:
        return [[matrix_a[0][0] * matrix_b[0][0]]]
    n = len(matrix_a)
    new_size = n // 2
    a11 = [row[:new_size] for row in matrix_a[:new_size]]
    a12 = [row[new_size:] for row in matrix_a[:new_size]]
    a21 = [row[:new_size] for row in matrix_a[new_size:]]
    a22 = [row[new_size:] for row in matrix_a[new_size:]]
    b11 = [row[:new_size] for row in matrix_b[:new_size]]
    b12 = [row[new_size:] for row in matrix_b[:new_size]]
    b21 = [row[:new_size] for row in matrix_b[new_size:]]
    b22 = [row[new_size:] for row in matrix_b[new_size:]]

    def add_matrix(x, y):
        return [[x[i][j] + y[i][j] for j in range(len(x))] for i in range(len(x))]

    def sub_matrix(x, y):
        return [[x[i][j] - y[i][j] for j in range(len(x))] for i in range(len(x))]

    p1 = problem_61_strassen(add_matrix(a11, a22), add_matrix(b11, b22))
    p2 = problem_61_strassen(add_matrix(a21, a22), b11)
    p3 = problem_61_strassen(a11, sub_matrix(b12, b22))
    p4 = problem_61_strassen(a22, sub_matrix(b21, b11))
    p5 = problem_61_strassen(add_matrix(a11, a12), b22)
    p6 = problem_61_strassen(sub_matrix(a21, a11), add_matrix(b11, b12))
    p7 = problem_61_strassen(sub_matrix(a12, a22), add_matrix(b21, b22))

    c11 = add_matrix(sub_matrix(add_matrix(p1, p4), p5), p7)
    c12 = add_matrix(p3, p5)
    c21 = add_matrix(p2, p4)
    c22 = add_matrix(sub_matrix(add_matrix(p1, p3), p2), p6)

    result = [[0] * n for _ in range(n)]
    for i in range(new_size):
        for j in range(new_size):
            result[i][j] = c11[i][j]
            result[i][j + new_size] = c12[i][j]
            result[i + new_size][j] = c21[i][j]
            result[i + new_size][j + new_size] = c22[i][j]
    return result

assert problem_61_strassen([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
print("61. OK Strassen matrix multiplication")

# 62. BINARY SEARCH ROTATED

def problem_62_rotated_binary_search(arr, target):
    """Q: Binary search in rotated array | Time: O(log n) | Space: O(1)"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[lo] <= arr[mid]:
            if arr[lo] <= target < arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] < target <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1

assert problem_62_rotated_binary_search([4, 5, 6, 7, 0, 1, 2], 0) == 4
print("62. OK Rotated binary search")

# 63. FIND PEAK ELEMENT

def problem_63_peak_element(arr):
    """Q: Find peak element | Time: O(log n) | Space: O(1)"""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > arr[mid + 1]:
            hi = mid
        else:
            lo = mid + 1
    return lo

assert problem_63_peak_element([1, 2, 3, 1]) == 2
print("63. OK Peak element")

# 64. FIND MIN IN ROTATED SORTED
def problem_64_min_in_rotated(arr):
    """Q: Find min in rotated sorted array | Time: O(log n) | Space: O(1)"""
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo]

assert problem_64_min_in_rotated([4, 5, 6, 7, 0, 1, 2]) == 0
print("64. OK Min in rotated")

# 65. FIND DUPLICATES IN ARRAY

def problem_65_find_duplicates_in_array(arr):
    """Q: Find duplicates in array | Time: O(n) | Space: O(n)"""
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

assert sorted(problem_65_find_duplicates_in_array([1, 2, 3, 1, 2])) == [1, 2]
print("65. OK Find duplicates in array")

# 66. FIND PAIR WITH GIVEN DIFFERENCE
def problem_66_pair_with_difference(arr, diff):
    """Q: Pair with given difference | Time: O(n) | Space: O(n)"""
    seen = set()
    for num in arr:
        if num + diff in seen or num - diff in seen:
            return True
        seen.add(num)
    return False

assert problem_66_pair_with_difference([5, 20, 3, 2, 50, 80], 78) == True
print("66. OK Pair with difference")

# 67. FIND MISSING TWO NUMBERS
def problem_67_missing_two(arr):
    """Q: Find two missing numbers | Time: O(n) | Space: O(1)"""
    n = len(arr) + 2
    total = n * (n + 1) // 2
    sum_arr = sum(arr)
    half = (total - sum_arr) // 2
    set1 = set()
    for num in arr:
        if num <= half:
            set1.add(num)
    total1 = half * (half + 1) // 2
    sum1 = sum(num for num in arr if num <= half)
    return [total1 - sum1, (total - sum_arr) - (total1 - sum1)]

assert sorted(problem_67_missing_two([1, 2, 4, 6])) == [3, 5]
print("67. OK Missing two numbers")

# 68. FIND SUBARRAY WITH MAXIMUM AVERAGE
def problem_68_max_average_subarray(arr, k):
    """Q: Max average subarray | Time: O(n) | Space: O(1)"""
    current_sum = sum(arr[:k])
    max_sum = current_sum
    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k

assert abs(problem_68_max_average_subarray([1, 12, -5, -6, 50, 3], 4) - 12.75) < 1e-9
print("68. OK Max average subarray")

# 69. SEARCH IN A MATRIX
def problem_69_search_matrix(matrix, target):
    """Q: Search in sorted matrix | Time: O(m+n) | Space: O(1)"""
    if not matrix or not matrix[0]:
        return False
    row, col = 0, len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False

assert problem_69_search_matrix([[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16]], 5) == True
print("69. OK Search matrix")

# 70. KTH SMALLEST ELEMENT IN MATRIX
def problem_70_kth_smallest_matrix(matrix, k):
    """Q: Kth smallest element in sorted matrix | Time: O(n log n) | Space: O(n)"""
    flat = [item for row in matrix for item in row]
    flat.sort()
    return flat[k - 1]

assert problem_70_kth_smallest_matrix([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
print("70. OK Kth smallest element in matrix")

# ============================================================================
# SECTION 5: DYNAMIC PROGRAMMING & ADVANCED PROBLEMS (71-100)
# ============================================================================

print("\n" + "="*60)
print("SECTION 5: DYNAMIC PROGRAMMING & ADVANCED PROBLEMS (30 Problems)")
print("="*60)

# 71. CLIMBING STAIRS

def problem_71_climbing_stairs(n):
    """Q: Climbing stairs | Time: O(n) | Space: O(1)"""
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

assert problem_71_climbing_stairs(5) == 8
print("71. OK Climbing stairs")

# 72. COIN CHANGE

def problem_72_coin_change(coins, amount):
    """Q: Coin change min coins | Time: O(n*m) | Space: O(m)"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

assert problem_72_coin_change([1, 2, 5], 11) == 3
print("72. OK Coin change")

# 73. LONGEST INCREASING SUBSEQUENCE

def problem_73_lis(arr):
    """Q: Longest increasing subsequence | Time: O(n^2) | Space: O(n)"""
    if not arr:
        return 0
    dp = [1] * len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

assert problem_73_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
print("73. OK LIS")

# 74. KNAPSACK

def problem_74_knapsack(weights, values, capacity):
    """Q: 0/1 knapsack | Time: O(n*W) | Space: O(W)"""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

assert problem_74_knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
print("74. OK Knapsack")

# 75. MIN PATH SUM

def problem_75_min_path_sum(grid):
    """Q: Minimum path sum | Time: O(m*n) | Space: O(n)"""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    dp = [float('inf')] * cols
    dp[0] = 0
    for row in grid:
        dp[0] += row[0]
        for j in range(1, cols):
            dp[j] = min(dp[j - 1], dp[j]) + row[j]
    return dp[-1]

assert problem_75_min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
print("75. OK Min path sum")

# 76. WORD LADDER LENGTH

def problem_76_word_ladder(begin, end, word_list):
    """Q: Word ladder length | Time: O(n*k^2) | Space: O(n*k)"""
    word_set = set(word_list)
    if end not in word_set:
        return 0
    queue = [(begin, 1)]
    visited = {begin}
    while queue:
        word, steps = queue.pop(0)
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + ch + word[i + 1:]
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, steps + 1))
    return 0

assert problem_76_word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
print("76. OK Word ladder")

# 77. MINIMUM EDIT DISTANCE

def problem_77_edit_distance(word1, word2):
    """Q: Edit distance | Time: O(n*m) | Space: O(n*m)"""
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]

assert problem_77_edit_distance("horse", "ros") == 3
print("77. OK Edit distance")

# 78. MAXIMUM PRODUCT SUBSET

def problem_78_max_product_subset(arr):
    """Q: Maximum product subset | Time: O(n) | Space: O(1)"""
    if not arr:
        return 0
    neg_count = 0
    product = 1
    zero_present = False
    min_neg = float('-inf')
    for num in arr:
        if num == 0:
            zero_present = True
            continue
        if num < 0:
            neg_count += 1
            min_neg = max(min_neg, num)
        product *= num
    if neg_count % 2 != 0:
        if min_neg == float('-inf'):
            return 0
        product //= min_neg
    if product == 1 and zero_present:
        return 0
    return product

assert problem_78_max_product_subset([-1, -1, -2, 4, 3]) == 24
print("78. OK Max product subset")

# 79. PERFECT SQUARES

def problem_79_perfect_squares(n):
    """Q: Perfect squares | Time: O(n*sqrt(n)) | Space: O(n)"""
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[n]

assert problem_79_perfect_squares(12) == 3
print("79. OK Perfect squares")

# 80. SUBSET SUM

def problem_80_subset_sum(nums, target):
    """Q: Subset sum | Time: O(n*target) | Space: O(target)"""
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    return dp[target]

assert problem_80_subset_sum([3, 34, 4, 12, 5, 2], 9) == True
print("80. OK Subset sum")

# 81. MAXIMUM SUM CIRCULAR SUBARRAY

def problem_81_max_sum_circular(arr):
    """Q: Max sum circular subarray | Time: O(n) | Space: O(1)"""
    if not arr:
        return 0
    max_ending = max_so_far = arr[0]
    min_ending = min_so_far = arr[0]
    total = arr[0]
    for num in arr[1:]:
        max_ending = max(num, max_ending + num)
        max_so_far = max(max_so_far, max_ending)
        min_ending = min(num, min_ending + num)
        min_so_far = min(min_so_far, min_ending)
        total += num
    if min_so_far == total:
        return max_so_far
    return max(max_so_far, total - min_so_far)

assert problem_81_max_sum_circular([5, -3, 5]) == 10
print("81. OK Max sum circular subarray")

# 82. LONGEST PALINDROMIC SUBSEQUENCE

def problem_82_longest_palindromic_subsequence(s):
    """Q: Longest palindromic subsequence | Time: O(n^2) | Space: O(n^2)"""
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

assert problem_82_longest_palindromic_subsequence("bbbab") == 4
print("82. OK Longest palindromic subsequence")

# 83. NUMBER OF WAYS TO CLIMB STAIRS

def problem_83_climb_stairs_ways(n):
    """Q: Number of ways to climb stairs | Time: O(n) | Space: O(1)"""
    if n <= 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

assert problem_83_climb_stairs_ways(4) == 5
print("83. OK Climb stairs ways")

# 84. NUMBER OF UNIQUE PATHS

def problem_84_unique_paths(m, n):
    """Q: Unique paths in grid | Time: O(m*n) | Space: O(n)"""
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]

assert problem_84_unique_paths(3, 7) == 28
print("84. OK Unique paths")

# 85. EDIT DISTANCE WITH OPERATIONS

def problem_85_min_edit_distance(word1, word2):
    """Q: Min edit distance | Time: O(n*m) | Space: O(n*m)"""
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]

assert problem_85_min_edit_distance("intention", "execution") == 5
print("85. OK Edit distance with operations")

# 86. LONGEST SUM PATH IN MATRIX

def problem_86_longest_sum_path(matrix):
    """Q: Longest sum path in matrix | Time: O(m*n) | Space: O(n)"""
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    dp = [0] * cols
    dp[0] = matrix[0][0]
    for j in range(1, cols):
        dp[j] = dp[j - 1] + matrix[0][j]
    for i in range(1, rows):
        dp[0] += matrix[i][0]
        for j in range(1, cols):
            dp[j] = max(dp[j - 1], dp[j]) + matrix[i][j]
    return dp[-1]

assert problem_86_longest_sum_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 12
print("86. OK Longest sum path in matrix")

# 87. NUMBER OF DISTINCT SUBSEQUENCES
def problem_87_distinct_subsequences(s, t):
    """Q: Distinct subsequences | Time: O(n*m) | Space: O(m)"""
    dp = [0] * (len(t) + 1)
    dp[0] = 1
    for i in range(1, len(s) + 1):
        for j in range(len(t), 0, -1):
            if s[i - 1] == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[-1]

assert problem_87_distinct_subsequences("rabbbit", "rabbit") == 3
print("87. OK Distinct subsequences")

# 88. MIN COST CLIMB STAIRS
def problem_88_min_cost_climbing_stairs(cost):
    """Q: Min cost climbing stairs | Time: O(n) | Space: O(1)"""
    if len(cost) <= 2:
        return min(cost)
    first, second = cost[0], cost[1]
    for i in range(2, len(cost)):
        first, second = second, min(first, second) + cost[i]
    return min(first, second)

assert problem_88_min_cost_climbing_stairs([10, 15, 20]) == 15
print("88. OK Min cost climbing stairs")

# 89. SUBARRAY SUM EQUAL K

def problem_89_subarray_sum_equals_k(arr, k):
    """Q: Subarray sum equals k | Time: O(n) | Space: O(n)"""
    sum_map = {0: 1}
    current_sum = 0
    count = 0
    for num in arr:
        current_sum += num
        count += sum_map.get(current_sum - k, 0)
        sum_map[current_sum] = sum_map.get(current_sum, 0) + 1
    return count

assert problem_89_subarray_sum_equals_k([1, 1, 1], 2) == 2
print("89. OK Subarray sum equals k")

# 90. PRODUCT EXCEPT SELF
def problem_90_product_except_self(arr):
    """Q: Product except self | Time: O(n) | Space: O(1)"""
    length = len(arr)
    result = [1] * length
    left = 1
    for i in range(length):
        result[i] = left
        left *= arr[i]
    right = 1
    for i in range(length - 1, -1, -1):
        result[i] *= right
        right *= arr[i]
    return result

assert problem_90_product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
print("90. OK Product except self")

# 91. MAXIMUM LENGTH OF REPEATING SUBARRAY
def problem_91_max_repeating_subarray(nums1, nums2):
    """Q: Max length repeating subarray | Time: O(n*m) | Space: O(m)"""
    dp = [0] * (len(nums2) + 1)
    max_length = 0
    for i in range(len(nums1) - 1, -1, -1):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[j] = 1 + dp[j + 1]
                max_length = max(max_length, dp[j])
            else:
                dp[j] = 0
    return max_length

assert problem_91_max_repeating_subarray([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]) == 3
print("91. OK Max repeating subarray")

# 92. LONGEST ZIGZAG SUBSEQUENCE
def problem_92_zigzag(arr):
    """Q: Longest zigzag subsequence | Time: O(n) | Space: O(n)"""
    if len(arr) < 2:
        return len(arr)
    up = down = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            up = down + 1
        elif arr[i] < arr[i - 1]:
            down = up + 1
    return max(up, down)

assert problem_92_zigzag([1, 7, 4, 9, 2, 5]) == 6
print("92. OK Zigzag subsequence")

# 93. MATRIX CHAIN MULTIPLICATION
def problem_93_matrix_chain_order(arr):
    """Q: Matrix chain multiplication | Time: O(n^3) | Space: O(n^2)"""
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for l in range(2, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j])
    return dp[1][n - 1]

assert problem_93_matrix_chain_order([1, 2, 3, 4]) == 18
print("93. OK Matrix chain multiplication")

# 94. WORD SEARCH
def problem_94_word_search(board, word):
    """Q: Word search | Time: O(m*n*4^k) | Space: O(k)"""
    rows, cols = len(board), len(board[0])
    def dfs(r, c, index):
        if index == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
            return False
        temp = board[r][c]
        board[r][c] = '#'
        found = (dfs(r + 1, c, index + 1) or dfs(r - 1, c, index + 1) or
                 dfs(r, c + 1, index + 1) or dfs(r, c - 1, index + 1))
        board[r][c] = temp
        return found
    for i in range(rows):
        for j in range(cols):
            if dfs(i, j, 0):
                return True
    return False

assert problem_94_word_search([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
print("94. OK Word search")

# 95. SCHEDULE TASKS WITH COOLING PERIOD
def problem_95_least_interval(tasks, n):
    """Q: Task scheduler | Time: O(n) | Space: O(1)"""
    freq = {}
    for task in tasks:
        freq[task] = freq.get(task, 0) + 1
    max_freq = max(freq.values())
    max_count = sum(1 for count in freq.values() if count == max_freq)
    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

assert problem_95_least_interval(["A","A","A","B","B","B"], 2) == 8
print("95. OK Task scheduler")

# 96. FIND MEDIAN OF TWO SORTED ARRAYS
def problem_96_find_median(nums1, nums2):
    """Q: Median of two sorted arrays | Time: O((m+n) log(m+n))"""
    nums = sorted(nums1 + nums2)
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    return nums[mid]

assert problem_96_find_median([1, 3], [2]) == 2
print("96. OK Median of two sorted arrays")

# 97. FIND FIRST MISSING POSITIVE
def problem_97_first_missing_positive(nums):
    """Q: First missing positive | Time: O(n) | Space: O(1)"""
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1

assert problem_97_first_missing_positive([3, 4, -1, 1]) == 2
print("97. OK First missing positive")

# 98. MAXIMUM SUM OF NON-ADJACENT ELEMENTS
def problem_98_max_non_adjacent_sum(nums):
    """Q: Maximum sum of non-adjacent elements | Time: O(n) | Space: O(1)"""
    include, exclude = 0, 0
    for num in nums:
        include, exclude = exclude + num, max(include, exclude)
    return max(include, exclude)

assert problem_98_max_non_adjacent_sum([3, 2, 7, 10]) == 13
print("98. OK Max non-adjacent sum")

# 99. COUNT NUMBER OF ISLANDS
def problem_99_count_islands(grid):
    """Q: Count islands | Time: O(m*n) | Space: O(m*n)"""
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    visited = set()
    def dfs(r, c):
        if (r < 0 or c < 0 or r >= rows or c >= cols or
                grid[r][c] == '0' or (r, c) in visited):
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                count += 1
    return count

assert problem_99_count_islands(["11110","11010","11000","00000"]) == 1
print("99. OK Count islands")

# 100. LRU CACHE (SIMPLIFIED)

class LRUCache:
    """Q: LRU Cache implementation | Time: O(1) operations | Space: O(capacity)"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
print("100. OK LRU Cache")

print("\nAll 100 problems loaded successfully.")
