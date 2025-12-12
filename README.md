# Agrichain – Automation Assignment


1. **Program to find the length of the longest substring without repeating characters**
2. **Web automation of a sample website (agrichain.com)** which accepts a string and displays the longest unique substring length on the next page.


---

# 📌 Problem 1:

I used a simple sliding-window logic to solve this in O(n) time.

I implemented a simple Python solution using the sliding window technique.
The logic continuously expands a window, and whenever a repeated character is found, the window is adjusted.
This helps efficiently calculate the length of the longest substring with unique characters.


# 📌 Problem 2:

# Test Cases for Assumed Website

# Manual Test Cases

- Check if input box and submit button are visible.

- Enter a valid string and verify correct result.

- Enter empty input → check for error message.

- Enter special characters.

- Enter numbers.

 - Very long string performance.

 - Verify navigation from Home Page → Result Page.

- Test on Chrome.

# Automation Test Cases

- Valid input (“abcabcbb”) should return 3

- Input “bbbbb” should return 1

- Validate error message for empty input

- Verify navigation after clicking submit

- Verify behavior for special characters




# Framework Structure

- utils/  ***Browser initialization***

- locators/ ***Stores all element locators***

- pages/  ***Page Object Model (page actions like enter text, click submit)***

 - tests/  ***Contains the actual automated test case***

- I automated one test case where I input a sample string and validate that the correct longest substring length is displayed on the next page.
