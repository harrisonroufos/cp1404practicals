"""
CP1404 Practical
languages
Estimate: 25 minutes
Actual:
"""
from prac_06.programming_language import ProgrammingLanguage

# test = ProgrammingLanguage("Test", "Dynamic", True, 1991)
# print(test.is_dynamic())

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)


programming_languages_data = [ProgrammingLanguage("Python", "Dynamic", True, 1991),
                              ProgrammingLanguage("Ruby", "Dynamic", True, 1995),
                              ProgrammingLanguage("Visual Basic", "Static", False, 1991)]

print("The dynamically typed languages are:")
for language in programming_languages_data:
    if language.is_dynamic():
        print(language.name)
