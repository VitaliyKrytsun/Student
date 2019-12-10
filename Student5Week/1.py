# try:
#     n = int(input())
#     # print(1 / n)
#     # import sdfas
#     assert n > 0
# except (ZeroDivisionError,ImportError) as e:
#     print(e)
# except AssertionError as e:
#     print('AssertionError')
# else:
#     print('Success')
# finally:
#     print('done')
# try:
#     pass
# except Exception:
#     pass

# print(dir(Exception), Exception.__subclasses__())

# class MyException(Exception):
#     pass
# n = int(input())
# try:
#     print(n / 0)
# except Exception as e:
#     if n == 1:
#         raise MyException()
#     raise e
# finally:
#     print('done')

# with open('D:\Python\Week1\Student\Student5Week\Point.py', 'r') as file_text:
#     for line in file_text:
#         print(line)

# file_without_counxt = open('D:\Python\Week1\Student\Student5Week\Point.py', 'r')
# for line in file_without_counxt:
#     print(line)
# file_without_counxt.close()

x = int(input())
y = int(input())

try:
    print(x*y)
    if  



