def palindrome(nums):
    for num in nums:
        if num == num[::-1]:
            print("True")
        else:
            print("False")


result = input().split(", ")
palindrome(result)