################# Algo #########################

#reverse integer
# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def revInt(x):
    string = str(x)

    if string[0] == '-':
        return int('-' + string[:0:-1])
    else:
        return int(string[::-1])

print(revInt(-213))
print(revInt(345))

#average word length
# For a given sentence, return the average word length.
# Note: Remember to remove punctuation first

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"

def avgWordLen(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    words = sentence.split()
    return round(sum(len(word) for word in words)/len(words),2)

print(avgWordLen(sentence1))
print(avgWordLen(sentence2))

#add strings
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.

num1 = '364'
num2 = '1836'

def addStr(num1, num2):
    eval(num1) + eval(num2)
    return str(eval(num1) + eval(num2))

print(addStr(num1, num2))

#first unique character
# Given a string, find the first non-repeating character in it and return its index.
# If it doesn't exist, return -1. # Note: all the input strings are already lowercase.

def firstUniqChar(s):
    freq = {}
    for i in s:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i
    return -1

print(firstUniqChar('alphabet'))
print(firstUniqChar('barbados'))
print(firstUniqChar('crunchy'))

#palindrome
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# The string will only contain lowercase characters a-z.

s = 'radkar'
def palindrome(s):
    for i in range(len(s)):
        #temp is begining to i plus one after i to the end
        temp = s[:i] + s[i+1:]
        if temp == temp[::-1]:
            return True

    return s == s[::-1]

print(palindrome(s))

#monotonic array
# Given an array of integers, determine whether the array is monotonic or not.

A = [6, 5, 4, 4]
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def mono(nums):
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))

print(mono(A))
print(mono(B))
print(mono(C))

#move zeros
#Given an array nums, write a function to move all zeroes to the end of it
#while maintaining the relative order of
#the non-zero elements.

array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]

def moveZeros(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

print(moveZeros(array1))
print(moveZeros(array2))

#fill the blanks
# Given an array containing None values fill in the None values with most recent
# non None value in the array

array01 = [1,None,2,3,None,None,5,None]

def fillInThe(array):
    valid = 0
    results = []
    for i in array:
        if i is not None:
            results.append(i)
            valid = i
        else:
            results.append(valid)
    return results

print(fillInThe(array01))

#matched and mismatched words
#Given two sentences, return an array that has the words that appear
#in one sentence and not
#the other and an array with the words in common.

sentence1 = 'We are really pleased to meet you in our city'
sentence2 = 'The city was hit by a really heavy storm'

def matAndMisMat(sen1, sen2):
    set1 = set(sen1.split())
    set2 = set(sen2.split())

    # ^ A.symmetric_difference(B), & A.intersection(B)
    inOneAndNotOther = sorted(list(set1 ^ set2))
    inCommon = sorted(list(set1 & set2))

    return inOneAndNotOther, inCommon

print(matAndMisMat(sentence1, sentence2))

#prime numbers array
# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.
# Definition: A prime number is a natural number greater than 1
#that has no positive divisors other than 1 and itself.

n = 35
def primeNumArr(n):
    primeNums = []
    for num in range(n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primeNums.append(num)
    return primeNums

print(primeNumArr(n))

#maximum sum
# Take an array with positive and negative numbers and
# find the maximum sum of the array

def largest(arr):
    if len(arr) == 0:
        return print("Too Small")

    maxSum = arr[0]
    currentSum = arr[0]

    for num in arr[1:]:
        currentSum = max(currentSum + num, num)
        maxSum = max(currentSum, maxSum)

    return maxSum

print(largest([7,1,2,-1,3,4,10,-12,3,21,-19]))